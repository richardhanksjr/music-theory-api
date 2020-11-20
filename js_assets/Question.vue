<template>
    <div name="question" id="question">
        <br>
            <h2 :style="styleQuestion">{{ questionPackage.question }}</h2>
        <br>
            <fieldset v-for="(answer, index) in questionPackage.answer_options" class="custom-control custom-radio">
                <div class="radio-buttons">
                    <input class="list-group-item" v-model="answerVal" :disabled="disableAnswer" :value="answer" type="radio" id="answer" name="response" @click="evaluateAnswer(answer); hideHints = true;"><label class="label">{{ answer }}</label><br>
                </div>
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
                        <div v-for="(hint, index) in hints">

                            <br>
                                <h4 :style="styleMessage">{{ hint['prompt'] }}</h4>
                            <br>
                                <h6 v-if="hintIndex > index">{{ hint['answer'] }}</h6>

                                <button v-if="hintIndex === index" :style="styleQuestion" class="btn btn-outline-secondary" @click="hintIndex++; showNextHintButton = true;">Show Answer</button>
                            <br>
                                <button v-if="hintIndex === (index + 1) && showNextHintButton && hintLength > 1" :style="styleQuestion" class="btn btn-outline-secondary" @click="helpSteps">Show Next Hint</button>
                            <br>
                        </div>
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
                hints: [],
                noMoreHintsMessage: "",
                correct: false,
// the inchworm that inches ahead of the index in the for loop:
                hintIndex: 0,
// the length of the current state of the array:
                hintLength: 0,
// how many hints user requested:
                hintCount: 0,
                showNextHintButton: false,
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
                    axios.post('api/attempt', {"key": this.questionPackage.key, "answer": answer})
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
                this.hints = [];
                this.correct = false;
                this.hintGiven = false;
                this.hideHints = false;
                this.showNextHintButton = false;
                this.noMoreHintsMessage = "";
                this.hintIndex = 0;
                this.hintCount = 0;
                this.hintLength = 0;
            },
             helpSteps(){
                         this.hintLength = Object.keys(this.questionPackage.help_steps).length;
                            if(this.hintLength){
                                const oneHint = this.questionPackage.help_steps.pop();
                                this.hints.push(oneHint);
                                this.hintGiven = true;
                                this.showAnswerButton = true;
                                this.showNextHintButton = false;
                                this.hintCount++;
                                }
            },
        },
        computed : {
            noMoreHints() {
                if(this.hintLength === 1) {
                    return this.noMoreHintsMessage = "We're not giving out any more hints on this one";
                }
            },
            disableAnswer() {
                if (this.answerVal) {
                    return true
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