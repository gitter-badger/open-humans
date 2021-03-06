'use strict';

var $ = require('jquery');

module.exports = function () {
  // AJAX toggling for public data sharing
  $('form.toggle-sharing').on('click', 'input[type=submit]', function (e) {
    e.preventDefault();

    var $form = $(this).parent();
    var formUrl = $form.attr('action');

    var isPublic = $(this).siblings('input[name=public]').val() === 'True';

    var newState = isPublic ? 'False' : 'True';
    var newValue = isPublic ? 'Stop public sharing' : 'Share publicly';

    var self = this;

    $.post(formUrl, $form.serialize(), function () {
      $(self).val(newValue);
      $(self).siblings('input[name=public]').val(newState);
    }).fail(function () {
      // fall back to a regular form submission if AJAX doesn't work
      $form.submit();
    });
  });
};
