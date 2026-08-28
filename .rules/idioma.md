# Reglas de Idioma y Comunicación

## 1. Propósito
Establecer las directivas de idioma oficial para garantizar la coherencia, claridad y accesibilidad en toda la comunicación, documentación técnica, comentarios de código y mensajes de control de versiones dentro del proyecto.

## 2. Alcance
Aplica a todas las interacciones de los agentes autónomos, redacción de archivos de documentación (`.md`), comentarios y *docstrings* en el código fuente, así como a los mensajes de *commit* en Git.

## 3. Reglas Principales

| Ámbito | Idioma Requerido | Directiva |
| :--- | :--- | :--- |
| **Respuestas y Comunicación** | Español | Toda interacción, explicación o reporte dirigido al usuario debe ser en español. |
| **Documentación Técnica** | Español | Manuales, archivos `README.md`, guías y reglas del proyecto deben redactarse en español. |
| **Comentarios y Docstrings** | Español | Toda explicación lógica interna, descripción de funciones y clases debe documentarse en español. |
| **Mensajes de Commit** | Español | Los mensajes de Git deben redactarse en español siguiendo el estándar de *Conventional Commits*. |
| **Nomenclatura de Código** | Español / Inglés técnico | Se permite el uso de términos técnicos estándar de la industria, manteniendo coherencia en cada módulo. |

## 4. Excepciones
* **Instrucciones Explícitas:** Cuando el usuario solicite de forma expresa un idioma o traducción específica en su consulta.
* **Términos Técnicos Universales:** Palabras clave de lenguajes de programación, nombres de librerías, comandos de terminal o identificadores de APIs de terceros no deben traducirse literalmente.

## 5. Ejemplos de Aplicación

### Documentación de Código
```python
def calcular_total(subtotal: float, impuesto: float) -> float:
    """
    Calcula el monto total aplicando el porcentaje de impuesto correspondiente.
    
    :param subtotal: Monto base antes de impuestos.
    :param impuesto: Tasa o valor del impuesto a aplicar.
    :return: Total final calculado.
    """
    # Sumar el impuesto al subtotal base
    return subtotal + impuesto
```

### Mensajes de Commit en Git
* `feat: agregar funcionalidad de busqueda binaria`
* `docs: actualizar documentacion en archivo README`
* `fix: corregir validacion de entrada numerica`
