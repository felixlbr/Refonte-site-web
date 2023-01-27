var colorMode;
$(document).ready(function() {
    colorMode = true;
    $("header").css("position","sticky");
    hauteurNav();
    $(window).resize(function() {refresh()});
    $("button").click(function(){switchMode();});
});
function hauteurNav(){
    $("header").css("top", (0 - $('nav').offset().top) + "px");
}
function refresh() {
    if(document.documentElement.scrollTop>$('nav').offset().top){
        $("header").css("display", "none");
        setTimeout("location.reload()", 1000);
    }
    hauteurNav();    
}