# Generated by Django 5.1.6 on 2025-02-28 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=500, unique=True)),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
        ),
    ]
