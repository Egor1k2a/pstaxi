from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'display_event_count', ]
    list_display_links = ['id', 'title', ]


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title', ]


class FullnessFilter(admin.SimpleListFilter):
    title = 'Заполненность'
    parameter_name = 'fullness_filter'

    def lookups(self, request, model_admin):
        return models.Event.FULLNESS_VARIANTS

    def queryset(self, request, queryset):
        filter_value = self.value()
        if filter_value:
            events_id = []
            if filter_value == models.Event.FULLNESS_FREE:
                for event in queryset:
                    if event.get_fullness_legend() == models.Event.FULLNESS_LEGEND_FREE:
                        events_id.append(event.id)
            elif filter_value == models.Event.FULLNESS_MIDDLE:
                for event in queryset:
                    if event.get_fullness_legend() == models.Event.FULLNESS_LEGEND_MIDDLE:
                        events_id.append(event.id)
            elif filter_value == models.Event.FULLNESS_FULL:
                for event in queryset:
                    if event.get_fullness_legend() == models.Event.FULLNESS_LEGEND_FULL:
                        events_id.append(event.id)
            return queryset.filter(id__in=events_id)
        return queryset


class ReviewInstanceInline(admin.TabularInline):
    model = models.Review
    extra = 0
    can_delete = False
    readonly_fields = [field.name for field in model._meta.fields]

    def has_add_permission(self, request, obj):
        return False


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'date_start', 'is_private',
                    'participants_number', 'display_enroll_count', 'display_places_left', ]
    list_display_links = ['id', 'title', ]
    list_select_related = ['category']
    list_filter = [FullnessFilter, 'category', 'features', ]
    ordering = ['date_start', ]
    filter_horizontal = ['features', ]
    readonly_fields = ['display_enroll_count', 'display_places_left', ]
    search_fields = ['title', ]
    inlines = [ReviewInstanceInline]


@admin.register(models.Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event', 'created', ]
    list_display_links = ['id', 'user', 'event', ]
    list_select_related = ['user', 'event', ]


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event', 'rate', 'created', 'updated', ]
    list_display_links = ['id', 'user', 'event', ]
    list_filter = ['created', 'event', ]
    list_select_related = ['user', 'event', ]
    fields = ['user', 'event', 'rate', 'text', ('created', 'updated'), 'id']
    readonly_fields = ['created', 'updated', 'id', ]
