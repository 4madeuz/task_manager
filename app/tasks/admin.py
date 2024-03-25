from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'status',
        'get_users',
    )
    search_fields = ('title',)
    list_filter = ('status',)
    list_prefetch_related = ('users',)

    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .prefetch_related(*self.list_prefetch_related)
        )
        return queryset

    def get_users(self, obj):
        return ','.join([user.username for user in obj.users.all()])

    get_users.short_description = 'Users'


admin.site.register(Task, TaskAdmin)
