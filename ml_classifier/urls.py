from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("project/<str:page>/", views.view_project, name="project"),
    path("predict/", views.predict, name="predict"),
    path("table/", views.view_table, name="table"),

    path("<path:all_paths>/", views.error_page, name="error_page"),
]