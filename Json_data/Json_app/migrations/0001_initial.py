# Generated by Django 3.0 on 2020-06-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timeslat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('time', models.ManyToManyField(to='Json_app.Timeslat')),
            ],
        ),
    ]