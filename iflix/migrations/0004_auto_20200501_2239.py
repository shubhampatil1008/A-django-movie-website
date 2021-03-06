# Generated by Django 3.0.5 on 2020-05-01 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iflix', '0003_user_account_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_account',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user_account',
            name='username',
        ),
        migrations.AddField(
            model_name='user_account',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_account',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
