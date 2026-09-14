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

# Bosquejo a mano
#
# Instancia: c = Calificador() -> c.notas = []
#
# Llamada: c.cargar(85, 92, 110, 78, -5, 88)
# Reviso cada nota con validar():
# - nota = 85  -> ¿0 <= 85 <= 100? V -> Notas: [85]
# - nota = 92  -> ¿0 <= 92 <= 100? V -> Notas: [85, 92]
# - nota = 110 -> ¿0 <= 110 <= 100? F -> Se descarta
# - nota = 78  -> ¿0 <= 78 <= 100? V -> Notas: [85, 92, 78]
# - nota = -5  -> ¿0 <= -5 <= 100? F -> Se descarta
# - nota = 88  -> ¿0 <= 88 <= 100? V -> Notas: [85, 92, 78, 88]
#
# Retorno de cargar(): [85, 92, 78, 88]
# Imprime: [85, 92, 78, 88]
#
# Llamada: c.promedio()
# Suma = 85 + 92 + 78 + 88 = 343
# Total de elementos = 4
# Promedio = 343 / 4 = 85.75
# Imprime: 85.75


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

# Bosquejo a mano
#
# Instancia: at = AnalizadorTexto()
# at.palabras_unicas = set()
# at.lista_palabras = []
#
# Llamada: at.agregar_multiples("hola", "mundo", "hola")
# Iteración 1: palabra = "hola"
# - ¿"hola" no está en palabras_unicas? Sí (está vacío)
# - Agrego a set: {"hola"}
# - Agrego a lista: ["hola"]
# Iteración 2: palabra = "mundo"
# - ¿"mundo" no está en palabras_unicas? Sí
# - Agrego a set: {"hola", "mundo"}
# - Agrego a lista: ["hola", "mundo"]
# Iteración 3: palabra = "hola"
# - ¿"hola" no está en palabras_unicas? No (ya existía en el conjunto)
# - No hace nada, ignora duplicado.
#
# print(at.lista_palabras) -> Imprime: ['hola', 'mundo']
# print(at.contar_palabras()) -> Tamaño del set = 2 -> Imprime: 2


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

# Bosquejo a mano
#
# Estado del diccionario tras agregar artículos:
# c.articulos = {"pan": 2.50, "leche": 3.00, "arroz": 5.50, "carne": 10.00}
#
# Método total_carrito():
# total = 0
# - precio 2.50 -> total = 2.50
# - precio 3.00 -> total = 5.50
# - precio 5.50 -> total = 11.00
# - precio 10.00 -> total = 21.00
# Retorna: 21.0
# Imprime: 21.0
#
# Método articulos_por_rango(2, 6):
# Rango buscado: [2.00 , 6.00]
# resultado = []
# - "pan": 2.50 -> ¿2 <= 2.50 <= 6? V -> resultado = ["pan"]
# - "leche": 3.00 -> ¿2 <= 3.00 <= 6? V -> resultado = ["pan", "leche"]
# - "arroz": 5.50 -> ¿2 <= 5.50 <= 6? V -> resultado = ["pan", "leche", "arroz"]
# - "carne": 10.00 -> ¿2 <= 10.00 <= 6? F -> Se salta
# Retorna: ["pan", "leche", "arroz"]
# Imprime: ['pan', 'leche', 'arroz']


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

# Bosquejo a mano
#
# Llamada 1: inv.invertir_lista([1, 2, 3])
# len(lista) = 3 -> range(2, -1, -1) [índices: 2, 1, 0]
# - i = 2: lista[2] = 3 -> lista_invertida = [3]
# - i = 1: lista[1] = 2 -> lista_invertida = [3, 2]
# - i = 0: lista[0] = 1 -> lista_invertida = [3, 2, 1]
# Imprime: [3, 2, 1]
#
# Llamada 2: inv.invertir_multiples([1, 2, 3], [4, 5, 6], [7, 8])
# Procesando cada lista:
# 1) [1, 2, 3] -> original = (1, 2, 3) | invertida = [3, 2, 1]
# 2) [4, 5, 6] -> original = (4, 5, 6) | invertida = [6, 5, 4]
# 3) [7, 8]    -> original = (7, 8)    | invertida = [8, 7]
#
# Imprime: {(1, 2, 3): [3, 2, 1], (4, 5, 6): [6, 5, 4], (7, 8): [8, 7]}


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

