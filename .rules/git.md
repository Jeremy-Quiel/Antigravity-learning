# Reglas de Control de Versiones y Git

## 1. Propósito
Garantizar la persistencia continua y la sincronización inmediata de cualquier cambio realizado en el código fuente, configuración o documentación del proyecto con el repositorio remoto en GitHub.

## 2. Alcance
Aplica a todos los agentes autónomos, desarrolladores y herramientas automatizadas que creen, editen o eliminen archivos en este espacio de trabajo.

## 3. Reglas Obligatorias
- **Confirmación Inmediata (Commit):** Cada vez que se realice un cambio en los archivos del proyecto, se debe registrar inmediatamente un *commit* con un mensaje claro y descriptivo.
- **Sincronización Remota (Push):** Todo *commit* generado debe enviarse (`git push`) de manera inmediata a la rama correspondiente en el repositorio de GitHub.
- **Atomicidad:** Cada modificación o conjunto de cambios relacionados debe confirmarse y sincronizarse de forma oportuna sin acumular cambios pendientes.

## 4. Creación de Ramas
- **Origen Obligatorio:** Toda nueva rama debe crearse exclusivamente a partir de la rama `main`.
- **Sincronización Previa:** Antes de crear cualquier rama, verifica que la rama `main` esté completamente actualizada con el remoto (`git pull origin main`).
- **Árbol Limpio:** Asegúrate de que no existan cambios locales sin commitear antes de iniciar la bifurcación.

```bash
# 1. Cambiar a main y actualizar con el remoto
git checkout main
git pull origin main

# 2. Verificar que no haya cambios pendientes
git status

# 3. Crear y cambiar a la nueva rama
git checkout -b <tipo>/<nombre-descriptivo>
```

## 5. Flujo de Ejecución Estándar
```bash
# 1. Preparar archivos modificados
git add .

# 2. Registrar el cambio con mensaje descriptivo
git commit -m "tipo: descripción concisa del cambio"

# 3. Sincronizar con el repositorio remoto
git push origin <rama_actual>
```