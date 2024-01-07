function list_banks() {
  console.log("hola");
  $.ajax({
    url: "/bills/bank/",
    type: "get",
    dataType: "json",
    success: function (response) {
      if ($.fn.dataTable.isDataTable("#examplesss")) {
        $("#examplesss").DataTable().destroy();
      }
      $("#examplesss tbody").empty();
      datalength = Object.keys(response).length;
      console.log(datalength);
      console.log(response)

      for (var i = 0; i < datalength; i++) {
        var fila = "<tr>";
        fila += "<td>" + response[i]["fields"]["name"] + "</td>";
        
        if (response[i]["fields"]["frequent"]==true) {
        fila += "<td>" + 'Frequent' + "</td>";
        }
        else{
        fila += "<td>" + "No Frequent" + "</td>";
        }
       fila += "<td>" + response[i]["fields"]["bill"] + "</td>";
       fila +=
         '<td><button type="button" class="btn btn-secondary" onclick="open_modal_detail_bank(\'/bills/bank/'+response[i]['pk']+'\');">Detail</button></td>';
fila +=
  '<td><button type="button" class="btn btn-primary" onclick="open_modal_update_bank(\'/bills/bank/'+response[i]['pk']+'/update\');">Update</button></td>';
        fila += "</tr>";
        $("#examplesss tbody").append(fila);
      }
       $("#examplesss").DataTable({
         scrollCollapse: true,
         scrollY: "50vh",
         scrollbars: true,
       });
    },
    error: function (error) {
      console.log(error);
    },
  });
}

$(document).ready(function () {
  list_banks();
});


function open_modal_update_bank(url) {
  $("#update_bank").load(url, function () {
    $(this).modal("show");
  });
}
function open_modal_detail_bank(url) {
  $("#detail_bank").load(url, function () {
    $(this).modal("show");
  });
}

function close_modal_update_bank() {
  $("#update_bank").modal("hide");
}

function activatebutton_bank() {
  if ($("#button_update_bank").prop("disabled")) {
    $("#button_update_bank").prop("disabled", false);
  } else {
    $("#button_update_bank").prop("disabled", true);
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

function show_error_update(errors) {
  $("#errorsUpdate_Bank").empty();
  let error = " ";
  for (let item in errors.responseJSON.error) {
    error +=
      '<div class="alert alert-danger" <strong>' +
      errors.responseJSON.error[item] +
      "</strong></div>";
  }
  $("#errorsUpdate_Bank").append(error);
}

function update_bank() {
  activatebutton_bank();
  $.ajax({
    data: $("#form_update_bank").serialize(),
    url: $("#form_update_bank").attr("action"),
    type: $("#form_update_bank").attr("method"),
    success: function (response) {
      notification_success(response.message);
      list_banks();
      close_modal_update_bank();
    },
    error: function (error) {
      notification_error(error.responseJSON.message);
      show_error_update(error);
      activatebutton_bank();
    },
  });
}