# Generated by Django 5.1.7 on 2025-03-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myopensoft', '0004_employee_employee_id_alter_leave_leave_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='awarded_date',
        ),
        migrations.AddField(
            model_name='award',
            name='reward_points',
            field=models.IntegerField(default=0),
        ),
    ]
