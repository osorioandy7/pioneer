console.log("Hello World")
function hideTopics(){
$('#pickCollege').hide();
$('#pickMajor').hide();
$('#pickFinancial').hide();
$('#pickLinks').hide();
$(".slider").hover(highlightIn,highlightOut);
}
function highlightIn(){
$(this).css("background-color", "#b3b3b3");
}
function highlightOut(){
  $(this).css("background-color", "#cccccc");
}

function slideCollege(){
$('#pickCollege').slideToggle();
}


function slideMajor(){
$('#pickMajor').slideToggle();
}

function slideFinancial(){
$('#pickFinancial').slideToggle();
}
function slideLinks(){
$('#pickLinks').slideToggle();
}

function setUpListener(){
$('#pickMajor').click(slideMajor);
$('#pickFinancial').click(slideFinancial);
$('#pickCollege').click(slideCollege);
}

$(document).ready(hideTopics);
$(document).ready(setUpListener);
