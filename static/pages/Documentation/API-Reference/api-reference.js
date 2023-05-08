const sidebar = document.getElementById('DocumentationSidebar');
const documentationNotFound = $('#DocumentationNotFound');

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
		let nodeName = $(event.target).context.innerHTML;
		LoadNode(nodeName);
	});
});

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
		}
	}
	else
	{
		// Show error article
		documentationNotFound.css('display', 'block');
	}
}