# Generated by Django 3.2.5 on 2021-10-07 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saigym', '0022_alter_card_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='display', to=settings.AUTH_USER_MODEL),
        ),
    ]
