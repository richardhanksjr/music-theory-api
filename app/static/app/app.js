//var question = "What is the fourth scale degree of Messian's 9 note symmetrical scale, also known as the fourth mode of limited transposition, if the root is concert G?";
//
var answer = "An interval that encompasses an octave or less"

import { onBeforeMount, onMounted } from '@vue/composition-api';
//window.onload = function () {
const questionPage = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
         questionPackage: [],
         message: "",
         answerVal: "",
         }
    },
    methods: {
    evaluateAnswer(Answer, answerVal) {
             this.Answer = Answer;
             if (Answer === answer) {
                this.message = "Correct!"

             }
             else {
                this.message = `Sorry, the correct answer is "${answer}"`
             }
            this.answerVal = "";
        }
    },

export default {
  setup() {
    onBeforeMount(() => {
      console.log('V3 beforeMount!');
    })

    onMounted(() => {
      console.log('V3 mounted!');
    })
  }
};

})

//}

//   export default {
//
//    onMounted(() =>
//           {
//           console.log('V3 mounted');
//            axios.get('/api/question/')
//                .then(response => {
//                this.questionPackage = response.data
//                });
//            },
//       }