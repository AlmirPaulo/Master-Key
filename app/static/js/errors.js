new Vue({
    el:'#app',
    delimiters: ['[[',']]'],
    template: `<div class="container">
                <p class="text-light fw-bold">[[ msg ]]</p>
                <button class="btn btn-success" v-on:click="validations() === 'OK' ? getMSGs() : validations()">Ok!</button>

            </div>`  
,
    data: {msg: ''},
    methods: { 
        getMSGs(){
            //Set Variables
            const req = new XMLHttpRequest()
            const url = window.location
            const hint = document.getElementById('hint')
            const mp = document.getElementById('mp')
            const repeatMP = document.getElementById('repeat-mp')

            const data = {mp:mp.value, repeat_mp:repeatMP.value, hint:hint.value}

            //Send Post Resquest
            req.open('POST', url, false)
            req.setRequestHeader("Content-Type","application/json")
            req.send(JSON.stringify(data))
            //Get Response
            this.msg = req.responseText


        },
        validations(){
            const hint = document.getElementById('hint')
            const mp = document.getElementById('mp')
            const repeatMP = document.getElementById('repeat-mp')
           if(hint.value === '' || mp.value === ''|| repeatMP.value === ''){
            this.msg = 'All fields must to be filleds.'
           } 
            else{ return 'OK'}
        }
    },


})
