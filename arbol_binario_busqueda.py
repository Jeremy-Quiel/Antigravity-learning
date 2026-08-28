from typing import List, Optional


class Nodo:
    """Representa un nodo individual en un árbol binario de búsqueda.

    Cada nodo almacena un valor entero, así como referencias a sus nodos hijos
    izquierdo y derecho. La ausencia de un nodo hijo se representa con ``None``.
    """

    def __init__(self, valor: int):
        """Inicializa un nodo con un valor entero.

        :param valor: El valor entero que se almacenará en el nodo.
        """
        self.valor: int = valor
        self.izquierdo: Optional["Nodo"] = None
        self.derecho: Optional["Nodo"] = None

    def __repr__(self) -> str:
        """Devuelve una representación legible en cadena de texto del nodo."""
        return f"Nodo({self.valor})"


class ArbolBinarioBusqueda:
    """Implementación de un árbol binario de búsqueda para valores enteros."""

    def __init__(self):
        """Inicializa un árbol binario de búsqueda vacío sin nodo raíz."""
        self.raiz: Optional[Nodo] = None

    # =========================================================================
    # INSERCIÓN
    # =========================================================================
    def insertar(self, valor: int) -> None:
        """Inserta un nuevo valor entero en el árbol.

        Si el valor ya existe en el árbol, no se vuelve a insertar.
        :param valor: El valor entero a insertar.
        :raises TypeError: Si el valor no es un número entero.
        """
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un número entero.")

        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, actual: Nodo, valor: int) -> None:
        """Ubica un valor de forma recursiva según las reglas del árbol binario de búsqueda.

        :param actual: El nodo que se está evaluando actualmente.
        :param valor: El valor a insertar.
        """
        if valor < actual.valor:
            # Los valores menores pertenecen al subárbol izquierdo
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(actual.izquierdo, valor)
        elif valor > actual.valor:
            # Los valores mayores pertenecen al subárbol derecho
            if actual.derecho is None:
                actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(actual.derecho, valor)
        else:
            # Se ignoran los valores duplicados para mantener elementos únicos
            pass

    # =========================================================================
    # BÚSQUEDA
    # =========================================================================
    def buscar(self, valor: int) -> Optional[Nodo]:
        """Busca un valor y devuelve el nodo correspondiente o ``None``.

        :param valor: El valor entero buscado.
        :return: El nodo encontrado o None si no existe.
        :raises TypeError: Si el valor buscado no es un número entero.
        """
        if not isinstance(valor, int):
            raise TypeError("El valor a buscar debe ser un número entero.")
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, actual: Optional[Nodo], valor: int) -> Optional[Nodo]:
        """Busca en el árbol de forma recursiva descartando el subárbol no correspondiente.

        :param actual: El nodo examinado actualmente.
        :param valor: El valor buscado.
        :return: El nodo coincidente o None.
        """
        if actual is None or actual.valor == valor:
            return actual

        if valor < actual.valor:
            return self._buscar_recursivo(actual.izquierdo, valor)
        return self._buscar_recursivo(actual.derecho, valor)

    def contiene(self, valor: int) -> bool:
        """Comprueba si un valor existe dentro del árbol.

        :param valor: El valor a verificar.
        :return: True si el valor está presente; de lo contrario, False.
        """
        return self.buscar(valor) is not None

    # =========================================================================
    # ELIMINACIÓN
    # =========================================================================
    def eliminar(self, valor: int) -> None:
        """Elimina un valor entero del árbol, en caso de que exista.

        :param valor: El valor entero a eliminar.
        :raises TypeError: Si el valor a eliminar no es un número entero.
        """
        if not isinstance(valor, int):
            raise TypeError("El valor a eliminar debe ser un número entero.")
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, actual: Optional[Nodo], valor: int) -> Optional[Nodo]:
        """Elimina un valor de forma recursiva y actualiza la estructura del árbol.

        :param actual: El nodo raíz del subárbol actual.
        :param valor: El valor a eliminar.
        :return: La nueva raíz del subárbol tras la operación de eliminación.
        """
        if actual is None:
            return None

        # Navegación hacia el nodo destino según las propiedades del árbol de búsqueda
        if valor < actual.valor:
            actual.izquierdo = self._eliminar_recursivo(actual.izquierdo, valor)
        elif valor > actual.valor:
            actual.derecho = self._eliminar_recursivo(actual.derecho, valor)
        else:
            # Se ha encontrado el nodo a eliminar

            # Caso 1: El nodo no tiene hijos (nodo hoja)
            if actual.izquierdo is None and actual.derecho is None:
                return None

            # Caso 2: El nodo tiene exactamente un hijo
            if actual.izquierdo is None:
                return actual.derecho
            elif actual.derecho is None:
                return actual.izquierdo

            # Caso 3: El nodo tiene dos hijos
            # Encontrar el sucesor inorden (nodo con el valor mínimo en el subárbol derecho)
            sucesor = self._obtener_minimo(actual.derecho)
            actual.valor = sucesor.valor
            # Eliminar el nodo sucesor del subárbol derecho
            actual.derecho = self._eliminar_recursivo(actual.derecho, sucesor.valor)

        return actual

    def _obtener_minimo(self, nodo: Nodo) -> Nodo:
        """Obtiene el nodo con el valor más pequeño en un subárbol.

        :param nodo: El nodo inicial desde el cual buscar el valor mínimo.
        :return: El nodo con el valor mínimo encontrado.
        """
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    # =========================================================================
    # RECORRIDO INORDEN
    # =========================================================================
    def inorden(self) -> List[int]:
        """Devuelve todos los valores del árbol en orden ascendente.

        :return: Lista con todos los valores enteros ordenados.
        """
        elementos: List[int] = []
        self._inorden_recursivo(self.raiz, elementos)
        return elementos

    def _inorden_recursivo(
        self, actual: Optional[Nodo], elementos: List[int]
    ) -> None:
        """Agrega valores recursivamente siguiendo el orden Izquierda-Raíz-Derecha.

        :param actual: El nodo visitado actualmente.
        :param elementos: La lista destino para almacenar los valores ordenados.
        """
        if actual is not None:
            self._inorden_recursivo(actual.izquierdo, elementos)
            elementos.append(actual.valor)
            self._inorden_recursivo(actual.derecho, elementos)


# =============================================================================
# EJEMPLO DE USO Y PRUEBAS
# =============================================================================
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()

    print("=== Insertar valores ===")
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)
    print(f"Valores insertados: {valores}")
    print(f"Recorrido inorden (ordenado): {arbol.inorden()}")

    print("\n=== Buscar valores ===")
    for valor in [40, 99]:
        resultado = arbol.buscar(valor)
        if resultado:
            print(f"Valor {valor} encontrado en el nodo: {resultado}")
        else:
            print(f"Valor {valor} no encontrado en el árbol.")

    print("\n=== Eliminar valores ===")
    print("1. Eliminar nodo hoja (20)...")
    arbol.eliminar(20)
    print(f"Recorrido inorden actual: {arbol.inorden()}")

    print("2. Eliminar nodo con un hijo (30)...")
    arbol.eliminar(30)
    print(f"Recorrido inorden actual: {arbol.inorden()}")

    print("3. Eliminar nodo con dos hijos (raíz: 50)...")
    arbol.eliminar(50)
    print(f"Recorrido inorden actual: {arbol.inorden()}")
