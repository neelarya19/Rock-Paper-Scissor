# Generated by Django 4.0.1 on 2022-01-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Move', models.CharField(max_length=60)),
                ('Score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Move', models.CharField(choices=[('R', 'Rock'), ('P', 'Paper'), ('S', 'Scissor')], max_length=1)),
                ('Score', models.IntegerField()),
            ],
        ),
    ]
