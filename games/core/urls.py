from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    CSVUploadView,
    GetGamesView,
    GetScoresView,
    HandleUploadView,
    HomeTemplateView,
)

app_name = "core"

router = SimpleRouter()
router.register("games", GetGamesView, basename="games"),


urlpatterns = router.urls

urlpatterns += [
    path("", HomeTemplateView.as_view(), name="home"),
    path("csv-upload/", CSVUploadView.as_view(), name="csv_upload"),
    path("import-data/", HandleUploadView.as_view(), name="import_data"),
    path("get-scores/", GetScoresView.as_view(), name="get_scores"),
]