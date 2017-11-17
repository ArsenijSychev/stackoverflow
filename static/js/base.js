$(function () {
	$('.subnavbar').find ('li').each (function (i) {
		var mod = i % 3;
		if (mod === 2) {
			$(this).addClass ('subnavbar-open-right');
		}
	});
	var screenHeight = window.innerHeight + 100;
	var footerHeight = $('.footer').height();
	$('.main').css('min-height', (screenHeight - footerHeight - 183) + 'px');
});
var main_row = $('#dv-main-row');
var notifications = {
	time_show: 300,
	time_hide: 300,
	time_close: 3000,
	div: $('#dv-notifications-pane'),
	template_close: $('<a />', { 'href': '#', 'class': 'close', 'data-dismiss': 'alert', 'aria-label': 'close', 'html': '&times;' }),
	template: '<div class="alert alert-{alert_class}">'
			+ '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>'
			+ '<strong>{alert_strong_text}</strong>{alert_text}</div>',
	classes: {
		success: 'alert-success',
		error: 'alert-danger',
		warning: 'alert-warning',
		info: 'alert-info'
	},
	strong: {
		success: 'Success! ',
		error: 'Error! ',
		warning: 'Warning! ',
		info: 'Info! '
	},
	error: function(text){
		notifications.show(notifications.build('error', text));
	},
	info: function(text){
		notifications.show(notifications.build('info', text));
	},
	success: function(text){
		notifications.show(notifications.build('success', text));
	},
	warning: function(text){
		notifications.show(notifications.build('warning', text));
	},
	show: function(alert){
		notifications.div.append(alert);
		alert.show(notifications.time_show, function(el){
			setTimeout(function(){
				alert.hide(notifications.time_hide, function(){
					alert.remove();
				});
			}, notifications.time_close);
		});
	},
	build: function(type, text){
		var div = $('<div />', { 'class': 'alert' }).hide();
		div.addClass(notifications.classes[type]);
		div.append(notifications.template_close.clone());
		div.append($('<strong />', { 'html': notifications.strong[type] }));
		div.html(div.html() + text);
		return div;
	}
};
var fade_screen = function(){
	main_row.prepend($('<div />', { 'class': 'modal-backdrop fade in' }));
};
var un_fade_screen = function(){
	main_row.find('.modal-backdrop').remove();
};
var get_csrf = document.cookie.match(/csrftoken=([^\s]+)/)[1];
