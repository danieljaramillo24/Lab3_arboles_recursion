
"""**Punto 2  (25%)**
* Resuleva con recursión binaria el siguiente problema
* Implemente la solución en python
* Pruebe la solución
* Analice si es posible implementar la solución con recursión Líneal.

Juan  este ahorrando dinero para viajar por europa en las próximas vacaciones.  EL ahorro de juan se vienen realizando hace un año y cuidadosamente a llevado regisro de cada aporte.
1.  Mamá  500.000
2.  Papá  600.000
3.  Hermano 10.000
4.  Mamá 20.000
.....
100  Juan  30.0000

Despues de 100 registros, juan desea saber cuando dinero tiene ahorrado.
NOTA: Use cualquier representación de lista para resolver el problema.

Supuestos: 

- No se conoce el rango de aportes, se dejan por defecto valores minimos y máximos, pero se permite al usuario definirlos.

- Se asume que los beneficiarios son fijos y conocidos, pero se pueden modificar si es necesario con el atributo `BENEFICIARIOS`. Constante de la clase.

- Se pide unicamente la suma total de los aportes de juan, se añade la funcionalidad para sumar aportes de cualquier beneficiario. Pero no se realiza un desglose de los aportes individuales al no ser solicitado.

- Se garantiza que los aportes son positivos, y el generador de aportes no disparará excepciones para el método estatico `suma_aportes_por_clave`. Sin embargo con independencia de la generación aleatoria de los aportes, el método estatico garantiza el manejo de errores en caso tal de contar con aportes predefinidos no validos. 
"""
import random
from typing import List, Tuple


class GestorAportes:
    BENEFICIARIOS = ["Juan", "Mamá", "Papá", "Hermano"]

    def __init__(self):
        self.aportes: List[Tuple[str, int]] = []
    
    def mostrar_total_aportes_por_clave(self, clave: str) -> int:
        """
        Devuelve la suma total de los aportes realizados por una clave específica.

        Args:
            clave (str): Nombre del benefactor a buscar.

        Returns:
            int: Total acumulado de la clave.
        """
        return self.suma_aportes_por_clave(self.aportes, clave)

    def generar_aportes(
        self, cantidad: int = 100, minimo: int = 10000, maximo: int = 500000
    ) -> None:
        """Genera aportes aleatorios para los beneficiarios disponibles.

        Crea una cantidad específica de aportes con montos aleatorios dentro del rango establecido, asignados a beneficiarios seleccionados al azar.

        Args:
            cantidad (int): Número de aportes a generar (por defecto 100)
            minimo (int): Valor mínimo para los montos (por defecto 10,000)
            maximo (int): Valor máximo para los montos (por defecto 500,000)

        Raises:
            ValueError: Si el mínimo es mayor que el máximo o son negativos
            AttributeError: Si no hay beneficiarios registrados
        """
        if minimo > maximo:
            raise ValueError("El monto mínimo no puede ser mayor al máximo")
        if minimo < 0 or maximo < 0:
            raise ValueError("Los montos deben ser valores positivos")

        self.aportes = [
            (random.choice(self.BENEFICIARIOS), random.randint(minimo, maximo))
            for _ in range(cantidad)
        ]
        # Usamos _ dentro del for como convención para indicar que no necesitamos el índice del bucle. Podemos ver que solo queremos repetir para todos los aportes así agregamos todos los beneficiarios y montos aleatorios. Pero no necesitamos el índice del ciclo for.

    @staticmethod
    def suma_aportes_por_clave(lista: List[Tuple[str, int]], clave: str) -> int:
        """
        Suma los valores asociados a una clave específica utilizando recursión binaria
        
        Args:
            lista (List[Tuple[str, int]]): Lista de tuplas con nombre y monto
            clave (str): Clave para la cual se sumarán los montos
        
        Raises:
            ValueError: Si la tupla no tiene exactamente dos elementos
            TypeError: Si uno de los valores no es del tipo esperado (str, int)
        
        Returns:
            int: Suma total de los montos asociados a la clave
        """
        try:
            if len(lista) == 0:
                return 0
            if len(lista) == 1:
                nombre, monto = lista[0]
                return monto if nombre == clave else 0

            medio = len(lista) // 2
            izquierda = GestorAportes.suma_aportes_por_clave(lista[:medio], clave)
            derecha = GestorAportes.suma_aportes_por_clave(lista[medio:], clave)
            return izquierda + derecha

        except ValueError as ve:
            print(
                f"ValueError: la tupla no tiene exactamente dos elementos.\nDetalle: {ve}"
            )
            return 0
        except TypeError as te:
            print(
                f"TypeError: uno de los valores no es del tipo esperado (str, int).\nDetalle: {te}"
            )
            return 0

if __name__ == "__main__":
    gestor = GestorAportes()
    gestor.generar_aportes(cantidad=100, minimo=10000, maximo=10**6)
    
    clave_buscada = "Juan"
    total = gestor.mostrar_total_aportes_por_clave(clave_buscada)
    print(f"Total de aportes para {clave_buscada}: {total}")
    
    clave_buscada = "Mamá"
    total = gestor.mostrar_total_aportes_por_clave(clave_buscada)
    print(f"Total de aportes para {clave_buscada}: {total}")
