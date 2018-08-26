$(document).ready(function(){
    $('span[linkurl]').click(function(){
        var direction = $(this).attr('linkurl');
        setTimeout('document.location = "'+direction+'";', 500);
    }).mousedown(function () {
        $(this).addClass('clicked');
    }).mouseup(function () {
        $(this).removeClass('clicked');
    });;

    $('.card').mousedown(function(){
        $(this).addClass('active');
    }).mouseup(function(){
        $(this).removeClass('active');
    })

    $('.backbutton').mousedown(function(){
        $(this).addClass('active');
    }).mouseup(function(){
        $(this).removeClass('active');
    });
});
