<template>
    <div>
        <hr class="rounded">
            <h5 :style="styleMessage">{{ message }}</h5>
        <br>
    </div>
</template>

<script>


    export default {
        name: "Answer",
        props: {
            message: String,
            styleMessage: Object,
        },

  }
</script>

<style scoped>

</style>