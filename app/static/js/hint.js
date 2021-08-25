new Vue({
    el:'#app',
    template: `<a href="#" v-on:click='hint' class="text-danger ">I Forgot my Master Password!</a>`,
    methods: {
        hint(){
            //fetch hint at endpoint
            alert('hint')
        }
    },
    data: { hint: ''}iidd

})
