new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    template: `
      <div>
    <a href="#" v-on:click='getHint()' class="text-white ">I FORGET my Master Password!</a>
    </div>`,
    methods: {
        getHint(){
            const req = new XMLHttpRequest()
            const url = 'http://localhost:5010/hint'
            req.open('GET', url, false)
            req.send()
            const hint = req.responseText
            alert(hint)
        }
    }


})
