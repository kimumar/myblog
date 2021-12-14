# Generated by Django 3.2.8 on 2021-10-26 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('email', models.EmailField(blank=True, max_length=80, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, max_length=2000, null=True)),
                ('status', models.CharField(blank=True, choices=[('New', 'New'), ('Read', 'Read')], max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='alpha.post')),
            ],
        ),
    ]
