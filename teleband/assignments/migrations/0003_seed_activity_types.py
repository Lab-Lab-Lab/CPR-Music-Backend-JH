# Generated by Django 3.2.11 on 2022-01-08 02:36

from django.db import migrations


def update_site_forward(apps, schema_editor):
    """Set site domain and name."""
    ActivityCategory = apps.get_model("assignments", "ActivityCategory")
    ActivityType = apps.get_model("assignments", "ActivityType")

    db = {elem.name: elem for elem in ActivityCategory.objects.all()}

    for name, category in [
        ("Melody", "Perform"),
        ("Bassline", "Perform"),
        ("Creativity", "Create"),
        ("Reflection", "Respond"),
    ]:
        ActivityType.objects.update_or_create(name=name, category=db[category])


class Migration(migrations.Migration):

    dependencies = [
        ("assignments", "0002_seed_activity_categories"),
    ]

    operations = [migrations.RunPython(update_site_forward, migrations.RunPython.noop)]
