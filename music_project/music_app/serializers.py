from django.contrib.auth import get_user_model
from rest_framework import serializers
from . import models


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username', 'password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


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
        fields = ['id', 'name', 'band', 'image', 'username', 'user_id']


class SongSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = models.Song
        fields = ['id', 'name', 'duration', 'album', 'username', 'user_id']


class AlbumReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = models.AlbumReview
        fields = ['id', 'album', 'content', 'score', 'likes_count', 'username', 'user_id']

    def get_likes_count(self, obj):
        return models.AlbumReviewLike.objects.filter(albumreview=obj).count()

class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlbumReviewLike
        fields = ['id']