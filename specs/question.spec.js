import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import { mount } from '@vue/test-utils'
import Question from '/code/js_assets/Question.vue'



test('mount question component', () => {
    const wrapper = mount(Question)
    expect(wrapper.html()).toMatchSnapshot()
 })
