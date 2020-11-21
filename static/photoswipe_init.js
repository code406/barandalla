
'use strict';
(function($) {
    var container = [];

    $('#gallery').find('.brick').each(function(){
    var $link = $(this).find('a'),
        item = {
            src: $link.attr('href'),
            w: $link.data('width'),
            h: $link.data('height'),
            title: $link.data('caption')
        };
        container.push(item);
    });

    $('.brick-link').click(function(event){
        event.preventDefault();
        var $pswp = $('.pswp')[0],
            options = {
                index: $(this).parent('.brick').index(),
                bgOpacity: 0.85,
                showHideOpacity: true
            };

        // Initialize PhotoSwipe
        var gallery = new PhotoSwipe($pswp, PhotoSwipeUI_Default, container, options);
        gallery.init();
    });

}(jQuery));