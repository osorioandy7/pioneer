

function applyFilterClick() {
  $('#apply_button').click(applyFilter);
}

$(document).ready(
  applyFilterClick
);

function applyFilter() {
  // still doesn't account for clicking both!!
  $('.mit').show();
  $('.uci').show();
  $('.ucsd').show();
  $('.northridge').show();
  $('.ucsc').show();
  $('.ucb').show();
  $('.cppomona').show();
  $('.cpslo').show();


  if ($('#uci').is(':checked')){
    $('.mit').hide();
    $('.uci').show();
    $('.ucsd').hide();
    $('.northridge').hide();
    $('.ucsc').hide();
    $('.ucb').hide();
    $('.cppomona').hide();
    $('.cpslo').hide();
  }
  else if ($('#ucsd').is(':checked')) {
    $('.mit').hide();
    $('.uci').hide();
    $('.ucsd').show();
    $('.northridge').hide();
    $('.ucsc').hide();
    $('.ucb').hide();
    $('.cppomona').hide();
    $('.cpslo').hide();
  }
  else if ($('#mit').is(':checked')) {
    $('.mit').show();
    $('.uci').hide();
    $('.ucsd').hide();
    $('.northridge').hide();
    $('.ucsc').hide();
    $('.ucb').hide();
    $('.cppomona').hide();
    $('.cpslo').hide();
  }

  else if ($('#ucb').is(':checked')) {
    $('.mit').hide();
    $('.uci').hide();
    $('.ucsd').hide();
    $('.northridge').hide();
    $('.ucsc').hide();
    $('.ucb').show();
    $('.cppomona').hide();
    $('.cpslo').hide();
  }

  else if ($('#northridge').is(':checked')) {
    $('.mit').hide();
    $('.uci').hide();
    $('.ucsd').hide();
    $('.northridge').show();
    $('.ucsc').hide();
    $('.ucb').hide();
    $('.cppomona').hide();
    $('.cpslo').hide();
  }

  else if ($('#ucsc').is(':checked')) {
    $('.mit').hide();
    $('.uci').hide();
    $('.ucsd').hide();
    $('.northridge').hide();
    $('.ucsc').show();
    $('.ucb').hide();
    $('.cppomona').hide();
    $('.cpslo').hide();
  }

  else if ($('#cppomona').is(':checked')) {
    $('.mit').hide();
    $('.uci').hide();
    $('.ucsd').hide();
    $('.northridge').hide();
    $('.ucsc').hide();
    $('.ucb').hide();
    $('.cppomona').show();
    $('.cpslo').hide();
  }

  else if ($('#cpslo').is(':checked')) {
    $('.mit').hide();
    $('.uci').hide();
    $('.ucsd').hide();
    $('.northridge').hide();
    $('.ucsc').hide();
    $('.ucb').hide();
    $('.cppomona').hide();
    $('.cpslo').show();
  }

  else {
    // $('.uci').show();
    // $('.ucsd').show();
    // console.log("hehhehehehsxfdsf");
    }

}
