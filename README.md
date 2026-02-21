# Python Service Monitor

Mini herramienta de automatización en Python para monitorizar y recuperar servicios Linux automáticamente.

## 📌 Descripción

Este script comprueba el estado de un servicio gestionado por systemd.

Si el servicio no está activo:
- Intenta habilitarlo
- Intenta arrancarlo
- Registra el resultado en un archivo log

Incluye manejo de errores, logging estructurado y códigos de salida correctos.

## 🚀 Uso
sudo python3 service_monitor.py <service_name>
