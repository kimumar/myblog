# Generated by Django 3.2.8 on 2021-11-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0005_delete_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]