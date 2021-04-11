// Ex1 Finding Nemo

var nemo = prompt("Enter a sentence containing the word Nemo");
var count = nemo.indexOf(nemo);
console.log(`I found Nemo at ${count}`);

if (Number.parseFloat === undefined) {
   Number.parseFloat = parseFloat;


// Ex1 Evaluation

var line1 = [5 >= 1];
console.log(line1);

var line2 = [0 === 1];
console.log(line2);

var line3 = [4 <= 1];
console.log(line3);

var line4 = [1 != 1];
console.log(line4);

var line5 = ["A" > "B"];
console.log(line5);

var line6 = ["B" < "C"];
console.log(line6);

var line7 = ["a" > "A"];
console.log(line7);

var line8 = ["b" < "A"];
console.log(line8);

var line9 = [true === false];
console.log(line9);

var line10 = [true != true];
console.log(line10);



//Exercise 2 Evaluation(2)

let c;
let a = 34;
let b = 21;

a = 2;
a + b;

// 1. what will be the outcome of a + b
console.log(a + b);

//Answer is 23 since the new value of a = 2

//2. What is the value of c?
console.log(c);

// answer is undefined

//3. the outcome for console.log(3 + 4 + '5');
// is 75


//Exercise 3 Ask for numbers 
var number = prompt('Please enter a string of numbers separated by commas');
var newNumber = parseFloat(number, 10);

// not sure how to implement below

// const toNumbers = number => number.map(Number);
// toNumbers(['1', '2', '3','4']);

