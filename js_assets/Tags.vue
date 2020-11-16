<template>
    <div>
        <button v-for="tag in tagList" :key="tag.name">
            {{ tag.name }}
        </button>
    </div>
</template>

<script>


    export default {
        name: "tags",
        props: {
            message: String,
            styleMessage: Object,
        },

  }
</script>

<style scoped>

</style>