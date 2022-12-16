"""calcular el promedio final de los equipos de futbol en un torneo. 
Para ello, debemos considerar tres aspectos: 

** jugaron 20 partidos durante el torneo, 
** los partidos poseen diferente puntaje según el resultado, 
** los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos,
el promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos

**partidos_ganados 8
**partido_empatados 7
**partido_perdidos 5
"""

print("Partidos River plate - Categoría Junior")

part_gan = input('Ingrese los partidos ganados: ') 
part_emp = input('Ingrese los partidos empoatados: ') 
part_per = input('Ingrese los partidos perdidos: ')
part_total = input('Ingrese los partidos totales: ')

print("El promedio de todos los partidos jugados en la temporada")
      
      

print(('de '),part_total ,"partidos, En" ' partidos ganados: ',part_gan , ', partidos empatados: ', part_emp , ', partidos perdidos: ',int(part_total) - int(part_gan) - int(part_emp), ', Total de puntos: ' ,  int(part_gan)* 3 + int(part_emp) * 2 )

print('y el promedio en ',part_total,"partidos es: " ,(int(part_gan)* 3 + int(part_emp) * 2 ) / int(part_total))





