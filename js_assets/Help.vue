<template>
    <div>
        <button :style="styleQuestion" class="btn btn-outline-secondary" @click="helpSteps">Want a hint?</button>
        <br>
            <hr v-if="hints" class="rounded">
        <br>
            <h5 :style="styleMessage">{{ hints }}</h5>
    </div>
</template>

<script>

    var prompts = [
    "Think of it this way...",
    "Did you try this?...",
    "The hypotenuse bro...THE HYPOTENUSE!!!",
    "Call 1-800-ask-now1"
   ]

    export default {
        name: "Help",
        data() {
            return {
                hints: "",
                styleQuestion: {
                    color: 'Dark midnight blue'
                    },
                styleMessage: {
                    color: 'darkred',
                },
            }
        },
        methods: {
            helpSteps(){
                var hint = prompts[Math.floor(Math.random() * prompts.length)];
                this.hints = `${hint}`
            }
        },

  }
</script>

<style scoped>

</style>