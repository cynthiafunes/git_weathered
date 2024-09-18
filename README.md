# CLI Clima

Aplicación CLI para obtener datos climáticos usando la API de WeatherAPI.

## Características

- Datos en tiempo real de temperatura, condición, precipitación, humedad, etc.
- Salida en formatos **JSON** y **CSV**.

## Instalación y Ejecución

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/cynthiafunes/git_weathered.git
    ```

2. **Ejecuta el script de automatización:**

    ```bash
    ./automatizacion.sh
    ```

   Este script realiza las siguientes acciones:
   - Activa el entorno virtual.
   - Instala las dependencias.
   - Ejecuta la aplicación CLI con un ejemplo de ciudad (`edinburgh`) en formato JSON.

3. **Configura tu clave de API** en `api_key.py` si no lo has hecho aún:

    ```python
    api_key = 'tu_clave_api'
    ```

## Uso Manual

Si prefieres ejecutar la aplicación manualmente, sigue estos pasos:

1. **Activa el entorno virtual:**

    ```bash
    source .venv/Scripts/activate
    ```

2. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Ejecuta la aplicación CLI:**

    ```bash
    python cli.py <ciudad> <json|csv>
    ```

   - `<ciudad>`: Nombre de la ciudad.
   - `<json|csv>`: Formato de salida.