from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions
from rest_framework.validators import ValidationError
from . import models, serializers


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
        

class AlbumReviewLikeList(generics.ListCreateAPIView):
    queryset = models.AlbumReviewLike.objects.all()
    serializer_class = serializers.AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AlbumReviewLike.objects.all()
    serializer_class = serializers.AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, *args, **kwargs):
        albumreviewlike = models.AlbumReviewLike.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if albumreviewlike.exists():
            return self.destroy(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only delete your own likes.'))
        
    def put(self, *args, **kwargs):
        albumreviewlike = models.AlbumReviewLike.objects.filter(pk=kwargs['pk'],
        user = self.request.user,)
        if albumreviewlike.exists():
            return self.update(self.request, *args, **kwargs)
        else:
            raise ValidationError(_('Can only update your own likes.'))