# Bosquejo a mano
#
# Llamada: an.separar(1, 2, 3, 4, 5)
# Reinicia self.resultado = {"pares": [], "impares": []}
# Evaluando con es_par():
# - 1 % 2 == 1 -> Impar -> impares: [1]
# - 2 % 2 == 0 -> Par   -> pares: [2]
# - 3 % 2 == 1 -> Impar -> impares: [1, 3]
# - 4 % 2 == 0 -> Par   -> pares: [2, 4]
# - 5 % 2 == 1 -> Impar -> impares: [1, 3, 5]
#
# Imprime: {'pares': [2, 4], 'impares': [1, 3, 5]}
#
# Llamada: an.cantidad_pares_impares()
# cantidad_pares = len([2, 4]) = 2
# cantidad_impares = len([1, 3, 5]) = 3
# Retorna: (2, 3)
# Imprime: (2, 3)


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

# Bosquejo a mano
#
# gt.registrar_multiples(20, 25, 18, 30)
# Lista interna: self.temperaturas = [20, 25, 18, 30]
#
# Calculando estadísticas:
# - len(temperaturas) = 4 (es mayor a 0)
# - minima() -> min([20, 25, 18, 30]) = 18
# - maxima() -> max([20, 25, 18, 30]) = 30
# - promedio() -> sum([20, 25, 18, 30]) / 4 = 93 / 4 = 23.25
#
# Saludidas por consola:
# Imprime: Mínima: 18
# Imprime: Máxima: 30
# Imprime: Promedio: 23.25


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

# Bosquejo a mano
#
# Diccionario guardado:
# self.personas = {"Ana": 28, "Bob": 17, "Carlos": 22}
#
# Llamada: gp.personas_mayores(18)
# Filtro: edad >= 18
# - "Ana": 28 >= 18 V -> mayores = ["Ana"]
# - "Bob": 17 >= 18 F -> se descarta
# - "Carlos": 22 >= 18 V -> mayores = ["Ana", "Carlos"]
# Imprime: ['Ana', 'Carlos']
#
# Llamada: gp.edad_promedio()
# Cantidad de personas = 3
# Suma de edades = 28 + 17 + 22 = 67
# Promedio = 67 / 3 = 22.3333...
# Imprime: 22.333333333333332


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

# Bosquejo a mano
#
# Registro de operaciones:
# - crear_equipo("A") -> {"A": []}
# - crear_equipo("B") -> {"A": [], "B": []}
# - agregar_jugador("A", "Juan") -> {"A": ["Juan"], "B": []}
# - agregar_jugador("A", "Pedro") -> {"A": ["Juan", "Pedro"], "B": []}
# - agregar_jugador("B", "Carlos") -> {"A": ["Juan", "Pedro"], "B": ["Carlos"]}
#
# print(eq.equipos)
# Imprime: {'A': ['Juan', 'Pedro'], 'B': ['Carlos']}
#
# Llamada: equipo_mayor_integrantes()
# Iniciales: equipo_mayor = "", mayor_cantidad = -1
# - Equipo "A": len = 2. ¿2 > -1? V -> equipo_mayor = "A", mayor_cantidad = 2
# - Equipo "B": len = 1. ¿1 > 2? F -> no cambia
# Retorna "A"
# Imprime: A


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

# Bosquejo a mano
#
# Llamada: astr.contar_por_tipo("Hola123")
# len("Hola123") = 7 > len("") = 0 -> texto_mas_largo = "Hola123"
# Recorrido caracter por caracter:
# - 'H': es letra -> ¿es vocal? F -> consonantes = 1
# - 'o': es letra -> ¿es vocal? V -> vocales = 1
# - 'l': es letra -> ¿es vocal? F -> consonantes = 2
# - 'a': es letra -> ¿es vocal? V -> vocales = 2
# - '1': es dígito -> digitos = 1
# - '2': es dígito -> digitos = 2
# - '3': es dígito -> digitos = 3
#
# Imprime: {'vocales': 2, 'consonantes': 2, 'digitos': 3}
# print(astr.texto_mas_largo) -> Imprime: Hola123


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

# Bosquejo a mano
#
# Carga de tareas:
# self.tareas = [("Estudiar", "alta"), ("Leer", "baja"), ("Hacer deberes", "alta")]
#
# Llamada: t.tareas_prioritarias()
# Filtro tarea[1] == "alta":
# - ("Estudiar", "alta") -> Entra
# - ("Leer", "baja") -> Ignora
# - ("Hacer deberes", "alta") -> Entra
# Imprime: [('Estudiar', 'alta'), ('Hacer deberes', 'alta')]
#
# Llamada: t.eliminar_completada("Estudiar")
# Busca tarea[0] == "Estudiar":
# - Coincide en la primera tupla -> la elimina de self.tareas
#
# print(t.tareas)
# Quedan: [('Leer', 'baja'), ('Hacer deberes', 'alta')]
# Imprime: [('Leer', 'baja'), ('Hacer deberes', 'alta')]


