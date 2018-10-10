
document.getElementById('add_menu_item').addEventListener('submit', addMenu);
function addMenu(e){
    e.preventDefault();
    let item_category = document.getElementById('item_category').value,
        item_name = document.getElementById('item_name').value,
        item_price = parseInt(document.getElementById('item_price').value);
    let data = {item_category, item_name, item_price};
     var str = document.location.search;
     var parts = str.split(/[#\?&]/g); 
     var filteredParts = parts.filter(function (part) {
     return part.split('=')[0] === 'Authorization';
     });
     var auth_token = filteredParts[0].split('=')[1];
    //  alert(auth_token);
    fetch('http://127.0.0.1:5000/api/v1/admin/menu' ,{
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
            if(data.Message === 'Menu Item Added Successfully'){
                alert('Menu Item Added Successfully');
            }
            else{
                alert('Menu Item Not Created ');
            }
        } )
}

document.getElementById('all_orders_button').addEventListener('click', getOrdersPlaced);
function getOrdersPlaced(){
    var str = document.location.search;
     var parts = str.split(/[#\?&]/g); 
     var filteredParts = parts.filter(function (part)  {
     return part.split('=')[0] === 'Authorization';
     });
     var auth_token = filteredParts[0].split('=')[1];
    //  alert(auth_token);
    fetch('http://127.0.0.1:5000/api/v1/users/orders', {
        method: 'GET',
        cache: 'no-cache',
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': auth_token
        },
    })
        .then((res) => res.json())
        .then(data => {
           if(data.Message === 'Order Successfully Fetched'){
            orderValue = `
            <table id="all_orders" width="90%">
            <tr colspan='9'><input type='text'>  </tr>
                <thead style="background-color: #fde9d9;">
                    <tr>
                        <th>ORDER ID</th>
                        <th>USER ID</th>
                        <th>ORDER NAME</th>
                        <th>QUANTITY</th>
                        <th>TOTAL AMOUNT</th>
                        <th>PAYMENT MODE</th>
                        <th colspan="3">ACTION</th>
                    </tr>
                </thead>
                <tbody id="orders_tbody" style="text-align:center; background-color: white; border-color: #f79646 #ccc;">
            `;
             console.log(data.orders)
             for (x in data.orders){
                output = `
                <tr >
                        <td>${data.orders[x].order_id}</td>
                        <td>${data.orders[x].user_id}</td>
                        <td>${data.orders[x].order_name}</td>
                        <td>${data.orders[x].quantity}</td>
                        <td>${data.orders[x].total_amount}</td>
                        <td>${data.orders[x].payment_mode}</td>
                        <td>Accept</td>
                      
                        <td>Decline</td>
                        <td>Complete</td>
                </tr>      
             `
            orderValue += output;  
             }
             orderValue += `  </tbody>
             </table>`;
             document.getElementById('placed_div').innerHTML = orderValue
        }
                
        }  
        );
}

document.getElementById('menu_button').addEventListener('click', getMenu);
function getMenu(){

    let menuDiv =  document.getElementById('menu_div');

    var str = document.location.search;
     var parts = str.split(/[#\?&]/g); 
     var filteredParts = parts.filter(function (part)  {
     return part.split('=')[0] === 'Authorization';
     });
     var auth_token = filteredParts[0].split('=')[1];
    //  alert(auth_token);
    fetch('http://127.0.0.1:5000/api/v1/menu', {
        method: 'GET',
        cache: 'no-cache',
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': auth_token
        },
    })
        .then((res) => res.json())
        .then(data => {
           if(data.Message === "Menu Fetched Successfully"){

            dataValue = `
            <table id="menu" width="90%">
                <thead style="background-color: #fde9d9;">

                    <tr>
                        <th>ITEM ID</th>
                        <th>ITEM CATEGORY</th>
                        <th>ITEM NAME</th>
                        <th>ITEM PRICE</th>
                    </tr>
                </thead>
                <tbody id="menu_tbody" style="text-align:center; background-color: white; border-color: #f79646 #ccc;">
            `;
             console.log(data.Available_Menu)
             for (x in data.Available_Menu){
                output = `
                <tr>
                        <td>${data.Available_Menu[x].item_id}</td>
                        <td>${data.Available_Menu[x].item_category}</td>
                        <td>${data.Available_Menu[x].item_name}</td>
                        <td>${data.Available_Menu[x].item_price}</td>
                </tr>      
             `
            dataValue += output;   
             }
             dataValue += `  </tbody>
             </table>`;
             document.getElementById('menu_div').innerHTML = dataValue
        }      
        }   
        );
}

// document.getElementById('specific_order').addEventListener('click', getSingleOrder);
// function getSingleOrder(){
   
//     var str = document.location.search;
//      var parts = str.split(/[#\?&]/g); 
//      var filteredParts = parts.filter(function (part)  {
//      return part.split('=')[0] === 'Authorization';
//      });
//      var auth_token = filteredParts[0].split('=')[1];
//     //  alert(auth_token);
//     fetch('http://127.0.0.1:5000/api/v1/admin/orders/1', {
//         method: 'GET',
//         cache: 'no-cache',
//         headers: {
//             'Accept': 'application/json',
//             'Content-type': 'application/json',
//             'Authorization': auth_token
//         },
//     })
//         .then((res) => res.json())
//         .then(data => {
//            if(data.message === 'Order Fetched Successfully'){
//             orderValue = `
//             <table id="single_order" width="90%">
//             <tr colspan='9'><input type='text'>  </tr>
//                 <thead style="background-color: #fde9d9;">
//                     <tr>
//                         <th>ORDER ID</th>
//                         <th>USER ID</th>
//                         <th>ORDER NAME</th>
//                         <th>QUANTITY</th>
//                         <th>TOTAL AMOUNT</th>
//                         <th>PAYMENT MODE</th>
//                         <th colspan="3">ACTION</th>
//                     </tr>
//                 </thead>
//                 <tbody id="order_tbody" style="text-align:center; background-color: white; border-color: #f79646 #ccc;">
//             `;
//              console.log(data.orders)
//              for (x in data.orders){
//                 output = `
//                 <tr >
//                         <td>${data.orders[x].order_id}</td>
//                         <td>${data.orders[x].user_id}</td>
//                         <td>${data.orders[x].order_name}</td>
//                         <td>${data.orders[x].quantity}</td>
//                         <td>${data.orders[x].total_amount}</td>
//                         <td>${data.orders[x].payment_mode}</td>
//                         <td>Accept</td>
                      
//                         <td>Decline</td>
//                         <td>Complete</td>
//                 </tr>      
//              `
//             orderValue += output;  
//              }
//              orderValue += `  </tbody>
//              </table>`;
//              document.getElementById('single_order_div').innerHTML = orderValue
//         }
                
//         }  
//         );
// }


// function getOrdersPlaced(getOrdersPlaced){
//     let ordersMessage = document.getElementById('orders_placed_message');
//     let ordersDiv =  document.getElementById('placed_div');
//     var str = document.location.search;
//     var parts = str.split(/[#\?&]/g); 
//     var filteredParts = parts.filter(function (part) {
//     return part.split('=')[0] === 'Authorization';
//     });
//     var auth_token = filteredParts[0].split('=')[1];
//     alert(auth_token);
//     fetch('http://127.0.0.1:5000/api/v1/users/orders', {
//         method: 'GET',
//         cache: 'no-cache',
//         headers: {
//             'Accept': 'application/json',
//             'Content-type': 'application/json',
//             'Authorization': auth_token
//         }
      
//     })
//         .then((res) => res.json())
//         .then((data) => {
//             const message = 'Order Successfully Fetched';
//             if(data.Message === message){
//                 let numberOfOrdersPlacedMessage = null;
//                 if(data.orders.length > 0){
//                     let ordersPlaced = [];
//                     data.orders.forEach(order => {
//                         ordersPlaced.push({
//                             'order_id': order_id,
//                             'user_id': user_id,
//                             'order_name': order_name,
//                             'quantity': quantity,
//                             'total_amount': total_amount,
//                             'payment_mode': payment_mode
//                         });
                        
//                     });
//                     alert(order);
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
//             }
//             // else{
//             //     goToLogin();
//             // }
            
//         });
// }
// function displayToUser(ordersPlaced){
//     let orddersDiv =  document.getElementById('placed_div');
//     let tableData = '';
//     ordersPlaced.forEach(order => {
//         tableData += `
//         <tr>
//             <td>${order_id}</td>
//             <td>${user_id}</td>
//             <td>${order_name}</td>
//             <td>${quantity}</td>
//             <td>${total_amount}</td>
//             <td>${payment_mode}</td>
//         </tr>
//         `;
//     });
//     displayTableData(orders_tbody, tableData, ordersDiv);
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
