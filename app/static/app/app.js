//var question = "What is the fourth scale degree of Messian's 9 note symmetrical scale, also known as the fourth mode of limited transposition, if the root is concert G?";
//
//var answer = "B"

//window.onload = function () {
const app = new Vue({
    delimiters: ['[[', ']]'],
    el: "#questionPage",
    data: {

         questionPackage: [],
         message: "",
         answerVal: "",
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