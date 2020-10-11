<template>
    <child :message="message"></child>
</template>

<script>
    import Child from './Child.vue'
    export default {
        components: {
            'child': Child
        },
        data(){
            return {
                message: "Hello from parent!!"
            }
        }
    }

</script>

<style scoped>

</style>