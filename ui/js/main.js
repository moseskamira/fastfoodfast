function openAdminAction(event, adminAction) {
    
    // Declare all variables
    let i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName('tabcontent');
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = 'none';
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName('tablinks');
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(' active', '');
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(adminAction).style.display = 'block';
    event.className += ' active';

}

let offersTab = document.getElementById('defaultOpen'),
    requestsTab = document.getElementById('requests_button'),
    addOrderTab = document.getElementById('add_irder_button'),
    allOrdersTab = document.getElementById('all_orders_button');

offersTab.addEventListener('click', () => openadminAction(offersTab, 'view_orders'));
offersTab.click();
requestsTab.addEventListener('click', () => openOrderAction(requestsTab, 'view_requests'));
addOrderTab.addEventListener('click', () => openAdminAction(addOrderTab, 'add_order'));
allRidesTab.addEventListener('click', () => openAdminAction(allOrdersTab, 'all_orders'));




// Get the header
let header = document.getElementById("myMenu");

// Get the offset position of the navbar
let sticky = header.offsetTop;


// When the user scrolls the page, execute myFunction 
window.onscroll = () => {
    // Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
      } else {
        header.classList.remove("sticky");
      }
};