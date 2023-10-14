//페이지 로드 시 이벤트 처리기 등록
addEventListener('load', function(evt) {
    console.log('페이지 로드 됨');
    let button = document.getElementById('getTime');
    console.dir(button);

    button.addEventListener('click', function(evt) {
        let date = new Date();
        console.log(`현재 시각은 ${date} 입니다`);
    });
    
    //타이머
    setTimeout(function(){
        console.log('1초타이머');
    }, 1000);
    setTimeout(function(){
        console.log('0.5초타이머');
    }, 500);

    let sec = 0;
    setInterval(function(){
        sec++;
        console.log("인터벌: " + sec);
    },1000);
});

console.log('페이지 로드 안됨')