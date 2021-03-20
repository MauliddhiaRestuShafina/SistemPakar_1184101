# Sistem Pakar_1184101_Mauliddhia Restu Shafina

# Depth First Searching
Merupakan salah satu algoritma yang digunakan untuk pencarian jalur. Caranya berawal dari node root atau akar 
bergerak untuk memeriksa dahulu semua anak atau turunan dari suatu cabang sebelum beralih ke cabang lain. Gambaran 
pada DFS_1184101 yang saya buat adalah berawal dari 1 ke 2, 1 ke 3, 1 ke 0, 3 ke 2, 2 ke 3, 3 ke 4, 4 ke 5, 5 ke 0, dan 0 ke 1.
Pada DFS_1184101 ini, hasilnya seperti berikut :
1. Apabila dirun dari (1) maka hasilnya yaitu 1,2,3,4,5,0
2. Apabila dirun dari (2) maka hasilnya yaitu 2,3,4,5,0,1
3. Apabila dirun dari (3) maka hasilnya yaitu 3,2,4,5,0,1
4. Aapabila dirun dari (4) maka hasilnya yaitu 4,5,0,1,2,3
5. Apabila dirun dari (5) maka hasilnya yaitu 5,0,1,2,3,4
6. Apabila dirun dari (0) maka hasilnya yaitu 0,1,2,3,4,5

# Breadth Fisrt Searching
Merupakan salah satu algoritma yang digunakan untuk pencarian jalur. Bedanya, cara BFS ini mengecek per level bukan 
mengecek kedalaman tiap level. Gambaran pada BFS_1184101 ini saya buat sama dengan DFS_1184101. Pada BFS_1184101 hasilnya
akan seperti berikut ini :
1. Apabila dirun dari (1) maka hasilnya yaitu 1,2,3,0,4,5
2. Apabila dirun dari (2) maka hasilnya yaitu 2,3,4,5,0,1
3. Apabila dirun dari (3) maka hasilnya yaitu 3,2,4,5,0,1
4. Apabila dirun dari (4) maka hasilnya yaitu 4,5,0,1,2,3
5. Apabila dirun dari (5) maka hasilnya yaitu 5,0,1,2,3,4
6. Apabila dirun dari (0) maka hasilnya yaitu 0,1,2,3,4,5
