
<style scoped>
    p {
        font-size: 2em;
        color: red;
        background-color: black;
    }
</style>

<template>
  <p> {{message}} </p>
</template>

<script>
  export default {
    props: {
        message: String
    }
  }
</script>
