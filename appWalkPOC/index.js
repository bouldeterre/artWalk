// renderer.js

// const zerorpc = require("zerorpc")
// let client = new zerorpc.Client()
// client.connect("tcp://127.0.0.1:4242")
//
// let button = document.querySelector('#button')
//
//
// button.addEventListener('click', function () {
//        audio.currentTime = 0;
//        audio.play();
// });
// formula.addEventListener('input', () => {
//   client.invoke("calc", formula.value, (error, res) => {
//     if(error) {
//       console.error(error)
//     } else {
//       result.textContent = res
//     }
//   })
// })
// formula.dispatchEvent(new Event('input'))

var app = new Vue({
  el: '#app',
  data: {
    message: 'Helloue!'
  },
  methods: {
    pushButton: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
