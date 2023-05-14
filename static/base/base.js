const BREAKPOINT_SMALL = 576;
const BREAKPOINT_MEDIUM = 768;
const BREAKPOINT_LARGE = 992;
const BREAKPOINT_EXTRA_LARGE = 1200;
const BREAKPOINT_EXTRA_EXTRA_LARGE = 1400;

function IsDeviceExtraSmall()
{
    return $(document).width() < BREAKPOINT_SMALL;
}

function IsDeviceSmall()
{
    return $(document).width() >= BREAKPOINT_SMALL && $(document).width() < BREAKPOINT_MEDIUM;
}

function IsDeviceMedium()
{
    return $(document).width() >= BREAKPOINT_MEDIUM && $(document).width() < BREAKPOINT_LARGE;
}

function IsDeviceLarge()
{
    return $(document).width() >= BREAKPOINT_LARGE && $(document).width() < BREAKPOINT_EXTRA_LARGE;
}

function IsDeviceExtraLarge()
{
    return $(document).width() >= BREAKPOINT_LARGE && $(document).width() < BREAKPOINT_EXTRA_LARGE;
}

function IsDeviceExtraExtraLarge()
{
    return $(document).width() >= BREAKPOINT_EXTRA_EXTRA_LARGE;
}

function SetPageURL(url)
{
    window.history.pushState({ }, document.title, url);
    window.history.replaceState({ }, document.title, url);
}

function SetPageTitle(title)
{
    document.title = title;
}

function GetURL()
{
    return window.location.href;
}

function GetSubURL()
{
	let url = window.location.href;
	url = url.substring(0, url.length - 1);
    return url.substring(url.lastIndexOf('/') + 1, url.length);
}

function GetNonSubURL()
{
    let url = window.location.href;
    url = url.substring(0, url.length - 1);
    return url.substring(0, url.lastIndexOf('/') + 1);
}

function Exists(element)
{
    return element.length !== 0;
}

function SetAttribute(element, attributeName, attributeValue)
{
    element.attr(attributeName, attributeValue);
}

function ToggleAttribute(element, attributeName)
{
    let attribute = element.attr(attributeName);
    if (attribute === 'true')
    {
        element.attr(attributeName, 'false');
        return false;
    }
    else
    {
        element.attr(attributeName, 'true');
        return true;
    }
}

function AreCookiesAllowed()
{
    return navigator.cookieEnabled;
}

function GetPositionOfElementInNormalizedScreenSpace(element)
{
	// Get the element's offset position relative to the document
	const offset = element.offset();

	// Calculate the element's position relative to the viewport
	const top = offset.top - $(window).scrollTop();
	const left = offset.left - $(window).scrollLeft();

	// Calculate the normalized coordinates
	const viewportWidth = $(window).width();
	const viewportHeight = $(window).height();
	const x = left / viewportWidth;
	const y = top / viewportHeight;

	// Return the normalized coordinates as an object
	return { x, y };
}