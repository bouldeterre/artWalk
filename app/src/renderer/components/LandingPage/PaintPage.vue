<template>
  <div  id="paint-page" >
    <div id="paint-info"  class="info" >

      <electron-link
         class="link"
         href="https://www.rijksmuseum.nl/nl/collectie/SK-C-5">
         <div class="title">{{PaintName}}</div>
         <p>eeeeeeeeeeeeeeeeeeeeeeee</p>
       </electron-link>

    </div>

    <div class="paint-actions info" >
      <p>{{ message }}</p>
      <button v-on:click="reverseMessage">Next</button>
    </div>

    <div class="info">
      <div class="title">Information</div>
      <div class="items">
        <div class="item">
          <div class="name">Path:</div>
          <div class="value">{{ path }}</div>
        </div>
        <div class="item">
          <div class="name">Route Name:</div>
          <div class="value">{{ name }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import ElectronLink from 'vue-electron-link'
  const zerorpc = require('zerorpc')
  let client
  export default {
    components: {
      ElectronLink
    },
    data () {
      return {
        electron: process.versions.electron,
        name: this.$route.name,
        node: process.versions.node,
        path: this.$route.path,
        platform: require('os').platform(),
        vue: require('vue/package.json').version,
        message: 'Hello Vue.js!',
        PaintName: 'Schutters van wijk II onder leiding van kapitein Frans Banninck Cocq, bekend als de ‘Nachtwacht’',
        PaintURL: ''
      }
    },
    methods: {
      reverseMessage: function () {
        this.message = this.message.split('').reverse().join('')
        console.log('Invoke echo')
        client.invoke('echo', 'toto', (error, res) => {
          if (error) {
            console.error(error)
          }
          console.log('Res:' + res)
        })
      },
      handleRemoved: function (success) {
        alert('success' + success)
      }
    },
    beforeMount () {
      console.log('beforeMount')
      client = new zerorpc.Client()
      client.connect('tcp://127.0.0.1:4242')
    }
  }
</script>
<style scoped>

  #paint-page {
    height: 100vh;
    width: 100vw;
    padding: 0;
    margin: 0;
    background-repeat: no-repeat;
    background-position: center ;
    background-size: cover;
    background-image: url("~@/assets/walk.jpg");
    background-color: black;
  }

  .info {
    background-color: #222222;
    width:200;
    margin: 5px;
  }

  .info p {
      color: #ffffff;
  }

  .title {
    color: #ffffff;
    font-size: 18px;
    font-weight: initial;
    letter-spacing: .25px;
    margin-top: 10px;
  }

  .items { margin-top: 8px; }

  .item {
    display: flex;
    margin-bottom: 6px;
  }

  .item .name {
    color: #999999;
    margin-right: 6px;
  }

  .item .value {
    color: #ff00ff;
    font-weight: bold;
  }
</style>
