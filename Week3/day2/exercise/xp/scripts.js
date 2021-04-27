// Exercise 1 : Change The Article
// Instructions
// <article>
//     <h1> Some Facts </h1>
//     <h2> The Chocolate </h2>
//     <h3>History of the chocolate</h3>
//     <p> Chocolate is made from tropical Theobroma cacao tree seeds. 
//     Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
//     <p> After the European discovery of the Americas, chocolate became 
//     very popular in the wider world, and its demand exploded. </p>
//     <p> Chocolate has since become a popular food product that millions enjoy every day, 
//     thanks to its unique, rich, and sweet taste.</p> 
//     <p> But what effect does eating chocolate have on our health?</p> 
// </article>
// <form>
//   <label for="fname">First name:</label><br>
//   <input type="text" id="fname" name="fname"><br>
//   <label for="lname">Last name:</label><br>
//   <input type="text" id="lname" name="lname"><br><br>
//   <input type="submit" value="Submit" id="submit">
// </form> 
// <div class="usersAnswer"></div>


// Using DOM methods, remove the last paragraph in the <article> tag from the DOM.

// document.getElementsByTagName('p')[3].remove();

// Add an event listener which will change the background color of the 
//h2 tag from the DOM when clicked on.
// let changeColor = document.getElementsByTagName('h2')[0];
// let randomSize = document.getElementsByTagName('h1')[0];
// let ranNum = Math.floor(Math.random() *110);

//     changeColor.addEventListener("click", RespondClick);
//     randomSize.addEventListener("click", RespondMouseOver);

//     function RespondClick() {
//         changeColor.style.backgroundColor = "red";
//     }

//     function RespondMouseOver() {
//         randomSize.style.fontSize = (`${ranNum}px`);
//    }
    

// Set the font size of the h1 tag to a random pixel size between 0 to 100.(
//Check out this documentation)


// Add an event listener which will hide the h3 when it’s clicked on 
//(use the display property).

// let hidden = document.getElementsByTagName('h3')[0]

// hidden.addEventListener("click", returnClick); 

// function returnClick() {
//     hidden.style.display = 'none';
// }

// Add a <button> to the HTML file, that when clicked on, should make the 
////text of all the paragraphs, bold.


// let button = document.createElement('button')
// button.innerHTML = "Make Bold";
// document.body.appendChild(button)


// button.addEventListener('click', btn)
//      function btn() {
//          let allP = document.getElementsByTagName('p')
//     for (i = 0; i <allP.length;i++) {
//         allP[i].style.fontWeight = 'bold';

//          }
//      }


// When the “Submit” button of the form is clicked:
// get the values of the input tags
// make sure that they are not empty,
// then append them to a HTML table, in the div, below the form.

// let submit = document.getElementById('submit')
// let firstName = document.getElementById('fname')
// let secondName = document.getElementById('lname')

// submit.addEventListener("click", submitForm() {
//          console.log(firstName)
//      }
// )

// When you hover on the 2nd paragraph, it should fade out 
//(    Check out “fade css animation” on Google)



// Exercise 2 : Transform The Sentence
// Instructions
// Add this sentence to your HTML file then follow the steps :

// <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
// <strong>end</strong> you <strong>will</strong> be great Developers!
// <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>


// Create a function called getBold_items() that takes no parameter. 
// This function should 
// collect all the bold items inside the paragraph.
// Create a function called highlight() that changes the color of all 
// the bold text to blue.
// Create a function called return_normal() that changes the color of all the bold 
// text back to black.
// Call the function highlight() onmouseover 
// (ie. when the mouse pointer is moved onto the paragraph), 
// and the function return_normal() onmouseout (ie. when the mouse pointer is
//     moved out of the paragraph). Look at this example




// function getBold_items() {
//     let paraStrong = document.getElementsByTagName('strong')
//     return paraStrong
// }


// let para = document.getElementsByTagName("p")[0];
// para.addEventListener('mouseover', highLight, false)

//     function highLight() {
//     let paraStrong = getBold_items();
//     for(let i = 0; i < paraStrong.length; i++) {
//         paraStrong[i].style.color = "blue";
//     }
// };

// para.addEventListener('mouseleave', return_normal, false)
// function return_normal() {
//     let paraStrong = getBold_items();
//     for(let i = 0; i < paraStrong.length; i++) {
//         paraStrong[i].style.color = "black";
// 		console.log('black');
//     }
// };






// Exercice 3 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. 
// Use the code below as a base:
// body> 
// <p>Input radius value and get the volume of a sphere.</p> 
// <form  id="MyForm"> 
//     <label for="radius">Radius</label><input type="text" name="radius" id="radius" required> 
//     <label for="volume">Volume</label><input type="text" name="volume" id="volume"> 
//     <input type="submit" value="Calculate" id="submit">    
// </form> 
// </body>



let submit = document.getElementById('submit')
let input = document.getElementById('radius')

let form = document.forms.my;

form.addEventListener("click", test)

function test(){
    let volume = (4/3) * (Math.PI * input.value ** 3)
    console.log(volume)
    document.getElementById('volume').value = volume
    
    console.log(volume)
  
}
