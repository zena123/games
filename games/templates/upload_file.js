 let UploadApp = new Vue({
    el: '#fileUpload',
    mixins: [djVueMixin],
    data() {
        return {
            actionURL: '{% url "core:import_data" %}',
            form: {

            }
        }
    },
    methods: {
        success(response) {
            window.location.reload();
        }
    }
})
// remove hidden
let appEl = document.getElementById('fileUpload');
appEl.removeAttribute("hidden");