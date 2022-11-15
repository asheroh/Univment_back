# Generated by Django 4.0.4 on 2022-11-15 18:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20, null=True)),
                ('isDefault', models.BooleanField(default=False)),
                ('question1', models.TextField(max_length=500)),
                ('question2', models.TextField(max_length=500)),
                ('question3', models.TextField(max_length=500)),
                ('question4', models.TextField(max_length=500)),
                ('generated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'generated_user')},
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('event_date', models.DateField(default=datetime.date.today)),
                ('timeline', models.BooleanField(default=False)),
                ('answer1', models.TextField(max_length=500)),
                ('answer2', models.TextField(max_length=500)),
                ('answer3', models.TextField(max_length=500)),
                ('answer4', models.TextField(max_length=500)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
