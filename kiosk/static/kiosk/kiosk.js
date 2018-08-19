$(document).ready(function(){
    $('span[linkurl]').click(function(a, b, c){
        document.location = $(this).attr('linkurl');
    })
});
