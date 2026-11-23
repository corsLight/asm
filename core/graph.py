
import networkx as nx

from .models import Note, NoteLink


def build_graph():
    graph = nx.DiGraph()

    # Every note becomes a node.
    for note in Note.objects.all():
        graph.add_node(
            str(note.id),
            label=note.title,
            category=note.category,
        )

    # Every NoteLink becomes a directed connection.
    for link in NoteLink.objects.select_related("source", "target"):
        graph.add_edge(
            str(link.source_id),
            str(link.target_id),
            relationship=link.relationship,
        )

    return graph


def get_graph_data():
    graph = build_graph()

    nodes = [
        {
            "data": {
                "id": node_id,
                "label": attributes["label"],
                "category": attributes["category"],
            }
        }
        for node_id, attributes in graph.nodes(data=True)
    ]

    edges = [
        {
            "data": {
                "id": f"{source}-{target}",
                "source": source,
                "target": target,
                "label": attributes["relationship"],
            }
        }
        for source, target, attributes in graph.edges(data=True)
    ]

    return {"elements": nodes + edges}
