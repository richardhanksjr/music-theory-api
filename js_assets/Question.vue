<template>
    <div>
        <br>
            <h2 :style="styleQuestion" name="question" id="question">{{ questionPackage.question }}</h2>
        <br>
            <fieldset v-for="answer in questionPackage.answer_options" class="custom-control custom-radio">
                    <input class="list-group-item" v-model="answerVal" :value="answer" type="radio" id="answer" name="response" @click="evaluateAnswer(answer); hideHints = true;"><label class="label">{{ answer }}</label><br>
            </fieldset>

                <answer :message="message" :styleMessage="styleMessage"></answer>
        <br>
            <button :style="styleMessage" v-if="message" class="btn btn-outline-secondary" @click="nextQuestion">Next Question</button>
        <br>
        <br>
            <div v-if="!hideHints">
                    <button  :style="styleQuestion" class="btn btn-outline-secondary" @click="helpSteps">Want a hint?</button>
                <br>
                    <hr v-if="hints" class="rounded">
                <br>
                    <h5 :style="styleMessage">{{ hints }}</h5>
            </div>
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

    var prompts = [
    "Think of it this way...",
    "Did you try this?...",
    "The hypotenuse bro...THE HYPOTENUSE!!!",
    "Call 1-800-ask-now1"
   ]

    import Answer from './Answer.vue'
    export default {
        name: "Question",
        components: {
            'answer': Answer,
        },
        data() {
            return {
                questionPackage: [],
                helpPackage: [],
                answerVal: "",
                message: "",
                hints: "",
                correct: false,
                hideHints: false,
                hintGiven: false,
                styleMessage: {
                    color: 'darkred',
                },
                styleQuestion: {
                    color: 'Dark midnight blue'
                    }
            }
        },
        methods: {
            evaluateAnswer(answer) {
                axios.post('api/answer', {"key": this.questionPackage.key, "answer": answer})
                .then(response => {

                    if (response.data.correct && this.hintGiven) {
                    //they got it right but not without help
                    this.message = "That's right, keep studying though.";
                    }
                    if (response.data.correct && !this.hintGiven) {
                        //they got it right on their own
                        this.message = "Correct!";
                        this.correct = true;
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
                // reset everything
                this.answerVal = "";
                this.message = "";
                this.hints = "";
                this.correct = false;
                this.hideHints = false;
                this.hintGiven = false;
            },
            helpSteps(){
            axios.post('api/help', {"key": this.questionPackage.key})
                .then(response => {
                        if (response.data) {
                            this.helpPackage = response.data;
                            var hint = helpPackage[Math.floor(Math.random() * helpPackage.length)];
                            this.hints = `${hint}`;
                            this.hintGiven = true;
                            }
                        else {
                            this.hints = "Sorry, we don't have any helpful hints on this one."
                        }
                   }
            }
        },
        mounted() {
            axios.get('/api/question')
                .then(response => {
                    this.questionPackage = response.data
                });
            },
    };

</script>

<style scoped>

</style>