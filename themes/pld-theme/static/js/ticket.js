/*
  Main purpose of this script is:
  Handle ticket payment request.
 */
function atou(str){
  return decodeURIComponent(escape(window.atob(str)));
}

$(document).ready(function(){
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
      console.log("Yeees its here");

      var req_decoded = decodeURIComponent(vals['req']);
      var json_decoded = atou(req_decoded);
      var data = JSON.parse(json_decoded);

      console.log(data);
      $("#tickets-payment-promise").text(data["promise"]);
      $("#tickets-payment-variable-symbol").text(data["variable_symbol"]);
      $("#tickets-payment-bank-account").text(data["bank_account"]);
      $("#tickets-payment-name").text(data["name"]);
      $('#tickets-modal').modal('toggle');
    }
  }
});
