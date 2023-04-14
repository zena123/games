 let UploadApp = new Vue({
    el: '#fileUpload',
    mixins: [djVueMixin],
    data() {
        return {
            actionURL: '{% url "core:import_data" %}',
            form: {
                csv_file: "",
            }
        }
    },
    methods: {
        success(response) {
            console.log("success")
        }
    }
})
// remove hidden
let appEl = document.getElementById('fileUpload');
appEl.removeAttribute("hidden");