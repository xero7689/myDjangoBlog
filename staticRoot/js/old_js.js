/*scroll slide album*/
	
	for(var i = 0; i < img_thumb_set.length; i++)
	{
		img_thumb_set[i].parentNode.style.width = img_thumb_set[i].clientWidth + "px";
		total_width += img_thumb_set[i].clientWidth;
	}
	//set tumb_set_width
	$("#img_set").css({"width": total_width});

	/*scroll image button*/
	//count thumb_end
	var thumb_index_left = 0;
	var thumb_index_right = window_width;
	var thumb_left = 0;
	var rest_space = total_width - window_width;
	var scroll_interval = 200 //px
	$("#work_left_button").click(function(){
		if(rest_space < total_width){
			$("#img_set").animate({left:"+=" + scroll_interval + "px"}, "2000");
			rest_space += scroll_interval;
			
		}
	});
	$("#work_right_button").click(function(){
		if(rest_space >= 0){	//still have space to scroll
			if(rest_space >= scroll_interval){	//if rest of space isenough for an interval
				$("#img_set").animate({left:"-=" + scroll_interval + "px"}, "2000");
				rest_space -= scroll_interval;
			}
			else // rest of space is not enough for an interval
			{
				$("#img_set").animate({left:"-=" + rest_space + "px"}, "2000");
				rest_space -= rest_space;
			}
		}
	});
