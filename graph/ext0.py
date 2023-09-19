import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

# ツリーグラフを作成
G = nx.DiGraph()  # 有向グラフを作成


G.add_node("root")
G.add_edge("root", "child1")
G.add_edge("root", "child2")
G.add_edge("child2", "subchild1")
G.add_edge("child2", "subchild2")


# ツリーグラフの描画
#pos = nx.spring_layout(G)  # ノードの配置

pos = graphviz_layout(G, prog="dot")

nx.draw(G, pos=pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
plt.show()
