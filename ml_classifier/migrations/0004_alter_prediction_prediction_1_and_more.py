# Generated by Django 4.2.8 on 2023-12-10 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ml_classifier", "0003_rename_slides_slide"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prediction",
            name="prediction_1",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="prediction_2",
            field=models.CharField(max_length=100),
        ),
    ]