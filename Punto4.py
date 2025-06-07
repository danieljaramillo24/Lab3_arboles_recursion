"""
Punto 4: Implementa una agenda de contactos usando un árbol binario de búsqueda.
Cada contacto se guarda ordenadamente por nombre, permitiendo insertar, eliminar y listar.

Supuestos: 
- Los nombres de los contactos son únicos.
- Los números de teléfono son cadenas de texto.
- El árbol se mantiene ordenado alfabéticamente por el nombre del contacto.
- Utilizamos métodos nativos de python __str__ , __eq__  y __lt__ para definir la representación y comparación de los contactos.

- El ordando alfabetico se define por el método __lt__ de la clase Contacto. Es decir, vamos a usar la convencion de Python para comparar cadenas. Utilizando el orden de los caracteres Unicode. No se toma en cuenta la cantidad de caracteres, sino el orden de los caracteres en la cadena.

Ejmplo: 
    Supongamos que tenemos los siguientes contactos:
    - "Ana" con teléfono "123456789"
    - "Alvaro" con teléfono "987654321"
    
    Bajo la convención de python:
    Primer caracter de "Ana"  y "Alvaro es 'A' = (Unicode 65), sin embargo el segundo es 'n' (Unicode 110) y 'l' (Unicode 108), por lo que "Alvaro" es menor que "Ana" en el orden alfabético."""


class Contacto:
    """
    Representa un contacto con nombre y número de teléfono.

    Atributos:
        nombre (str): Nombre del contacto.
        telefono (str): Número de teléfono del contacto.

    Métodos:
        __lt__: Permite comparar dos contactos usando su nombre (menor que).
        __eq__: Permite determinar si dos contactos tienen el mismo nombre.
        __str__: Devuelve una representación legible del contacto.
    """
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __lt__(self, otro):
        """
        Permite comparar contactos por orden alfabético del nombre.

        Returns:
            bool: True si este contacto es "menor" al otro según su nombre.
        """
        return self.nombre < otro.nombre

    def __eq__(self, otro):
        """
        Permite comparar si dos contactos tienen el mismo nombre.

        Returns:
            bool: True si los nombres de ambos contactos son iguales.
        """
        return self.nombre == otro.nombre

    def __str__(self):
        """
        Representación del contacto, actualización de nuestro print().

        Returns:
            str: Cadena con el formato "Nombre: Teléfono"
        """
        return "{}: {}".format(self.nombre, self.telefono)


