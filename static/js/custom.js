jQuery( document ).ready(function( $ ) {

	"use strict";

    function visible(partial) {
        var $t = partial,
            $w = jQuery(window),
            viewTop = $w.scrollTop(),
            viewBottom = viewTop + $w.height(),
            _top = $t.offset().top,
            _bottom = _top + $t.height(),
            compareTop = partial === true ? _bottom : _top,
            compareBottom = partial === true ? _top : _bottom;

        return ((compareBottom <= viewBottom) && (compareTop >= viewTop) && $t.is(':visible'));

    }

    $(window).scroll(function(){

        if(visible($('.count-digit')))
        {
            if($('.count-digit').hasClass('counter-loaded')) return;
            $('.count-digit').addClass('counter-loaded');
            
            $('.count-digit').each(function () {
                var $this = $(this);
                jQuery({ Counter: 0 }).animate({ Counter: $this.text() }, {
                duration: 3000,
                easing: 'swing',
                step: function () {
                    $this.text(Math.ceil(this.Counter));
                }
                });
            });
        }
    })



    // Collaborator Universities 
    if ($('.owl-partners').length) {
        $('.owl-partners').owlCarousel({
            loop: true,
            nav: false,
            dots: false,
            items: 1,
            margin: 30,
            autoplay: true,
            smartSpeed: 1000,
            autoplayTimeout: 2000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 2,
                    margin: 20
                },
                992: {
                    items: 4,
                    margin: 30
                }
            }
        });
    }
});

$(document).ready(function(){
  $("#l_news").click(function(){
      $("#tr_news").removeClass("d-none");
      $("#tr_research").addClass("d-none");
      $("#tr_project").addClass("d-none");
  });
});

$(document).ready(function(){
  $("#l_research").click(function(){
    $("#tr_news").addClass("d-none");
     $("#tr_research").removeClass("d-none");
      $("#tr_project").addClass("d-none");
  });
});

$(document).ready(function(){
    $("#l_project").click(function () {
      $("#tr_news").addClass("d-none");
     $("#tr_research").addClass("d-none");
      $("#tr_project").removeClass("d-none");
      
  });
});


