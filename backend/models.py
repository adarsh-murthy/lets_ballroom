"""Define the database schema for the backend service."""
from django.db import models

from django.conf import settings


class Location(models.Model):
    """Describes the location of a user."""
    zip_code = models.IntegerField()
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=255, blank=True, null=True)


class BallroomCompetition(models.Model):
    """List of competitions in our database."""
    name = models.CharField(max_length=255)
    location = models.ForeignKey(
        Location,
        related_name='competition',
        on_delete=models.CASCADE,
    )
    registration_link = models.URLField()
    competition_website = models.URLField()


class Profile(models.Model):
    """Defines a user profile."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user',
        on_delete=models.CASCADE,
    )
    dob = models.DateTimeField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    SERIOUSNESS_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    seriousness = models.IntegerField(
        choices=SERIOUSNESS_CHOICES,
        default=LOW,
    )
    o2cm_link = models.URLField(blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    time_commitment = models.IntegerField()
    affiliated_institute = models.CharField(max_length=255,
                                            blank=True,
                                            null=True)
    location = models.ForeignKey(
        Location,
        related_name='profile',
        on_delete=models.CASCADE,
    )


class DanceStyle(models.Model):
    """Describes dance style with level."""
    profile = models.ForeignKey(
        Profile,
        related_name='dance_style',
        on_delete=models.CASCADE,
    )
    LATIN = 'Latin'
    STANDARD = 'Standard'
    RHYTHM = 'Rhythm'
    SMOOTH = 'Smooth'
    STYLE_CHOICES = (
        (LATIN, 'Latin'),
        (STANDARD, 'Standard'),
        (RHYTHM, 'Rhythm'),
        (SMOOTH, 'Smooth'),
    )
    style = models.CharField(max_length=30, choices=STYLE_CHOICES)
    NEWCOMER = 0
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    OPEN_NOVICE = 10
    OPEN_PRECHAMP = 11
    OPEN_CHAMP = 12
    LEVEL_CHOICES = (
        (NEWCOMER, 'NEWCOMER'),
        (BRONZE, 'BRONZE'),
        (SILVER, 'SILVER'),
        (GOLD, 'GOLD'),
        (OPEN_NOVICE, 'OPEN_NOVICE'),
        (OPEN_PRECHAMP, 'OPEN_PRECHAMP'),
        (OPEN_CHAMP, 'OPEN_CHAMP'),
    )
    level = models.IntegerField(choices=LEVEL_CHOICES)


class ProfilePicture(models.Model):
    """A specific picture for a profile."""
    picture = models.FileField(upload_to='images')
    profile = models.ForeignKey(
        Profile,
        related_name='pictures',
        on_delete=models.CASCADE,
    )


class ProfileVideo(models.Model):
    """Uploaded video of a user."""
    profile = models.ForeignKey(
        Profile,
        related_name='video',
        on_delete=models.CASCADE,
    )
    video_link = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos', blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class UserCompetition(models.Model):
    """Competition that a user has marked as going."""
    profile = models.ForeignKey(
        Profile,
        related_name='user_competition',
        on_delete=models.CASCADE,
    )
    competition = models.ForeignKey(
        BallroomCompetition,
        related_name='user_competition',
        on_delete=models.CASCADE,
    )
