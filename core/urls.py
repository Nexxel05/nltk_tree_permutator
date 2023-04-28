from django.urls import path

from core.views import paraphrases_view

urlpatterns = [
    path("paraphrase/", paraphrases_view, name="paraphrases")
]

app_name = "core"
