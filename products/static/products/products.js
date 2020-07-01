

$(document).ready(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
    
      type: 'get',
      dataType: 'json',
      beforeSend: function () {

        $("#modal-product .modal-content").html("");//optional--html() return innerHtml of selected elements
        $("#modal-product").modal("show");
      },
      success: function (data) {
        
        $("#modal-product .modal-content").html(data.html_form);//model-product and model content is in index.html below tabel which will show form pop up 
        
      }
    });
  };

  
  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      dataType: 'json',
      type: form.attr("method"),
      
     
      success : function (data) {
        if (data.form_is_valid) {//means if data['form_is_valid'] = True in views.py
        
         $("#modal-product .close").click();//hide modal i.e form
     
        // $('#product-table tbody').html(data.html_product_list); // <-- Replace the table body
    
       
        
          //Goto id="product-table"  tbody and then pass data in tbody contain in data.html_product_list
       
         // $("#modal-product").modal('hide');--similar but differ in some version
        }
        else {// data['form_is_valid'] = False
          
          $("#modal-product .modal-content").html(data.html_form);//$("#server-results").html(response);
        }
      }
    });
    return false;
  };


  $(".js-product-create").click(loadForm);
  $("#modal-product").on("submit", ".js-product-create-form", saveForm);

  
  $("#product-table").on("click", ".js-product-update", loadForm);
  $("#modal-product").on("submit", ".js-product-update-form", saveForm);


  $("#product-table").on("click", ".js-product-delete", loadForm);
  $("#modal-product").on("submit", ".js-product-delete-form", saveForm);

});


