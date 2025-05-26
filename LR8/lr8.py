import osmnx as ox
from collections import defaultdict
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="Выберите OSM-файл",
    filetypes=[("OSM files", "*.osm *.xml")]
)

if not file_path:
    print("Файл не выбран.")
    exit()

G = ox.graph_from_xml(file_path, simplify=True)

road_lengths = defaultdict(float)

for u, v, data in G.edges(data=True):
    highway_type = data.get('highway')
    length = data.get('length', 0)

    if highway_type:
        if isinstance(highway_type, list):
            highway_type = highway_type[0]
        road_lengths[highway_type] += length

print("\nСуммарная длина дорог по типам (в метрах):")
for road_type, total_length in sorted(road_lengths.items(), key=lambda x: -x[1]):
    print(f"{road_type:20s} : {total_length:.2f} м")
