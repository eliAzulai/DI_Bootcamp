
// Create a drumset using HTML, CSS, JS.

// 1. Focus on the JS. Get it working. Make it look pretty later.

// 2. Look up how to play audio in html and js. (w3schools)

// 3. Add event listeners for keyboard and/or mouse clicks.
//     - for keyboard events, you can get the key by looking at the "event" object's keyCode.

//     - for mouse click events, you can get the key by looking at the "this" object.

// 4. The repo contains a folder with soundfiles.


//  This looks complex, but its pretty simple.

//  - Get the clicked element, or key press.
//  - Use it's value to get the correct audio element.
//  - Play the audio element.

//  Have fun, good luck!
 
//  ![Alt text](./screenshot.png?raw=true)

//for (let i=0; i< drumContainer.length; i++)


//boom sound
let soundSet = ["boom.wav", "clap.wav", "hihat.wav", "kick.wav", "openhihat.wav", "ride.wav", "snare.wav", "tink.wav", "tom.wav"];

let boom = document.getElementsByClassName('container')

for (let s=0; s < soundSet.length; s++)


boom.addEventListener("click", soundHit) 
function soundHit() {
        let audio = new Audio("./sounds/boom.wav");
        audio.play();
    }
    
    document.addEventListener("keydown", function(event) {
        if (event.key == 32) {
            let audio = new Audio("./sounds/boom.wav");
            audio.play(); 
        }  
      }); 
