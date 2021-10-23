# Generated by Django 3.2.5 on 2021-10-02 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saigym', '0008_register_birthplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('securityQue', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('answer', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SaveCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
                ('admission', models.DateTimeField(auto_now_add=True, null=True)),
                ('regno', models.IntegerField()),
                ('select', models.CharField(blank=True, max_length=20, null=True)),
                ('jan', models.CharField(blank=True, max_length=10, null=True)),
                ('feb', models.CharField(blank=True, max_length=10, null=True)),
                ('mar', models.CharField(blank=True, max_length=10, null=True)),
                ('apr', models.CharField(blank=True, max_length=10, null=True)),
                ('may', models.CharField(blank=True, max_length=10, null=True)),
                ('jun', models.CharField(blank=True, max_length=10, null=True)),
                ('july', models.CharField(blank=True, max_length=10, null=True)),
                ('aug', models.CharField(blank=True, max_length=10, null=True)),
                ('sept', models.CharField(blank=True, max_length=10, null=True)),
                ('octt', models.CharField(blank=True, max_length=10, null=True)),
                ('nov', models.CharField(blank=True, max_length=10, null=True)),
                ('dec', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
