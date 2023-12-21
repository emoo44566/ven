import networkx as nx
import matplotlib.pyplot as plt

# ایجاد گراف
G = nx.Graph()

# اضافه کردن گره‌ها
G.add_nodes_from(range(1, 6))

# اضافه کردن یال‌ها به صورت مثال
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# تنظیم ویژگی‌های گره‌ها
node_attributes = {1: {'load': 30, 'generation': 20},
                   2: {'load': 25, 'generation': 30},
                   3: {'load': 35, 'generation': 15},
                   4: {'load': 20, 'generation': 25},
                   5: {'load': 30, 'generation': 20}}

nx.set_node_attributes(G, node_attributes)

# نمایش گراف
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(1, 2): 'Line 1', (2, 3): 'Line 2', (3, 4): 'Line 3', (4, 5): 'Line 4', (5, 1): 'Line 5'})

plt.show()