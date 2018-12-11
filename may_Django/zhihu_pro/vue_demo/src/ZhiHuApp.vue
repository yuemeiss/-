<template>
    <div class="container">
      <div class="question">{{question.title}}</div>
      <hr>
      <div class="answer" v-for="(con,index) in answer.results" :key="index">
        <div v-html="con.content"></div>
        <hr>
      </div>
    </div>
</template>

<script>
  import axios from 'axios'
    export default {
        data(){
          return {
            question:'',
            answer:'',
          }

        },
      mounted(){
        const url = 'http://127.0.0.1:8000/question/300268616';
        // this.$http.get(url).then(
        //   response => {
        //     //成功了
        //     this.question = response.data;
        //   },
        //   response => {
        //     //失败了
        //     console.log('请求失败');
        //   }
        // )
        //使用axios 发送请求
      //   axios.get(url).then(response => {}).catch(error => {})
        //封装一个ajax的请求函数
        async function getData(url) {
          return axios.get(url).then(response => {
            return response.data
          }).catch(err =>{
            alert('请求失败！')
          })
        }
        let prdat = this;
        async function sendData(urls) {
        let reuslt = await getData(urls);
        // console.log('===',reuslt);
          prdat.question = reuslt;
        let newurl = `http://127.0.0.1:8000/answer/${reuslt.id}`;
        prdat.answer = await getData(newurl);
        // console.log(res);
        }
        sendData(url);
      },
      // methods
        name: "zhihuApp"
    }
</script>

<style scoped>

</style>
