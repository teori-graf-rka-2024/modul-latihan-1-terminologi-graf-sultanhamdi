import networkx as nx
import time
from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

def main():
    print("\n🚀 Selamat datang di Program Uji Coba Graf! 🚀\n")
    
    # Membuat graf dari daftar sisi
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    G = create_graph(edges)
    print("📌 Graf berhasil dibuat!")
    
    # Menampilkan derajat dari simpul tertentu
    node = 4
    print(f"\n📊 Derajat simpul {node}: {get_degree(G, node)}")
    time.sleep(1)
    
    # Traversal DFS
    start_node = 1
    print(f"\n🔍 DFS Traversal dari simpul {start_node}: {dfs_traversal(G, start_node)}")
    time.sleep(1)
    
    # Traversal BFS
    print(f"\n🔍 BFS Traversal dari simpul {start_node}: {bfs_traversal(G, start_node)}")
    time.sleep(1)
    
    # Mencari jalur terpendek
    source, target = 1, 5
    print(f"\n🎯 Jalur terpendek dari {source} ke {target}: {find_shortest_path(G, source, target)}")
    time.sleep(1)
    
    # Visualisasi graf
    print("\n📡 Menampilkan visualisasi graf...")
    time.sleep(2)
    visualize_graph(G)
    
    print("\n✅ Semua pengujian selesai! Terima kasih telah menggunakan program ini. 😊")

if __name__ == "__main__":
    main()
