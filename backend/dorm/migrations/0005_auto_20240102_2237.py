# Generated by Django 3.2.16 on 2024-01-02 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0004_dormitory_interiorimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomexchange',
            name='dormitory',
        ),
        migrations.RemoveField(
            model_name='roomexchange',
            name='fromTeam',
        ),
        migrations.RemoveField(
            model_name='roomexchange',
            name='toTeam',
        ),
        migrations.DeleteModel(
            name='MemberExchange',
        ),
        migrations.DeleteModel(
            name='RoomExchange',
        ),
    ]
