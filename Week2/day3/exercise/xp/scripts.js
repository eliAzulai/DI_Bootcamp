
// Exercise 1

// var colours = ["blue", "red", "green"];

// for (var i in colours) {
//     console.log(`My #${i} colour is ${colours[i]}`);
// }


// Exercies 2 list of people

let people = ["Greg", "Mary", "Devon", "James"];

//1. Write code to remove “Greg” from the people array.

people.splice(0,1,);

//2. Write code to replace “James” to “Jason”.

people.splice(2,1,"Jason");

//3. Write code to add your name to the end of the people array.

people.push("Eli");

//4. Using a loop, iterate through the people array and console.log each person.

for (let i of people) {
    console.log(i);
}
// 5. Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
// not sure what im doing wrong here!

for (let i of people) {
    if (i === "Jason"); {
        break;
    }
}

// 6. Write code to make a copy of the people array using slice. 
//The copy should NOT include “Mary” or your name.

// let newPeople = people.slice(1, 3);

// 7. Write code that console.logs Mary’s index. take a look at indexOf on google.

// people.indexOf("Mary");

// 8. Write code that gives the indexOf “Foo” (this should return -1). 
//Why does it return -1

// people.indexOf("foo");

// -1 means that its not found in the index

//// 9. Create a variable called last which value is the last element of the array
//.�Hint: What is the relationship?


// var last = people.lastIndexOf();


//Exercise 3

// let active = true;

// while (active) {
// let num = prompt("Enter any number");
// if (num > 10) {
//     active = false;
//     }

// }


//exercise 4

let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }

let name =  prompt("What is your name?");
  for (name in guestList) {
      console.log(`Hi! I'm ${name}, and I'm from ${guestList}`);
  }





