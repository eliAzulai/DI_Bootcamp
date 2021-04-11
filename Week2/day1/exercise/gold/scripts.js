// Exercise 1

let me = ["my", "favourite", "colour", "is", "blue"];
let sentence = me.join();
console.log(sentence);

// Exercise 2

var str1 = "mix ";
var str2 = "pod";

var newStr1 = str1.slice(2);
var newStr2 = str2.slice(2);

var result1 = "po" + newStr1;
var result2 = "mi" + newStr2;

let newWord = result1 + result2;

// console.log (newWord);

// Exercise 3

var num1 = prompt("Enter your first number");
var intNum1 = parseFloat(num1, 10);
var num2 = prompt("Enter your second number");
var intNum2 = parseFloat(num2, 10);
alert(`your answer is ${intNum1 + intNum2}`);
