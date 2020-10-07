
// Vue Instance
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

const url = '/api/answer'
var jabs = ["No gigs for you.",
            "You were kidding, right?",
            "We're all speechless at your ineptitude.",
            "Welp, the good news is there's no money to be made in music anyway.",
            "You jive turkey.",
            "Get off the stage!",
            "Booooooooooo!",
            "Go study and don't forget to vote.",
            "Look, why not just give up? You're parents wanted you to be a lawyer anyway."]

const questionPage = Vue.createApp({
    delimiters: ['[[', ']]'],

    data() {
         return {
            questionPackage: [],
            message: "",
            answerVal: "",
         }
    },
    methods: {
    evaluateAnswer(answer) {
            axios.post(url, {"key": this.questionPackage.key, "answer": answer})
            .then(response => {

                if (response.data.correct) {
                    this.message = "Correct!"
                }
                else {
                        var jab = jabs[Math.floor(Math.random() * jabs.length)];
                        this.message = `'${response.data.correct_answer}' was the correct answer. ${jab}`
                }
            })
            this.answerVal = "";
        },
    nextQuestion() {
        axios.get('/api/question')
                .then(response => {
                this.questionPackage = response.data
                });
            this.answerVal = "";
            this.message = "";
    }
    },
    mounted() {
            axios.get('/api/question')
                .then(response => {
                this.questionPackage = response.data
                });
            },
    })

questionPage.mount("#questionPage");
//}