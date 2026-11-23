
import networkx as nx

from .models import Note, NoteLink


def build_graph():
    G = nx.Graph()

    # Add database records as nodes
    for note in Note.objects.all():
        G.add_node(
            str(note.id),
            label=note.title,
            category=note.category
        )

    # Add relationships as edges
    for link in NoteLink.objects.all():
        G.add_edge(
            str(link.source_id),
            str(link.target_id),
            relationship=link.relationship
        )

    return G


def get_graph_data():
    G = build_graph()

    nodes = [
        {
            "data": {
                "id": node,
                "label": attributes["label"],
                "category": attributes["category"]
            }
        }
        for node, attributes in G.nodes(data=True)
    ]

    edges = [
        {
            "data": {
                "id": f"{source}-{target}",
                "source": source,
                "target": target,
                "label": attributes["relationship"]
            }
        }
        for source, target, attributes in G.edges(data=True)
    ]

    return {
        "elements": nodes + edges
    }
