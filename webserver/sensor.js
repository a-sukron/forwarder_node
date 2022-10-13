setInterval(function(){ 
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("val").innerHTML = this.responseText;
      }
    };
    xmlhttp.open("GET","get.php",true);
    xmlhttp.send();
}, 1000);
