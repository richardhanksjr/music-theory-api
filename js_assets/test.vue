<template>
  <div>
    <h1>{{ value }}</h1>
  </div>
</template>

<script>
  export default {
    props: {
      value: {
        type: String,
        default: 'RichardHanks2020'
      }
    }
  }
</script>
