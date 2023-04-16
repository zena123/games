 let AppScore= new Vue({
    el: '#getScores',
    mixins: [djVueMixin],
    data() {
        return {
            actionURL: '{% url "core:get_scores" %}',
            games: [],
            scores: [],
            form: {


            }
        }
    },
     created: function () {
        this.fetch_games();
     },
    methods: {
        success(response) {
            console.log("success")
        },
        fetch_games: function () {
            axios.get("{% url 'core:games-list' %}")
                .then(response => {
                    this.games = response.data.results
                })
        },
        delete_game: function (pk){
            axios.delete("{% url 'core:games-detail' 0 %}".replace(0,pk))
                .then(response => {
                    this.fetch_games();
                })
        },
    }
})
// remove hidden
let appEl2 = document.getElementById('getScores');
appEl2.removeAttribute("hidden");