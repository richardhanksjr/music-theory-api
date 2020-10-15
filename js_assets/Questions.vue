<template>
    <div>
        <br>
            <h2 :style="styleQuestion" name="question" id="question">{{ questionPackage.question }}</h2>
        <br>
            <choices :questionPackage="questionPackage"></choices>
        <br>
    </div>
</template>

<script>
    import Choices from './Choices.vue'
    export default {
        name: "Questions",
        components: {
            'choices': Choices,

        },
        data() {
            return {
                questionPackage: [],

                styleQuestion: {
                    color: 'Dark midnight blue'
                    }
            }
        },
        computed: {
            questionObject() {
                return this.questionPackage
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