<template>
    <div>
        <img class="logo" src="./assets/logo.png" alt="大Ｖ">
        <!-- ３．使用组件标签 -->
        <HellowWorld/>
    </div>
</template>

<script>
    // 1.　引入组件
    import HellowWorld from './components/HellowWorld.vue'

    export default {
        //2.映射组件标签
        components: {
            HellowWorld
        }
    }
</script>

<style>
    .logo {
        width: 200px;
        height: 200px;
    }
</style>




