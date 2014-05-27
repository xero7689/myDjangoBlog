//Seudo Code of album
$(".image_thumb").click(function(){
	var src= $(this).attr("data-img-href");
	image = $("<img />").attr("src", src);
$("#img_preview").hide().html(image).fadeIn();

$("#img_preview").html(image);
var img_width = $("#img_preview").clientWidth
var img_height= $("#img_preview").clientHeight
