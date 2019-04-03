# Generated by Django 2.0.13 on 2019-04-03 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190403_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='name', max_length=200),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='consumption',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.Consumption'),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='product',
            field=models.ForeignKey(default='Cocosette', on_delete=django.db.models.deletion.CASCADE, to='polls.Product'),
        ),
    ]
