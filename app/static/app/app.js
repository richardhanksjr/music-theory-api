//var question = "What is the fourth scale degree of Messian's 9 note symmetrical scale, also known as the fourth mode of limited transposition, if the root is concert G?";
//
var answer = "An interval that encompasses an octave or less"

//window.onload = function () {
const app = new Vue({
    delimiters: ['[[', ']]'],
    el: "#questionPage",
    data: {

         questionPackage: [],
         message: "",
         answerVal: "",
    },
    methods: {
    evaluateAnswer(Answer, answerVal) {
             this.Answer = Answer;
             if (Answer === answer) {
                this.message = "Correct!"

             }
             else {
                this.message = `Sorry, the correct answer is "${answer}"`
             }
            this.answerVal = "";
        }
    },
    mounted:
        function () {
            axios.get('/api/question/')
                .then(response => {
                this.questionPackage = response.data
                });
            },
    })
//}