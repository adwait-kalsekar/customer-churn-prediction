from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("project/", views.view_project, name="project"),
    path("eda/", views.view_eda, name="eda"),
    path("results/", views.view_results, name="results"),
    path("eval/", views.view_eval, name="eval"),
    path("predict/", views.predict, name="predict"),
    path("table/", views.view_table, name="table"),
    path("data_dictionary/", views.view_data_dictionary, name="data_dictionary"),
    path("team/", views.view_team, name="team")
]