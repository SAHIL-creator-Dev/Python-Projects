# Generated by Django 5.1.1 on 2025-02-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_news_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_management',
            name='news_discription',
            field=models.TextField(max_length=260),
        ),
    ]
