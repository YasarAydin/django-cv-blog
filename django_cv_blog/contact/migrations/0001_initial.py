# Generated by Django 4.2.7 on 2023-11-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_firstname', models.CharField(max_length=50)),
                ('your_lastname', models.CharField(max_length=50)),
                ('your_email', models.EmailField(max_length=254)),
                ('your_message', models.TextField()),
            ],
        ),
    ]
