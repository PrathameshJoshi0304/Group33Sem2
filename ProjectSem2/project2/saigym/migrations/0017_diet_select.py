# Generated by Django 3.2.5 on 2021-10-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saigym', '0016_auto_20211002_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='select',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]