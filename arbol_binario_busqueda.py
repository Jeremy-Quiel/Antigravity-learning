from typing import List, Optional


class Knoten:
    """Repräsentiert einen einzelnen Knoten in einem binären Suchbaum.

    Jeder Knoten speichert einen ganzzahligen Wert sowie Verweise auf sein
    linkes und rechtes Kind. Ein fehlendes Kind wird durch ``None`` dargestellt.
    """

    def __init__(self, wert: int):
        """Initialisiert einen Knoten mit einem ganzzahligen Wert.

        :param wert: Der zu speichernde ganzzahlige Wert.
        """
        self.wert: int = wert
        self.links: Optional["Knoten"] = None
        self.rechts: Optional["Knoten"] = None

    def __repr__(self) -> str:
        """Gibt eine lesbare Zeichenkettendarstellung des Knotens zurück."""
        return f"Knoten({self.wert})"


class BinaererSuchbaum:
    """Implementierung eines binären Suchbaums für ganzzahlige Werte."""

    def __init__(self):
        """Erstellt einen leeren binären Suchbaum ohne Wurzelknoten."""
        self.wurzel: Optional[Knoten] = None

    # =========================================================================
    # EINFÜGEN
    # =========================================================================
    def einfuegen(self, wert: int) -> None:
        """Fügt einen neuen ganzzahligen Wert in den Baum ein.

        Falls der Wert bereits existiert, wird er nicht erneut eingefügt.
        :param wert: Der einzufügende ganzzahlige Wert.
        :raises TypeError: Wenn der Wert keine ganze Zahl ist.
        """
        if not isinstance(wert, int):
            raise TypeError("Der Wert muss eine ganze Zahl sein.")

        if self.wurzel is None:
            self.wurzel = Knoten(wert)
        else:
            self._einfuegen_rekursiv(self.wurzel, wert)

    def _einfuegen_rekursiv(self, aktuell: Knoten, wert: int) -> None:
        """Platziert einen Wert rekursiv gemäß den Regeln des binären Suchbaums.

        :param aktuell: Der aktuell betrachtete Knoten.
        :param wert: Der einzufügende Wert.
        """
        if wert < aktuell.wert:
            # Kleinere Werte gehören in den linken Teilbaum
            if aktuell.links is None:
                aktuell.links = Knoten(wert)
            else:
                self._einfuegen_rekursiv(aktuell.links, wert)
        elif wert > aktuell.wert:
            # Größere Werte gehören in den rechten Teilbaum
            if aktuell.rechts is None:
                aktuell.rechts = Knoten(wert)
            else:
                self._einfuegen_rekursiv(aktuell.rechts, wert)
        else:
            # Duplikate werden ignoriert, um eindeutige Werte beizubehalten
            pass

    # =========================================================================
    # SUCHEN
    # =========================================================================
    def suchen(self, wert: int) -> Optional[Knoten]:
        """Sucht nach einem Wert und gibt den Knoten zurück oder ``None``.

        :param wert: Der gesuchte ganzzahlige Wert.
        :return: Der gefundene Knoten oder None.
        :raises TypeError: Wenn der gesuchte Wert keine ganze Zahl ist.
        """
        if not isinstance(wert, int):
            raise TypeError("Der zu suchende Wert muss eine ganze Zahl sein.")
        return self._suchen_rekursiv(self.wurzel, wert)

    def _suchen_rekursiv(self, aktuell: Optional[Knoten], wert: int) -> Optional[Knoten]:
        """Durchsucht den Baum rekursiv durch Ausschluss des unzutreffenden Teilbaums.

        :param aktuell: Der aktuell untersuchte Knoten.
        :param wert: Der gesuchte Wert.
        :return: Der passende Knoten oder None.
        """
        if aktuell is None or aktuell.wert == wert:
            return aktuell

        if wert < aktuell.wert:
            return self._suchen_rekursiv(aktuell.links, wert)
        return self._suchen_rekursiv(aktuell.rechts, wert)

    def enthaelt(self, wert: int) -> bool:
        """Prüft, ob ein Wert im Baum vorhanden ist.

        :param wert: Der zu überprüfende Wert.
        :return: True, wenn der Wert vorhanden ist, andernfalls False.
        """
        return self.suchen(wert) is not None

    # =========================================================================
    # LÖSCHEN
    # =========================================================================
    def loeschen(self, wert: int) -> None:
        """Entfernt einen ganzzahligen Wert aus dem Baum, falls vorhanden.

        :param wert: Der zu entfernende ganzzahlige Wert.
        :raises TypeError: Wenn der zu löschende Wert keine ganze Zahl ist.
        """
        if not isinstance(wert, int):
            raise TypeError("Der zu löschende Wert muss eine ganze Zahl sein.")
        self.wurzel = self._loeschen_rekursiv(self.wurzel, wert)

    def _loeschen_rekursiv(self, aktuell: Optional[Knoten], wert: int) -> Optional[Knoten]:
        """Löscht einen Wert rekursiv und aktualisiert die Baumstruktur.

        :param aktuell: Der Wurzelknoten des aktuellen Teilbaums.
        :param wert: Der zu löschende Wert.
        :return: Der neue Wurzelknoten des Teilbaums nach dem Löschvorgang.
        """
        if aktuell is None:
            return None

        # Navigation zum Zielknoten anhand der Suchbaumeigenschaft
        if wert < aktuell.wert:
            aktuell.links = self._loeschen_rekursiv(aktuell.links, wert)
        elif wert > aktuell.wert:
            aktuell.rechts = self._loeschen_rekursiv(aktuell.rechts, wert)
        else:
            # Der zu löschende Knoten wurde gefunden

            # Fall 1: Knoten hat keine Kinder (Blattknoten)
            if aktuell.links is None and aktuell.rechts is None:
                return None

            # Fall 2: Knoten hat genau ein Kind
            if aktuell.links is None:
                return aktuell.rechts
            elif aktuell.rechts is None:
                return aktuell.links

            # Fall 3: Knoten hat zwei Kinder
            # Finde den Inorder-Nachfolger (kleinster Knoten im rechten Teilbaum)
            nachfolger = self._minimum_ermitteln(aktuell.rechts)
            aktuell.wert = nachfolger.wert
            # Lösche den Nachfolger-Knoten aus dem rechten Teilbaum
            aktuell.rechts = self._loeschen_rekursiv(aktuell.rechts, nachfolger.wert)

        return aktuell

    def _minimum_ermitteln(self, knoten: Knoten) -> Knoten:
        """Ermittelt den Knoten mit dem kleinsten Wert in einem Teilbaum.

        :param knoten: Der Startknoten für die Suche nach dem Minimum.
        :return: Der Knoten mit dem kleinsten Wert.
        """
        aktuell = knoten
        while aktuell.links is not None:
            aktuell = aktuell.links
        return aktuell

    # =========================================================================
    # INORDER-TRAVERSIERUNG
    # =========================================================================
    def inorder(self) -> List[int]:
        """Gibt alle Werte des Baums in aufsteigender Reihenfolge zurück.

        :return: Liste aller ganzzahligen Werte sortiert.
        """
        elemente: List[int] = []
        self._inorder_rekursiv(self.wurzel, elemente)
        return elemente

    def _inorder_rekursiv(
        self, aktuell: Optional[Knoten], elemente: List[int]
    ) -> None:
        """Fügt Werte rekursiv in der Reihenfolge Links-Wurzel-Rechts hinzu.

        :param aktuell: Der aktuell besuchte Knoten.
        :param elemente: Die Zielliste für die sortierten Werte.
        """
        if aktuell is not None:
            self._inorder_rekursiv(aktuell.links, elemente)
            elemente.append(aktuell.wert)
            self._inorder_rekursiv(aktuell.rechts, elemente)


