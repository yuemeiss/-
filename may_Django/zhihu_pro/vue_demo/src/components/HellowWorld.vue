<template>
    <div>
        <p class="msg">{{msg}}</p>
    </div>
</template>

<script>
    //默认向外　暴露一个配置对象
    export default { //配置对象（和ｖｕｅ代码一样）
        data() { //必须写成函数形式的
            return {
                msg: 'hello Vue component'
            }
        }
    }
</script>

<style>
    .msg {
        color: blue;
        font-size: 30px;
    }
</style>

