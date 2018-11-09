<template>
  <div id="wrapper">
   <!-- <main> -->
      <div class="left-side-column">
        <div class="">
          <router-link to="/">
            <img id="logo50" src="~@/assets/logo.png" alt="electron-vue" >
          </router-link>
        </div>
        <div class="">
          <router-link to="/informations">
            <img id="logo50" src="~@/assets/logo.png" alt="electron-vue" >
          </router-link>
        </div>


      </div>
      <div class="right-side">
        <paint-page></paint-page>
      </div>
    <!-- </main> -->
    <!--
      <div class="left-side-column">

        <router-link to="/">
          <img id="logo50" src="~@/assets/logo.png" alt="electron-vue" >
        </router-link>

      </div>


     -->
  </div>
</template>

<script>
  import PaintPage from './LandingPage/PaintPage'

  export default {
    name: 'landing-page',
    components: { PaintPage },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    }
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body { font-family: 'Source Sans Pro', sans-serif; }

  #wrapper {
    display: flex;
    background:
      radial-gradient(
        ellipse at top left,
        rgba(255, 255, 255, 1) 40%,
        rgba(229, 229, 229, .9) 100%
      );
    height: 100vh;
    padding: 0px 0px;
    width: 100vw;
  }

  #logo {
    width: 50px;
    height: 50px;
  }

  #logo50 {
    width: 50px;
    height: 50px;
    display: block;
    margin-right: auto;
    margin-left: auto;
    margin-top: 10px;
  }

  .left-side {
    display: flex;
    width: 10vh;
    height: 100vh;
    flex-direction: column;
    background-color: #444444
  }

  .right-side {
    display: flex;
    height: 100vh;
    width: 90vw;
  }

  .left-side-column {
    width: 20vh;
    height: 100vh;
    padding: 5px;
    background-color: #444444
  }

  .welcome {
    color: #555;
    font-size: 23px;
    margin-bottom: 10px;
  }

  .title {
    color: #2c3e50;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 6px;
  }

  .title.alt {
    font-size: 18px;
    margin-bottom: 10px;
  }

  .doc p {
    color: black;
    margin-bottom: 10px;
  }

  .left-side button {
    width: 50px;
    height: 50px;
    font-size: .8em;
    cursor: pointer;
    outline: none;
    padding: 0.75em 2em;
    border-radius: 2em;
    display: inline-block;
    color: #fff;
    background-color: #4fc08d;
    transition: all 0.15s ease;
    box-sizing: border-box;
    border: 1px solid #4fc08d;
  }

  .doc button {
    font-size: .8em;
    cursor: pointer;
    outline: none;
    padding: 0.75em 2em;
    border-radius: 2em;
    display: inline-block;
    color: #fff;
    background-color: #4fc08d;
    transition: all 0.15s ease;
    box-sizing: border-box;
    border: 1px solid #4fc08d;
  }

  .doc button.alt {
    color: #42b983;
    background-color: transparent;
  }
</style>
