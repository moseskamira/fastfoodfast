
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
    //  alert(auth_token);
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

document.getElementById('menu_button').addEventListener('click', getMenu);
function getMenu(){
    // let ordersMessage = document.getElementById('orders_placed_message');
    let menuDiv =  document.getElementById('menu_div');
    // loader.style.display = 'block';
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