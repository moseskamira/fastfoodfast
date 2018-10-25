
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
    fetch('https://apifastfoodfast.herokuapp.com/api/v1/admin/menu' ,{
        method: 'POST',
        cache: 'no-cache',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type': 'application/json',
            'x-access-token': auth_token
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
    let ordersMessage = document.getElementById('orders_placed_message');
    let orderssDiv =  document.getElementById('placed_div');
    var str = document.location.search;
     var parts = str.split(/[#\?&]/g); 
     var filteredParts = parts.filter(function (part)  {
     return part.split('=')[0] === 'Authorization';
     });
     var auth_token = filteredParts[0].split('=')[1];
    fetch('https://apifastfoodfast.herokuapp.com/api/v1/admin/orders', {
        method: 'GET',
        cache: 'no-cache',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type': 'application/json',
            'x-access-token': auth_token
        },
    })
        .then((res) => res.json())
        .then(data => {
           if(data.Message === 'Order Successfully Fetched'){
            orderValue = `
            <table id="all_orders" width="90%">
    
            <tr colspan='9'>
                <form method="GET" action=" ">
                    <p>Enter Order Id: <input type="text" name="order_id"><button type="submit" id="specific_order_button">Send</button></p>
                </form>
            </tr>
            <tr> <h2> <strong><center>AVAILABLE ORDERS </strong></center></h2>  </tr>
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
    fetch('https://apifastfoodfast.herokuapp.com/api/v1/menu', {
        method: 'GET',
        cache: 'no-cache',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type': 'application/json',
            'x-access-token': auth_token
        },
    })
        .then((res) => res.json())
        .then(data => {
           if(data.Message === "Menu Fetched Successfully"){

            dataValue = `
            <table id="menu" width="90%">
            <tr> <h2> <strong><center>AVAILABLE MENU ITEMS</strong></center></h2>  </tr>
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

document.getElementById('specific_order_button').addEventListener('click', getSpecificOrder);
function getSpecificOrder(){
    let ordersMessage = document.getElementById('orders_placed_message');
    let orderssDiv =  document.getElementById('placed_div');
    var str = document.location.search;
     var parts = str.split(/[#\?&]/g); 
     var filteredParts = parts.filter(function (part)  {
     return part.split('=')[0] === 'Authorization';
     });
     var auth_token = filteredParts[0].split('=')[1];
    fetch('https://apifastfoodfast.herokuapp.com/api/v1/admin/orders/<int order_id>', {
        method: 'GET',
        cache: 'no-cache',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type': 'application/json',
            'x-access-token': auth_token
        },
    })
        .then((res) => res.json())
        .then(data => {
           if(data.Message === 'Order Successfully Fetched'){
            orderValue = `
            <table id="all_orders" width="90%">
    
            <tr colspan='9'>
                <form method="GET" action=" ">
                    <p>Enter Order Id: <input type="text" name="order_id"><button type="submit">Send</button></p>
                </form>
            </tr>
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