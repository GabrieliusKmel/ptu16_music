from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions, mixins, response, status
from rest_framework.validators import ValidationError
from . import models, serializers


User = get_user_model()


class UserCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

    def delete(self, *args, **kwargs):
        user = User.objects.filter(pk=self.request.user.pk)
        if user.exists():
            user.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('User does not exist')


class BandList(generics.ListCreateAPIView):
    queryset = models.Band.objects.all()
    serializer_class = serializers.BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Band.objects.all()
    serializer_class = serializers.BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, *args, **kwargs):
        band = models.Band.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if band.exists():
            return self.destroy(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only delete your own bands.'))
        
    def put(self, *args, **kwargs):
        band = models.Band.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if band.exists():
            return self.update(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only update your own bands.'))


class AlbumList(generics.ListCreateAPIView):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, *args, **kwargs):
        album = models.Album.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if album.exists():
            return self.destroy(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only delete your own albums.'))
        
    def put(self, *args, **kwargs):
        album = models.Album.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if album.exists():
            return self.update(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only update your own albums.'))
        

class SongList(generics.ListCreateAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, *args, **kwargs):
        song = models.Song.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if song.exists():
            return self.destroy(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only delete your own songs.'))
        
    def put(self, *args, **kwargs):
        song = models.Album.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if song.exists():
            return self.update(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only update your own songs.'))


class AlbumReviewList(generics.ListCreateAPIView):
    queryset = models.AlbumReview.objects.all()
    serializer_class = serializers.AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AlbumReview.objects.all()
    serializer_class = serializers.AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, *args, **kwargs):
        albumreview = models.AlbumReview.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if albumreview.exists():
            return self.destroy(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only delete your own reviews.'))
        
    def put(self, *args, **kwargs):
        albumreview = models.AlbumReview.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if albumreview.exists():
            return self.update(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only update your own reviews.'))
        
        
class AlbumReviewLike(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = serializers.AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        albumreview = models.AlbumReview.objects.get(pk=self.kwargs['pk'])
        return models.AlbumReviewLike.objects.filter(albumreview=albumreview, user=user)
    
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError("You can like this album only once.")
        user = self.request.user
        albumreview = models.AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(albumreview=albumreview, user=user)

    def delete(self, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("You can only unlike this album after you like it.")