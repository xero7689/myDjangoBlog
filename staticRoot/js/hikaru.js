/*fadeIn display*/
$(window).load(function(){
	$(".index_article").hide().fadeIn('fast');
	$(".post_article").hide().fadeIn('fast');
	$(".tag_Post_List").hide().slideDown('fast');
	$("#about").slideDown('fast');
	$("#tag_list").slideDown('fast');
	$("#contact").slideDown('fast');
	$("#archive").slideDown('fast');
	$("#img_set").hide().fadeIn('fast');
	
	/***masnry***/
	//post
	
	var $container = $('#post');
	$container.imagesLoaded(function(){
	$container.masonry({
	isAnimated: true,
	
		});
	});
	
	/*//work
	var $work_container = $('#work');
	$work_container.imagesLoaded(function(){
	$work_container.masonry({
		  columnWidth: 30,
		});
	});*/
	/***masnry***/
	
	
  /*left_panel_widget_animate*/
  $(".left_panel_widget_title").mouseenter(function(){
  $(this).animate({opacity: '1'}, "fast");
  });
  $(".left_panel_widget_title").mouseleave(function(){
    $(this).animate({opacity: '0.6'}, "fast");
  });
  
  /*index_post_continue_bottom*/
  $(".index_article").mouseenter(function(){
  $(this).children(".continue").fadeIn("fast");
  });
  $(".index_article").mouseleave(function(){
  $(this).children(".continue").fadeOut("fast");
  });  
  
	$("#img_preview_window").hide();
  /*style the width of every work image*/
  /*created by myself. Peter Lee TwT*/
	var img_thumb_set = document.querySelectorAll(".image_thumb");
	var total_width = 0;
	var window_width = $("#img_preview_window").width();
	var window_height = $("#img_preview_window").height();
	
	for(var i = 0; i < img_thumb_set.length; i++)
	{
		img_thumb_set[i].parentNode.style.width = img_thumb_set[i].clientWidth + "px";
		total_width += img_thumb_set[i].clientWidth;
	}
	//set tumb_set_width
	$("#img_set").css({"width": total_width});

	/*scroll image button*/
	
	var move_space_max = total_width - window_width;
	var rest_space = move_space_max;
	var scroll_interval = 400 //px
	$("#work_right_button").click(function(){
		if(rest_space >= 0){	//still have space to scroll
			if(rest_space >= scroll_interval){	//if rest of space isenough for an interval
				$("#img_set").animate({left:"-=" + scroll_interval + "px"}, "2000");
				rest_space -= scroll_interval;
			}
			else // rest of space is not enough for an interval
			{
				$("#img_set").animate({left:"-=" + rest_space + "px"}, "2000");
				rest_space -= rest_space; //now the rest_space = 0;
			}
		}
	});
	
	$("#work_left_button").click(function(){
		if(rest_space < move_space_max){
			if((move_space_max - rest_space) >= scroll_interval){
				$("#img_set").animate({left:"+=" + scroll_interval + "px"}, "2000");
				rest_space += scroll_interval;
			}
			else
			{
				$("#img_set").animate({left:"+=" + (move_space_max - rest_space) + "px"}, "2000");
				rest_space += (move_space_max - rest_space);
			}
		}
	});

	
	/*Show image in preview window*/
	$(".image_thumb").click(function(){
		$("#img_preview_window").slideDown();
		var src= $(this).attr("data-img-href");
		var img_width = $(this).attr("data-img-width");
		var img_height= $(this).attr("data-img-height");
		var w_ratio;
		var h_ratio;
		var f_r;
		var f_w;
		var f_h;
		
		if(img_width > window_width || img_height > window_height)
		{
			//count ratio
			w_ratio = window_width / img_width;
			h_ratio = window_height/ img_height;
			//get the smaller
			if(w_ratio > h_ratio)
			{
				f_r = h_ratio;
			}
			else if(w_ratio < h_ratio)
			{
				f_r = w_ratio;
			}
			//count final width/height
			f_w = img_width * f_r;
			f_h = img_height * f_r;
		}
		else
		{
			f_w = img_width;
			f_h = img_height;
		}
		//image vertical center
		var v_c = (window_height - f_h)/2
		var image = $("<img  />").attr("src", src).attr("width", f_w).attr("height", f_h);
		$("#img_preview").css({"top": v_c + "px"});
		$("#img_preview").hide().html(image).fadeIn();
		$("#img_log").text(total_width + "px");
	});

});
