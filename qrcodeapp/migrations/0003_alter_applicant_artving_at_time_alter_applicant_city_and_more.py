# Generated by Django 4.2.7 on 2023-11-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodeapp', '0002_accepted_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='artving_at_time',
            field=models.CharField(choices=[('I Can', 'I Can'), ('I Try', 'I Try')], default='I Can', max_length=30),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='city',
            field=models.CharField(default='Baghdad', max_length=100),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='university',
            field=models.CharField(default='Baghded University', max_length=100),
        ),
    ]
