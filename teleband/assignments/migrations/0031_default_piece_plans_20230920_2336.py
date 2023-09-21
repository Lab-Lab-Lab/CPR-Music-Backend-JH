# Generated by Django 3.2.11 on 2023-09-21 03:36

from django.db import migrations


piece_names = [
    "Air for Band",
    "Celebration for a New Day",
    "America the Beautiful",
    "The Favorite",
    "Freedom 2040 (Band)",
    "Freedom 2040 (Orchestra)",
    "Down by the Riverside",
    "Deep River",
    "I Want to be Ready",
    "Beginning Band - When the Saints Go Marching In",
    "Beginning Band - Ode to Joy",
    "Beginning Band - London Bridge",
    "Beginning Band - Jolly Old St. Nick",
    "Beginning Band - Jingle Bells",
    "Beginning Band - Hot Cross Buns",
    "Beginning Band - Good King Wenceslas",
    "Beginning Band - Go Tell Aunt Rhody",
    "Beginning Band - Aura Lee",
    "Beginning Band - Amazing Grace",
    "Beginning Orchestra - Bile em Cabbage Down",
    "Beginning Orchestra - Go Tell Aunt Rhody",
    "Beginning Orchestra - Good King Wenceslas",
    "Beginning Orchestra - Hot Cross Buns",
]

connect_map = {
    "The Favorite": {
        "activity_type_name": "Connect Benjamin",
        "category": "Connect Benjamin",
    },
    "Freedom 2040 (Band)": {
        "activity_type_name": "Connect Green",
        "category": "Connect Green",
    },
    "Freedom 2040 (Orchestra)": {
        "activity_type_name": "Connect Green",
        "category": "Connect Green",
    },
    "Down by the Riverside": {
        "activity_type_name": "Connect Danyew",
        "category": "Connect Danyew",
    },
    "Deep River": {
        "activity_type_name": "Connect Danyew",
        "category": "Connect Danyew",
    },
    "I Want to be Ready": {
        "activity_type_name": "Connect Danyew",
        "category": "Connect Danyew",
    },
    "Beginning Band - When the Saints Go Marching In": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Band - Ode to Joy": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Band - London Bridge": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Band - Jolly Old St. Nick": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Band - Jingle Bells": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Band - Hot Cross Buns": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Band - Good King Wenceslas": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Band - Go Tell Aunt Rhody": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Band - Aura Lee": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Band - Amazing Grace": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Orchestra - Bile em Cabbage Down": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Orchestra - Go Tell Aunt Rhody": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Orchestra - Good King Wenceslas": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
    "Beginning Orchestra - Hot Cross Buns": {
        "activity_type_name": "Beginner Connect",
        "category": "Connect",
    },
}

og_act = [
    {"activity_type_name": "Melody", "category": "Perform"},
    {"activity_type_name": "Bassline", "category": "Perform"},
    {"activity_type_name": "Creativity", "category": "Create"},
    {"activity_type_name": "Reflection", "category": "Respond"},
]


def update_site_forward(apps, schema_editor):
    Activity = apps.get_model("assignments", "Activity")
    ActivityType = apps.get_model("assignments", "ActivityType")
    ActivityCategory = apps.get_model("assignments", "ActivityCategory")
    PartType = apps.get_model("musics", "PartType")
    combined_part = PartType.objects.get(name="Combined")
    act_cat, act_cat_created = ActivityCategory.objects.get_or_create(name="Connect")
    act_typ, act_typ_created = ActivityType.objects.get_or_create(
        name="Beginner Connect", category=act_cat
    )
    connect_act, connect_act_created = Activity.objects.get_or_create(
        activity_type_id=act_typ.pk,
        part_type_id=combined_part.pk,
        activity_type_name=act_typ.name,
        category=act_cat.name,
        body="Now that you have learned this tune, write about what you have learned about playing your instrument.",
    )
    
    Piece = apps.get_model("musics", "Piece")
    PiecePlan = apps.get_model("assignments", "PiecePlan")
    PlannedActivity = apps.get_model("assignments", "PlannedActivity")
    Curriculum = apps.get_model("assignments", "Curriculum")
    CurriculumEntry = apps.get_model("assignments", "CurriculumEntry")
    Course = apps.get_model("courses", "Course")
    course = Course.objects.get(slug="6th-grade-band")

    curriculum = Curriculum.objects.create(name="ALL Curriculum", course=course)

    for piece_num, piece_name in enumerate(piece_names):
        piece = Piece.objects.get(name=piece_name)
        plan = PiecePlan.objects.create(name=f"ALL-{piece_name}", piece=piece)
        curriculum_entry = CurriculumEntry.objects.create(
            curriculum=curriculum, piece_plan=plan, order=piece_num + 1
        )
        acts = og_act.copy()
        if piece_name in connect_map:
            acts.append(connect_map[piece_name])
        for i, act in enumerate(acts):
            # activity_type = ActivityType.objects.get(name=act["activity_type_name"])
            # activity_category = ActivityCategory.objects.get(name=act["category"])
            # print(act["activity_type_name"], act["category"])
            activity = Activity.objects.get(
                activity_type_name=act["activity_type_name"], category=act["category"]
            )
            PlannedActivity.objects.create(
                piece_plan=plan, activity=activity, order=i + 1
            )


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0030_alter_assignmentgroup_type"),
    ]

    operations = [migrations.RunPython(update_site_forward, migrations.RunPython.noop)]
