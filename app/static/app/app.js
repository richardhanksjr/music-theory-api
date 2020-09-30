//var question = "What is the fourth scale degree of Messian's 9 note symmetrical scale, also known as the fourth mode of limited transposition, if the root is concert G?";
//
//var answer = "B"


const questionPage = Vue.createApp({
    delimiters: ['[[', ']]'],
    export {
    setup() {
            const questionPackage = []


            const getRandomQuestion = () => {
            const url = "/api/question/";
            axios.get(url)
                .then(response => {
                    this.questionPackage = response.data
                    console.log(this.questionPackage)
                })
            }
        }
    },

 })