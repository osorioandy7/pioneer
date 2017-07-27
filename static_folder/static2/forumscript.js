console.log("hihihiihihi");


function applyFilterClick() {
  $('#apply_button').click(applyFilter);
  console.log("CONSOLEELELELELELLELE")
}

$(document).ready(
  applyFilterClick
);

function applyFilter() {
  // still doesn't account for clicking both!!
  $('.uci').show();
  $('.ucsd').show();
  console.log("hehhehehehsxfdsf");

  if ($('#uci').is(':checked')){
    $('.ucsd').hide();
    $('.uci').show();
    console.log("U C I");
  }
  else if ($('#ucsd').is(':checked')) {
    $('.uci').hide();
    $('.ucsd').show();
    console.log("U C S D");
  }
  else {
    // $('.uci').show();
    // $('.ucsd').show();
    // console.log("hehhehehehsxfdsf");
    }

}
