//Exercise 1

let fruits = ['Banana', 'Apples', 'Oranges', 'Blueberries'];
fruits.splice(0,1);

fruits.sort();

fruits.push('Kiwi');

fruits.shift();

fruits.reverse();

console.log(fruits);


//Exercise 2

let moreFruits = ['Banana', ['Apples', ['Oranges'],'Blueberries']];
let favFruit = moreFruits[1][1][0];

console.log(favFruit);