class Nodo:
    """
    Clase que representa un nodo en un árbol binario de búsqueda.

    Atributos:
        valor (Contacto): Contacto almacenado en el nodo.
        izquierda (Nodo | None): Hijo izquierdo.
        derecha (Nodo | None): Hijo derecho.
    """
    def __init__(self, valor, ):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolAgenda:
    """
    Árbol binario de búsqueda para manejar contactos.
    Los contactos se ordenan alfabéticamente por nombre.
    """
    def __init__(self):
        """Inicializa un árbol vacío."""
        self.raiz = None

    def esta_vacio(self):
        """Verifica si el árbol está vacío."""
        return self.raiz is None

    def insertar(self, nombre, telefono):
        """
        Inserta un nuevo contacto en el árbol.

        Args:
            nombre (str): Nombre del contacto.
            telefono (str): Número de teléfono.
        """
        nuevo_contacto = Contacto(nombre, telefono)
        self.raiz = self._insertar_recursivo(self.raiz, nuevo_contacto)

    def _insertar_recursivo(self, nodo, contacto):
        """
        Inserta recursivamente un contacto en el árbol.

        Args:
            nodo (Nodo): Nodo actual.
            contacto (Contacto): Contacto a insertar.

        Returns:
            Nodo: Nodo actualizado.
        """
        if nodo is None:
            return Nodo(contacto)

        if contacto < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, contacto)
        elif contacto > nodo.valor:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, contacto)
        else:
            print("El contacto {} ya existe. No se insertó".format(contacto.nombre))

        return nodo

    def eliminar(self, nombre):
        """
        Elimina un contacto del árbol por nombre.

        Args:
            nombre (str): Nombre del contacto a eliminar.
        """
        self.raiz = self._eliminar_recursivo(self.raiz, nombre)

    def _eliminar_recursivo(self, nodo, nombre):
            """
            Elimina recursivamente un contacto del árbol.

            Este método recorre el árbol desde el nodo dado, comparando el nombre a eliminar con
            los valores del árbol. Dependiendo de la ubicación y los hijos del nodo, se aplican
            distintas reglas para eliminarlo:

            - Si no se encuentra el nodo (nodo es None), se retorna None.
            - Si el nombre buscado es menor, se sigue por la izquierda.
            - Si es mayor, se sigue por la derecha.
            - Si el nombre coincide:
                - Si el nodo no tiene hijos, se elimina devolviendo None.
                - Si tiene un solo hijo, se reemplaza por ese hijo.
                - Si tiene dos hijos:
                    - Se busca el sucesor inorden (mínimo del subárbol derecho).
                    - Se reemplaza el valor actual por el del sucesor.
                    - Se elimina recursivamente el sucesor desde el subárbol derecho.

            Args:
                nodo (Nodo): Nodo actual desde donde buscar y eliminar.
                nombre (str): Nombre del contacto a eliminar.

            Returns:
                Nodo: Nodo actualizado después de la eliminación.
            """
            if nodo is None:
                print("El contacto '{}' no fue encontrado en el arbol.".format(nombre))
                return None

            if nombre < nodo.valor.nombre:
                nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, nombre)
            elif nombre > nodo.valor.nombre:
                nodo.derecha = self._eliminar_recursivo(nodo.derecha, nombre)
            else:
                # Caso 1: el nodo es una hoja (sin hijos)
                if nodo.izquierda is None and nodo.derecha is None:
                    return None
                # Caso 2: el nodo tiene solo hijo derecho
                elif nodo.izquierda is None:
                    return nodo.derecha
                # Caso 3: el nodo tiene solo hijo izquierdo
                elif nodo.derecha is None:
                    return nodo.izquierda
                # Caso 4: el nodo tiene dos hijos
                else:
                    sucesor = self._minimo(nodo.derecha)  # encontrar el nodo más pequeño del subárbol derecho
                    nodo.valor = sucesor.valor  # reemplazar el valor actual por el del sucesor
                    nodo.derecha = self._eliminar_recursivo(nodo.derecha, sucesor.valor.nombre)  # eliminar el sucesor

            return nodo

    def _minimo(self, nodo):
        """
        Encuentra el nodo con el valor mínimo en el subárbol.

        Args:
            nodo (Nodo): Nodo raíz del subárbol.

        Returns:
            Nodo: Nodo con el valor mínimo.
        """
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def listar_contactos(self):
        """Lista todos los contactos en orden alfabético."""
        self._inorden(self.raiz)

    def _inorden(self, nodo):
        """
        Recorrido inorden para imprimir contactos ordenados.

        Args:
            nodo (Nodo): Nodo actual.
        """
        if nodo:
            self._inorden(nodo.izquierda)
            print(nodo.valor)
            self._inorden(nodo.derecha)


if __name__ == "__main__":
    # Crear instancia del árbol agenda
    agenda = ArbolAgenda()

    # Insertar algunos contactos
    agenda.insertar("Cielo", "3214567890")
    agenda.insertar("Ana", "3001234567")
    agenda.insertar("Alvaro", "3001234567")
    agenda.insertar("Diana", "3209876543")
    agenda.insertar("Beatriz", "3119876543")
    agenda.insertar("Daniel", "3103332211")
    agenda.insertar("Camila", "3501122334")

    print("\n Lista de contactos (ordenados alfabéticamente):")
    agenda.listar_contactos()

    # Intentar insertar un contacto duplicado
    agenda.insertar("Ana", "3001234567")

    # Eliminar un contacto que existe
    print("\n Eliminando contacto 'Beatriz':")
    agenda.eliminar("Beatriz")

    print("\n Lista actualizada de contactos:")
    agenda.listar_contactos()

    # Eliminar un contacto que no existe
    print("\n Intentando eliminar contacto 'Ximena' (no existe):")
    agenda.eliminar("Ximena")

    # Eliminar un nodo con dos hijos
    print("\n Eliminando contacto 'Cielo' (tiene dos hijos):")
    agenda.eliminar("Cielo")

    print("\n Lista final de contactos:")
    agenda.listar_contactos()
