satual=1;
smax=2;
stmp=5000;

function troca(){
    document.getElementById("p1").style.visibility="hidden";
    document.getElementById("p2").style.visibility="hidden";
    
    document.getElementById("p"+satual).style.visibility="visible";
    
    satual=satual+1;
    if(satual > smax){
        satual=1;
    }
}

function slider(){
    document.getElementById("p1").style.visibility="hidden";
   document.getElementById("p2").style.visibility="visible";
   
   sliderTimer=setInterval(troca,stmp);
}