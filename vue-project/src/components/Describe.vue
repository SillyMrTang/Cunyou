<template>
  <div>
    <div class="describe-title">
      <p>趣村游·{{contentObj.name}}</p>
      <div style="margin-top: 10px">
        <img src="http://app-image.cunyougo.com/favicon.ico.png" alt="">
        <span style="height:100%;
    vertical-align:middle;font-size: 18px;font-weight: 500;color: #000">趣村游</span>
      </div>
    </div>
    <a :href="item.path" v-for="item in contentObj.contents">
      <div class="describe-content">
        <div class="lf">
          {{item.name}}
        </div>
        <img class="rg" :src="item.image" alt="">
      </div>
    </a>
    <div v-if="contentObj.contents.length==0" style="font-size: 18px;margin-top: 200px">
      敬请期待
    </div>
  </div>

</template>

<script>
  import axios from 'axios'
  export default {
    name: "Describe",
    data() {
      return {
        contentObj:{
          contents:[]
        }
      }
    },
    mounted() {
      console.log(this.$route.params.id);
      const that = this;
      const id = that.$route.params.id;
      axios.get(`http://127.0.0.1:8000/api/typeInfo/${id}/`).then(function (res) {
        if (res.data) {
          console.log(res.data);
          that.contentObj = res.data
        }
      })
    }
  }
</script>

<style scoped>
  .describe-title {
    text-align: left;
    margin-left: 15px;
    border-bottom: 1px solid #dcdcdc;
    padding: 15px 15px 15px 0;
  }

  .describe-title img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    vertical-align: middle;
    margin-right: 10px;
  }

  .describe-title p {
    font-size: 24px;
    font-weight: 500;
    color: #000;
    margin-bottom: 0;
    margin-top: 0;

  }

  .describe-content {
    padding: 15px 15px 15px 0;
    height: 116px;
    margin-left: 15px;
    border-bottom: 1px solid #dcdcdc;
  }

  .describe-content div {
    width: 340px;
    font-size: 24px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    text-align: left;

  }

  .describe-content img {
    width: 185px;
    height: 116px;
  }

  .lf {
    float: left;
  }

  .rg {
    float: right;
  }

  @media screen and (max-width: 450px) {
    .describe-content div {
      font-size: 20px;
      width: 200px;
    }

    .describe-content img {
      width: 150px;
      height: 100px;
    }

    .describe-content {
      height: 100px;
    }
  }

  @media screen and (max-width: 375px) {
    .describe-content div {
      font-size: 16px;
      width: 170px;
    }

    .describe-content img {
      width: 140px;
      height: 85px;
    }

    .describe-content {
      height: 85px;
    }
  }
</style>
