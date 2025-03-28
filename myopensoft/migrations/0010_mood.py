# Generated by Django 5.1.7 on 2025-03-23 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myopensoft', '0009_review_performance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vibe_score', models.IntegerField()),
                ('emotion_zone', models.CharField(choices=[('Sad Zone', 'Sad Zone'), ('Leaning to happy zone', 'Leaning to happy zone'), ('Neutral Zone(OK)', 'Neutral Zone(OK)'), ('Excited Zone', 'Excited Zone'), ('Frustrated Zone', 'Fruustrated Zone')], max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mood', to='myopensoft.employee')),
            ],
        ),
    ]
