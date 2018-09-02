function Authenticate(){
  var username = document.querySelector("#username").value;
  var password = document.querySelector("#password").value;
  if(username==='user' && password ==="user"){
     window.location.href ="user.html";
  }else if(username==='admin' && password ==="admin"){
    var username = document.querySelector("#username").value;
    var password = document.querySelector("#password").value;
    window.location.href ="admin.html";

  }else{

    
  }
}