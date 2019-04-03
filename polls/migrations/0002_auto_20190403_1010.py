# Generated by Django 2.0.13 on 2019-04-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Producto',
            new_name='Product',
        ),
        migrations.RemoveField(
            model_name='team_member',
            name='consumo_productos',
        ),
        migrations.RemoveField(
            model_name='team_member',
            name='consumo_total',
        ),
        migrations.AddField(
            model_name='team_member',
            name='consumed_products',
            field=models.CharField(default=[], max_length=500),
        ),
        migrations.AddField(
            model_name='team_member',
            name='consumption',
            field=models.CharField(default=[], max_length=500),
        ),
    ]
