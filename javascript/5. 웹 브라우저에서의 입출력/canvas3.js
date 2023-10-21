window.addEventListener('load', function(){
    let canvas = document.querySelector('#myCanvas');
    let ctx = canvas.getContext('2d');

    let radian30 = 30*Math.PI / 180;
    let radian120 = 120*Math.PI / 180;

    ctx.beginPath();
    ctx.arc(100,100,80,radian30,radian120, false);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(95,90,80,radian30,radian120, true);
    ctx.stroke();
});