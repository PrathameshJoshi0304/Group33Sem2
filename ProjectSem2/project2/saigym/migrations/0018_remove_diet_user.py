# Generated by Django 3.2.5 on 2021-10-03 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saigym', '0017_diet_select'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='user',
        ),
    ]
