# Generated by Django 4.1.2 on 2022-10-12 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quiz_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="questions", old_name="ans", new_name="answer",
        ),
        migrations.RenameField(
            model_name="questions", old_name="op1", new_name="option_1",
        ),
        migrations.RenameField(
            model_name="questions", old_name="op2", new_name="option_2",
        ),
        migrations.RenameField(
            model_name="questions", old_name="op3", new_name="option_3",
        ),
        migrations.RenameField(
            model_name="questions", old_name="op4", new_name="option_4",
        ),
    ]