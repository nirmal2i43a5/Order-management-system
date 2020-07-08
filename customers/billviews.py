from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


from django.views.generic import View
from customers.models import Customer
from orders.models import Order
from datetime import datetime
from django.shortcuts import get_object_or_404

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GenerateBILL(View):
    
    def get(self, request, *args, **kwargs):
        template = get_template('customers/bill.html')
        # customers = Customer.objects.all()
        customers = get_object_or_404(Customer,pk=kwargs.get("cid"))
        
        customers_order = customers.order_set.all()#particular customer particular bill generate
        myDate = datetime.now()
        formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
        
        
        
        #for total price
        # order_count = customers_order.count() 
          
        new_total=0.00
        for order in customers.order_set.all():
            per_total_price = float(order.product.price) * order.quantity
            # customer.per_total = per_total_price--to get the price of respective products
            #return value of first product i.e first row
            new_total += per_total_price
            
        
        context={'customers_order':customers_order,'customer_total_price':new_total,
                 'customers':customers,
                 'myDate':formatedDate}
       
        html = template.render(context)
        
        pdf = render_to_pdf('customers/bill.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341232")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        
        return HttpResponse("Not found")