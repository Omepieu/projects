from django.contrib import admin
from polls.models import *

# Register your models here.
#StackedInline
class ChoixInline(admin.TabularInline):
    model = Choix
    extra = 2
    fieldsets =[
        ("Ajouter une sous question au choix", {"fields":["choix_text"]}),
        ("Votes", {"fields":["votes"]})

    ]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "fut_publier_recent"]
    # fieldsets =[
    #     ("Question de sondage", {"fields":["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"], "classes":['collapse']})
    # ]
    inlines = [ChoixInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choix)