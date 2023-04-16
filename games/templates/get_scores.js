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
        this.fetch_scores();
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
        fetch_scores: function (){
            axios.get("{% url 'core:get_scores' %}")
            .then(response => {
                    this.scores = response.data
                })
        },
        delete_game: function (pk){
            axios.delete("{% url 'core:games-detail' 0 %}".replace(0,pk))
                .then(response => {
                    this.fetch_games();
                })
        },
        update_game:  function (pk){
            let data = {};
            for (const i in this.games) {
                if (this.games[i]["pk"] == pk){
                    // data["team1"] = this.games[i]["team1"];
                    data["team1_score"] = this.games[i]["team1_score"];
                    // data["team2"] = this.games[i]["team2"]
                    data["team2_score"] = this.games[i]["team2_score"]
                }
            }
            axios.patch("{% url 'core:games-detail' 0 %}".replace(0,pk) ,data)
            .then(response => {
                    this.fetch_games();
                })
        },
    }
})
// remove hidden
let appEl2 = document.getElementById('getScores');
appEl2.removeAttribute("hidden");