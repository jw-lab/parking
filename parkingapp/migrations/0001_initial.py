# Generated by Django 2.2.2 on 2021-05-10 23:16

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
                ('model', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('company', models.CharField(max_length=50, null=True)),
                ('color', models.CharField(blank=True, choices=[('white', 'white'), ('black', 'black'), ('gray', 'gray'), ('silver', 'silver'), ('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('gold', 'gold'), ('brown', 'brown'), ('orange', 'orange')], default='', max_length=6)),
                ('plate', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=13, null=True)),
                ('lot', models.CharField(max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
