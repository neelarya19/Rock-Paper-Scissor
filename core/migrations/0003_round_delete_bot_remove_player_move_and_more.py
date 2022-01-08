# Generated by Django 4.0.1 on 2022-01-06 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_bot_move'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Move', models.CharField(choices=[('R', 'Rock'), ('P', 'Paper'), ('S', 'Scissor')], max_length=1)),
                ('Score', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bot',
        ),
        migrations.RemoveField(
            model_name='player',
            name='Move',
        ),
        migrations.RemoveField(
            model_name='player',
            name='Score',
        ),
        migrations.AddField(
            model_name='round',
            name='Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.player'),
        ),
    ]