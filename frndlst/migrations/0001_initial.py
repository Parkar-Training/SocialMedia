# Generated by Django 3.2 on 2021-10-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='frnd_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FrndId', models.CharField(max_length=3)),
                ('FuserId', models.CharField(max_length=3)),
                ('Stat', models.CharField(max_length=3)),
            ],
        ),
    ]