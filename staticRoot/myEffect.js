$(document).ready(function(){
	$(".indexPost").hover(function(){
		$(this).animate({zoom: '125%'}, 'fast');
		},
		function(){
		$(this).animate({zoom: '100%'}, 'fast');
	});
});