/////////////////////////////////
let name = "park";
let string = `Hello ${name}`;
console.log(string)

///////////////////////////////////
//템플릿 리터럴
console.log(`
안녕하세요
반갑습니다
`)

let a = 5;
let b = 10;
console.log(a + ' + ' + b + ' = ' + (a+b));

console.log(`${a} + ${b} = ${a+b}`);
////////////////////////////////////////////////
//객체
//객체 리터럴로 객체 생성
// 프로퍼티로 suit, rank를 가지는 객체 
let card = { suit: '하트', rank : 'A'};
console.log(card)
//프로퍼티의 이름은 문자열이 되어도 상관없다.
card = {'suit':'하트', 'rank': 'A'}

//프로퍼티값의 참조 방법
console.log(card.suit);
console.log(card['rank']);
console.log(card.test)   //일부러 틀리게함 , 뭐가나오는지 확인하기위해
//없는 프로퍼티값을 참고하면, 자동으로 undifined를 출력

//프로퍼티의 값 추가
card.value = 14;
console.log(card.value);

//객체의 프로퍼티 삭제
card.value = 14;
console.log(card.value)

//객체의 프로퍼티 삭제
delete card.value;
console.log(card.value)

//객체의 프로퍼티 보유 여부 확인
console.log('suit' in card);
console.log('random' in card);
console.log('toString' in card);

///////////////////////////////
// 메서드
card = {
    suit : '하트',
    rank : 'A',
    showCard: function() {
        //this 키워드는 함수의 소유자를 가리킨다.
        //함수 뒤에 식별자(함수 이름)이 없음으로 익명 함수라고 부른다
        console.log(`이 카드는 ${this.suit} ${this.rank}입니다`)
    }
};

card.showCard();

///////////////////////////////////////////
//함수

function square(x) {
    return x*x;
}
console.log(square(9));

//함수는 객체이다.
//객체와 동일한 조작이 가능
square.test = 'testValue';
console.log(square.test);
//JS에서는 모든 객체가 일급객체
console.log(square)
//이것도 console이라는 객체에 log라는 메서드에 square라는 함수(객체)가 메개변수로 들어간것이라고 이해하면 편할듯

///////////////////////////////////////
//객체 생성자
function Card(suit, rank) {
    //new 키워드가 붙은 경우:
    //this = {};
    this.suit = suit;
    this.rank = rank;
    //return this;
}
card = new Card('하트', 'A');
console.log('하트', 'A');
//new 키워드가 붙지 않은 전역함수의 this는 기본적으로
//글로벌 객체인  window를 가리킨다.
card = Card('하트', 'A');
console.log(card);
console.log(window.suit, window.rank);

//////////////////////////////////////////////////
//클래스(ES6버전 생성자)
class Circle {
    //파이썬의 init역할
    constructor(center, radius) {
        this.center = center;
        this.radius = radius;
    }
    //원의 면적 계산 메서드
    area() {
        return Math.PI * (this.radius**2);
    }
}
let circle = new Circle({x:0, y:0},2.0);
console.log(`넓이 = ${circle.area()}`);

class Product {
    constructor(name, weight, price){
        this.name = name;
        this.weight = weight;
        this.price = price;
    }
    calculate(weight){
        let num = weight/this.weight;
        return this.price*num;
    }
}
let product = new Product(name = '삼겹살', weight = 100, price = 1690)
console.log(product.calculate(150))