# =============================================================================
# ANWENDUNGSBEISPIEL UND TESTS
# =============================================================================
if __name__ == "__main__":
    baum = BinaererSuchbaum()

    print("=== Werte einfügen ===")
    werte = [50, 30, 70, 20, 40, 60, 80]
    for wert in werte:
        baum.einfuegen(wert)
    print(f"Eingefügte Werte: {werte}")
    print(f"Inorder-Traversierung (sortiert): {baum.inorder()}")

    print("\n=== Nach Werten suchen ===")
    for wert in [40, 99]:
        ergebnis = baum.suchen(wert)
        if ergebnis:
            print(f"Wert {wert} gefunden in Knoten: {ergebnis}")
        else:
            print(f"Wert {wert} nicht im Baum gefunden.")

    print("\n=== Werte löschen ===")
    print("1. Blattknoten löschen (20)...")
    baum.loeschen(20)
    print(f"Aktuelle Inorder-Traversierung: {baum.inorder()}")

    print("2. Knoten mit einem Kind löschen (30)...")
    baum.loeschen(30)
    print(f"Aktuelle Inorder-Traversierung: {baum.inorder()}")

    print("3. Knoten mit zwei Kindern löschen (Wurzel: 50)...")
    baum.loeschen(50)
    print(f"Aktuelle Inorder-Traversierung: {baum.inorder()}")
