<template>
  <div class="hello">
    <div class="list-group" v-for="item in typeList" @click="goToContent(item.id)">
      <img :src="item.image"
           alt="">
      <div class="optice"></div>
      <p>{{item.name}}</p>
    </div>


  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'HelloWorld',

    data() {
      return {
        typeList: []
      }
    },
    created() {
      var that = this;
      axios.get('http://127.0.0.1:8000/api/typeInfo/').then(function (res) {
        if (res.data) {
          that.typeList = res.data
        }
      })
    },
    methods:{
      goToContent(id){
          this.$router.push({
            path:`/describe/${id}`
          })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .list-group {
    width: 300px;
    height: 200px;
    padding: 10px 0 0 10px;
    float: left;
    position: relative;
    text-align: center;
  }

  .list-group p {
    position: absolute;
    top: 45%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 24px;
  }

  .list-group img {
    width: 100%;
    height: 100%;

  }

  .optice {
    width: 300px;
    height: 200px;
    background: rgba(0, 0, 0, 0.2);
    position: absolute;
    top: 10px;
    left: 10px;
  }

  @media screen and (max-width: 450px) {
    .list-group {
      width: 192px;
      height: 140px;

    }

    .optice {
      width: 192px;
      height: 140px;
      background: rgba(0, 0, 0, 0.2);
      position: absolute;
      top: 10px;
      left: 10px;
    }

    .list-group p {
      position: absolute;
      top: 40%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: white;
      font-size: 20px;
    }
  }

  @media screen and (max-width: 375px) {
    .list-group {
      width: 172px;
      height: 130px;

    }

    .optice {
      width: 172px;
      height: 130px;
      background: rgba(0, 0, 0, 0.2);
      position: absolute;
      top: 10px;
      left: 10px;
    }

    .list-group p {
      position: absolute;
      top: 40%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: white;
      font-size: 22px;
    }
  }
</style>
<style>

</style>
