const navbar = document.getElementById('NavBar');
const navbarList = document.getElementById('NavBarList');

/* --- GENERAL --- */

$(document).ready(function()
{
    $('.autocomplete-form input').autocomplete({
        maxResult: 5
    })

    $('.autocomplete-form .dropdown-menu').on('click', function(event) {
        $(event.target).submit();
    });

    $(document).on('click', '#MobileNavBarClose', function()
    {
        MoveNavbar(false, function() {
            navbar.classList.add('navbar');
            navbar.classList.remove('mobile-navbar');
        });
        ToggleAttribute($(navbar), 'expanded');
    });

    $(document).on('click', '#MobileNavBarOpen', function()
    {
        navbar.classList.add('mobile-navbar');
        navbar.classList.remove('navbar');

        MoveNavbar(open, null);
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


function MoveNavbar(open, onfinish)
{
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

    let id = setInterval(frame, Number.EPSILON);
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

/* --- SPECIFIC --- */

function SubmitDocumentationSearch(form)
{
    let search = form.search.value;
	if (search !== '')
	{
        let autocompleteMenu = $(form).find('.dropdown-menu');
        if (Exists(autocompleteMenu) && autocompleteMenu.children().length > 0)
        {
            if (!location.href.includes('API-Reference'))
            {
                location.href = '/Documentation/API-Reference/' + search;
            }
            else
            {
                LoadNode(search);
                form.search.value = '';
            }
        }
	}

	return false;
}

const dateFormatter = new Intl.RelativeTimeFormat('en', { numeric: 'auto' });
function FormatDateDifference(date)
{
    let dayCount = Math.abs(Math.floor(date / 86400000));
    if (dayCount <= 30)
    {
        return dateFormatter.format(Math.round(date / 86400000), 'day');
    }
    else
    {
        let monthCount = Math.abs(Math.floor(date / 2678400000));
        if (monthCount <= 12)
        {
            return dateFormatter.format(Math.round(date / 2678400000), 'month');
        }
        else
        {
            return dateFormatter.format(Math.round(date / 31536000000), 'year');
        }
    }
}