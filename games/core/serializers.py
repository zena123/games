from djvue.fields import FileField
from rest_framework import serializers

from django.core.validators import FileExtensionValidator

from djvue.serializers import FileUploadSerializer
from rest_framework.reverse import reverse_lazy
from .helper_functions import import_teams, import_games
from .models import Game, Team


class CSVUploadSerializer(FileUploadSerializer):
    """ Allows only CSV files to be uploaded """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["file"].validators.append(FileExtensionValidator(allowed_extensions=['csv']))


class HandleUploadSerializer(serializers.Serializer):
    """ get uploaded file and call function to import data"""
    csv_file = FileField(style={"upload_url": reverse_lazy("csv_upload")})

    def create(self, validated_data):
        file = validated_data.pop('csv_file', None)
        import_teams(file['path'])
        import_games(file['path'])
        return self.instance


class TeamSerializer(serializers.ModelSerializer):
    """ serialize team objects"""

    class Meta:
        model = Team
        Fields = ('pk', 'name',)
        read_only_fields = ('pk',)


class GameSerializer(serializers.ModelSerializer):
    """serialize game objects"""
    team1 = TeamSerializer()
    team2 = TeamSerializer()

    class Meta:
        model = Game
        fields = (
            "pk",
            "team1",
            "team2",
            "team1_score",
            "team2_score"
        )

    def update(self, instance, validated_data):
        """ update game data, in case of new Team , it will be created then added to game"""
        # make sure to add only team.name in the front
        team1_name = validated_data.pop("team1", None)
        team2_name = validated_data.pop("team2", None)
        obj1, created = Team.objects.get_or_create(name=team1_name)
        obj2, created = Team.objects.get_or_create(name=team2_name)
        instance = super(GameSerializer, self).update(instance, validated_data)
        instance.team1 = obj1
        instance.team2 = obj2
        instance.save()
        return instance
