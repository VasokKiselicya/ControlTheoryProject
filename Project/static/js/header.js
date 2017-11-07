$(document).ready(function() {

  $('.selected').click(function() {
    $('.custom-sel').addClass('show-sel');
    $('.custom-sel a').removeClass('hidden');
  });

  $('.custom-sel').focusout(function() {
    $('.custom-sel').removeClass('show-sel');
    $('.custom-sel a:not(:first)').addClass('hidden');
  }).blur(function() {
    $('.custom-sel').removeClass('show-sel');
    $('.custom-sel a:not(:first)').addClass('hidden');
  });

});

// function changeLang(formId) {
//   console.log("HERE");
//     $(`#${formId}`);
// }
