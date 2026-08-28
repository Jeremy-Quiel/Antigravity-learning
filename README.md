# Documentación de Modelos - Antigravity SDK

Este documento explica los modelos de Inteligencia Artificial compatibles con la herramienta **Google Antigravity SDK**. El sistema está diseñado para trabajar con agentes autónomos. Estos modelos asisten a los agentes en el razonamiento, uso de herramientas, aplicación de políticas y orquestación de subagentes.

## Procesamiento Rápido y Orquestación de Agentes (Baja Latencia)

Estos modelos proporcionan respuestas rápidas, toma de decisiones ágil y gestionan el ciclo de vida completo de los agentes autónomos.

### Gemini 3.7 Flash
* **Características Principales:** El modelo predeterminado principal en el SDK de Antigravity desde mediados o finales de 2026. Optimizado y co-entrenado para el *harness* de Antigravity, proporcionando alta velocidad para tool calling y delegación a subagentes.
* **Uso Recomendado:** Ideal como modelo base para agentes de propósito general, flujos de trabajo automatizados de alta velocidad, interacciones de terminal y tareas estándar que requieren respuestas casi instantáneas.

### Gemini 3.5 Flash
* **Características Principales:** El modelo predeterminado inicial en el lanzamiento de Antigravity 2.0. Altamente confiable para la gestión del estado del agente, registro de herramientas personalizadas y ejecución de hooks del ciclo de vida.
* **Uso Recomendado:** Excelente para compatibilidad hacia atrás con agentes heredados, pruebas de regresión o tareas auxiliares donde el uso de recursos debe minimizarse sin perder capacidades agentivas.

## Análisis Profundo y Tareas Complejas (Alto Razonamiento)

Modelos de alta capacidad diseñados para contextos extensos, razonamiento avanzado y resolución de desafíos algorítmicos complejos.

### Gemini 3.1 Pro
* **Características Principales:** Variante "Pro" enfocada en la comprensión lógica profunda, análisis de bases de código completas del repositorio y planificación de múltiples pasos (multi-step planning).
* **Uso Recomendado:** Refactorización de código a gran escala, diseño de nuevas arquitecturas de sistemas, auditorías de seguridad en profundidad e investigaciones complejas que requieren retención y referencias cruzadas de datos extensos del repositorio.

### Claude 4.6 (Opus)
* **Características Principales:** El modelo más capaz de la familia Anthropic soportado en la plataforma. Destaca en la asimilación de contextos grandes, redacción técnica clara y razonamiento lógico abstracto.
* **Uso Recomendado:** Redacción de manuales técnicos extensos, análisis de dependencias cruzadas en proyectos monolíticos heredados y resolución de desafíos arquitectónicos de software de alto nivel.

## Flujos de Trabajo Versátiles e Interactivos

Modelos equilibrados que ofrecen una relación óptima entre inteligencia, retención de contexto y latencia de respuesta.

### Claude 4.6 (Sonnet)
* **Características Principales:** Variante optimizada de Anthropic que combina una sólida comprensión del lenguaje natural y del código (similar a Opus) con tiempos de respuesta reducidos.
* **Uso Recomendado:** Asistencia de código interactiva, pair-programming en Antigravity IDE, revisiones de Pull Requests y generación rápida de pruebas unitarias para código recién creado.

## Despliegues Privados y Ecosistema Abierto (Open Source)

Modelos diseñados para políticas estrictas de privacidad de datos, entornos aislados o necesidades de investigación abierta.

### GPT-OSS-120B
* **Características Principales:** Modelo de lenguaje de pesos abiertos a gran escala (120 mil millones de parámetros). Proporciona una alternativa robusta a los modelos propietarios en el SDK, permitiendo la inspección completa y la transparencia de los pesos y el entorno de ejecución.
* **Uso Recomendado:** Despliegues de agentes locales on-premise donde los datos corporativos no pueden salir de la red privada, cumplimiento de políticas estrictas de seguridad air-gapped o personalizaciones de bajo nivel para investigación científica.