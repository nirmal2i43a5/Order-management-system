from django.http import HttpResponse
from .resources import CustomerResource

def export(request):
    customer_resource = CustomerResource()
    dataset = customer_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="customers.json"'
    return response


