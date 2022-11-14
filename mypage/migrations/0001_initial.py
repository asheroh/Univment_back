# Generated by Django 4.1.2 on 2022-11-13 07:51

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
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project1', models.CharField(blank=True, max_length=23, null=True)),
                ('project2', models.CharField(blank=True, max_length=23, null=True)),
                ('project3', models.CharField(blank=True, max_length=23, null=True)),
                ('project4', models.CharField(blank=True, max_length=23, null=True)),
                ('project5', models.CharField(blank=True, max_length=23, null=True)),
                ('user', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profileimage', models.ImageField(upload_to='profileimages/')),
                ('user', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('myname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('major', models.CharField(blank=True, max_length=20)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contests',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contest1', models.CharField(blank=True, max_length=23, null=True)),
                ('contest2', models.CharField(blank=True, max_length=23, null=True)),
                ('contest3', models.CharField(blank=True, max_length=23, null=True)),
                ('contest4', models.CharField(blank=True, max_length=23, null=True)),
                ('contest5', models.CharField(blank=True, max_length=23, null=True)),
                ('user', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phonenumber', models.CharField(max_length=13, unique=True)),
                ('insta', models.CharField(blank=True, max_length=20)),
                ('github', models.CharField(blank=True, max_length=30, null=True)),
                ('blog', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('club1', models.CharField(blank=True, max_length=23, null=True)),
                ('club2', models.CharField(blank=True, max_length=23, null=True)),
                ('club3', models.CharField(blank=True, max_length=23, null=True)),
                ('club4', models.CharField(blank=True, max_length=23, null=True)),
                ('club5', models.CharField(blank=True, max_length=23, null=True)),
                ('user', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activity1', models.CharField(blank=True, max_length=23, null=True)),
                ('activity2', models.CharField(blank=True, max_length=23, null=True)),
                ('activity3', models.CharField(blank=True, max_length=23, null=True)),
                ('activity4', models.CharField(blank=True, max_length=23, null=True)),
                ('activity5', models.CharField(blank=True, max_length=23, null=True)),
                ('user', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
