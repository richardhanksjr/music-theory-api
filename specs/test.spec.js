import { mount, shallowMount } from '@vue/test-utils'
import TestComponent from '/code/js_assets/test.vue'
import Question from '/code/js_assets/Question.vue'



test('mount a vue component', () => {
    const wrapper = mount(TestComponent, {
        propsData: {
            value: 'RichardHanks2020'
        }
    })
    expect(wrapper.html()).toMatchSnapshot()
 })

// comparing mount and shallow mount --- mount is recommended as a
// default to detect errors in child components early
test('QuestionComponent Shallow', () => {
    console.log(mount(Question).html())
    console.log(shallowMount(Question).html())
})

