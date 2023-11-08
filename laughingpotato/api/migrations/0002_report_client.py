# Generated by Django 4.2.1 on 2023-05-08 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="client",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.PROTECT, to="api.client"
            ),
            preserve_default=False,
        ),
    ]
