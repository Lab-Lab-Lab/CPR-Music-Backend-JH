from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import (
    ActivityCategory,
    ActivityType,
    Activity,
    Assignment,
    Curriculum,
    CurriculumEntry,
    PiecePlan,
    PlannedActivity,
    AssignmentGroup,
)


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(VersionAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(ActivityType)
class ActivityTypeAdmin(VersionAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Activity)
class ActivityAdmin(VersionAdmin):
    list_display = ("id", "activity_type", "part_type")
    list_filter = ("activity_type", "part_type")


@admin.register(Assignment)
class AssignmentAdmin(VersionAdmin):
    list_display = (
        "id",
        "activity",
        "enrollment",
        "part",
        # "deadline",
        # "instrument",
        # "created_at",
    )
    list_filter = (
        "activity",
        "piece",
        # "deadline",
        # "instrument",
        # "created_at",
    )
    search_fields = ("activity__activity_type__name", "enrollment__user__username")
    date_hierarchy = "created_at"
    save_as = True


class PiecePlanActivityInline(admin.TabularInline):
    model = PlannedActivity
    extra = 0
    ordering = ("order",)


@admin.register(PiecePlan)
class PiecePlanAdmin(VersionAdmin):
    list_display = (
        "id",
        "name",
        "piece",
        "type",
    )
    list_filter = (
        ("piece", admin.RelatedOnlyFieldListFilter),
        "type",
    )
    inlines = (PiecePlanActivityInline,)
    raw_id_fields = ("activities",)
    save_as = True


class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 0
    ordering = ("-id",)


@admin.register(AssignmentGroup)
class AssignmentGroupAdmin(VersionAdmin):
















    list_display = (
        "id",
        "type",
    )
    list_filter = ("type",)
    inlines = (AssignmentInline,)


# @admin.register(PlannedActivity)
# class PlannedActivityAdmin(VersionAdmin):
#     list_display = (
#         "id",
#         "piece_plan",
#         "activity",
#         "order",
#     )
#     list_filter = (
#         "piece_plan",
#         "activity",
#     )


class CurriculumEntryInline(admin.TabularInline):
    model = CurriculumEntry
    extra = 0
    ordering = ("order",)


@admin.register(Curriculum)
class CurriculumAdmin(VersionAdmin):
    list_display = (
        "id",
        "name",
        "course",
        "ordered",
    )
    list_filter = (
        "course",
        "ordered",
    )
    inlines = (CurriculumEntryInline,)
    raw_id_fields = ("piece_plans",)
    save_as = True
