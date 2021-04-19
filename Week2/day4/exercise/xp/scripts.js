// Exercise 1 : Keyless Car
// Instructions
// Ask the user for their age, and save the value to a variable.
// Create a function called checkDriverAge() that will notify the user if they are permitted to drive. 
// They must be at least 18 to drive.
// if the user is too young, alert “Sorry, you are too young to drive this car. Powering off”
// if the user is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// if the user just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”
// Instead of using prompt to ask the user for their age, have the checkDriverAge() function accept an argument age.


// let driverAge= +prompt('What is your age?');

// function checkDriverAge() { 
//     if (driverAge < 18) {
//         console.log("Sorry, you are too young to drive this car. Powering off")
//     } else if (driverAge > 18) {
//         console.log("You are old enough to drive, Powering On. Enjoy the ride!")
//     } else {
//         console.log("Congratulations on your first year of driving. Enjoy the ride!")
//     }
//  }

//  checkDriverAge();

//  Exercise 2 : What’s In My Wallet ?
//  Instructions
//  Given a item price and an array representing the amount of change in your pocket, 
//  determine whether or not you can afford the item.
//  Change will always be represented in the following order: quarters, dimes, nickels, pennies.
//  Quarters  = 0.25
//  Dimes = 0.10
//  Nickels = 0.05
//  Pennies = 0.01
//  To illustrate:
//  changeEnough([25, 20, 5, 0], 4.25) should return true, since having 25 quarters, 
//20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

// quaters, dimes, nickels, pennies


// var changePocket = [25, 20, 5, 0]

// const change = [0.25, 0.1, 0.05, 0.01]

// let changePocket = [25, 20, 5, 0]
// let price = 8.51

// function changeEnough() {
//             sum = 0; 
//             for (let i = 0; i < change.length; i++) {
//                sum += change[i] * changePocket[i]; 
//             } if (sum >= price) {
//                 console.log('great you can afford the item')
//             } else {
//                 console.log('Sorry you do not have enough for this item')
//             }
            
// }

// changeEnough();

//  Examples
 
//  changeEnough([2, 100, 0, 0], 14.11) ➞ false
//  changeEnough([0, 0, 20, 5], 0.75) ➞ true


// Exercise 3: Find The Multiples Of 23
// Instructions
// Write a js function that console.logs all multiples of 23 less than 500,
// at the end return the sum of all the multiples.

// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// 391 414 437 460 483
// Sum : 5313


//Try a counter with an if statement: 

let sum = [];

function times23() {
    for (let i=0; i < 30; i++) {
        let multiple23 = [i] * 23
        if (multiple23 < 500) {
            sum.push(multiple23)
            console.log(multiple23)
            
            
        }
    }
}
    times23();   
    
    
    let total = sum.reduce()
    console.log(total)