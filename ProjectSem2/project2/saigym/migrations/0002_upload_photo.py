# Generated by Django 3.2.5 on 2021-08-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saigym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='saigym/images')),
            ],
        ),
    ]
