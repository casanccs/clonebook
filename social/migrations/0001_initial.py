# Generated by Django 4.1.5 on 2023-04-23 17:44

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppic', models.ImageField(upload_to='')),
                ('dob', models.DateField()),
                ('gender', models.TextField()),
                ('nfollowers', models.IntegerField(default=0)),
                ('nfollowing', models.IntegerField(default=0)),
                ('bio', models.CharField(max_length=1000)),
                ('city', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
