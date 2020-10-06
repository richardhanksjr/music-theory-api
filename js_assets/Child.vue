<style scoped>
    p {
        font-size: 2em;
        color: red;
        background-color: black;
    }
</style>

<template>
  <p>{{ greeting }} Vue!</p>
</template>

<script>
module.exports = {
  data: function() {
    return {
      greeting: "Hello"
    };
  }
};
</script>

