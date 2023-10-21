window.addEventListener('load', function(){
    let canvas = document.querySelector('#myCanvas');
    let ctx = canvas.getContext('2d');

    let character = {
        x:0,
        y:0,
        width:32,
        height:32,
        key : {  // 키 눌림 상태
            ArrowUp : false,
            ArrowDown: false,
            ArrowLeft: false,
            ArrowRight: false
        }
    };
    //캐릭터 그리는함수
    function drawcharacter(){
        ctx.strokeRect(
            character.x,
            character.y,
            character.width,
            character.height
        );
    };
    drawcharacter();
    //사각형 지우는함수
    function clearcharacter(){
        ctx.clearRect(
            character.x-1,
            character.y-1,
            character.width+2,
            character.height+2
        )
    };
    //충동 체크 함수
    function checkCollision(){
        if (character.x < 0) character.x = 0;
        if (character.x>608) character.x = 608;
        if (character.y<0) character.y = 0;
        if (character.y > 368) character.y = 368;
    }
    //캐릭터 움직이는함수
    function moveCharacter() {
        if (character.key.ArrowLeft == true) {
            character.x -= 4;
        }
        if (character.key.ArrowRight == true){
            character.x += 4;
        }
        if (character.key.ArrowUp == true) {
            character.y -= 4;
        }
        if (character.key.ArrowDown == true){
            character.y += 4;
        }
    };
  
    //키다운
    window.addEventListener('keydown', function(evt){
        console.log('[DOWN]' + evt.key)
        character.key[evt.key] = true;
    });
    //키업
    window.addEventListener('keyup', function(evt){
        console.log(`[ UP ]`+ evt.key)
        character.key[evt.key] = false;
    });

    //게임이벤트루프  30fps
    setInterval(function() {
        clearcharacter();
        moveCharacter();
        checkCollision();
        drawcharacter();
    }, 1000/30);
});
//충돌체크를 함수를 통해 하는 방법도 있지만 movecharacter에서 키를 바꾸지 않는 방법으로도 사용할 수 있겠다는 생각이 들었다