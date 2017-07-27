

function applyFilterClick() {
  $('#apply_button').click(applyFilter);
}

$(document).ready(
  applyFilterClick
);

$('.mit').show();
$('.uci').show();
$('.ucsd').show();
$('.northridge').show();
$('.ucsc').show();
$('.ucb').show();
$('.cppomona').show();
$('.cpslo').show();

function applyFilter() {
  // still doesn't account for clicking both!!
  $('.mit').hide();
  $('.uci').hide();
  $('.ucsd').hide();
  $('.northridge').hide();
  $('.ucsc').hide();
  $('.ucb').hide();
  $('.cppomona').hide();
  $('.cpslo').hide();

  if ($('#uci').is(':checked')){
    $('.uci').show();

  }
  if ($('#ucsd').is(':checked')) {

    $('.ucsd').show();

  }
  if ($('#mit').is(':checked')) {
    $('.mit').show();
  }

  if ($('#ucb').is(':checked')) {
    $('.ucb').show();

  }

  if ($('#northridge').is(':checked')) {

    $('.northridge').show();

  }

  if ($('#ucsc').is(':checked')) {
    $('.ucsc').show();

  }

  if ($('#cppomona').is(':checked')) {
    $('.cppomona').show();

  }

  if ($('#cpslo').is(':checked')) {
    $('.cpslo').show();
  }

  else {
    // $('.uci').show();
    // $('.ucsd').show();
    // console.log("hehhehehehsxfdsf");
    }

}
