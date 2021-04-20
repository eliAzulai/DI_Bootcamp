// Exercise 1 : Change The Navbar
// Instructions
//  <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>


// In the <div> above, change the value of the id attribute from 
//navBar to socialNetworkNavigation, using the setAttribute method.

// let newDiv = document.getElementById("navBar")
// newDiv.setAttribute('id', "socialNetworkNavigation");

// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// getElementsByTagName('ul')
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.

// let newList = document.createElement('li');
// newList.innerHTML = "Logout";
// document.getElementsByTagName('ul')[0].appendChild(newList);


// Bonus
// Use the firstElementChild and the lastElementChild properties to
// retrieve the first 
// and last li elements from their parent element (ul). 
// Display the text of each link. (Hint: use the textContent property).

// let first = document.body.firstElementChild.firstElementChild.firstElementChild.textContent;
// let last = document.body.firstElementChild.firstElementChild.lastElementChild.textContent;




// Exercise 2 : Users
// Instructions
// <html>
// <body>
//   <div id="container">Users:</div>
//   <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
//   </ul>
//   <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
//   </ul>
// </body>
// </html>


// // In the HTML above change the name “Pete” to “Richard”.
// let rich = document.getElementsByTagName('li')[1].innerHTML = "Richard"

// // Change each first name of the two <ul>'s to your name.
// let myName = document.getElementsByTagName('li')[0].innerHTML = "Eli"
// let myNameTwo = document.getElementsByTagName('li')[2].innerHTML = "Eli"

// // At the end of each <ul> add a <li> that says “Hey students”.
// let newList = document.createElement('li')
// newList.innerHTML = "Hey students"
// document.getElementsByTagName('ul')[0].appendChild(newList);

// let newListTwo = document.createElement('li')
// newListTwo.innerHTML = "Hey students"
// document.getElementsByTagName('ul')[1].appendChild(newListTwo);

// Delete the name Sarah from the second <ul>.
// let parentElem = document.getElementById("main");
// let childElem = document.getElementById("hint");
// parentElem.removeChild(childElem);

// let parentElem = document.getElementsByTagName('li');
// let childElem = document.getElementsByTagName('li')

// let sarahName = document.getElementsByTagName('li')[4]
// sarahName.parentElement.removeChild(sarahName);


// Bonus
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.


// Exercise 3 : Users And Style
// Instructions
//  <html>
// <body>
//   <div>Users:</div>
//   <ul>
//     <li>John</li>
//     <li>Pete</li>
//   </ul>
// </body>
// </html>


// For the following exercise use the HTML presented above:

// Add a “light blue” background color and some padding to the <div>.
document.getElementById("myDiv").style.backgroundColor = "lightblue";
document.getElementById("myDiv").style.padding = '10px';

// Do not display the first name (John) in the list.
let firstName = document.getElementsByTagName('li')[0]
firstName.parentElement.removeChild(firstName);

// Add a border to the second name (Pete).
//document.getElementById("myDiv").style.border = '10px,solid';
document.getElementsByTagName('li')[0].style.border = "thick solid #0000FF";;
// Change the font size of the whole body.
document.body.style.fontSize = '24px'
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).


let secondName = document.getElementsByTagName('li')[1]
if (backgroundColor == 'lightblue') {
    alert(`Hello ${firstNAme} and ${secondName}`)
}