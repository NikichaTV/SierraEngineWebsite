const navbar = document.getElementById('NavBar');
const navbarList = document.getElementById('NavBarList');

$(document).ready(function()
{
    $('.autocomplete-form input').autocomplete({
        maxResult: 5
    })

    $(document).on('click', '#MobileNavBarClose', function()
    {
        // navbarList.animate([{ transform: 'translateX(-10vw)'}, { transform: 'translateX(10vw)' }], { duration: 350, iterations: 1, easing: 'ease-in-out' }).onfinish = (event) =>
        // {

            MoveSidebar(false, function() {
                navbar.classList.add('navbar');
                navbar.classList.remove('mobile-navbar');
            });
        // }
        ToggleAttribute($(navbar), 'expanded');
    });

    $(document).on('click', '#MobileNavBarOpen', function()
    {
            navbar.classList.add('mobile-navbar');
            navbar.classList.remove('navbar');
            MoveSidebar(open, null);
        // navbarList.animate([{ transform: 'translateX(10vw)'}, { transform: 'translateX(-10vw)' }], { duration: 350, iterations: 1, easing: 'ease-in-out' }).onfinish = (event) => {
        //
        // }
        ToggleAttribute($(navbar), 'expanded');
    });

    CheckFooter();

    $(window).resize(function()
    {
        CheckFooter();
    });

    $(window).scroll(function()
    {
        CheckFooter();
    });

    $(window).on('click', function()
    {
        CheckFooter()
    });
});

var id = null;
function MoveSidebar(open, onfinish) {
    const SPEED = 2;

    let target, right;
    if (open)
    {
        target = 0
        right = -100
    }
    else
    {
        target = -100
        right = 0
    }

    clearInterval(id);
    id = setInterval(frame, Number.EPSILON);
    function frame()
    {
        if (right === target)
        {
            clearInterval(id);
            if (onfinish != null) onfinish();
        }
        else
        {
            if (right < target) right += SPEED;
            else right -= SPEED;
            navbarList.style.right = right + 'vw';
        }
    }
}

window.matchMedia('(prefers-color-scheme: light)').addEventListener('change',({ matches }) => {
  if (matches) OnLightTheme();
  else OnDarkTheme();
});

let themeColor = document.getElementById('ThemeColor');
function OnLightTheme()
{
    themeColor.setAttribute('content', '#FFFFFF');
}

function OnDarkTheme()
{
    themeColor.setAttribute('content', '#202125');
}

const copyrightSection = document.getElementById('CopyrightSection');

function CheckFooter()
{
    if ($(window).scrollTop() + $(window).height() >= $(document).height() - $(document).height() / 63.0) copyrightSection.style.opacity = '1.0'; // Scrolled to bottom
    else copyrightSection.style.opacity = '0.0';
}