$('.modal').on("show.bs.modal", function () {
    $(this).find('.lazy_load').each(function(){
        var img = $(this);
        var attr = img.attr('src')
        if(typeof attr == 'undefined' || attr == false) {
            console.log(`lazy loading ${img.data('src')}`)
            img.attr('src', img.data('src'));
        }
    });
});
