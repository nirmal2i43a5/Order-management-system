

$(document).ready(function(){


  $("#js-search-form").on("click", function(event){
    event.preventDefault();
      var form = $(this);

          $.ajax({
              url: form.attr("action"),
              type: 'get',
              
          //   data: {'value_placeholder':searchWord},
              data : form.serialize(),
              dataType: 'json',
              success: function(data){

                  $("#get_table_body").html('');
                  $("#get_table_body").html(data['html_list']);

              },
              error: function(error){

                  console.log(error);
                  $("#Message").addClass("alert alert-danger");
                  $("#Message").html(error.responseText);
              }

          });


     
  });



});






// $(document).ready(function(){

//   bindEvents();

// });



// function bindEvents(){


//   $("#js-search-form").on("click", function(event){

//       getUserSearchDetails($(this));
//   });


// }


// function getUserSearchDetails(object){

// console.log(object);
// // var searchWord = $('#js-search-form  .form-control').val();

// //    if(searchWord !== ""){

//   $.ajax({
//       url: object.attr("action"),
//       type: 'get',
    
//     //   data: {'value_placeholder':searchWord},
//     data : object.serialize(),
//       dataType: 'json',
//       success: function(data){

//           $("#get_table_body").html('');
//           $("#get_table_body").html(data['html_form']);

//       },
//       error: function(error){

//           console.log(error);
//           $("#Message").addClass("alert alert-danger");
//           $("#Message").html(error.responseText);
//       }

//   });
// }
