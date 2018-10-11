
document.getElementById('login_user').addEventListener('submit', loginUser);
function loginUser(e){
    e.preventDefault();
    let email_address = document.getElementById('email_address').value;
    let password = document.getElementById('password').value;
    const data = {email_address, password};
            fetch('http://127.0.0.1:5000/api/v1/auth/login', {
                method: 'POST',
                headers : { 
                  'Content-Type': 'application/json',
                  'Accept': 'application/json',
                  // 'Authorization': auth_Token

                 },
                 cache: 'no-cache',
                 body: JSON.stringify(data)
              })
              .then((res) => res.json())
              .then((result) => {
                  if(result.status === 'success'){
                      if (email_address ==='james@gmail.com'){
                        
                        window.location.href = 'admin.html?Authorization='+result.auth_Token;
                      }else{
                      window.location.href = 'userrole.html?Authorization='+result.auth_Token;
                      }
                    //   alert(result.auth_Token);
                     }
                  else{
                      alert('Incorrect email address or password');
                    }
                });
}
