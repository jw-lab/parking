# Generated by Django 2.2.2 on 2021-05-17 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('plate', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=13)),
                ('lot', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
