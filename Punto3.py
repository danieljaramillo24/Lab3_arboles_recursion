
from Punto2 import GestorAportes

""" 

**Punto 3 (30%)**
Implemente una solución recursiva en Python para el siguiente problema

* Realice un algoritmo que permita insertar en un arbol binario,  el dinero recolectado por juan (en el punto 3, limite el tamaño de la lista a 25 elementos)

* implemente una función que permita buscar entre los elementos del árbol, los aportes que realizo uno cualqueira de los benefactores  y  conocer cuanto fue el total aportado por dicho benefactor.

Supuestos:

Nos piden conocer el total de aportes realizados por un beneficiario específico, recorriendo un árbol binario.

Por lo tanto, no se utilizan los métodos definidos en el gestor de aportes, sino que se crea un árbol binario para almacenar los aportes de cada beneficiario.

Por el contrario, si se puede extender la funcionalidad del árbol para que pueda recibir aportes generados por el gestor, y poderlos agregar al arbol se extiende la clase ya que es clave generar los aportes aleatorios.

- CUIDADO, no se HEREDA el atributo self.aportes directamente del GestorAportes dado que el número de aportes es máximo 25 como lo solicita el ejecicio. Por lo que se prefiere extender la instancia del gestor y no heredar su atributo directamente (valga la redundancia).
"""

class NodoAporte:
    """
    Representa un nodo en un árbol binario que almacena información de aportes monetarios.

    Cada nodo contiene el nombre del benefactor, el monto total de su aporte, y referencias
    a sus hijos izquierdo y derecho, lo cual permite mantener el árbol ordenado
    alfabéticamente por nombre.

    Atributos:
        nombre (str): Nombre del benefactor (clave de ordenamiento).
        monto (int): Monto total acumulado aportado por el benefactor.
        izquierda (NodoAporte | None): Hijo izquierdo del nodo.
        derecha (NodoAporte | None): Hijo derecho del nodo.
    """

    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto
        self.izquierda = None
        self.derecha = None


class ArbolAportes:
    """
    Esta clase se encarga de organizar los aportes realizados por distintos beneficiarios
    dentro de un árbol binario. Cada nodo representa un beneficiario, y si un nombre se repite,
    se acumula el aporte en lugar de crear otro nodo.

    El árbol se ordena alfabéticamente por nombre del benefactor.
    """

    def __init__(self):
        # Inicialmente el árbol está vacío
        self.raiz = None

    def insertar(self, nombre: str, monto: int):
        """
        Inserta un nuevo aporte en el árbol. Si el nombre ya existe, acumula el monto.
        """
        self.raiz = self._insertar_nodo_recursivo(self.raiz, nombre, monto)

    def _insertar_nodo_recursivo(self, nodo, nombre, monto):
        """
        Función auxiliar recursiva que busca el lugar correcto para insertar un nuevo nodo,
        o acumula el monto si el beneficiario ya está en el árbol.
        """
        # Caso base: si llegamos a una rama vacía, insertamos el nuevo nodo aquí
        if nodo is None:
            return NodoAporte(nombre, monto)

        # Si el nombre ya está, sumamos el monto al existente
        if nombre == nodo.nombre:
            nodo.monto += monto
        # Si el nombre va antes (alfabéticamente), vamos a la izquierda
        elif nombre < nodo.nombre:
            nodo.izquierda = self._insertar_nodo_recursivo(
                nodo.izquierda, nombre, monto
            )
        # Si va después, lo mandamos a la derecha
        else:
            nodo.derecha = self._insertar_nodo_recursivo(nodo.derecha, nombre, monto)

        return nodo  # Devolvemos el nodo actualizado

    def total_por_clave(self, clave: str) -> int:
        """
        Devuelve el total aportado por una persona en específico, usando búsqueda recursiva.

        Args:
            clave (str): Nombre del benefactor a buscar.
        """
        return self._buscar_total(self.raiz, clave)

    def _buscar_total(self, nodo, clave):
        """
        Función recursiva que busca el nodo por nombre y devuelve su monto.
        Si no lo encuentra, devuelve 0.
        """
        # Si llegamos al final sin encontrarlo, no aportó nada
        if nodo is None:
            return 0

        # Si encontramos la clave, devolvemos el monto acumulado
        if nodo.nombre == clave:
            return nodo.monto
        # Si la clave es menor, seguimos buscando por la izquierda
        elif clave < nodo.nombre:
            return self._buscar_total(nodo.izquierda, clave)
        # Si es mayor, vamos por la derecha
        else:
            return self._buscar_total(nodo.derecha, clave)


class NodoAporte:
    """
    Nodo que representa un único aporte en un árbol binario, ordenado por monto.
    """

    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto
        self.izquierda = None
        self.derecha = None


