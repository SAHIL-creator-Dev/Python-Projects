# Generated by Django 5.1.1 on 2024-10-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_alter_student_details_fifth_sem_marks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='fifth_sem_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='first_sem_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='first_year_tot_cgpa',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='first_year_tot_per',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='forth_sem_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='inter_per',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='passing_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='second_sem_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='second_year_tot_cgpa',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='second_year_tot_per',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='sel_high_board',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='sel_inter_board',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='sixth_sem_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='third_sem_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='third_year_tot_cgpa',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='third_year_tot_per',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
