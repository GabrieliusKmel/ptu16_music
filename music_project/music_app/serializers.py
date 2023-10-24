from rest_framework import serializers
from . import models


class BandSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = models.Band
        fields = ['id', 'name', 'username', 'user_id']


class AlbumSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = models.Album
        fields = ['id', 'name', 'band', 'username', 'user_id']


class SongSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = models.Song
        fields = ['id', 'name', 'duration', 'album', 'username', 'user_id']


class AlbumReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = models.AlbumReview
        fields = ['id', 'album', 'content', 'score', 'username', 'user_id']


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = models.AlbumReviewLike
        fields = ['id', 'albumreview', 'username', 'user_id']