<template>
  <div>
    <header class="jumbotron">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <h1>请发表对ｖｕｅ的评论</h1>
          </div>
        </div>
      </div>
    </header>
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <form action="">
            <div class="form-group">
              <label>用户名</label>
              <input type="text" class="form-control" placeholder="用户名" v-model="name">
            </div>
            <div class="form-group">
              <label>评论内容</label>
              <textarea class="form-control" placeholder="评论内容" rows="6" v-model="content"></textarea>
            </div>
            <div class="form-group">
              <button class="btn btn-default pull-right" type="button" @click="add">提交</button>
            </div>
          </form>
        </div>
        <div class="col-md-8">
          <h3 class="reply">评论回复：</h3>
          <h2 v-show="comments.length===0">暂无评论，点击左侧添加评论！！！</h2>
          <ul class="list-group">
            <!--<li class="list-group-item">-->
              <!--<a href="#" class="btn btn-primary btn-xs pull-right" >删除</a>-->
              <!--<p class="user">-->
                <!--<em>xxx</em><span>说：</span>-->
              <!--</p>-->
              <!--<p class="content">vue不错</p>-->
            <!--</li>-->

            <li class="list-group-item" v-for="(comment,index) in comments" :key="index">
              <a href="#" class="btn btn-primary btn-xs pull-right" @click="deleteItem(index)">删除</a>
              <p class="user">
                <em>{{comment.name}}</em><span>说：</span>
              </p>
              <p class="content">{{comment.content}}</p>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        comments:[
        {
          name:'Bob',
          content:'啥几把玩意！！'
        },
        {
          name:'TFBOY',
          content:'啥几把玩意！！'
        },
        {
          name:'TOM',
          content:'啥几把玩意！！'
        }
      ],
        name:'',
        content:'',
    }
    },
    methods:{
      add(){
        //检查输入的合法性
        const name = this.name.trim();
        const content = this.content.trim();
        if (!name || !content){
          alert('姓名或内容不能为空！');
          return;
        }
        const comment = {
          name,
          content,
        };
        this.comments.unshift(comment);
        this.name='';
        this.content = '';

      },
      deleteItem(index){
        const comment_list = this.comments;
        if(window.confirm(`确定删除${comment_list[index].name}评论吗？`)){
          comment_list.splice(index,1);
        }
      }
    },
    name: "Practice",


  }
</script>

<style scoped>
  .reply{
    margin-top: 0;
  }
  .user{
    font-size: 22px;
  }
  .user em{
    font-style: normal;
  }
  .content{
    padding:0 50px;
  }
</style>
