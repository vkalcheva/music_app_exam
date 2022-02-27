from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from music_app.web.validators import validate_username


class Profile(models.Model):
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 15
    AGE_MIN_VALUE = 0
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_username,
        )
    )
    email = models.EmailField()
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )


class Album(models.Model):
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'RNB Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'

    GENRES = [(x, x) for x in (POP_MUSIC, JAZZ_MUSIC, RNB_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE, HIP_HOP_MUSIC, OTHER)]

    ALBUM_NAME_MAX_LEN = 30
    ARTIST_NAME_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    PRICE_MIN_VALUE = 0


    name = models.CharField(
        unique=True,
        max_length=ALBUM_NAME_MAX_LEN,
    )
    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LEN,
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=GENRES,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField()
    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )



