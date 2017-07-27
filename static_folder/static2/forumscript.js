console.log("hihihiihihi");

//
// function applyFilterClick() {
//   $('#apply_button').click(applyFilter);
//   console.log("CONSOLEELELELELELLELE")
// }
//
// $(document).ready(
//   applyFilterClick,
//   applyFilter
// );

function applyFilter() {
  $('.uci').show();
  $('.ucsd').show();
  console.log("hehhehehehsxfdsf")

  if ($('#uci').is(':checked')){
    $('.ucsd').hide();
    console.log("U C I");
  }
  else if ($('#ucsd').is(':checked')) {
    $('.uci').hide();
    console.log("U C S D");
  }
  else {
    $('.uci').show();
    $('.ucsd').show();
    console.log("hehhehehehsxfdsf")
  }

}
