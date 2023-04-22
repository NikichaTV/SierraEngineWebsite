let mobileNavbarSizeRequirement = 991;
let navbar = document.getElementById('NavBar');
let copyrightSection = document.getElementById("CopyrightSection");

var lastDocumentSize = $(document).width();

$(document).ready(function()
{
    CheckFooter();

    $(document).on('click', '#MobileNavBarClose', async function()
    {
        navbar.style.opacity = '0';
        navbar.classList.add('navbar');
        navbar.classList.remove('mobile-navbar');
    });

    $(document).on('click', '#MobileNavBarOpen', async function()
    {
         // 192.168.100.255

        navbar.style.opacity = '1';
        navbar.classList.add('mobile-navbar');
        navbar.classList.remove('navbar');
    });

    $(window).resize(function()
    {
        CheckFooter();
        CheckNavbar();
    });

    $(window).scroll(function()
    {
        CheckFooter();
    });
});

function CheckNavbar()
{
    let currentDocumentSize = $(document).width();
    if (currentDocumentSize > lastDocumentSize && currentDocumentSize > mobileNavbarSizeRequirement)
    {
        let oldDuration= navbar.style.transitionDuration;
        navbar.style.transitionDuration = '0';
        navbar.style.opacity = '1';
        navbar.style.transitionDuration = oldDuration;
    }
    else if (currentDocumentSize <= lastDocumentSize && currentDocumentSize <= mobileNavbarSizeRequirement)
    {
        let oldDuration= navbar.style.transitionDuration;
        navbar.style.transitionDuration = '0';
        navbar.style.opacity = '0';
        navbar.style.transitionDuration = oldDuration;
    }

    lastDocumentSize = currentDocumentSize;
}

function CheckFooter()
{
    if ($(window).scrollTop() + $(window).height() >= $(document).height() - $(document).height() / 63.0)
    {
        // Scrolled to bottom
        copyrightSection.style.opacity = 1.0;
    }
    else
    {
        copyrightSection.style.opacity = 0.0;
    }
}

function Delay(time)
{
    return new Promise(resolve => setTimeout(resolve, time * 1000));
}