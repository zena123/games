from django.core.validators import FileExtensionValidator
from djvue.fields import FileField
from djvue.serializers import FileUploadSerializer
from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from .helper_functions import import_games, import_teams
from .models import Game, Team


class CSVUploadSerializer(FileUploadSerializer):
    """Allows only CSV files to be uploaded"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["file"].validators.append(
            FileExtensionValidator(allowed_extensions=["csv"])
        )


class HandleUploadSerializer(serializers.Serializer):
    csv_file = FileField(style={"upload_url": reverse_lazy("core:csv_upload")})

    def create(self, validated_data):
        file = validated_data.pop("csv_file", None)
        import_teams(file["path"])
        import_games(file["path"])
        return file


class TeamSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField()
    name = (
        serializers.CharField()
    )  # disable the validation since it's nested and unique will cause issues

    class Meta:
        model = Team
        fields = (
            "pk",
            "name",
        )


class GameSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()

    class Meta:
        model = Game
        fields = (
            "pk",
            "team1",
            "team1_score",
            "team2",
            "team2_score",
        )

    def update(self, instance, validated_data):
        """update game data, in case of new Team """
        team1 = validated_data.pop("team1", None)
        team2 = validated_data.pop("team2", None)
        if team1 and team1.get("name"):
            Team.objects.filter(pk=team1["pk"]).update(name=team1["name"])
        if team2 and team2.get("name"):
            Team.objects.filter(pk=team2["pk"]).update(name=team2["name"])
        instance = super(GameSerializer, self).update(instance, validated_data)
        return instance