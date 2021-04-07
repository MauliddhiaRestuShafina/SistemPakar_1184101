# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:43:01 2021

@author: Asus VIVOBOOK
"""

#Program Python3 untuk mencetak DFS traversal dari grafik yang diberikan
from collections import defaultdict
 
# Kelas ini mewakili grafik terarah menggunakan
# Representasi daftar kedekatan
 
class Graph:
 
    # Membuat
    def __init__(self):
 
        # Default untuk menyimpan grafik
        self.graph = defaultdict(list)
 
    # Berfungsi untuk menambahkan tepi pada grafik
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # Fungsi yang digunakan oleh DFS
    def DFSUtil(self, v, visited):
 
        # Tandai node saat ini sebagai dikunjungi dan cetak
        visited.add(v)
        print(v, end=' ')
 
        
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # Fungsi untuk melakukan DFS traversal. 
    # Menggunakan rekursif DFSUtil ()
    def DFS(self, v):
 
        # Buat satu set untuk menyimpan simpul yang dikunjungi
        visited = set()
 
        # Panggil fungsi pembantu rekursif untuk mencetak DFS traversal
        self.DFSUtil(v, visited)
 
# Menjalankan kode
 
 
# Buat grafik yang diberikan
# pada diagram di atas
g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 0)
g.addEdge(3, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 0)
g.addEdge(0, 1)
 
print("Hasil dari Depth First Searching")
g.DFS(0)
 
# This code is contributed by Neelam Yadav
