from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Band(models.Model):
    name = models.CharField(_("band"), max_length=50)
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Album(models.Model):
    name = models.CharField(_("album"), max_length=50)
    band = models.ForeignKey(Band, verbose_name=_("band"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} by {self.band}"
    

class Song(models.Model):
    name = models.CharField(_("song"), max_length=50)
    duration = models.DurationField(_("duration"))
    album = models.ForeignKey(Album, verbose_name=_("album"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} in {self.album}"


class AlbumReview(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    album = models.ForeignKey(Album, verbose_name=_("album"), on_delete=models.CASCADE)
    content = models.TextField(_("content"), max_length=500)
    score = models.CharField(_("score"), max_length=5)


    def __str__(self) -> str:
        return f"Review for {self.album} by {self.user}"


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    albumreview = models.ForeignKey(AlbumReview, verbose_name=_("albumreview"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()