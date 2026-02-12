from PIL import Image, ImageDraw, ImageFont
import os

directorio_actual = os.path.dirname(os.path.abspath(__file__))

def aplicar_marca(ruta, texto, posicion, font_size=30):
    try:
        imagen = Image.open(ruta).convert("RGBA") # Convertimos a RGBA para mejor manejo
        txt_layer = Image.new('RGBA', imagen.size, (255,255,255,0))
        
        dibujo = ImageDraw.Draw(txt_layer)
        
        try:
            fuente = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            fuente = ImageFont.load_default()
            
        dibujo.text(posicion, texto, fill=(255,255,255,128), font=fuente)
        
        combinada = Image.alpha_composite(imagen, txt_layer)
        return combinada.convert("RGB") # Volver a RGB para guardar como JPG/PNG normal
    except Exception as e:
        print(f"Error al procesar {ruta}: {e}")
        return None


nombre_carpeta_entrada = 'imagenes' 

carpeta_origen = os.path.join(directorio_actual, nombre_carpeta_entrada)
carpeta_destino = os.path.join(directorio_actual, 'imagenes_marca_agua')

texto_marca_agua = '@juangomez'
posicion_texto = (10, 10)

if not os.path.exists(carpeta_origen):
    print(f"ERROR: No se encuentra la carpeta: {carpeta_origen}")
else:
    os.makedirs(carpeta_destino, exist_ok=True)
    archivos = os.listdir(carpeta_origen)
    
    procesados = 0
    for archivo in archivos:
        if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            ruta_completa = os.path.join(carpeta_origen, archivo)
            imagen_marca = aplicar_marca(ruta_completa, texto_marca_agua, posicion_texto)
            
            if imagen_marca:
                ruta_guardado = os.path.join(carpeta_destino, archivo)
                imagen_marca.save(ruta_guardado)
                print(f"✅ Procesado con éxito: {archivo}")
                procesados += 1
    
    if procesados == 0:
        print("No se encontraron imágenes .png o .jpg en la carpeta.")
    else:
        print(f"\nTerminado. Se procesaron {procesados} imágenes.")