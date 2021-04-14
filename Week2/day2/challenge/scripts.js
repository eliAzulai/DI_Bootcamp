

// var sentence = prompt("Enter a sentence containing the words not and bad");
var sentence = ("the movie is not that bad I like it")
var wordNot = sentence.indexOf("not"); 
var wordBad = sentence.indexOf("bad");
var substitute


if (wordBad > wordNot  && wordNot != -1) {
    substitute = sentence.substring(wordNot, WordBad)
    console.log(sentence.splice(wordBad, wordNot));
    // console.log('good')
} else {
    console.log(sentence)
};

