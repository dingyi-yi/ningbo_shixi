# Generated by Django 2.2.24 on 2021-08-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managesit', '0003_auto_20210806_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='building_info',
            name='house_kind',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='building_info',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]