<template>
    <div name="question" id="question">
        <br>
            <h2 :style="styleQuestion">{{ questionPackage.question }}</h2>
        <br>
            <fieldset v-for="answer in questionPackage.answer_options" class="custom-control custom-radio">
                    <input class="list-group-item" v-model="answerVal" :value="answer" type="radio" id="answer" name="response" @click="evaluateAnswer(answer), logAttempt(answer); hideHints = true;"><label class="label">{{ answer }}</label><br>
            </fieldset>

                <answer :message="message" :styleMessage="styleMessage"></answer>
        <br>
            <button :style="styleMessage" v-if="message" class="btn btn-outline-secondary" @click="nextQuestion">Next Question</button>
        <br>
        <br>
            <div class="text-muted" v-if="!hideHints">


                    <button v-if="!hintGiven" :style="styleQuestion" class="btn btn-outline-secondary" @click="helpSteps">Hint</button>
                    <div v-if="hintGiven">
                        <h3 class="text-muted">Hints</h3>
                        <br>
                            <h4 :style="styleMessage">{{ questionPackage.help_steps[0]['prompt'] }}</h4>
                        <br>
                            <h6 v-if="showAnswer">{{ questionPackage.help_steps[0]['answer'] }}</h6>
                        <br>
                            <button v-if="showAnswerButton" :style="styleQuestion" class="btn btn-outline-secondary" @click="showAnswer = true; showAnswerButton = false; showNextHintButton = true;">Show Hint's Answer</button>
                        <br>
                            <button v-if="hintLength > 1 && showNextHintButton" :style="styleQuestion" class="btn btn-outline-secondary" @click="showNextHint = true; showNextAnswerButton = true; showNextHintButton = false; hintCount++;">Show Next Hint</button>
                        <br>
                            <h4 v-if="showNextHint" :style="styleMessage">{{ questionPackage.help_steps[hintIndex]['prompt'] }}</h4>
                        <br>
                            <h6 v-if="showNextAnswer">{{ questionPackage.help_steps[hintIndex]['answer'] }}</h6>
                        <br>
                            <button v-if="showNextAnswerButton" :style="styleQuestion" class="btn btn-outline-secondary" @click="showNextAnswer = true; showNextAnswerButton = false;">Show Hint's Answer</button>
                        <br>
                            <p>{{ noMoreHintsMessage }}</p>
                    </div>
            </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import VueAxios from 'vue-axios';
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
                noMoreHintsMessage: "",
                correct: false,
                hintIndex: 0,
                hintLength: 0,
                hintCount: 0,
                hideHints: false,
                showAnswer: false,
                showAnswerButton: false,
                showNextAnswer: false,
                showNextAnswerButton: false,
                showNextHint: false,
                showNextHintButton: false,
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
            logAttempt(answer) {
                axios.post('api/attempt', {"key": this.questionPackage.key, "answer": answer})
                .then(response => {
                    console.log(response);
                })
            },
            nextQuestion() {
            axios.get('/api/question')
                    .then(response => {
                    this.questionPackage = response.data
                    });
                // reset everything
                this.answerVal = "";
                this.message = "";

                this.correct = false;
                this.showAnswer = false;
                this.showAnswerButton = false;
                this.showNextAnswer = false;
                this.showNextAnswerButton = false;
                this.hideHints = false;
                this.hintGiven = false;
                this.showNextHint = false;
                this.showNextHintButton = false;
                this.noMoreHintsMessage = "";
                this.multipleHints = false;
                this.hintIndex = 0;
                this.hintCount = 0;
            },
             helpSteps(){
                         this.hintLength = Object.keys(this.questionPackage.help_steps).length;
                            if(this.hintLength){
                                if(this.hintLength === 1) {
                                    this.hintGiven = true;
                                    this.showAnswerButton = true;
                                    this.hintCount++;
                                    }
                                else {
                                    this.hintGiven = true;
                                    this.showAnswerButton = true;
                                    this.hintIndex++;
                                    this.hintCount++;
                                    }
                                }
            },
        },
        computed : {
            noMoreHints() {
                if(this.hintCount === this.hintLength) {
                    return this.noMoreHintsMessage = "We're not giving out any more hints on this one";
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