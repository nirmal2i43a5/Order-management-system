

$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
      
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-product .modal-content").html("");
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
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#product-table tbody").html(data.html_product_list);
            $("#modal-product").modal("hide");

          
          }
          else {
            $("#modal-product .modal-content").html(data.html_form);
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