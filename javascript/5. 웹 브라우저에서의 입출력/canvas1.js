window.addEventListener('load',function(){
    // querySelctor는 getElement~처럼 HTML 요소를 가져올때 
    // 사용한다.
    // id값을 가져오는 경우: #{id}
    // tag로 가져오는경우: 태그명
    //class 로 가져오는경우 : .class
    //기타 속성으로 가져오는경우 : {속성명 = 속성값}
    let canvas = this.document.querySelector('#myCanvas');

    //그림을 그리기 위한 환경을 가져옴
    let ctx = canvas.getContext('2d')

    //좌표 (50,60) 위치에 너비 200, 높이 100 짜리 사각형 그리기
    ctx.strokeRect(50,60,200,100);
    ctx.fillRect(50,60,200,100);
    
})