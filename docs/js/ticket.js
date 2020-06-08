/*
  Main purpose of this script is:
  Handle ticket payment request.
 */
function atou(str){
  return decodeURIComponent(escape(window.atob(str)));
}

function ticketFormSubmit(token) {
  //validate form
  var errors_occured = false;
  $("#ticket-form input.required").each(function(index){
    if(! $(this).val()){
      $(this).addClass("err").attr("title", "Vyplň mě prosím.").change(function(e){
        //remove warning on change
        if($(this).val()){
          $(this).removeClass("err").attr("title", "");
        }
      });

      errors_occured = true;
    }
  });

  if(!errors_occured){
    $("#ticket-form input").each(function(index){
      $(this).addClass('shadow');
    });

    $('#ticket-form-btn').text("Odesílám ...").attr("disabled", true);
    document.getElementById("ticket-form").submit();
  }
}

$(document).ready(function(){
  //redirect on modal close
  $(".modal-payment-close").each(function(index){
    $(this).click(function(e){
      window.location = "#tickets";
    });
  });

  var hash = location.hash;
  if(hash.length > 2 && hash[0] == "#"){
    var pairs = hash.substring(1).split("&");

    //parse param values
    var vals = {};
    pairs.forEach(function(item, index){
      var kv = item.split("=");
      var kv_len = kv.length;
      if(kv_len = 2){
        vals[kv[0]] = kv[1];
      }else if(kv_len){
        vals[kv[0]] = null;
      }
    });

    if("tickets" in vals && "req" in vals){
      var req_decoded = decodeURIComponent(vals['req']);
      var json_decoded = atou(req_decoded);
      var data = JSON.parse(json_decoded);

      $("#tickets-payment-promise").text(data["promise"] + " Kč");
      $("#tickets-payment-variable-symbol").text(data["variable_symbol"]);
      $("#tickets-payment-bank-account").text(data["bank_account"]);
      $("#tickets-payment-name").text(data["name"]);
      $('#tickets-modal').modal('toggle');
    }else if("tickets" in vals && "err" in vals){
      $("#tickets").get(0).scrollIntoView();
      $("#ticket-form-warning").addClass("show");
    }
  }
});
