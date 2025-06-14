# Generated by Django 5.1.1 on 2024-10-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_rename_sel_board_student_details_sel_high_board_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_details',
            name='address',
        ),
        migrations.AddField(
            model_name='student_details',
            name='current_address',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student_details',
            name='passing_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_details',
            name='permanent_address',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
