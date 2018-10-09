let loader = document.getElementById('loader');
document.getElementById('signup').addEventListener('submit',addUser);
function addUser(e){
    e.preventDefault();
    loader.style.display = 'block';
    let first_name = document.getElementById('fName').value;
    let last_name = document.getElementById('lName').value;
    let email_address = document.getElementById('email').value;
    let phone_number = document.getElementById('pNumber').value;
    let password = document.getElementById('user_password').value;
    let confirm_password = document.getElementById('passwordRepeat').value;
    if (password != confirm_password){
        alert("Passwords Do Not Match");
    }
    else{
        const data = {"first_name":first_name, "last_name":last_name, "email_address":email_address, "phone_number":phone_number,"password":password};
    fetch('http://127.0.0.1:5000/api/v1/auth/signup',{
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        },
        cache: 'no-cache',
        body: JSON.stringify(data)
    })  
    .then((res) => {
        if(res.status=='400'){
            loader.style.display = 'none';
            alert('Sorry, Email already exists');
        }
        else if (res.status=='201'){
            loader.style.display = 'none';
            alert('You have successfully registered. You can login');
        }
    })
        .catch(() => {
            showNoNetwork(loader);
        });
}   
}
