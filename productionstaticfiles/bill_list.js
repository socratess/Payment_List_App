  function list_bills() {
      console.log('Requesting JSON');
      $.getJSON('/bills', function(rowz){
        console.log('JSON', rowz);
        if($.fn.dataTable.isDataTable('#example')){
          $('#example').DataTable().destroy();
        }
        $('#example tbody').empty();
        datalength=Object.keys(rowz).length
        for (var i = 0; i < datalength; i++) {
          var fila = '<tr>'
          fila += '<td>' + rowz[i]["fields"]["title"]+ '</td>';
          fila += '<td>' + rowz[i]["fields"]["description"]+ '</td>';
          fila += '<td>' + rowz[i]["fields"]["price"]+ '</td>';
          fila += '<td>' + rowz[i]["fields"]["created"]+ '</td>';
           if (rowz[i]["fields"]["important"]==true){
            fila += '<td>' + 'Yes'+ '</td>';
           }
           else{
            fila += '<td>' + 'No'+ '</td>';
           }
          fila +=
            '<td><button type="button" class="btn btn-secondary" onclick="open_modal_detail(\'/bills/'+rowz[i]['pk']+'\')">Detail</button></td>';
          fila += '<td><button type="button" class="btn btn-primary" onclick="open_modal_update(\'/bills/'+rowz[i]['pk']+'/update\');">Update</button></td>';
          fila += '<td><button type="button" class="btn btn-danger" onclick="open_modal_delete(\'/bills/'+rowz[i]['pk']+'/delete\');">Delete</button></td>';  
          if (rowz[i]["fields"]["datecompleted"] === null) {
            fila +=
              '<td><button type="button" class="btn btn-warning" onclick="open_modal_payment(\'/bills/'+rowz[i]['pk']+'/pay\')">Add Pay</button></td>';
          } else {
            /**
          <form action="#" method="post">{%csrf_token%} </form>
          **/
            fila += "<td>" + "it is already paid" + "</td>";
          }


          fila += '</tr>'
          $('#example tbody').append(fila);
        }
        $('#example').DataTable({
          scrollCollapse: true,
          scrollY: '50vh',
          scrollbars: true
        });
        //setTimeout('updateMsg()', 4000);
    });
  }
  // Make sure JSON requests are not cached
  $(document).ready(function() {
    $.ajaxSetup({ cache: false });
    list_bills();
  });

/*function open_detail_windows(url){
window.open(url);
}
*/

function open_modal_create(url) {
  $("#create").load(url, function () {
    $(this).modal("show");
  });
}

function open_modal_update(url) {
  $("#update").load(url, function () {
    $(this).modal("show");
  });
}
function open_modal_delete(url) {
  $("#delete").load(url, function () {
    $(this).modal("show");
  });
}
function open_modal_payment(url) {
  $("#payment").load(url, function () {
    $(this).modal("show");
  });
}

function open_modal_detail(url) {
  $("#detail").load(url, function () {
    $(this).modal("show");
  });
}
function open_modal_upload(url) {
   $("#upload").load(url, function () {
     $(this).modal("show");
   });
}
function close_modal_payment() {
  $("#payment").modal("hide");
}
function close_modal_create() {
  $("#create").modal("hide");
}
function close_modal_upload() {
  $("#upload").modal("hide");
}
function close_modal_update() {
  $("#update").modal("hide");
}
function close_modal_delete() {
  $("#delete").modal("hide");
}

function create_bill_bank() {
  activatebutton();
  $.ajax({
    data: $("#form_create").serialize(),
    url: $("#form_create").attr("action"),
    type: $("#form_create").attr("method"),
    success: function (response) {
      notification_success(response.message);
      list_bills();
      close_modal_create();
    },
    error: function (error) {
      notification_error(error.responseJSON.message);
      show_error_create(error);
      activatebutton();
    },
  });
}

function activatebutton(){
  if ($("#button_create").prop('disabled')){
    $("#button_create").prop('disabled', false);
  } else {
    $("#button_create").prop("disabled", true);
  }
}

function show_error_create(errors){
  $("#errors").empty();
  let error = " ";
  for(let item in errors.responseJSON.error){
    error += '<div class="alert alert-danger" <strong>' + errors.responseJSON.error[item]  + '</strong></div>';
  }
  $("#errors").append(error);
}

function show_error_update(errors) {
  $("#errorsUpdate").empty();
  let error = " ";
  for (let item in errors.responseJSON.error) {
    error +=
      '<div class="alert alert-danger" <strong>' +
      errors.responseJSON.error[item] +
      "</strong></div>";
  }
  $("#errorsUpdate").append(error);
}

function notification_error(message) {
Swal.fire({
  title: 'Error!',
  text: message,
  icon: 'error'
})
}

function notification_success(message) {
  Swal.fire({
    title: "Good Job!",
    text: message,
    icon: "success",
  });
}

function update_bill(){
  activatebutton();
$.ajax({
  data: $("#form_update").serialize(),
  url: $("#form_update").attr("action"),
  type: $("#form_update").attr("method"),
  success: function (response) {
    notification_success(response.message);
    list_bills();
    close_modal_update();
  },
  error: function (error) {
    notification_error(error.responseJSON.message);
    show_error_update(error);
    activatebutton();
  },
});
}

function pay_bill() {
  activatebutton();
  $.ajax({
    data: $("#form_payment").serialize(),
    url: $("#form_payment").attr("action"),
    type: $("#form_payment").attr("method"),
    success: function (response) {
      notification_success(response.message);
      list_bills();
      close_modal_payment();
    },
    error: function (error) {
      notification_error(error.responseJSON.message);
      activatebutton();
    },
  });
}

function delete_bill(pk) {
  activatebutton();
  $.ajax({
    data: {
      csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
    },
    url: "/bills/" + pk + "/delete",
    type: "post",
    success: function (response) {
      notification_success(response.message);
      list_bills();
      close_modal_delete();
    },
    error: function (error) {
      notification_error(error.responseJSON.message);
    },
  });
}

function upload_manual_bill_bank() {
  activatebutton();
   var form = $('#form_upload')[0];
   var data = new FormData(form);
  $.ajax({
    url: $("#form_upload").attr("action"),
    type: $("#form_upload").attr("method"),
    enctype: $("#form_upload").attr("enctype"),
    data: data,
    processData: false,
    contentType: false,
    cache: false,
    success: function (response) {
      notification_success(response.message);
      list_bills();
      close_modal_upload();
    },
    error: function (error) {
      notification_error(error.responseJSON.message);
      activatebutton();
    },
  });
}