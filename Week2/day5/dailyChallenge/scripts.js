// Prompt the user for a number to begin counting down bottles.
// In the song everytime a bottle falls we subtract the bottles by 1.
// What your code should do is:
// instead of subtracting by 1, everytime a bottle drops the subtracted number should go up by 1
// For example the first time a bottle drops we subtract by 1,
// the second time we subtract by 2 and so on.
// Take a look below for more help.

// ==============================

// 99 bottles of beer on the wall
// 99 bottles of beer
// Take 1 down, pass it around
// 98 bottles of beer on the wall
// 98 bottles of beer on the wall
// 98 bottles of beer
// Take 2 down, pass them around
// 96 bottles of beer on the wall
// 96 bottles of beer on the wall
// 96 bottles of beer
// Take 3 down, pass them around
// 93 bottles of beer on the wall

// ==============================

// How will you choose to make the song end?
// Make sure you get the grammar correct.

// For 1 bottle, you pass “it” around.
// For more than one bottle, you pass “them” around.

let i = +prompt("Enter in a number to counting down bottles of beer");
let down = 1;

while (i >= 1) {
  console.log(`${i} bottles of beer on the wall`);
  console.log(`${i} bottles of beer`);

  if (down == 1) {
    console.log(`Take ${down} down pass it around`);
     } else {
    console.log(`Take ${down} down pass them around`);
    }   

    i -= down;
    down++;
}
console.log("Oh no there are no bottles of beer on the wall, oh well lets go down the pub!");
