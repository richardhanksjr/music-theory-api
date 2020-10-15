<template>
    <div>
        <fieldset v-for="answer in questionPackage.answer_options" class="custom-control custom-radio">
                    <input class="list-group-item" v-model="answerVal" :value="answer" type="radio" id="answer" name="response" @click="evaluateAnswer(answer)"><label class="label">{{ answer }}</label><br>
        </fieldset>
        <answer :message="message" :styleMessage="styleMessage"></answer>
        <br>
         <button :style="styleMessage" v-if="message" class="btn btn-outline-secondary" @click="nextQuestion">Next Question</button>
    </div>
</template>

<script>
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

    var jabs = ["No gigs for you.",
            "You were kidding, right?",
            "We're all speechless at your ineptitude.",
            "Welp, the good news is there's no money to be made in music anyway.",
            "You jive turkey.",
            "Get off the stage!",
            "Booooooooooo!",
            "Go study and don't forget to vote.",
            "Look, why not just give up? You're parents wanted you to be a lawyer anyway."]
    import Answer from './Answer.vue'
    export default {
        name: "Choices",
        components: {
            answer: Answer
        },
        props: {
            questionPackage: Object,
        },
        data() {
            return {
                answerVal: "",
                message: "",
                styleMessage: {
                    color: 'darkred',
                },
            }

        },
        computed: {
           questionObject() {
                return this.questionPackage
           }
        },
        methods: {
            evaluateAnswer(answer) {
                axios.post('api/answer', {"key": this.questionObject.key, "answer": answer})
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
}


</script>

<style scoped>

</style>