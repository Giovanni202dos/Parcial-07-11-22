"""2 - Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para 
resolver las siguientes tareas:
a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la 
cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;
e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes."""
from grafo import Grafo
grafoo = Grafo(dirigido=False)

grafoo.insertar_vertice('luke skywalker')
grafoo.insertar_vertice('rey skywalker')
grafoo.insertar_vertice('kanan jarrus')
grafoo.insertar_vertice('ahsoka tano')
grafoo.insertar_vertice('coleman trebor')
grafoo.insertar_vertice('Yoda')
grafoo.insertar_vertice('Mandalorian')

grafoo.insertar_vertice('Darth Vader')
grafoo.insertar_vertice('Boba Fett')
grafoo.insertar_vertice('C3PO')
grafoo.insertar_vertice('Leia')
grafoo.insertar_vertice('Kylo Ren')
grafoo.insertar_vertice('Chewbacca')
grafoo.insertar_vertice('Han Solo')
grafoo.insertar_vertice('R2D2')
grafoo.insertar_vertice('Obi Wan kenobi')
grafoo.insertar_vertice('BB8')


grafoo.insertar_arista('luke skywalker','rey skywalker',3)
grafoo.insertar_arista('luke skywalker','kanan jarrus',4)
grafoo.insertar_arista('kanan jarrus','rey skywalker',5)
grafoo.insertar_arista('rey skywalker','coleman trebor',6)
grafoo.insertar_arista('rey skywalker','Yoda',7)
grafoo.insertar_arista('Yoda','coleman trebor',8)
grafoo.insertar_arista('rey skywalker','Mandalorian',9)

grafoo.insertar_arista('Mandalorian','Darth Vader',120)
grafoo.insertar_arista('Darth Vader','Boba Fett',10)
grafoo.insertar_arista('Darth Vader','C3PO',11)
grafoo.insertar_arista('Darth Vader','Leia',12)
grafoo.insertar_arista('ralker','Mandalorian',13)
grafoo.insertar_arista('Leia','Kylo Ren',14)
grafoo.insertar_arista('Leia','Chewbacca',15)
grafoo.insertar_arista('Leia','Han Solo',16)
grafoo.insertar_arista('Leia','R2D2',17)
grafoo.insertar_arista('Leia','coleman trebor',123)
grafoo.insertar_arista('R2D2','Obi Wan kenobi',18)
grafoo.insertar_arista('R2D2','BB8',19)
grafoo.insertar_arista('R2D2','ahsoka tano',21)
grafoo.insertar_arista('Darth Vader','rey skywalker',24)

print('B)')
#b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
arbol_minimo_completo=grafoo.kruskal()
print(arbol_minimo_completo)

print()
print('C)')
#c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
for conexion in grafoo.obtener_vector_con_los_jedis_q_tienen_mas_a_x_episodios_con_otro(4):
    print(conexion)

#d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;
print()
print('E)')
#E. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.
print()
print(grafoo.vertice_con_mayor_aristas_o_con_mayor_conexion_con_adyacentes())

