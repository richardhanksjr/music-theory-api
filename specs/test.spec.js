import { mount } from '@vue/test-utils'
import TestComponent from '/code/js_assets/test.vue'



test('mount a vue component', () => {
    const wrapper = mount(TestComponent)
    expect(wrapper.html()).toMatchSnapshot
 })
