new Vue({
    el:'#app',
    delimiters: ['[[',']]'],
    template: '<p class="text-danger">[[ msg ]]</p>',
    data: {msg: ''},
    methods: { 
        getMSGs(){
            const xhr = new XMLHttpRequest();
            xhr.open("POST", window.location, false); 
            xhr.onload = function(event){ 
                alert("Success, server responded with: " + event.target.response); // raw response
            }; 
        }
    }


})
