# Generated by Django 3.2.4 on 2021-08-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0005_alter_writer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='password',
            field=models.CharField(max_length=128, verbose_name='비밀번호'),
        ),
    ]