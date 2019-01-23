# Generated by Django 2.1.5 on 2019-01-23 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BallroomCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registration_link', models.URLField()),
                ('competition_website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='DanceStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('Latin', 'Latin'), ('Standard', 'Standard'), ('Rhythm', 'Rhythm'), ('Smooth', 'Smooth')], max_length=30)),
                ('level', models.IntegerField(choices=[(0, 'NEWCOMER'), (1, 'BRONZE'), (2, 'SILVER'), (3, 'GOLD'), (10, 'OPEN_NOVICE'), (11, 'OPEN_PRECHAMP'), (12, 'OPEN_CHAMP')])),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('street_address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('seriousness', models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=0)),
                ('o2cm_link', models.URLField(blank=True, null=True)),
                ('summary', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('time_commitment', models.IntegerField()),
                ('affiliated_institute', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='backend.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='images')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='backend.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.URLField(blank=True, null=True)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='videos')),
                ('description', models.TextField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='backend.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_competition', to='backend.BallroomCompetition')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_competition', to='backend.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='dancestyle',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dance_style', to='backend.Profile'),
        ),
        migrations.AddField(
            model_name='ballroomcompetition',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition', to='backend.Location'),
        ),
    ]
