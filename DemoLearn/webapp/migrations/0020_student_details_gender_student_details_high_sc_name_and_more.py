# Generated by Django 5.1.1 on 2024-10-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_alter_student_details_fifth_sem_marks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student_details',
            name='high_sc_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student_details',
            name='high_sc_pass_year',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='student_details',
            name='inter_col_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student_details',
            name='inter_col_pass_year',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
