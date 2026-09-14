#EJERCICIO 1
#Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100,
# False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, 
#las valide, agregue solo las válidas a una lista interna, y retorne esa lista; (3) 
#tenga método promedio() que retorne el promedio de notas almacenadas.

class Calificador:

    def __init__(self):
        self.notas = []

    def validar(self, nota):

        if 0 <= nota <= 100:
            return True
        else:
            return False

    def cargar(self, *args):

        for nota in args:

            if self.validar(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):

        return sum(self.notas) / len(self.notas)


c = Calificador()

print(c.cargar(85, 92, 110, 78, -5, 88))

print(c.promedio())


#EJERCICIO 2
#Clase AnalizadorTexto que: (1) tenga método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados) y a una lista (para el orden); (2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; 
#(3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios.
#

class AnalizadorTexto:

    def __init__(self):
        self.palabras_unicas = set()
        self.lista_palabras = []

    def agregar_palabra(self, palabra):

        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.lista_palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):

        for palabra in args:
            self.agregar_palabra(palabra)


at = AnalizadorTexto()

at.agregar_multiples("hola", "mundo", "hola")

print(at.lista_palabras)
print(at.contar_palabras())

#Ejercicio 3  
#Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) que guarde en un 
#diccionario {nombre: precio}; (2) tenga método total_carrito() que retorne la suma de todos 
#los precios; (3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista 
#con artículos dentro del rango.


class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):

        total = 0

        for precio in self.articulos.values():
            total += precio

        return total

    def articulos_por_rango(self, precio_min, precio_max):

        resultado = []

        for nombre, precio in self.articulos.items():

            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)

        return resultado


c = CarroCompras()

c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
c.agregar_articulo("arroz", 5.50)
c.agregar_articulo("carne", 10.00)

print(c.total_carrito())

print(c.articulos_por_rango(2, 6))


#EJERCICIO 4
#Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que retorne la lista 
#invertida sin usar reversed() (usa manual con bucles); (2) tenga método invertir_multiples(*listas) 
#que reutilice el anterior para invertir
# varias listas y retorne un diccionario {lista_original: lista_invertida}.

class InversorSecuencia:

    def invertir_lista(self, lista):

        lista_invertida = []

        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])

        return lista_invertida

    def invertir_multiples(self, *listas):

        resultado = {}

        for lista in listas:

            original = tuple(lista)
            invertida = self.invertir_lista(lista)

            resultado[original] = invertida

        return resultado


inv = InversorSecuencia()

print(inv.invertir_lista([1, 2, 3]))

print(inv.invertir_multiples(
    [1, 2, 3],
    [4, 5, 6],
    [7, 8]
))


#EJERCICIO 5
#Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False;
# (2) tenga método separar(*numeros) que retorne un diccionario
# {'pares': [...], 'impares': [...]} reutilizando es_par; (3) tenga método cantidad_pares_impares()
# que retorne una tupla (cant_pares, cant_impares).

class AnalizadorNumeros:

    def __init__(self):
        self.resultado = {
            "pares": [],
            "impares": []
        }

    def es_par(self, numero):

        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):

        self.resultado = {
            "pares": [],
            "impares": []
        }

        for numero in numeros:

            if self.es_par(numero):
                self.resultado["pares"].append(numero)
            else:
                self.resultado["impares"].append(numero)

        return self.resultado

    def cantidad_pares_impares(self):

        cantidad_pares = len(self.resultado["pares"])
        cantidad_impares = len(self.resultado["impares"])

        return (cantidad_pares, cantidad_impares)


an = AnalizadorNumeros()

print(an.separar(1, 2, 3, 4, 5))

print(an.cantidad_pares_impares())




#EJERCICIO 6
#Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp)
#que guarde en una lista; (2) tenga método minima()`, `maxima()`, `promedio() 
#que calculen estadísticas; (3) tenga método registrar_multiples(*temps) que reutilice
# el registro para varias temperaturas.

