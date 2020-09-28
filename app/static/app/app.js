var question = "What is the fourth scale degree of Messian's 9 note symmetrical scale, also known as the fourth mode of limited transposition, if the root is concert G?";

var answer = "B"

var encouragement = "You got this!"

questionPage = new Vue({
    delimiters: ['[[', ']]'],
    el: '#questionPage',
    data: {
        question: question,
        encouragement: encouragement,
        answer: answer,
    },
 })