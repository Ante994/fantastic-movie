# Generated by Django 2.0.4 on 2018-04-29 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=2)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('profile_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=2)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('profile_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.CharField(max_length=30)),
                ('poster_path', models.TextField()),
                ('release_date', models.DateField()),
                ('budget', models.IntegerField()),
                ('renevue', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('vote_average', models.DecimalField(decimal_places=2, max_digits=4)),
                ('vote_count', models.IntegerField()),
                ('actors', models.ManyToManyField(to='App1.Actor')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App1.Director')),
                ('genres', models.ManyToManyField(to='App1.Genre')),
            ],
        ),
    ]
