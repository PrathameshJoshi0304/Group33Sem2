# Generated by Django 3.2.5 on 2021-08-31 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saigym', '0003_alter_upload_photo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50)),
            ],
        ),
    ]
