
document.getElementById('add_order_form').addEventListener('submit', addOrder);

function addOrder(e){
    e.preventDefault();

    let order_name = document.getElementById('order_name').value,
        quantity = parseInt(document.getElementById('quantity').value),
        total_amount = parseInt(document.getElementById('total_amount').value),
        payment_mode = document.getElementById('payment_mode').value;

    let data = {order_name, quantity, total_amount, payment_mode};

     var str = document.location.search;
     var parts = str.split(/[#\?&]/g); 
     var filteredParts = parts.filter(function (part) {
     return part.split('=')[0] === 'Authorization';
     });
     var auth_token = filteredParts[0].split('=')[1];
     alert(auth_token);

    fetch('http://127.0.0.1:5000/api/v1/users/orders' ,{
        method: 'POST',
        cache: 'no-cache',
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': auth_token
        },
        body: JSON.stringify(data)
    })
        .then((res) => res.json())
        .then((data) => {
            if(data.Message === 'Order Added Successfully'){
                alert('Order added successfully');
            }
            else{
                alert('Order Not Created ');
            }
        } )
}

// document.getElementById('all_orders_button').addEventListener('click', getOrdersPlaced);


// function getOrdersPlaced(){
//     // loader.style.display = 'block';
//     fetch('http://127.0.0.1:5000/api/v1/admin/orders', {
//         // headers: siteHeaders
//     })
//         .then((res) => res.json())
//         .then((data) => {
//             const message = 'Order Successfully Fetched';
//             if(data.Message === message){
//                 let numberOfOrdersPlacedMessage = null;
//                 if(data.requests.length > 0){
//                     let ordersplaced = [];
//                     data.requests.forEach(order => {
//                         ordersplaced.push(
//                             {
//                                 'order_id': order_id,
//                                 'user_name': user_id,
//                                 'order_name': order_name,
//                                 'quantity': quantity,
//                                 'total_amount': total_amount,
//                                 'payment_mode': payment_mode
//                             });
//                     });
//                     numberOfOrdersPlacedMessage = `<p>Number of Orders Placed: ${data.requests.length}</p>`;
//                     displayNumber('no_of_orders_placed', numberOfOrdersPlacedMessage);
//                     getOrdersPlaced(ordersplaced);
//                 }else{
//                     numberOfOrdersPlacedMessage = '<p>Number of Orders Placed: 0</p>';
//                     displayNumber('no_of_orders_placed', numberOfOrdersPlacedMessage);
//                     getOrdersPlaced([]);
//                 }
//             }else{
//                 goToLogin();
//             }
            
//         });
// }

// function getOrdersPlaced(getOrdersPlaced){
//     let ordersMessage = document.getElementById('orders_placed_message');
//     let ordersDiv =  document.getElementById('placed_div');
//     fetch('http://127.0.0.1:5000/api/v1/user/orders', {
//         headers: siteHeaders
//     })
//         .then((res) => res.json())
//         .then((data) => {
//             const message = 'results retrieved successfully';
//             if(data.message === message){
//                 let numberOfOrdersPlacedMessage = null;
//                 if(data.orders.length > 0){
//                     let ordersPlaced = [];
//                     data.orders.forEach(order => {
//                         ordersPlaced.push({
//                             'order_name': order_name,
//                             'quantity': quantity,
//                             'total_amount': total_amount,
//                             'payment_mode': 'payment_mode'
//                         });
//                     });
//                     let orders = [...ordersPlaced];
//                     numberOfOrdersPlacedMessage = `<p>Number of Orders Placed: ${data.orders.length}</p>`;
//                     displayNumberPlaced('no_of_orders_placed', numberOfOrdersPlacedMessage); 
//                     displayToUser(orders);
//                 }else if(ordersPlaced.length > 0){
//                     numberOfOrdersPlacedMessage = '<p>Number of Orders Placed: 0</p>';
//                     displayNumberPlaced('no_of_orders_placed', numberOfOrdersPlacedMessage); 
//                     displayToUser(ordersPlaced);
//                 }else{
//                     numberOfOrdersPlacedMessage = '<p>Number of Orders Placed: 0</p>';
//                     displayNumberPlaced('no_of_orders_placed', numberOfOrdersPlacedMessage); 
//                     noContentFound(loader, ordersDiv, ordersMessage, 'You have not Placed orders yet');
//                 }
//             }else{
//                 goToLogin();
//             }
            
//         });
// }

// function displayToUser(ordersPlaced){
//     let orddersDiv =  document.getElementById('placed_div');
//     let tableData = '';
//     ordersPlaced.forEach(order => {
//         tableData += `
//         <tr>
//             <td>${order_name}</td>
//             <td>${quantity}</td>
//             <td>${total_amount}</td>
//             <td>${payment_mode}</td>
//         </tr>
//         `;
//     });
//     displayTableData(loader, 'orders_tbody', tableData, ordersDiv);
// }

// document.getElementById('requests_button').addEventListener('click', getUserOrders);

// function getUserOrders(){
//     loader.style.display = 'block';
//     let requestMessage = document.getElementById('order_request_message');
//     let requestsDiv = document.getElementById('requests_div');
//     requestMessage.style.display = 'none'; 
//     fetch('http://127.0.0.1:5000/api/v1/user/orders', {
//         headers: siteHeaders
//     })
//         .then((res) => res.json())
//         .then((data) => {
//             const message = 'results retrieved successfully';
//             if(data.message === message){
//                 if(data.order.length > 0){
//                     let orderOptions = '';
//                     let orderNumber = 0;
//                     data.orders.forEach(order => {
//                         rideOptions += `
//                             <option value=${order.order_id}>Order ${orderNumber += 1}</option>
//                         `;
//                     });
//                     displayTableData(loader, 'order_offer', orderOptions, requestsDiv);
//                     getOrderRequests();
                    
//                 }else{
//                     const displayMessage = 'You have not placed orders yet. Requests can not be made.';
//                     noContentFound(loader, requestsDiv, requestMessage, displayMessage);
//                 }
//             }else{
//                 goToLogin();
//             }
            
//         });
// }

// let selectElement = document.getElementById('order');
// selectElement.addEventListener('change', getOrderRequests);

// function getOrderRequests(){
//     loader.style.display = 'block';
//     let requestMessage = document.getElementById('order_request_message');
//     let requestsDiv = document.getElementById('requests_div');
//     requestMessage.style.display = 'none'; 
//     fetch(`http://127.0.0.1:5000/api/v1/users/orders/${selectElement.value}/requests`, {
//         headers: siteHeaders
//     })
//         .then((res) => res.json())
//         .then((data) => {
//             const message = 'result retrieved successfully';
//             if(data.message === message){
//                 if(data.requests.length > 0){
//                     let RequestRows = '';
//                     data.requests.forEach(request => {
//                         RequestRows += `
//                             <tr>
//                                 <td>${request.passenger_name}</td>
//                                 <td>${request.request_status}</td>
//                                 <td>
//                                     <button type="button" data-acceptid="${request.request_id}" data-acceptrid = "${request.ride_id}" class="accept">Accept</button>
//                                 </td>
//                                 <td>
//                                     <button type="button" data-rejectid="${request.request_id}" data-rejectrid = "${request.ride_id}" class="reject">Reject</button>
//                                 </td>
//                             </tr>
//                         `;
//                     });
//                     displayTableData(loader, 'order_requests', RequestRows, requestsDiv);
//                     activateButtons('accept');
//                     activateButtons('reject');
//                 }else{
//                     noContentFound(loader, requestsDiv, requestMessage, 'No requests made on the order yet.');
//                 }
//             }else{
//                 goToLogin();
//             }
//         });
// }

// function acceptRjectRequest(orderId, requestId, data){
//     loader.style.display = 'block';
//     fetch(`http://127.0.0.1:5000//api/v1/users/orders/${order_Id}/requests/${requestId}`, {
//         method: 'PUT',
//         headers: siteHeaders,
//         cache: 'no-cache',
//         body: JSON.stringify(data)
//     })
//         .then((res) => res.json())
//         .then(result => {
//             if(result){
//                 if(data.request_status === 'Accepted'){
//                     loader.style.display = 'none';
//                     Alert.render('Request accepted successfully');
//                 }else{
//                     loader.style.display = 'none';
//                     Alert.render('Request rejected successfully');
//                 }
//             }else{
//                 goToLogin();
//             }
            
//         })
//         .catch(() => {
//             showNoNetwork(loader);
//         });
// }

// function activateButtons(buttonAction){
//     const acceptRejectButtons = document.getElementsByClassName(buttonAction);
//     let data = {};
//     [].forEach.call(acceptRejectButtons, (acceptRejectButton) => {
//         acceptRejectButton.addEventListener('click', () => {
//             if (acceptRejectButton.dataset.acceptid){
//                 data = {
//                     'request_status': 'Accepted'
//                 };
//                 acceptRjectRequest(acceptRejectButton.dataset.acceptrid, acceptRejectButton.dataset.acceptid, data);
//             }else{
//                 data = {
//                     'request_status': 'Rejected'
//                 };
//                 acceptRjectRequest(acceptRejectButton.dataset.rejectrid, acceptRejectButton.dataset.rejectid, data);
//             }
//         });
//     });
// }

// document.getElementById('log_out').addEventListener('click', logoutUser);

// function logoutUser(e){
//     e.preventDefault();
//     loader.style.display = 'block';
//     fetch('http://127.0.0.1:5000/api/v1/users/logout', {
//         method: 'POST',
//         headers: siteHeaders,
//         cache: 'no-cache'
//     })
//         .then((res) => res.json())
//         .then(data => {
//             const message = 'You are logged out successfully';
//             if(data.message === message){
//                 loader.style.display = 'none';
//                 goToLogin();
//             }else{
//                 loader.style.display = 'none';
//                 goToLogin();
//             }
            
//         })
//         .catch(() => {
//             showNoNetwork(loader);
//         });

// }
