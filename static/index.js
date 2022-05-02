console.log("I am running!");
let pathname = window.location.pathname;
let pages = ['home', 'sfx', 'gifs', 'login', 'profile']

$(document).ready(function() {
    $('.nav-item').each(function(i) {
        if (pathname.includes($(this).children().first().attr("href"))) $(this).addClass("active");
        else if (this.className.includes('active')) this.removeClass('active');
    });
});