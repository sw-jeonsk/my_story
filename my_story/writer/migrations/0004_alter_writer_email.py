# Generated by Django 3.2.4 on 2021-08-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0003_alter_writer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='email',
            field=models.EmailField(error_messages={'required': 'email no exist'}, help_text='writer login ID', max_length=64, unique=True, verbose_name='이메일'),
        ),
    ]
