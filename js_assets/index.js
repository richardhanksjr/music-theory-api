// import _ from 'lodash';
//
// function component() {
//   const element = document.createElement('div');
//   element.innerHTML = _.join(['hello', 'lodash', 'from rebuild']);
//   return element;
// }
// document.body.appendChild(component());
import Vue from 'vue';
import Index from './Index.vue';

new Vue({
   el: "#hello",
   render: h => h(Index)
});