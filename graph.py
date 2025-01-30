import matplotlib
matplotlib.use('Agg')  

import matplotlib.pyplot as plt
import networkx as nx
import io

class TrainNetwork:
    def __init__(self):
        self.graph = nx.Graph()
        self.lines = {
            "MRT Line 3": [
                "Taft Avenue", "Magallanes", "Ayala Avenue", "Buendia",
                "Guadalupe", "Boni Avenue", "Shaw Boulevard", "Ortigas",
                "Santolan-Annapolis", "Araneta Center Cubao (MRT 3)", 
                "GMA Kamuning", "Quezon Avenue", "North Avenue"
            ],
            "LRT Line 1": [
                "Fernando Poe Jr.", "Balintawak", "Monumento", "5th Avenue", "R. Papa",
                "Abad Santos", "Blumentritt", "Bambang", "Tayuman", "Doroteo Jose",
                "Carriedo", "Central Station", "United Nations", "Pedro Gil",
                "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", "EDSA", 
                "Baclaran", "Redemptorist", "Aseana", "Manila International Airport", "AsiaWorld", 
                "Ninoy Aquino", "Dr. Santos"
            ],
            "LRT Line 2": [
                "Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", 
                "Gilmore", "Betty Go-Belmonte", "Araneta Center Cubao (LRT 2)", 
                "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo"
            ]
        }
        self.station_positions = self._define_positions()
        self._build_graph()

    def _define_positions(self):
        return {
            "Taft Avenue": (-12.8, -51), "Magallanes": (-8.44, -50.85), "Ayala Avenue": (-3.3, -49.27), 
            "Buendia": (0.22, -45.13), "Guadalupe": (3.77, -37.3), "Boni Avenue": (6.32, -26.7), 
            "Shaw Boulevard": (7.47, -15.33), "Ortigas": (7.62, -10.36), "Santolan-Annapolis": (7.15, -0.56),
            "Araneta Center Cubao (MRT 3)": (5.68, 9.4), "GMA Kamuning": (3.88, 16.5), 
            "Quezon Avenue": (1.6, 22.1), "North Avenue": (-1.98, 27.27),

            "Fernando Poe Jr.": (-7.58, 30.1), "Balintawak": (-11.32, 30.3), "Monumento": (-14.22, 24.8),
            "5th Avenue": (-14.25, 19.8), "R. Papa": (-14.23, 15.2), "Abad Santos": (-14.25, 10.04),
            "Blumentritt": (-14.24, 4.3), "Tayuman": (-14.24, -0.6), "Bambang": (-14.23, -5),
            "Doroteo Jose": (-14.22, -10.3), "Carriedo": (-14.23, -14.8), "Central Station": (-14.22, -19.3),
            "United Nations": (-14.2, -24), "Pedro Gil": (-14.2, -28.4), "Quirino": (-14.2, -32.74),
            "Vito Cruz": (-14.23, -37.44), "Gil Puyat": (-14.2, -41.9), "Libertad": (-14.265, -46.6),
            "EDSA": (-14.265, -50.29), "Baclaran": (-14.265, -55.29), "Redemptorist": (-14.265, -57.34),
            "Aseana": (-14.265, -59.77), "Manila International Airport": (-16.11, -63.6), "AsiaWorld": (-17.543, -67.24),
            "Ninoy Aquino": (-18.96, -70.82), "Dr. Santos": (-20.78, -75.3),

            "Recto": (-13.5, -12.2), "Legarda": (-10.58, -12.15), "Pureza": (-7.7, -12), 
            "V. Mapa": (-4.44, -11.2), "J. Ruiz": (-2.01, -5.1), "Gilmore": (0.57, 1.28),
            "Betty Go-Belmonte": (3.12, 7.55), "Araneta Center Cubao (LRT 2)": (5.61, 14.04),
            "Anonas": (7.79, 18.43), "Katipunan": (10.7, 18.54), "Santolan": (13.53, 18.54),
            "Marikina": (16.47, 14.95), "Antipolo": (20.84, 13.06)
        }


    def _build_graph(self):
        for line, stations in self.lines.items():
            for i in range(len(stations) - 1):
                self.graph.add_edge(stations[i], stations[i + 1], line=line, weight=1)
        
        self.graph.add_edge("EDSA", "Taft Avenue", line="Connection", weight=1)
        self.graph.add_edge("Doroteo Jose", "Recto", line="Connection", weight=1)
        self.graph.add_edge("Araneta Center Cubao (MRT 3)", "Araneta Center Cubao (LRT 2)", line="Connection", weight=1)

    def get_stations(self):
        return self.graph.nodes

    def find_shortest_path(self, start, end):
        return nx.shortest_path(self.graph, source=start, target=end, weight='weight')

    def visualize_path(self, shortest_path):
        plt.figure(figsize=(15, 15))

        if not shortest_path:
            nx.draw(self.graph, self.station_positions, with_labels=True, node_size=800, 
                    node_color="lightblue", font_size=10, font_weight="normal")
            plt.title("Train Network Map")
        else:
            nx.draw(self.graph, self.station_positions, with_labels=True, node_size=800, 
                    node_color="lightblue", font_size=10, font_weight="normal")

            path_edges = list(zip(shortest_path, shortest_path[1:]))
            nx.draw_networkx_nodes(self.graph, self.station_positions, nodelist=shortest_path, 
                                node_color="orange", node_size=800)
            nx.draw_networkx_edges(self.graph, self.station_positions, edgelist=path_edges, 
                                edge_color="red", width=2)

            plt.title(f"Shortest Path from {shortest_path[0]} to {shortest_path[-1]}")

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()
        return img

