window.addEventListener('load', function(){
    let canvas = document.querySelector('#myCanvas');
    let ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(20,20); 
    ctx.lineTo(170,20);

    let startAngle = -90*Math.PI/180;
    let endAngle = 0*Math.PI/180;
    ctx.arc(170,40,20,startAngle,endAngle, false);
    ctx.lineTo(190,120);
    ctx.stroke();
});