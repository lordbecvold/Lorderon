
$( document ).on( "mousemove", function( event ) {
	
	if($(window).width() >= 800){
		
		centerX = event.pageX - $(window).width()/2;
		centerY = event.pageY - $(window).height()/2;
		
		houseDefaultX = $(window).width()-1622;
		houseDefaultY = $(window).height()-767;
		houseMoveX = houseDefaultX + centerX/250;
		houseMoveY = houseDefaultY + centerY/250;
		
		lycanDefaultX = -485;
		lycanDefaultY = -135;
		lycanMoveX = lycanDefaultX + -(centerX/100);
		lycanMoveY = lycanDefaultY + -(centerY/100);
		
		
		$('#houses').css({
			'background-position': +houseMoveX+'px '+houseMoveY+'px'
		});
		
		$('#lycan').css({
			'background-position': +lycanMoveX+'px '+lycanMoveY+'px'
		});
		
		$('#highlight').css({
			'top': +event.pageY+'px',
			'left': +event.pageX+'px'
		});
		
	}
	
});

$(window).resize(function(){
	$('#shownnav ul').perfectScrollbar('update');
});

$(document).ready(function() {
	
	if($(window).width() >= 800){
		$('#getContent').after('<video src="img/bg-animation.mp4" autoplay loop></video><div id="lycan"></div><div id="lycan_shadow"></div><div id="spears"></div>');
	}
	
    $('#shownnav ul').perfectScrollbar();
	
	$('#sec_down').click(function(){
		$.fn.fullpage.moveSectionDown();
	});
	
		
	$('#menuToggle').click(function(){
		$('#shownnav ul').perfectScrollbar('update');
		$('#shownnav').fadeToggle();
		$('#menuToggle').toggleClass('naviconActive');
		$('main, #sec_down, #fp-nav, #lycan, #lycan_shadow').toggleClass('mainBlur');
	});
	
	$('#shownnav ul li a').click(function(){
		$('#shownnav ul').perfectScrollbar('update');
		$('#shownnav').fadeToggle();
		$('#menuToggle').toggleClass('naviconActive');
		$('main, #sec_down, #fp-nav, #lycan, #lycan_shadow').toggleClass('mainBlur');
	});
	
	if($(window).width() < 1210){
		if($(window).width() < 1024){
			if($(window).width() < 800){
				$('#fullpage').fullpage({
					'verticalCentered': true,
					'css3': false,
					anchors:['intro', 'registration', 'download', 'ranking', 'vop', 'problems'],
					'sectionsColor': ['rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)'],
					'navigation': false,
					'scrollOverflow': true,
					'paddingTop':'22%',
					'paddingBottom':'12%',


				});
			}else{
				$('#fullpage').fullpage({
					'verticalCentered': true,
					'css3': false,
					anchors:['intro', 'registration', 'download', 'ranking', 'vop', 'problems'],
					'sectionsColor': ['rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)'],
					'navigation': true,
					'scrollOverflow': true,
					'paddingTop':'16%',
					'paddingBottom':'8%',
					'showActiveTooltip':false,
					'navigationPosition': 'right',
					'navigationTooltips': ['Úvod', 'Registrace', 'Stažení', 'Žebříček', 'vop', 'problems'],

					'onLeave': function(index, nextIndex){
						if(nextIndex == 1){
							$('#lycan,#lycan_shadow').fadeIn();
							$('.sd_text').text("go on a journey");
							if($(window).width() < 1690){
								$('#sec_down').css({'bottom':'120px'});
							}else{
								$('#sec_down').css({'bottom':'190px'});
							}
						}else{
							$('#lycan,#lycan_shadow').fadeOut();
							$('.sd_text').text("go on");
							if($(window).width() < 1690){
								$('#sec_down').css({'bottom':'30px'});
							}else{
								$('#sec_down').css({'bottom':'70px'});
							}
						}
						
					}
					

				});
				
			}
		}else{
			$('#fullpage').fullpage({
				'verticalCentered': true,
				'css3': false,
				anchors:['intro', 'registration', 'download', 'ranking', 'vop', 'problems'],
				'sectionsColor': ['rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)'],
				'navigation': true,
				'scrollOverflow': true,
				'paddingTop':'12%',
				'paddingBottom':'8%',
				'showActiveTooltip':false,
				'navigationPosition': 'right',
				'navigationTooltips': ['Úvod', 'Registrace', 'Stažení', 'Žebříček', 'vop', 'problems'],

				'onLeave': function(index, nextIndex){
					if(nextIndex == 1){
						$('#lycan,#lycan_shadow').fadeIn();
						$('.sd_text').text("go on a journey");
						if($(window).width() < 1690){
							$('#sec_down').css({'bottom':'120px'});
						}else{
							$('#sec_down').css({'bottom':'190px'});
						}
					}else{
						$('#lycan,#lycan_shadow').fadeOut();
						$('.sd_text').text("go on");
						if($(window).width() < 1690){
							$('#sec_down').css({'bottom':'30px'});
						}else{
							$('#sec_down').css({'bottom':'70px'});
						}
					}
					
				}
				
			});

		}
	}else{
		$('#fullpage').fullpage({
			'verticalCentered': true,
			'css3': false,
			anchors:['intro', 'registration', 'download', 'ranking', 'vop', 'problems'],
			'sectionsColor': ['rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)'],
			'navigation': true,
			'scrollOverflow': true,
			'paddingTop':'6%',
			'paddingBottom':'8%',
			'showActiveTooltip':true,
			'navigationPosition': 'right',
			'navigationTooltips': ['Úvod', 'Registrace', 'Stažení', 'Žebříček', 'vop', 'problems'],

			'onLeave': function(index, nextIndex){
				if(nextIndex == 1){
					$('#lycan,#lycan_shadow').fadeIn();
					$('.sd_text').text("go on a journey");
					if($(window).width() < 1690){
						$('#sec_down').css({'bottom':'140px'});
					}else{
						$('#sec_down').css({'bottom':'190px'});
					}
				}else{
					$('#lycan,#lycan_shadow').fadeOut();
					$('.sd_text').text("go on");
					if($(window).width() < 1690){
						$('#sec_down').css({'bottom':'30px'});
					}else{
						$('#sec_down').css({'bottom':'70px'});
					}
				}
				
			}
			
		});
	}
	
    $('#reg_pw').keyup(function() {
		
		safety = 0;
		safety = $(this).val().length;
		
		if($(this).val().match(/\d+/g) != null){
			safety = safety + 5;
		}
		
		if($(this).val().match(/[A-Z]/) != null){
			safety = safety + 5;
		}
		
		if(/^[a-zA-Z0-9- ]*$/.test($(this).val()) == false) {
			safety = safety + 5;
		}
		
		if(safety <= 11){
			$(".pws").css({'color':'red'}).text("Unsicher");
		}else if(safety > 11 && safety <= 20){
			$(".pws").css({'color':'orange'}).text("Okay");
		}else if(safety > 20 && safety <= 30){
			$(".pws").css({'color':'yellow'}).text("Sicher");
		}else if(safety > 30 && safety <= 50){
			$(".pws").css({'color':'green'}).text("Unknackbar!");
		}else if(safety > 50 && safety <= 55){
			$(".pws").css({'color':'orange'}).text("Hör auf random Zeichen in das Inputfeld zu hämmern!");
		}else if(safety > 55){
			$("body").addClass("nybumode");
			if(!$("#nybucat").length){
				$("body").append("<audio id='nybucat' autoplay><source src='sound/nybumode.mp3' type='audio/mpeg'></audio>")
			}
			setTimeout(function(){
			  alert("Secret nybu mode activated!");
			}, 2000);
		}
		
    });
	
	
	$('#reg_pw2').keyup(function() {
		
		if($('#reg_pw').val() == $('#reg_pw2').val()){
			$(".pwc").css({'color':'green'}).text("Passwörter stimmen überein!");
		}else{
			$(".pwc").css({'color':'red'}).text("Passwörter stimmen nicht überein!");
		}
			
	});
	
	
});

jQuery(window).load(function () {
   
   $( ".section" ).each(function( index ) {
		$(this).find('.slimScrollBar').hide();
		$(this).find('.slimScrollRail').hide();
	});

});


