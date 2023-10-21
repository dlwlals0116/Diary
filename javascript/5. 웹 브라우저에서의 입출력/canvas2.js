window.addEventListener('load', function(){
    let canvas = document.querySelector('#myCanvas');
    let ctx = canvas.getContext('2d');

    //속이 비어있는 삼각형 그리기
    ctx.beginPath();
    ctx.moveTo(60,10); 
    ctx.lineTo(110,100);
    ctx.lineTo(10,100);
    ctx.closePath();
    ctx.stroke();

    //속이 채워진 삼각형 그리기
    ctx.beginPath();
    ctx.moveTo(60,120);
    ctx.lineTo(110,210);
    ctx.lineTo(10,210);
    ctx.fill(); //fill의 경우 closepath를 호출할 필요없음
})