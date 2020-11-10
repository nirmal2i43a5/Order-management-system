


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
        console.log(form.serialize())
        $.ajax({
          headers: {'X-CSRFToken': csrftoken},
          url: form.attr("action"),//sending request to this url by passing form input data
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          // async : 'false',
          // dataType: "script",
         
      
        
          success : function (data) {//this is the response after data is save to database

            if (data.form_is_valid) {//means if data['form_is_valid'] = True in views.py
            
            alert("successful")
            // console.log(data.html_product_list)
            
             $("#modal-product .close").click();// Close the modal form
         
             

             $("#product-table tbody").html('').append(jQuery.parseHTML(data.html_product_list)); 
             
            // html('').append(jQuery.parseHTML(data, document, true));
            // <-- Replace the table body 
              //Goto id="product-table"  tbody and then pass data in tbody contain in data.html_product_list
           
            //  $("#modal-product").modal('hide');//--similar but differ in some version
            }

            else {// data['form_is_valid'] = False
            //if false then show the same form with respective warning
              
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
    
    getCookie = (name) => {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');
 