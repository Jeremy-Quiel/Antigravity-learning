# Documentación de Modelos - Antigravity SDK

Este texto explica los modelos de Inteligencia Artificial que funcionan con la herramienta **Google Antigravity SDK**. El sistema está hecho para trabajar con agentes automáticos. Estos modelos ayudan a los agentes a pensar, usar herramientas, seguir reglas de seguridad y coordinar ayudantes.

## Procesamiento Rápido y Orquestación de Agentes (Baja Latencia)

Estos modelos dan respuestas rápidas, deciden con agilidad y controlan el trabajo de los agentes de inicio a fin.

### Gemini 3.7 Flash
* **Características Principales:** Es el modelo principal de Antigravity SDK desde mediados o finales de 2026. Está preparado para la base (*harness*) de Antigravity. Funciona con mucha rapidez al usar herramientas (Tool Calling) y al pedir ayuda a otros agentes.
* **Uso Recomendado:** Es ideal como modelo básico para tareas generales, trabajos rápidos, chats en la terminal y tareas comunes que necesitan respuestas casi al instante.

### Gemini 3.5 Flash
* **Características Principales:** Fue el modelo inicial cuando salió Antigravity 2.0. Funciona muy bien para recordar el estado del agente, añadir herramientas propias y ejecutar avisos (*hooks*) de inicio a fin.
* **Uso Recomendado:** Es muy bueno para seguir usando agentes antiguos, hacer pruebas de control o tareas secundarias que gasten pocos recursos sin perder funciones útiles.

## Análisis Profundo y Tareas Complejas (Alto Razonamiento)

Modelos muy potentes creados para leer textos largos, pensar a fondo y resolver problemas difíciles.

### Gemini 3.1 Pro
* **Características Principales:** Versión "Pro" centrada en entender ideas difíciles, revisar carpetas enteras de código y planear tareas en varios pasos (multi-step planning).
* **Uso Recomendado:** Cambios grandes en el código, diseño de nuevos programas, revisiones de seguridad a fondo e investigaciones difíciles que necesitan recordar muchos datos de un proyecto.

### Claude 4.6 (Opus)
* **Características Principales:** Es el modelo más fuerte de Anthropic disponible en el sistema. Destaca por leer gran cantidad de datos, escribir explicaciones claras y analizar ideas abstractas.
* **Uso Recomendado:** Escribir manuales largos, revisar cómo se conectan las partes de proyectos antiguos y resolver problemas de diseño de programas que necesitan pensar en grande.

## Flujos de Trabajo Versátiles e Interactivos

Modelos equilibrados que combinan buen nivel de respuesta, memoria y rapidez.

### Claude 4.6 (Sonnet)
* **Características Principales:** Versión rápida de Anthropic. Entiende muy bien el lenguaje común y el código (como Opus), pero responde más rápido.
* **Uso Recomendado:** Ayuda al escribir código, trabajo en equipo en Antigravity IDE, revisión de cambios (Pull Requests) y creación rápida de pruebas para código nuevo.

## Despliegues Privados y Ecosistema Abierto (Open Source)

Modelos pensados para cuidar la privacidad de los datos, trabajar sin internet o hacer pruebas libres.

### GPT-OSS-120B
* **Características Principales:** Modelo libre y abierto de gran tamaño (120 mil millones de parámetros). Es una opción frente a los modelos cerrados del SDK. Permite ver todos sus datos y saber cómo funciona por dentro.
* **Uso Recomendado:** Uso en computadoras propias (on-premise) cuando los datos no deben salir de la oficina, cumplimiento de reglas estrictas de privacidad (lugares aislados o *air-gapped*) o ajustes especiales para ciencias e investigación.