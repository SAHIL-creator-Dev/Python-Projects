# Generated by Django 5.1.1 on 2024-10-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_rename_sexth_sem_marks_student_details_sixth_sem_marks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_details',
            old_name='sel_board',
            new_name='sel_high_board',
        ),
        migrations.AddField(
            model_name='student_details',
            name='inter_per',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='student_details',
            name='parent_phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_details',
            name='sel_inter_board',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
