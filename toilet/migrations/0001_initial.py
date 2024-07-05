# Generated by Django 4.0.1 on 2022-02-08 07:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToiletInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=200)),
                ('tlocation', models.CharField(max_length=300)),
                ('tlat', models.FloatField()),
                ('tlong', models.FloatField()),
                ('tnumber', models.CharField(max_length=200, null=True)),
                ('topen', models.CharField(max_length=200, null=True)),
                ('tbidget', models.BooleanField(null=True)),
                ('tpaper', models.BooleanField(null=True)),
                ('tpassword', models.BooleanField(null=True)),
                ('tpublic', models.BooleanField(null=True)),
                ('ttype', models.IntegerField(blank=True, choices=[(0, '좌변기'), (1, '양변기')], default=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('toilet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toilet.toiletinfo')),
            ],
        ),
    ]
