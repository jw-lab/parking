# Generated by Django 2.2.2 on 2021-04-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('plate', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('lot', models.CharField(max_length=50)),
            ],
        ),
    ]
