# Regex
import re

# pyttessereact
import pytesseract

# import Pyllow
from PIL import Image

# utils
from utils import verificar as validar_cedual, descarga_xlsx

def inicio_procesar_imagen():
    lista_estudiante = []

    # Validacion ruta de imagenes
    try:
        # Abre la imagen con pillow
        img = Image.open("./assets/imagen_con_texto.jpg") 
    except Exception as e:
        print('Error: Imagen no encontrada en el directorio actual.')
        return False
    
    img.load()
    # Extrae el texto de la imagen
    text = pytesseract.image_to_string(img, lang='spa') 

    # Convierte en lista por saltos de linea imagen mapeada
    list_from_text = text.split('\n')
    for i in list_from_text:
        # extrae cedula usando regex
        cedula = re.findall('[0-9]+', i)
        if len(cedula)>0:
            cedula = cedula[0]
        else:
            cedula = ''

        # Obtiene estudiante utilizando re o grep
        estudiante = " ".join(re.findall('[a-zA-Z^.*$]+', i))

        # aniade estudiante al listado de resultado
        lista_estudiante.append(
            {'estudiante': estudiante,
            'cedula': cedula,
            'cedula_valida': "La cedula es {valida}".format(
                valida = 'valida' if validar_cedual(cedula) else 'invalida' 
            ),
            'asistencia':'SI',})

    # escribe el archivo en excel
    descarga_xlsx(lista_estudiante)