class ArbolAportes:
    """
    Árbol binario que almacena individualmente cada aporte ordenado por su monto.
    Permite insertar aportes y calcular el total aportado por cualquier persona.
    """

    def __init__(self):
        self.raiz = None

    def insertar(self, nombre: str, monto: int):
        """Inserta un nuevo aporte individual al árbol."""
        self.raiz = self._insertar_nodo_recursivo(self.raiz, nombre, monto)

    def _insertar_nodo_recursivo(self, nodo, nombre, monto):
        """
        Esta función se encarga de insertar un nuevo aporte dentro del árbol.

        Cada vez que se llama, compara el monto del nuevo aporte con el del nodo actual y 
        decide si va a la izquierda o a la derecha. Se crea un nuevo nodo para cada aporte.

        Args:
            nodo: nodo actual donde estamos parados en el árbol.
            nombre: nombre de la persona que hizo el aporte.
            monto: valor que aportó esa persona.

        Returns:
            El nodo actualizado (puede ser uno nuevo si estaba vacío).
        """

        # Si no hay nada en esta posición, creamos un nuevo nodo y lo devolvemos
        if nodo is None:
            return NodoAporte(nombre, monto)

        # Si el monto es menor o igual al del nodo actual, bajamos por la izquierda
        if monto <= nodo.monto:
            nodo.izquierda = self._insertar_nodo_recursivo(nodo.izquierda, nombre, monto)
        else:
            # Si es mayor, bajamos por la derecha
            nodo.derecha = self._insertar_nodo_recursivo(nodo.derecha, nombre, monto)

        # Retornamos el nodo actual para que siga encajando en el árbol
        return nodo


    def total_por_clave(self, clave: str) -> int:
        """Calcula la suma total de los aportes realizados por el beneficiario dado."""
        return self._sumar_aportes(self.raiz, clave)

    def _sumar_aportes(self, nodo, clave):
        """Función recursiva que suma los aportes de un beneficiario específico.

        Args:
            nodo (NodoAporte | None): Nodo actual del árbol.
            clave (str): Nombre del beneficiario a buscar.

        Returns:
            int: Suma total de los aportes del beneficiario.
        """
        if nodo is None:
            return 0

        suma_acumulada_actual = nodo.monto if nodo.nombre == clave else 0
        suma_izquierda = self._sumar_aportes(nodo.izquierda, clave)
        suma_derecha = self._sumar_aportes(nodo.derecha, clave)

        # Suma el monto actual con los aportes de los subárboles izquierdo y derecho
        suma_actual_total = suma_acumulada_actual + suma_izquierda + suma_derecha
        return suma_actual_total
    

    def procesar_desde_gestor(self, gestor: GestorAportes):
        """Carga todos los aportes individuales desde el gestor al árbol."""
        for nombre, monto in gestor.aportes:
            self.insertar(nombre, monto)

    def imprimir_totales_x_beneficio(self, clave: str, gestor: GestorAportes) -> None:
        """
        Este método recibe un gestor de aportes y construye el árbol con sus datos.
        Luego muestra en pantalla cuánto aportó la persona indicada en 'clave'.

        Args:
            clave (str): Nombre del benefactor que queremos consultar.
            gestor (GestorAportes): Objeto que contiene todos los aportes generados.
        """
        try:
            # Insertamos cada aporte en el árbol
            for nombre, monto in gestor.aportes:
                self.insertar(nombre, monto)

            # Si la clave está entre los posibles beneficiarios, mostramos el total
            if clave in gestor.BENEFICIARIOS:
                total = self.total_por_clave(clave)
                print(f"Total aportado por {clave}: ${total:,}")
            else:
                # Si no está registrado, lo informamos
                print(f"No se encontraron aportes para {clave}.")

        except AttributeError as ae:
            print(f"AttributeError: verifique que el gestor tenga la lista 'aportes' y el atributo 'BENEFICIARIOS'.\nDetalle: {ae}")

        except TypeError as te:
            print(f"TypeError: asegúrese de que los aportes sean tuplas (str, int).\nDetalle: {te}")



if __name__ == "__main__":
    # Crear gestor y generar aportes
    gestor = GestorAportes()
    gestor.generar_aportes(cantidad=25, minimo=10000, maximo=1000000)

    # Crear árbol e insertar aportes del gestor
    arbol = ArbolAportes()
    arbol.procesar_desde_gestor(gestor)

    # Consultar e imprimir aportes por beneficiario
    arbol.imprimir_totales_x_beneficio(clave="Juan", gestor=gestor)
    arbol.imprimir_totales_x_beneficio(clave="Mamá", gestor=gestor)
    arbol.imprimir_totales_x_beneficio(clave="Papá", gestor=gestor)
    arbol.imprimir_totales_x_beneficio(clave="Hermano", gestor=gestor)

    # Beneficiario no existente
    arbol.imprimir_totales_x_beneficio(clave="Carlos", gestor=gestor)

