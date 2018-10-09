import {Alert} from './dialogs.js';
import {siteHeaders, goToLogin, showNoNetwork, noContentFound, displayTableData} from './reusable.js';
document.getElementById('defaultOpen').addEventListener('click', getAllRides);
let loader = document.getElementById('loader');
// var request = new XMLHttpRequest()
// request.open('GET', 'https://apifastfoodfast.herokuapp.com/api/v1/users/orders ')
// request.onload = function(){

// }
// request.send();

document.getElementById('defaultOpen').click();

function getAllOrders(){
    loader.style.display = 'block';
    let rideOffersMessage = document.getElementById('order_message');
    let allOrdersDiv = document.getElementById('all_orders_div');
    fetch('https://apifastfoodfast.herokuapp.com/api/v1/admin/orders', {
        headers: siteHeaders
    })
        .then((res) => res.json())
        .then((data) => {
            const message  = 'results retrieved successfully';
            if (data.message === message){
                if(data.order.length > 0){
                    let tableRows = '';
                    data.orders.forEach(order => {
                        tableRows += `
                            <tr>
                                <td>${order.order_name}</td>
                                <td>${order.quantity}</td>
                                <td>${order.total_amount}</td>
                                <td>${order.payment_mode}</td>
                            </tr>
                        `;
                    });
                    displayTableData(loader, 'orders_data', tableRows, allOrdersDiv);
                    makeDetailsModelActive();
                }else{
                    noContentFound(loader, allOrderssDiv, ordersMessage, 'No orders currently available');
                }
            
            }else{
                goToLogin();
            }
        });
}

let order_id = null;

// Get the modal
function makeDetailsModelActive() {

    const modal = document.getElementById('details_modal');

    // Get the button that opens the modal
    let btns = document.getElementsByClassName('view_details');
    
    // Get the <span> element that closes the modal
    const span = document.getElementsByClassName('close')[0];
    
    // Get the button that closes the modal
    const btn1 = document.getElementById('cancel_request');
    
    // When the user clicks on the button, open the modal
    [].forEach.call(btns, (el) => {
        el.addEventListener('click', () => {
            modal.style.display = 'block';
            getSingleOrder(el.id);
            order_id = el.id;
        });
    });
    
    // When the user clicks on the button, close the modal
    btn1.onclick = function(){
        modal.style.display = 'none';
    };
    
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = 'none';
    };
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    };

}

function getSingleOrder(order_Id){
    loader.style.display = 'block';
    fetch('http://127.0.0.1:5000//api/v1/orders/'+order_Id, {
        headers: siteHeaders
    })
        .then((res) => res.json())
        .then((data) => {
            const message = 'result retrieved successfully';
            if(data.message === message){

                let tableRow = `
                <tr>
                    <td>${data.order.order_name}</td>
                    <td>${data.order.quantity}</td>
                    <td>${data.order.total_amount}</td>
                    <td>${data.order.payment_mode}</td>
                </tr>
            `;
                loader.style.display = 'none';
                document.getElementById('order_data').innerHTML = tableRow;

            }else{
                goToLogin();
            }
            
        });

}

document.getElementById('order_request').addEventListener('click', joinARide);

function joinARide(){
    loader.style.display = 'block';
    fetch(`http://127.0.0.1:5000/api/v1/orders/${order_id}/requests`, {
        method: 'POST',
        headers: siteHeaders,
        cache: 'no-cache'
    })
        .then((res) => res.json())
        .then((data) => {
            let responseMessage = data.message;
            if(responseMessage === 'request sent successfully'){
                loader.style.display = 'none';
                Alert.render('Request sent successfully!');
            }else if(responseMessage === 'Request already exists'){
                loader.style.display = 'none';
                Alert.render('Request already exists!');
            }else{
                goToLogin();
            }
        })
        .catch(() => {
            showNoNetwork(loader);
        });

}
