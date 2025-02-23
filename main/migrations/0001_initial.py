# Generated by Django 5.1.5 on 2025-01-20 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100, null=True)),
                ('url', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['last_name', 'name'],
                'indexes': [models.Index(fields=['last_name', 'name'], name='main_author_last_na_cdc2b6_idx')],
            },
        ),
        migrations.CreateModel(
            name='Authorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_num', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_change', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
        ),
    ]
