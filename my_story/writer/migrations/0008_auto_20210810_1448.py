# Generated by Django 3.2.4 on 2021-08-10 05:48

from django.db import migrations, models
import writer.validators


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0007_alter_writer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='name',
            field=models.CharField(help_text='user name (firstname + second_name)', max_length=30, validators=[writer.validators.validate_name], verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='password',
            field=models.CharField(max_length=128, validators=[writer.validators.validate_password], verbose_name='비밀번호'),
        ),
    ]