#11 Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) que guarde en un diccionario contando repeticiones; 
#(2) tenga método elemento_mas_frecuente() que retorne el elemento con mayor frecuencia; 
# (3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece.
class ContadorFrecuencia:

    def __init__(self):
        self.diccionario = {}

    def agregar_elemento(self, elemento):
        if elemento in self.diccionario:
            self.diccionario[elemento] += 1
        else:
            self.diccionario[elemento] = 1

    def elemento_mas_frecuente(self):
        mayor = 0
        elemento_mayor = None

        for elemento, cantidad in self.diccionario.items():
            if cantidad > mayor:
                mayor = cantidad
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.diccionario:
            return self.diccionario[elemento]
        else:
            return 0


cf = ContadorFrecuencia()

cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")

print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))

# Bosquejo a mano
#
# Operaciones:
# - agregar_elemento("a") -> "a" no está -> diccionario = {"a": 1}
# - agregar_elemento("b") -> "b" no está -> diccionario = {"a": 1, "b": 1}
# - agregar_elemento("a") -> "a" sí está -> diccionario = {"a": 2, "b": 1}
#
# Llamada: cf.elemento_mas_frecuente()
# mayor = 0, elemento_mayor = None
# - "a": 2 -> ¿2 > 0? V -> mayor = 2, elemento_mayor = "a"
# - "b": 1 -> ¿1 > 2? F
# Retorna: "a"
# Imprime: a
#
# Llamada: cf.frecuencia_elemento("a")
# - "a" está en diccionario -> retorna self.diccionario["a"] -> 2
# Imprime: 2


#12Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango; 
# (2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto.
class SelectorRango:

    def __init__(self):
        self.conjunto = set()

    def crear_rango(self, inicio, fin):
        rango = ()

        for numero in range(inicio, fin + 1):
            rango += (numero,)

        return rango

    def elementos_en_multiples_rangos(self, *args):
        for inicio, fin in args:
            rango = self.crear_rango(inicio, fin)

            for numero in rango:
                self.conjunto.add(numero)

        return sorted(self.conjunto)


sr = SelectorRango()

print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))

# Bosquejo a mano
#
# Llamada: sr.elementos_en_multiples_rangos((1, 3), (2, 4))
#
# Arg 1: (1, 3)
# - crear_rango(1, 3) -> range(1, 4) -> retorna (1, 2, 3)
# - Agrega al conjunto: {1, 2, 3}
#
# Arg 2: (2, 4)
# - crear_rango(2, 4) -> range(2, 5) -> retorna (2, 3, 4)
# - Agrega al conjunto: {1, 2, 3, 4} (los duplicados 2 y 3 no se repiten)
#
# Retorna: sorted({1, 2, 3, 4}) -> [1, 2, 3, 4]
# Imprime: [1, 2, 3, 4]


#13.Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; 
#(2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.
class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []
        i = 0

        while i < len(lista1) or i < len(lista2):

            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

            i += 1

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = listas[0]

        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)

        return resultado


cl = CombinadorListas()

print(cl.intercalar([1, 2], [3, 4]))

# Bosquejo a mano
#
# Llamada: cl.intercalar([1, 2], [3, 4])
# len(lista1) = 2, len(lista2) = 2
# resultado = []
#
# - i = 0:
#   ¿0 < 2? Sí (lista1) -> agrega lista1[0] (1) -> resultado = [1]
#   ¿0 < 2? Sí (lista2) -> agrega lista2[0] (3) -> resultado = [1, 3]
# - i = 1:
#   ¿1 < 2? Sí (lista1) -> agrega lista1[1] (2) -> resultado = [1, 3, 2]
#   ¿1 < 2? Sí (lista2) -> agrega lista2[1] (4) -> resultado = [1, 3, 2, 4]
# - i = 2:
#   ¿2 < 2? No -> Termina el bucle.
#
# Imprime: [1, 3, 2, 4]


#14Clase RegistroNotas que: (1) tenga método registrar(estudiante, nota) que guarde en un diccionario; 
# (2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; 
# (3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.
class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        mejor_nombre = ""
        mejor_nota = 0

        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)


rn = RegistroNotas()

rn.registrar("Ana", 95)
rn.registrar("Bob", 70)

print(rn.estudiantes_aprobados(70))
print(rn.mejor_estudiante())

