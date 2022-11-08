"""1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de personajes de la saga de Star Wars, 
de los cuales se sabe su nombre, altura y peso. Además deberá contemplar los siguientes requerimientos (debe cargar al menos 20 personajes):
a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
e. mostrar un listado por nivel de los personajes del árbol;
f. determinar si Grogu esta en el árbol y responder lo siguiente:
mostrar toda su información;
en que tipo de nodo esta (hoja, intermedio o raíz);
que altura tiene el nodo dentro del árbol."""
from arbol import *
arboll = nodoArbol()

insertar_nodo(arboll,'luke skywalker',{'altura':1,'peso':2})
insertar_nodo(arboll,'rey skywalker',{'altura':3,'peso':4})
insertar_nodo(arboll,'kanan jarrus',{'altura':5,'peso':6})
insertar_nodo(arboll,'ahsoka tano',{'altura':7,'peso':8})
insertar_nodo(arboll,'coleman trebor',{'altura':9,'peso':10})
insertar_nodo(arboll,'Yoda',{'altura':12,'peso':100})
insertar_nodo(arboll,'Mandalorian',{'altura':122,'peso':20})

insertar_nodo(arboll,'yarael poof',{'altura':122,'peso':20})
insertar_nodo(arboll,'depa billaba',{'altura':122,'peso':20})
insertar_nodo(arboll,'kit fisto',{'altura':122,'peso':20})
insertar_nodo(arboll,'barriss offee',{'altura':122,'peso':20})
insertar_nodo(arboll,'coleman trebor',{'altura':122,'peso':20})
insertar_nodo(arboll,'count dooku',{'altura':122,'peso':20})
insertar_nodo(arboll,'bultar swan',{'altura':122,'peso':20})
insertar_nodo(arboll,'stass allie',{'altura':122,'peso':20})
insertar_nodo(arboll,'nahdar vebb',{'altura':122,'peso':20})
insertar_nodo(arboll,'ord enisence',{'altura':122,'peso':20})
insertar_nodo(arboll,'tera sinube',{'altura':122,'peso':20})
insertar_nodo(arboll,'tiplar',{'altura':122,'peso':20})
insertar_nodo(arboll,'bultar',{'altura':122,'peso':20})
insertar_nodo(arboll,'luminara unduli',{'altura':122,'peso':20})

cargar_nuevo_personaje(arboll,'aayla secura',30,50)
modificar_el_campo_nombre_de_x_jedi(arboll,'aayla secura','andres')
modificar_el_campo_altura_de_x_jedi(arboll,'kanan jarrus',12)
modificar_el_campo_peso_de_x_jedi(arboll,'rey skywalker',60)

print()
print('B)')
#b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
mostrar_todas_las_info_de_jedi_x(arboll,'Yoda')
mostrar_todas_las_info_de_jedi_x(arboll,'Mandalorian')
mostrar_todas_las_info_de_jedi_x(arboll,'Luke Skywalker')

print()
print('C)')
#c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
print()
mostrar_alfabeticamente_todos_los_personajes_jedis_q_midan_menos_q_altura_x(arboll,4)

print()
print('D)')
#d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
print()
mostrar_alfabeticamente_todos_los_personajes_jedis_q_pesan_mas_de_x_kilos(arboll,49)

print()
print('E)')
#e. mostrar un listado por nivel de los personajes del árbol;
print()
por_nivel(arboll)

print()
print('F)')
#f:
print()
print(jedi_x_esta_cargado(arboll,'ahsoka tano'))
if jedi_x_esta_cargado(arboll,'ahsoka tano'):
    mostrar_todas_las_info_de_jedi_x(arboll,'ahsoka tano')
    print()
    mostrar_altura_del_nodo_de_jedi_x(arboll,'ahsoka tano')
    print()
    nodo_de_jedi_x_es_hoja_intermedio_o_raiz(arboll,'ahsoka tano')
else:
    print('jedi no encontrado')





