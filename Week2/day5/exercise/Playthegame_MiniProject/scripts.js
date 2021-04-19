let counter = 0;

function playTheGame() {
  var answer = confirm("would you like to play the game");
  if (answer == false) {
    alert("No problem, Goodbye");
  } else {
    let userNumber = +prompt("please enter a number between 0-10");
    // check if user number is valid number
    if (isNaN(userNumber)) {
      alert("You did not enter a valid number goodbye!");
    }
    // check if user number in range of 0-10
    if (userNumber > 10 || userNumber < 0) {
      alert("Sorry it’s not a good number, Goodbye.");
    } else {
      alert("You entered a valid number");
      // creating a var that is random
      let computerNumber = Math.floor(Math.random() * 11);
      //                     console.log(computerNumber);
      test(userNumber, computerNumber);
    }
  }
}

// Second Part

function test(userNumber, computerNumber) {
  if (userNumber === computerNumber) {
    alert("WINNER");
  }
  if (userNumber > computerNumber) {
    alert("Your number is bigger then the computer’s, guess again");
    counter += 1;
    playTheGameAgain();
  }
  if (userNumber < computerNumber) {
    alert("Your number is smaller then the computer’s, guess again");
    counter += 1;
    playTheGameAgain();
  }
}

// Play the game again !

function playTheGameAgain() {
  var answer = confirm("would you like to play the game Again?");
  if (answer == false) {
    alert("No problem, Goodbye");
  } else {
    let userNumber = +prompt("please enter a NEW number between 0-10");
    // check if user number is valid number
    if (isNaN(userNumber)) {
      alert("You did not enter a valid number goodbye!");
    }
    // check if user number in range of 0-10
    if (userNumber > 10 || userNumber < 0) {
      alert("Sorry it’s not a good number, Goodbye.");
    } else {
      alert("You entered a valid number");
      // creating a var that is random
      let computerNumber = Math.floor(Math.random() * 11);
      //                     console.log(computerNumber);

      test(userNumber, computerNumber);
    }
  }
}

function count() {
  if (counter >= 3) {
    alert("out of tries");
    return;
  }
}
count();
