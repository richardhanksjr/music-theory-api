// import _ from 'lodash';
//
// function component() {
//   const element = document.createElement('div');
//   element.innerHTML = _.join(['hello', 'lodash', 'from rebuild']);
//   return element;
// }
// document.body.appendChild(component());
import Vue from 'vue';
import Parent from './Parent.vue';
import Questions from './Questions.vue'
import axios from 'axios';
import VueAxios from 'vue-axios';


new Vue({
   el: "#hello",
   render: h => h(Parent)
});

new Vue({
   el: "#questions",
   render: h => h(Questions)
});