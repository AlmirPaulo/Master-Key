new Vue({
    el:'#app',
    template: `<a href="#" v-on:click='hint' class="text-white ">I FORGET my Master Password!</a>`,
    methods: {
        hint(){
            //fetch hint at endpoint
            alert('hint')
        }
    },
    data: { hint: ''}

})
