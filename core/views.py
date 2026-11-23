from django.shortcuts import render
from django.http import JsonResponse
from .models import Note, NoteLink
from .graph import get_graph_data



def graph_page(request):
    return render(request, "core/graph.html")


def home(request):
    return render(request, 'core/home.html')



def graph_data(request):

    nodes = [
        {
            "data": {
                "id": str(note.id),
                "label": note.title,
                "category": note.category
            }
        }
        for note in Note.objects.all()
    ]

    edges = [
        {
            "data": {
                "id": str(link.id),
                "source": str(link.source_id),
                "target": str(link.target_id),
                "label": link.relationship
            }
        }
        for link in NoteLink.objects.select_related(
            "source", "target"
        )
    ]

    return JsonResponse({
        "elements": nodes + edges
    })






def graph_page(request):
    return render(request, "core/graph.html")


def graph_api(request):
    data = get_graph_data()

    return JsonResponse(data)