const sidebar = document.getElementById('DocumentationSidebar');
const documentationNotFound = $('#DocumentationNotFound');

var lastNode = null;
$(document).ready(function()
{
	RecalculateSidebar();
	LoadNode(GetSubURL());

	$(window).on('resize', function()
	{
		RecalculateSidebar();
	});

	$(document).on('click', '#DocumentationSidebarToggler', function()
	{
		if (!sidebar.classList.contains('documentation-sidebar-visible')) ShowSidebar();
		else HideSidebar();
	});

	$(document).on('click', '.documentation-namespace-dropdown', function(event)
	{
		let dropdown = $(event.target);
		while (!dropdown.hasClass('documentation-namespace-tab'))
		{
			dropdown = dropdown.parent();
		}

  		ToggleAttribute(dropdown, 'expanded');
	});

	$(document).on('click', '.documentation-namespace-title', function(event)
	{
		let dropdown = $(event.target).parent().children(0);
		ToggleAttribute(dropdown, 'expanded');
	});

	$(document).on('click', '.documentation-classes-information-name', function(event)
	{
		if (lastNode) lastNode.css('color', 'var(--main-text-accent-color)');

		lastNode = $(event.target);
		lastNode.css('color',  'var(--main-interactible-color)');

		let nodeName = lastNode.context.innerHTML;
		LoadNode(nodeName);

	});

	$(document).on('click', '.confetti-button', function(event) {
		let position = GetPositionOfElementInNormalizedScreenSpace($(event.target));
		confetti({
			particleCount: 100,
			startVelocity: 30,
			spread: 360,
			origin: {
				x: position.x,
				y: position.y
			}
		});
	});

	$(document).on('click', '#BadRateIcon', function() 	 { RatePage(1); });
	$(document).on('click', '#AverageRateIcon', function()  { RatePage(2); });
	$(document).on('click', '#GoodRateIcon', function() 	 { RatePage(3); });
});

function RatePage(rating)
{
    $.post(GetURL(), { rating: rating })
        .done(function(response) {
            // Successfully inserted new rating
        })
        .fail(function() {
            $.ajax({
                url: GetURL(),
                type: 'PUT',
                data: { rating: rating },
                success: function(response) {
                    // Successfully updated existing rating
                },
                fail: function(response) {
                    // Failed to insert/update rating
                }
            });
        });
}

function RecalculateSidebar()
{
	if (window.innerWidth >= 1200) ShowSidebar();
	else HideSidebar();
}

function ShowSidebar()
{
	sidebar.classList.remove('documentation-sidebar-hidden');
	sidebar.classList.add('documentation-sidebar-visible');
}

function HideSidebar()
{
	sidebar.classList.remove('documentation-sidebar-visible');
	sidebar.classList.add('documentation-sidebar-hidden');
}

const footer = $('#RateArticle');
const footerUpdateDifference = $('#ArticleFooterModifyTime');
function LoadNode(newNodeName)
{
	// Hide old node article
	const oldNodeName = GetSubURL();
	const oldNode = $(`#${ oldNodeName }Article`);
	oldNode.css('display', 'none');

	// Hide sidebar on small devices
	if (IsDeviceExtraSmall() || IsDeviceSmall() || IsDeviceMedium()) HideSidebar();

	// Show new node article
	const newNode = $(`#${ newNodeName }Article`);
	if (Exists(newNode))
	{
		// Show node's article and hide error article
		newNode.css('display', 'block');
		footer.css('display', 'block');
		documentationNotFound.css('display', 'none');

		// Check if new node is an actual class and not the default
		if (newNodeName !== 'API-Reference')
		{
			// Set the URL to a meaningful one
			if (oldNodeName === 'API-Reference') SetPageURL(GetURL() + newNodeName + '/');
			else SetPageURL(GetNonSubURL() + newNodeName + '/');

			// Expand the whole tree leading to our node
			let nodeObject = $(`#${ newNodeName }Node`);
			while (!nodeObject.hasClass('documentation-origin'))
			{
				nodeObject = nodeObject.parent();
				if (nodeObject.hasClass('documentation-namespace-tab'))
				{
					nodeObject.attr('expanded', 'true');
				}
			}

			// Calculate update time difference
			const classUpdateDateElement = newNode.find('.docs-time');
			if (Exists(classUpdateDateElement))
			{
				let dateParts = classUpdateDateElement.html().substring(14, classUpdateDateElement.html().length).split('.');
				let updateDate = new Date(dateParts[2], dateParts[1] - 1, dateParts[0]);
				let dateDifference = updateDate - new Date(Date.now());

				let dateDifferenceString = FormatDateDifference(dateDifference);
				dateDifferenceString = dateDifferenceString.charAt(0).toUpperCase() + dateDifferenceString.substring(1, dateDifferenceString.length);
				footerUpdateDifference.html(`Last updated: ${ dateDifferenceString }`);
			}
		}
		else
		{
			footerUpdateDifference.html('');
		}
	}
	else
	{
		// Show error article
		documentationNotFound.css('display', 'block');
		footer.css('display', 'none');
	}
}