var question = "What is the fourth scale degree of Messian's 9 note symmetrical scale, also known as the fourth mode of limited transposition, if the root is concert G?";

var answer = "B"


const questionPage = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            Question: question,
            Answers: [
            {id: 1, note: 'Bb'},
            {id: 2, note: 'C#'},
            {id: 3, note: 'B'},
            {id: 4, note: 'C'},
            ],
            message: "",
            answerVal: "",
        }
    },
    methods: {
        evaluateAnswer(Answer, answerVal) {
             this.Answer = Answer;
             if (Answer === answer) {
                this.message = "Correct!"

             }
             else {
                this.message = "Sorry, the correct answer is 'B'"
             }
            this.answerVal = "";
        }
    },

 })