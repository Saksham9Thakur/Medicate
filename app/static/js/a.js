var directionsService;
var directionsDisplay;
var k=0;
var s;
window.s="";
var ar=[];
var ba=[];
function initMap() 
{
  window.directionsService = new google.maps.DirectionsService;
  window.directionsDisplay = new google.maps.DirectionsRenderer;
  //console.log(window.directionsService);
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 6,
    center: {lat: 31.1033, lng: 77.1722}
  });
 /* window.s=1;*/
/*  console.log("Saksham");
    console.log("Saksham");
      console.log("Saksham");*/
}

function display()
{
     console.log("Saksham"); 
    var b=document.getElementsByClassName("saksham");
  
    /*console.log(b);
    console.log(window.directionsService);*/
    for(i in b)
    {
         console.log(document.getElementsByClassName('saksham')[i].innerText); 
    if(document.getElementsByClassName('saksham')[i]!=undefined)
    {
    //console.log(document.getElementsByClassName('saksham')[k].innerText);	
    calculateAndDisplayRoute(document.getElementsByClassName('saksham')[i].innerText);
  }
  else
  {  break;
console.log("ELSE");
/*window.s=0;*/
}
}
setTimeout(function()
{
  var score=0;
 var ans=[];
 console.log(ar);
for (var i = 0; i < ba.length; i++) 
{
 var c=ar[i];
 var a=0;
 var p=0;
 var l=0;
 for(k in c)
 {
  var ac=(c.charCodeAt(k));
  if(ac>=48 && ac<=57)
  {
    p=p*10+(ac-48);
    l=1;
  }
  else if(l==1)
  {
    a=a*(60)+p;
    p=0;
    l=0;
  }
 }
 ans.push(a); 
}
var po=document.getElementsByClassName("sakshaam");
var poo=document.getElementsByClassName("ma");
var m=[],aa=[];
var min=10;
var sc=0;
for (var i = 0; i < ba.length; i++) 
{
m.push((document.getElementsByClassName('sakshaam')[i].innerText));
}
console.log(ans);
console.log(m);
console.log(ba);
for (var i = 0; i < ba.length; i++) 
{
  sc=2/3;
  for(var j=0;j<=ans[i];j+=10)
  {
    sc=sc*(.9);
  }
  sc+=.33*(1-m[i]);
  aa.push(sc);
}
for (var i = 0; i < ba.length; i++) 
{
document.getElementsByClassName('sakshaam')[i].innerText=aa[i];
 po[i].style.display='block';
 poo[i].style.display='none';

}

},3000);
}
function calculateAndDisplayRoute(a) 
{
  var waypts = [];
/* console.log(" window.directionsService");*/
  window.directionsService.route({
    origin: "Jaypee University Of Information Technology",
    destination: a,
    waypoints: waypts,
    optimizeWaypoints: true,
    travelMode: 'DRIVING'
  },function(response, status) {
     var route = response.routes[0];
    if(status === 'OK') 
    {
/*        console.log(route.legs[0].duration.text+a);*/
    ar.push(route.legs[0].duration.text);
    ba.push(a);
    console.log(ba.length);
/*    for(i in window.ba)
    console.log(ar[ba[i]]+ba[i]+"sas\n");*/
    }
     else 
    {
      window.alert('Directions request failed due to ' + status);
    }

  }
  );
}