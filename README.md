
# Backend de Procesamiento de Archivos PDF a Imágenes y Documentos Word a PDF

Este backend Flask permite convertir archivos PDF a imágenes JPG, procesar estas imágenes en documentos Word con imágenes incrustadas, y luego convertir esos documentos Word a PDF. También proporciona funciones para eliminar páginas pares de un PDF y organizar documentos en una carpeta específica.

## Requisitos

- Python 3.7 o superior
- Flask
- PyMuPDF (fitz)
- python-docx
- Pillow
- docx2pdf

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://tu-repositorio.git
   cd tu-proyecto
   ```

**Instala las dependencias:**

```
pip install -r requirements.txt

```


## Configuración

El backend utiliza carpetas de carga (`uploads`) y descarga (`download`) configuradas en el archivo `app.py`.

## Uso

### Procesar un solo día

* **Endpoint:** `/api/process_single_day`
* **Método:** `POST`
* **Entrada esperada:** Archivo PDF
* **Salida:** Archivo Word y PDF procesados para el día actual

### Procesar el fin de semana

* **Endpoint:** `/api/process_weekend`
* **Método:** `POST`
* **Entrada esperada:** Tres archivos PDF (Viernes, Sábado, Domingo)
* **Salida:** Archivos Word y PDF procesados para cada día del fin de semana

### Descargar archivos generados

* **Endpoint:** `/api/download/<nombre-archivo>`
* **Método:** `GET`
* **Entrada esperada:** Nombre del archivo generado
* **Salida:** Descarga del archivo generado como archivo adjunto


## Ejecución

Para ejecutar el backend en modo de depuración:

```
python app.py
```


El servidor Flask se ejecutará en `http://localhost:5000` por defecto.

## Notas adicionales

* Los registros de operaciones se encuentran en la consola y están configurados en `INFO`.
* Asegúrate de tener configuradas las carpetas `uploads` y `download` en el mismo directorio que `app.py`.
