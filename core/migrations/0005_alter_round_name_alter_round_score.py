# Generated by Django 4.0.1 on 2022-01-07 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_round_move_alter_round_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='Name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.player'),
        ),
        migrations.AlterField(
            model_name='round',
            name='Score',
            field=models.IntegerField(default=0),
        ),
    ]
