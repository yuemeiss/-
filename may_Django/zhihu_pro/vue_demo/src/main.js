//  入口ｊｓ :创建Ｖue 实例
import Vue from 'vue'
// import App from './testApp.vue'
import AdminApp from './AdminApp'
// import VueResource from 'vue-resource'

//声明使用插件,
// Vue.use(VueResource); //ajax插件，内部会给ｖｍ和组件对象添加一个$http属性
new Vue({
  el: '#app',
  components: {
    AdminApp
  },
  template: '<AdminApp/>',
});

