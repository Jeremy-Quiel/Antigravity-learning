from typing import Optional, List


class Nodo:
    """Representa un nodo en el árbol binario de búsqueda."""

    def __init__(self, valor: int):
        self.valor: int = valor
        self.izquierda: Optional["Nodo"] = None
        self.derecha: Optional["Nodo"] = None

    def __repr__(self) -> str:
        return f"Nodo({self.valor})"


class ArbolBinarioBusqueda:
    """Implementación de un Árbol Binario de Búsqueda (BST)."""

    def __init__(self):
        self.raiz: Optional[Nodo] = None

    # =========================================================================
    # MÉTODO METER
    # =========================================================================
    def meter(self, valor: int) -> None:
        """Inserta/mete un nuevo valor entero en el árbol."""
        if not isinstance(valor, int):
            raise TypeError("El valor debe ser un número entero.")

        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._meter_recursivo(self.raiz, valor)

    def _meter_recursivo(self, actual: Nodo, valor: int) -> None:
        if valor < actual.valor:
            if actual.izquierda is None:
                actual.izquierda = Nodo(valor)
            else:
                self._meter_recursivo(actual.izquierda, valor)
        elif valor > actual.valor:
            if actual.derecha is None:
                actual.derecha = Nodo(valor)
            else:
                self._meter_recursivo(actual.derecha, valor)
        else:
            # Si el valor ya existe, no se duplica (o se puede omitir/ignorar)
            pass

    # =========================================================================
    # MÉTODO BUSCAR
    # =========================================================================
    def buscar(self, valor: int) -> Optional[Nodo]:
        """
        Busca un valor en el árbol.
        Retorna el Nodo correspondiente si se encuentra, o None si no existe.
        """
        if not isinstance(valor, int):
            raise TypeError("El valor a buscar debe ser un número entero.")
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, actual: Optional[Nodo], valor: int) -> Optional[Nodo]:
        if actual is None or actual.valor == valor:
            return actual

        if valor < actual.valor:
            return self._buscar_recursivo(actual.izquierda, valor)
        return self._buscar_recursivo(actual.derecha, valor)

    def contiene(self, valor: int) -> bool:
        """Verifica si un valor existe en el árbol retornando True o False."""
        return self.buscar(valor) is not None

    # =========================================================================
    # MÉTODO ELIMINAR
    # =========================================================================
    def eliminar(self, valor: int) -> None:
        """Elimina un valor entero del árbol."""
        if not isinstance(valor, int):
            raise TypeError("El valor a eliminar debe ser un número entero.")
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, actual: Optional[Nodo], valor: int) -> Optional[Nodo]:
        if actual is None:
            return None

        # 1. Navegar por el árbol
        if valor < actual.valor:
            actual.izquierda = self._eliminar_recursivo(actual.izquierda, valor)
        elif valor > actual.valor:
            actual.derecha = self._eliminar_recursivo(actual.derecha, valor)
        else:
            # Encontramos el nodo a eliminar

            # Caso 1: Nodo sin hijos (nodo hoja)
            if actual.izquierda is None and actual.derecha is None:
                return None

            # Caso 2: Nodo con un solo hijo
            if actual.izquierda is None:
                return actual.derecha
            elif actual.derecha is None:
                return actual.izquierda

            # Caso 3: Nodo con dos hijos
            # Encontrar el sucesor en inorden (nodo con el menor valor en el subárbol derecho)
            sucesor = self._obtener_minimo(actual.derecha)
            actual.valor = sucesor.valor
            # Eliminar el sucesor del subárbol derecho
            actual.derecha = self._eliminar_recursivo(actual.derecha, sucesor.valor)

        return actual

    def _obtener_minimo(self, nodo: Nodo) -> Nodo:
        """Encuentra el nodo con el valor mínimo a partir de un nodo dado."""
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    # =========================================================================
    # RECORRIDO AUXILIAR PARA PRUEBAS
    # =========================================================================
    def inorden(self) -> List[int]:
        """Retorna una lista con los elementos ordenados de menor a mayor."""
        elementos: List[int] = []
        self._inorden_recursivo(self.raiz, elementos)
        return elementos

    def _inorden_recursivo(self, actual: Optional[Nodo], elementos: List[int]) -> None:
        if actual is not None:
            self._inorden_recursivo(actual.izquierda, elementos)
            elementos.append(actual.valor)
            self._inorden_recursivo(actual.derecha, elementos)


# =============================================================================
# EJEMPLO DE USO Y PRUEBAS
# =============================================================================
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()

    print("=== Metiendo valores ===")
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arbol.meter(v)
    print(f"Valores metidos: {valores}")
    print(f"Recorrido In-Order (ordenado): {arbol.inorden()}")

    print("\n=== Buscando valores ===")
    for v in [40, 99]:
        resultado = arbol.buscar(v)
        if resultado:
            print(f"Valor {v} encontrado en el nodo: {resultado}")
        else:
            print(f"Valor {v} no encontrado en el árbol.")

    print("\n=== Eliminando valores ===")
    print("1. Eliminando nodo hoja (20)...")
    arbol.eliminar(20)
    print(f"In-Order actual: {arbol.inorden()}")

    print("2. Eliminando nodo con un solo hijo (30)...")
    arbol.eliminar(30)
    print(f"In-Order actual: {arbol.inorden()}")

    print("3. Eliminando nodo con dos hijos (raíz: 50)...")
    arbol.eliminar(50)
    print(f"In-Order actual: {arbol.inorden()}")

