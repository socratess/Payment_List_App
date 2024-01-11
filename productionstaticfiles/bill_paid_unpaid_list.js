function list_paid_bills(){

$.getJSON('/bills/paid',function(datareponse){
if ($.fn.dataTable.isDataTable("#table_paid")) {
  $("#table_paid").DataTable().destroy();
}
$("#table_paid tbody").empty();
datalength = Object.keys(datareponse).length;

for (var i = 0; i < datalength; i++) {
    var fila ='<tr>'
    fila += "<td>" + datareponse[i]['fields']['title']+"</td>";
    fila += "<td>" + datareponse[i]["fields"]["description"] + "</td>";
    fila += "<td>" + datareponse[i]["fields"]["price"] + "</td>";
    fila += "<td>" + datareponse[i]["fields"]["created"] + "</td>";
    fila += "<td>" + datareponse[i]["fields"]["datecompleted"] + "</td>";
     if (datareponse[i]["fields"]["important"] == true) {
       fila += "<td>" + "Yes" + "</td>";
     } else {
       fila += "<td>" + "No" + "</td>";
     }
      fila +=
            '<td><button type="button" class="btn btn-secondary" onclick="open_modal_detail(\'/bills/'+datareponse[i]['pk']+'\')">Detail</button></td>'; 
    fila += "</tr>";
    $('#table_paid tbody').append(fila);
}
$("#table_paid").DataTable({
  scrollCollapse: true,
  scrollY: "50vh",
  scrollbars: true,
});
});
}

 $(document).ready(function () {
   $.ajaxSetup({ cache: false });
   list_paid_bills();
 });



function open_modal_detail(url) {
  $("#detail").load(url, function () {
    $(this).modal("show");
  });
} 




function list_unpaid_bills() {
  $.getJSON("/bills/unpaid", function (datareponse) {
    if ($.fn.dataTable.isDataTable("#table_unpaid")) {
      $("#table_unpaid").DataTable().destroy();
    }
    $("#table_unpaid tbody").empty();
    datalength = Object.keys(datareponse).length;

    for (var i = 0; i < datalength; i++) {
      var fila = "<tr>";
      fila += "<td>" + datareponse[i]["fields"]["title"] + "</td>";
      fila += "<td>" + datareponse[i]["fields"]["description"] + "</td>";
      fila += "<td>" + datareponse[i]["fields"]["price"] + "</td>";
      fila += "<td>" + datareponse[i]["fields"]["created"] + "</td>";
      if (datareponse[i]["fields"]["important"] == true) {
        fila += "<td>" + "Yes" + "</td>";
      } else {
        fila += "<td>" + "No" + "</td>";
      }
      fila +=
        '<td><button type="button" class="btn btn-secondary" onclick="open_modal_detail(\'/bills/' +
        datareponse[i]["pk"] +
        "')\">Detail</button></td>";

        fila +=
          '<td><button type="button" class="btn btn-warning" onclick="open_modal_payment(\'/bills/' +
          datareponse[i]["pk"] +
          "/pay')\">Add Pay</button></td>";
         
      fila += "</tr>";
      $("#table_unpaid tbody").append(fila);
    }
    $("#table_unpaid").DataTable({
      scrollCollapse: true,
      scrollY: "50vh",
      scrollbars: true,
    });
  });
}

$(document).ready(function () {
  $.ajaxSetup({ cache: false });
  list_unpaid_bills();
});

function open_modal_detail(url) {
  $("#detail").load(url, function () {
    $(this).modal("show");
  });
} 
function open_modal_payment(url) {
  $("#payment").load(url, function () {
    $(this).modal("show");
  });
}
function close_modal_payment() {
  $("#payment").modal("hide");
}

function pay_bill() {
  activatebutton();
  $.ajax({
    data: $("#form_payment").serialize(),
    url: $("#form_payment").attr("action"),
    type: $("#form_payment").attr("method"),
    success: function (response) {
      notification_success(response.message);
      list_unpaid_bills();
      close_modal_payment();
    },
    error: function (error) {
      notification_error(error.responseJSON.message);
      activatebutton();
    },
  });
}
function activatebutton() {
  if ($("#button_create").prop("disabled")) {
    $("#button_create").prop("disabled", false);
  } else {
    $("#button_create").prop("disabled", true);
  }
}
function notification_error(message) {
  Swal.fire({
    title: "Error!",
    text: message,
    icon: "error",
  });
}

function notification_success(message) {
  Swal.fire({
    title: "Good Job!",
    text: message,
    icon: "success",
  });
}