# Bosquejo a mano
#
# Estado de notas: self.notas = {"Ana": 95, "Bob": 70}
#
# Llamada: rn.estudiantes_aprobados(70)
# - "Ana": 95 >= 70 V -> aprobados = ["Ana"]
# - "Bob": 70 >= 70 V -> aprobados = ["Ana", "Bob"]
# Imprime: ['Ana', 'Bob']
#
# Llamada: rn.mejor_estudiante()
# Iniciales: mejor_nombre = "", mejor_nota = 0
# - "Ana", 95: ¿95 > 0? V -> mejor_nota = 95, mejor_nombre = "Ana"
# - "Bob", 70: ¿70 > 95? F
# Retorna: ("Ana", 95)
# Imprime: ('Ana', 95)


#15.Clase DivisorFinder que: (1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores; 
# (2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; 
# (3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.
class DivisorFinder:

    def __init__(self):
        self.divisores = {}

    def encontrar_divisores(self, numero):
        lista = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                lista.append(i)

        return tuple(lista)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)

        suma = 0

        for divisor in divisores:
            if divisor != numero:
                suma += divisor

        if suma == numero:
            return True
        else:
            return False

    def encontrar_multiples_divisores(self, *numeros):
        for numero in numeros:
            self.divisores[numero] = self.encontrar_divisores(numero)

        return self.divisores


df = DivisorFinder()

print(df.encontrar_divisores(12))
print(df.es_perfecto(6))
print(df.encontrar_multiples_divisores(6, 12, 10))

# Bosquejo a mano
#
# Llamada 1: df.encontrar_divisores(12)
# Probar divisores de 1 a 12: 12 es divisible por 1, 2, 3, 4, 6, 12.
# Imprime: (1, 2, 3, 4, 6, 12)
#
# Llamada 2: df.es_perfecto(6)
# Divisores de 6: (1, 2, 3, 6)
# Sumar excluyendo el 6: 1 + 2 + 3 = 6
# ¿Suma (6) == numero (6)? V -> Retorna True
# Imprime: True
#
# Llamada 3: df.encontrar_multiples_divisores(6, 12, 10)
# Calcula divisores para cada uno:
# - 6  -> (1, 2, 3, 6)
# - 12 -> (1, 2, 3, 4, 6, 12)
# - 10 -> (1, 2, 5, 10)
# Imprime: {6: (1, 2, 3, 6), 12: (1, 2, 3, 4, 6, 12), 10: (1, 2, 5, 10)}


#16.Clase CodificadorCesar que: (1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %); 
#(2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; 
#(3) tenga un diccionario como atributo para historial de codificaciones.
class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        codigo = ord(letra)

        codigo = (codigo - ord('a') + desplazamiento) % 26

        letra_nueva = chr(codigo + ord('a'))

        return letra_nueva

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


cc = CodificadorCesar()

print(cc.codificar_palabra("hola", 3))

# Bosquejo a mano
#
# Llamada: cc.codificar_palabra("hola", 3)
# Procesando letra por letra con desplazamiento = 3:
# - 'h': ord('h') - ord('a') = 104 - 97 = 7
#   (7 + 3) % 26 = 10 -> chr(10 + 97) = chr(107) = 'k'
# - 'o': ord('o') - ord('a') = 111 - 97 = 14
#   (14 + 3) % 26 = 17 -> chr(17 + 97) = chr(114) = 'r'
# - 'l': ord('l') - ord('a') = 108 - 97 = 11
#   (11 + 3) % 26 = 14 -> chr(14 + 97) = chr(111) = 'o'
# - 'a': ord('a') - ord('a') = 97 - 97 = 0
#   (0 + 3) % 26 = 3 -> chr(3 + 97) = chr(100) = 'd'
#
# resultado = "krod"
# historial["hola"] = "krod"
# Imprime: krod


#17.Clase AgrupadorEdades que: (1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); 
# (2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; 
# (3) tenga método edad_promedio_categoria(categoria).
class AgrupadorEdades:

    def __init__(self):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):

        if edad < 13:
            return "niño"

        elif edad < 18:
            return "adolescente"

        elif edad < 65:
            return "adulto"

        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):

        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):

        edades = self.grupos[categoria]

        if len(edades) == 0:
            return 0

        suma = 0

        for edad in edades:
            suma += edad

        return suma / len(edades)


ae = AgrupadorEdades()

print(ae.agrupar_por_categoria(5, 15, 30, 70))

print(ae.edad_promedio_categoria("adulto"))

