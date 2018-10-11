// import {goToLogin} from './reusable.js';
function CustomAlert(){

    this.render = function(dialog){
        var winW = window.innerWidth;
        var winH = window.innerHeight;
        var dialogoverlay = window.getElementById('dialogoverlay');
        var dialogbox = window.getElementById('dialogbox');
        var dialogoverlay = window.getElementById('dialogoverlay');
        dialogoverlay.style.display = "block";
        dialogoverlay.style.height = winH+"px"; 
        dialogbox.style.top = "100px";
        dialogbox.style.display = "block";
        document.getElementById('dialogboxhead').innerHTML = "Acknowledge This Message";
        document.getElementById('dialogboxbody').innerHTML = dialog;
        document.getElementById('dialogboxfoot').innerHTML = '<button onclick ="Alert.ok()"> OK </button>';


    }
    this.ok = function(){
        document.getElementById('dialogboxoverlay').style.display = "None";
        document.getElementById('dialogbox').style.display = "None";
        







    }

   

}
var Alert = new CustomAleart();

