# Generated by Django 4.1.5 on 2023-01-20 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insurance_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='users',
            name='package',
            field=models.ForeignKey(default='7', on_delete=django.db.models.deletion.CASCADE, to='insurance_app.packages'),
        ),
    ]
