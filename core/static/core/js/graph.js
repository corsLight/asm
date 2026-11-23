
async function loadGraph() {
    const response = await fetch("/graph-data/");

    if (!response.ok) {
        throw new Error("Could not load graph data");
    }

    const graphData = await response.json();

    const cy = cytoscape({
        container: document.getElementById("network"),
        elements: graphData.elements,

        style: [
            {
                selector: "node",
                style: {
                    "label": "data(label)",
                    "background-color": "#3977db",
                    "color": "#ffffff",
                    "text-valign": "center",
                    "text-halign": "center",
                    "width": 50,
                    "height": 50,
                    "font-size": 11
                }
            },
            {
                selector: "edge",
                style: {
                    "label": "data(label)",
                    "line-color": "#888888",
                    "target-arrow-shape": "triangle",
                    "target-arrow-color": "#888888",
                    "curve-style": "bezier",
                    "width": 2,
                    "font-size": 9
                }
            }
        ],

        layout: {
            name: "cose",
            animate: true,
            nodeRepulsion: 4500
        }
    });

    cy.on("tap", "node", function(event) {
        const node = event.target;
        console.log("Selected:", node.data("label"));
    });
}

loadGraph().catch(console.error);
