


$(document).ready(function(){
    $("#js-order-search-form").on("click", function(){
        var form = $(this);
  
            $.ajax({
                url: form.attr("action"),
                type: 'get',
                
            //   data: {'value_placeholder':searchWord},
                data : form.serialize(),
                dataType: 'json',
                success: function(data){
  
                    $("#order_table_body").html('');
                    $("#order_table_body").html(data['html_list']);
  
                },
                error: function(error){
  
                    console.log(error);
                    $("#Message").addClass("alert alert-danger");
                    $("#Message").html(error.responseText);
                }
  
            });
  
  
       
    });
  
  
  
  });
  