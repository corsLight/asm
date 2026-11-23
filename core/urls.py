from django.urls import path
from . import views

urlpatterns = [

    path(
        "graph/",
        views.graph_page,
        name="graph"
    ),

    path(
        "graph-data/",
        views.graph_api,
        name="graph_api"
    ),

    
]


from django.urls import path
from . import views

urlpatterns = [


]