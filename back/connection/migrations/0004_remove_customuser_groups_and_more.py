# Generated by Django 4.1.13 on 2023-11-21 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0003_question_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]