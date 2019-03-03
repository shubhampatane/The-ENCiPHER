# Generated by Django 2.1.7 on 2019-03-03 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Co_Investigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Co_name', models.CharField(max_length=100)),
                ('Co_designation', models.CharField(max_length=100)),
                ('Co_contact_no', models.CharField(max_length=20)),
                ('Co_email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Principal_investigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Dept', models.CharField(max_length=100)),
                ('P_designation', models.CharField(max_length=100)),
            ],
        ),
    ]
