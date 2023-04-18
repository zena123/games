let AppScore = new Vue({
    el: '#app',
    mixins: [djVueMixin],
    data() {
        return {
            actionURL: '{% url "core:import_data" %}',
            scoresURL: '{% url "core:get_scores" %}',
            games: [],
            nextGamesURL: null,
            previousGamesURL: null,
            scores: [],
            form: {},
            add_form: {
                team1: {
                    name: "",
                },
                team1_score: 0,
                team2: {
                    name: "",
                },
                team2_score: 0,
            },
        }
    },
    created: function () {
        this.fetch_games();
        this.fetch_scores();
    },
    methods: {
        success(response) {
            this.fetch_games();
            this.fetch_scores();
        },
        fetch_games: function (url="{% url 'core:games-list' %}") {
            axios.get(url)
                .then(response => {
                    this.games = response.data.results
                    this.nextGamesURL = response.data.next;
                    this.previousGamesURL = response.data.previous;
                })
        },
        fetch_scores: function () {
            axios.get("{% url 'core:get_scores' %}")
                .then(response => {
                    this.scores = response.data
                })
        },
        add_game: function () {
            axios.post("{% url 'core:games-list' %}", this.add_form)
                .then(response => {
                    this.reset_add_form();
                    this.success();
                })
                .catch(this.error)
        },
        reset_add_form: function () {
            this.add_form = {
                team1: {
                    name: "",
                },
                team1_score: 0,
                team2: {
                    name: "",
                },
                team2_score: 0,
            };
        },
        delete_game: function (pk) {
            axios.delete("{% url 'core:games-detail' 0 %}".replace(0, pk))
                .then(response => {
                    this.success();
                })
        },
        update_game: function (pk) {
            let data = this.games.filter(game => game.pk === pk)[0]
            axios.patch("{% url 'core:games-detail' 0 %}".replace(0, pk), data)
                .then(response => {
                    this.success();
                })
        },
    }
})

// remove hidden
let appEl = document.getElementById('app');
appEl.removeAttribute("hidden");