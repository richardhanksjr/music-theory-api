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
            <div class="text-muted" v-if="!hideHints">
                    <button v-if="!hintGiven" :style="styleQuestion" class="btn btn-outline-secondary" @click="helpSteps">Hint</button>
                <br>

                <br>
                    <div v-for="hint in hints">
                        <h5 v-if="hints" :style="styleMessage"  @mouseover="showAnswer = true;" @mouseleave="showAnswer = false;">{{ hint['prompt'] }}</h5>

                        <h6 v-if="showAnswer">{{ hint['answer'] }}</h6>
                    </div>

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

    import Answer from './Answer.vue'
    export default {
        name: "Question",
        components: {
            'answer': Answer,
        },
        data() {
            return {
                questionPackage: {},
                answerVal: "",
                message: "",
                hints: {},
                correct: false,
                hideHints: false,
                showAnswer: false,
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

                    if (this.answerVal === this.questionPackage.answer) {
                        if (this.hintGiven) {
                            //they got it right but not without help
                            this.message = "That's right, keep studying though.";
                                }
                        else {
                            // they got it right on their own
                            this.message = "Correct!";
                            this.correct = true;
                            }
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
                this.hints = {};
                this.correct = false;
                this.hideHints = false;
                this.hintGiven = false;
            },
            helpSteps(){
                        if (this.questionPackage.help_steps) {
                            this.hints = this.questionPackage.help_steps;
                            this.hintGiven = true;
                            }
                        else {
                            this.hints = "Sorry, we don't have any helpful hints on this one."
                        }

            },

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