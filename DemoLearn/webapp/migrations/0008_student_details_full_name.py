# Generated by Django 5.1.1 on 2024-10-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_student_details_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='full_name',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
    ]