class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):

        for temperatura in temps:
            self.registrar_temperatura(temperatura)

    def minima(self):

        if len(self.temperaturas) > 0:
            return min(self.temperaturas)
        else:
            return None

    def maxima(self):

        if len(self.temperaturas) > 0:
            return max(self.temperaturas)
        else:
            return None

    def promedio(self):

        if len(self.temperaturas) > 0:
            return sum(self.temperaturas) / len(self.temperaturas)
        else:
            return 0


gt = GestorTemperatura()

gt.registrar_multiples(20, 25, 18, 30)

print("Mínima:", gt.minima())
print("Máxima:", gt.maxima())
print("Promedio:", gt.promedio())


#EJERCICIO 7
#Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario;
#(2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥; (3)
#tenga método edad_promedio() que retorne el promedio de edades.


class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):

        mayores = []

        for nombre, edad in self.personas.items():

            if edad >= edad_minima:
                mayores.append(nombre)

        return mayores

    def edad_promedio(self):

        if len(self.personas) == 0:
            return 0

        suma_edades = 0

        for edad in self.personas.values():
            suma_edades += edad

        return suma_edades / len(self.personas)


gp = GestorPersonas()

gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
gp.agregar_persona("Carlos", 22)

print(gp.personas_mayores(18))

print(gp.edad_promedio())

#EJERCICIO 8
#Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como
# una lista vacía en un diccionario; (2) tenga método agregar_jugador(equipo, jugador) 
#que añada el jugador al equipo; (3) tenga método equipo_mayor_integrantes() que retorne el 
#nombre del equipo con más jugadores.

class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):

        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)
            return True
        else:
            return False

    def equipo_mayor_integrantes(self):

        if len(self.equipos) == 0:
            return None

        equipo_mayor = ""
        mayor_cantidad = -1

        for nombre, jugadores in self.equipos.items():

            if len(jugadores) > mayor_cantidad:

                mayor_cantidad = len(jugadores)
                equipo_mayor = nombre

        return equipo_mayor


eq = Equipos()

eq.crear_equipo("A")
eq.crear_equipo("B")

eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")

eq.agregar_jugador("B", "Carlos")

print(eq.equipos)

print(eq.equipo_mayor_integrantes())

#EJERCICIO 9
#Clase AnalizadorString que: (1) tenga método solo_vocales(letra) que retorne True si es vocal; 
#(2) tenga método contar_por_tipo(texto) que retorne un diccionario 
#{'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
#(3) tenga atributo que guarde el texto más largo analizado.

class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):

        letra = letra.lower()

        if letra in "aeiouáéíóú":
            return True
        else:
            return False

    def contar_por_tipo(self, texto):

        resultado = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        for caracter in texto:

            if caracter.isdigit():
                resultado["digitos"] += 1

            elif caracter.isalpha():

                if self.solo_vocales(caracter):
                    resultado["vocales"] += 1
                else:
                    resultado["consonantes"] += 1

        return resultado


astr = AnalizadorString()

print(astr.contar_por_tipo("Hola123"))

print(astr.texto_mas_largo)

#EJERCICIO 10
#Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista
#de tuplas (descripción, prioridad); (2) tenga método tareas_prioritarias() que retorne solo 
#las de prioridad alta; (3) tenga método eliminar_completada(descripcion) que borre la tarea de la 
#lista.
class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):

        tarea = (descripcion, prioridad)

        self.tareas.append(tarea)

    def tareas_prioritarias(self):

        prioritarias = []

        for tarea in self.tareas:

            if tarea[1].lower() == "alta":
                prioritarias.append(tarea)

        return prioritarias

    def eliminar_completada(self, descripcion):

        for tarea in self.tareas:

            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True

        return False


t = Tareas()

t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.agregar_tarea("Hacer deberes", "alta")

print(t.tareas_prioritarias())

t.eliminar_completada("Estudiar")

print(t.tareas)



