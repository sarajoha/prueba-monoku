# Generated by Django 2.0.13 on 2019-04-12 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190412_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_member',
            name='consumptions',
        ),
        migrations.RemoveField(
            model_name='team_member',
            name='products',
        ),
        migrations.AddField(
            model_name='consumption',
            name='team_member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Team_member'),
        ),
    ]
