# Generated by Django 3.2.5 on 2021-10-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saigym', '0019_auto_20211006_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True),
        ),
    ]