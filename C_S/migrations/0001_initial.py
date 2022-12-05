# Generated by Django 4.1 on 2022-11-29 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('capital', models.CharField(max_length=20)),
                ('ISDCode', models.IntegerField(unique=True)),
                ('Timezone', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('capital', models.CharField(max_length=20)),
                ('population', models.FloatField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='C_S.country')),
            ],
        ),
    ]