# Bosquejo a mano
#
# Llamada 1: ae.agrupar_por_categoria(5, 15, 30, 70)
# - edad = 5  -> < 13 -> "niño"        -> grupos["niño"] = [5]
# - edad = 15 -> < 18 -> "adolescente" -> grupos["adolescente"] = [15]
# - edad = 30 -> < 65 -> "adulto"      -> grupos["adulto"] = [30]
# - edad = 70 -> >=65 -> "mayor"       -> grupos["mayor"] = [70]
#
# Imprime: {'niño': [5], 'adolescente': [15], 'adulto': [30], 'mayor': [70]}
#
# Llamada 2: ae.edad_promedio_categoria("adulto")
# edades = [30]
# len([30]) = 1
# suma = 30
# promedio = 30 / 1 = 30.0
# Imprime: 30.0


#18. Clase CalculadorDistancia que: (1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia; 
# (2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; 
# (3) tenga un atributo lista para guardar todas las distancias calculadas.
import math

class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_menor = float("inf")

        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano


cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0, 0), (3, 4)))
print(cd.punto_mas_cercano((0, 0), (3, 4), (1, 1), (5, 5)))

# Bosquejo a mano
#
# Llamada 1: cd.distancia_euclidiana((0, 0), (3, 4))
# x1=0, y1=0, x2=3, y2=4
# distancia = sqrt((3-0)^2 + (4-0)^2) = sqrt(9 + 16) = sqrt(25) = 5.0
# Imprime: 5.0
#
# Llamada 2: cd.punto_mas_cercano((0, 0), (3, 4), (1, 1), (5, 5))
# referencia = (0, 0)
# Iniciales: punto_cercano = None, distancia_menor = inf
#
# - punto = (3, 4):
#   distancia = sqrt(3^2 + 4^2) = 5.0
#   ¿5.0 < inf? V -> punto_cercano = (3, 4), distancia_menor = 5.0
#
# - punto = (1, 1):
#   distancia = sqrt(1^2 + 1^2) = sqrt(2) ≈ 1.414
#   ¿1.414 < 5.0? V -> punto_cercano = (1, 1), distancia_menor = 1.414
#
# - punto = (5, 5):
#   distancia = sqrt(5^2 + 5^2) = sqrt(50) ≈ 7.071
#   ¿7.071 < 1.414? F
#
# Retorna: (1, 1)
# Imprime: (1, 1)


#19.Clase Inventario que: (1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
# (2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
# (3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.
class Inventario:

    def __init__(self):
        self.productos = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.productos:
            if self.productos[producto] >= cantidad:
                self.productos[producto] -= cantidad
                return True

        return False

    def productos_bajo_stock(self, minimo):
        lista = []

        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                lista.append(producto)

        return lista


inv = Inventario()

inv.agregar_stock("pan", 50)

print(inv.restar_stock("pan", 30))

print(inv.productos_bajo_stock(15))

# Bosquejo a mano
#
# Operación: inv.agregar_stock("pan", 50)
# self.productos = {"pan": 50}
#
# Llamada: inv.restar_stock("pan", 30)
# ¿"pan" en productos? Sí
# ¿50 >= 30? Sí -> self.productos["pan"] = 50 - 30 = 20
# Retorna: True
# Imprime: True
#
# Llamada: inv.productos_bajo_stock(15)
# Revisa stock de "pan" = 20
# ¿20 < 15? F -> No se añade a la lista
# Retorna: []
# Imprime: []


#20.Clase AnalizadorPatrones que: (1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista; 
#(2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}; 
#(3) tenga método palabras_unicas() usando un conjunto.
class AnalizadorPatrones:

    def __init__(self):
        self.palabras = []

    def encontrar_palabras(self, texto, patron):

        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):

        palabras = texto.split()
        grupos = {}

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in grupos:
                grupos[longitud] = []

            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self):

        return set(self.palabras)


ap = AnalizadorPatrones()

print(ap.encontrar_palabras("el gato está aquí", "el"))
print(ap.agrupar_por_longitud("el gato está aquí"))

# Bosquejo a mano
#
# Llamada 1: ap.encontrar_palabras("el gato está aquí", "el")
# palabras = ["el", "gato", "está", "aquí"]
#
# Evalúa inicio con "el":
# - "el".startswith("el") -> True -> resultado = ["el"]
# - "gato".startswith("el") -> False
# - "está".startswith("el") -> False
# - "aquí".startswith("el") -> False
#
# Imprime: ['el']
#
# Llamada 2: ap.agrupar_por_longitud("el gato está aquí")
# palabras = ["el", "gato", "está", "aquí"]
#
# Medir longitudes:
# - "el": len = 2    -> grupos[2] = ["el"]
# - "gato": len = 4  -> grupos[4] = ["gato"]
# - "está": len = 4  -> grupos[4] = ["gato", "está"]
# - "aquí": len = 4  -> grupos[4] = ["gato", "está", "aquí"]
#
# Imprime: {2: ['el'], 4: ['gato', 'está', 'aquí']}