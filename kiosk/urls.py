from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sector/<int:sector_id>', views.projects, name='sector'),
    # ex: /polls/5/results/
    path('project/<int:project_id>', views.artifacts, name='project'),
    # ex: /polls/5/vote/
    path('artifact/<int:artifact_id>', views.artifact, name='artifact'),
]