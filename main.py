import time
import pygame as pg
from constantes_buscaminas import *
from biblioteca import *

pg.init()
pg.mixer.init()
# Configuracion de la ventana del juego con la Reso y los parámetros especificados.
pantalla = pg.display.set_mode(RESOLUCION_PANTALLA, pg.RESIZABLE)
pg.display.set_caption("Buscaminas")
color_fondo = COLOR_GRIS_CLARO

#Declaracion de las variables neecesarias para que funcione el juego

cantidad_minas_facil = str(CANTIDAD_MINAS_FACIL)
cantidad_minas_medio = str(CANTIDAD_MINAS_MEDIO)
cantidad_minas_dificil = str(CANTIDAD_MINAS_DIFICIL)
tiempo_inicial = 0
tiempo_transcurrido_minutos = 0
tiempo_transcurrido_segundos = "0".zfill(2)
tiempo_fin = 0
contador_puntaje = 0
bandera_boton_buscaminas = False
bandera_boton_nivel = False
bandera_campo_texto = False
bandera_tiempo_inicial = False
bandera_inicio = False
bandera_mina = False
bandera_fin = False


#Se cargan las imagenes desde una ruta y se acomoda para ser utilizada en el juego

ruta_imagen_mina = "C:/Users/Pato/Downloads/recursos/mina.jpg"
imagen_mina = pg.image.load(ruta_imagen_mina)
pg.display.set_icon(imagen_mina)


# FUNCION CREAR_IMAGEN:  Crea una imagen, toma x e y (int), una ruta (str) 
# y la transparencia (bool)  Retorna un diccionario de la imagen

ruta_imagen_mina_fin = "C:/Users/Pato/Downloads/recursos/mina_fin.gif"
dict_mina_dificil = crear_imagen(0, 0, ruta_imagen_mina_fin, False)

IMAGEN_MINA_ANCHO_MEDIO = dict_mina_dificil["superficie"].get_width() * 2
IMAGEN_MINA_ALTO_MEDIO = dict_mina_dificil["superficie"].get_height() * 2
dict_mina_medio = crear_imagen_transformada(IMAGEN_MINA_ANCHO_MEDIO, IMAGEN_MINA_ALTO_MEDIO, ruta_imagen_mina_fin)
IMAGEN_MINA_ANCHO_FACIL = dict_mina_dificil["superficie"].get_width() * 4
IMAGEN_MINA_ALTO_FACIL = dict_mina_dificil["superficie"].get_height() * 4
dict_mina_facil = crear_imagen_transformada(IMAGEN_MINA_ANCHO_FACIL, IMAGEN_MINA_ALTO_FACIL, ruta_imagen_mina_fin)

#MAS IMAGENES, ACA VAN LOS "FONDOS" + QUE NADA

dict_explosion = crear_imagen(0, 0, "C:/Users/Pato/Downloads/recursos/nuevo_fondo_inicio.jpg", False)
dict_trofeo = crear_imagen(0, 0, "C:/Users/Pato/Downloads/recursos/trofeo.png", True)
dict_elige_nivel = crear_imagen(0, 0, "C:/Users/Pato/Downloads/recursos/elige_tu_nivel.png", False)
dict_fondo_ganaste = crear_imagen(0, 0, "C:/Users/Pato/Downloads/recursos/ganaste.png", False)
dict_fondo_nombre_usuario = crear_imagen(0, 0, "C:/Users/Pato/Downloads/recursos/ingresa_tu_nombre.png", False)
dict_fondo_lista_puntajes = crear_imagen(0, 0, "C:/Users/Pato/Downloads/recursos/listado_puntajes.png", False)
dict_fondo_tablero_juego = crear_imagen(0, 0, "C:/Users/Pato/Downloads/recursos/fondo_tablero.png", False)

#RUTAS DE LAS FUENTES UTILIZADAS
ruta_fuente_pixel = "C:/Users/Pato/Downloads/recursos/pixelifysans_variablefont_wght.ttf"
ruta_fuente_jugando = "C:/Users/Pato/Downloads/recursos/digital_7.ttf"

#RETOQUE DE TAMAÑOS CON LAS CONSTANTES
fuente_inicio = pg.font.Font(ruta_fuente_pixel, TAMANIO_FUENTE_INICIO)
fuente_jugando = pg.font.Font(ruta_fuente_jugando, TAMANIO_FUENTE_JUGANDO)
fuente_casilleros_dificil = pg.font.Font(ruta_fuente_pixel, TAMANIO_FUENTE_CASILLEROS_DIFICIL)
fuente_casilleros_medio = pg.font.Font(ruta_fuente_pixel, TAMANIO_FUENTE_CASILLEROS_MEDIO)
fuente_casilleros_facil = pg.font.Font(ruta_fuente_pixel, TAMANIO_FUENTE_CASILLEROS_FACIL)

dict_nivel = crear_texto(108, 70, ruta_fuente_pixel, "NIVEL", TAMANIO_FUENTE_INICIO, COLOR_NARANJA)
dict_jugar = crear_texto(105, 170, ruta_fuente_pixel, "JUGAR", TAMANIO_FUENTE_INICIO, COLOR_NARANJA)
dict_puntajes = crear_texto(80, 270, ruta_fuente_pixel, "PUNTAJES", TAMANIO_FUENTE_INICIO, COLOR_NARANJA)
dict_salir = crear_texto(105, 370, ruta_fuente_pixel, "SALIR", TAMANIO_FUENTE_INICIO, COLOR_NARANJA)

#COORDENADAS Y CREACION DE TEXTO DE BOTONES DE NIVELES 
dict_nivel_facil = crear_texto(390, 300, ruta_fuente_pixel, "FACIL", TAMANIO_FUENTE_ELIGE_NIVEL, COLOR_NARANJA)
dict_nivel_medio =  crear_texto(380, 500, ruta_fuente_pixel, "MEDIO", TAMANIO_FUENTE_ELIGE_NIVEL, COLOR_NARANJA)
dict_nivel_dificil = crear_texto(360, 700, ruta_fuente_pixel, "DIFICIL", TAMANIO_FUENTE_ELIGE_NIVEL, COLOR_NARANJA)

#COORDENADAS Y CREACION DE TEXTO DE BOTONES DE INICIO Y VOLVER 


dict_inicio = crear_texto(460, 940, ruta_fuente_pixel, "INICIO", TAMANIO_FUENTE_INICIO, COLOR_NARANJA)

dict_volver = crear_texto(280, 770, ruta_fuente_pixel, "VOLVER", TAMANIO_FUENTE_INICIO, COLOR_NARANJA)

#COORDENADAS Y CREACION DE TEXTO DE BOTONES

dict_nombre_usuario = crear_texto(200, 300, ruta_fuente_pixel, "INGRESE NOMBRE:  ", TAMANIO_FUENTE_ELIGE_NIVEL, COLOR_ROJO)
nombre_ingresado = ""
dict_nombre_ingresado = crear_texto(400, 400, ruta_fuente_pixel, nombre_ingresado, TAMANIO_FUENTE_ELIGE_NIVEL, COLOR_ROJO)

dict_nombre = crear_texto(70, 70, ruta_fuente_pixel, "", TAMANIO_FUENTE_INICIO, COLOR_ROJO)
dict_puntaje = crear_texto(300, 70, ruta_fuente_pixel, "", TAMANIO_FUENTE_INICIO, COLOR_ROJO)

ruta_imagen_blanco = "C:/Users/Pato/Downloads/recursos/blanco.gif"

dict_blanco_dificil = crear_imagen(0, 0, ruta_imagen_blanco, False)

# IMAGENES: CREACION, ANCHO Y LARGO

IMAGEN_BLANCO_ANCHO_MEDIO = dict_blanco_dificil["superficie"].get_width() * 2
IMAGEN_BLANCO_ALTO_MEDIO = dict_blanco_dificil["superficie"].get_height() * 2
dict_blanco_medio = crear_imagen_transformada(IMAGEN_MINA_ANCHO_MEDIO, IMAGEN_MINA_ALTO_MEDIO, ruta_imagen_blanco)

IMAGEN_BLANCO_ANCHO_FACIL = dict_blanco_dificil["superficie"].get_width() * 4
IMAGEN_BLANCO_ALTO_FACIL = dict_blanco_dificil["superficie"].get_height() * 4
dict_blanco_facil = crear_imagen_transformada(IMAGEN_MINA_ANCHO_FACIL, IMAGEN_MINA_ALTO_FACIL, ruta_imagen_blanco)

ruta_imagen_reiniciar = "C:/Users/Pato/Downloads/recursos/cara_sonriente.gif"
dict_imagen_reiniciar = crear_imagen(0, 0, ruta_imagen_reiniciar, False)
IMAGEN_REINICIAR_ANCHO = dict_imagen_reiniciar["superficie"].get_width() * 2
IMAGEN_REINICIAR_ALTO = dict_imagen_reiniciar["superficie"].get_height() * 2
dict_imagen_reiniciar = crear_imagen_transformada(IMAGEN_REINICIAR_ANCHO, IMAGEN_REINICIAR_ALTO, ruta_imagen_reiniciar)
dict_imagen_reiniciar["pos"] = [300, 70]

ruta_imagen_triste_reiniciar = "C:/Users/Pato/Downloads/recursos/cara_triste.gif"
dict_imagen_triste_reiniciar = crear_imagen(0, 0, ruta_imagen_triste_reiniciar, False)
IMAGEN_TRISTE_REINICIAR_ANCHO = dict_imagen_triste_reiniciar["superficie"].get_width() * 2
IMAGEN_TRISTE_REINICIAR_ALTO = dict_imagen_triste_reiniciar["superficie"].get_height() * 2
dict_imagen_triste_reiniciar = crear_imagen_transformada(IMAGEN_REINICIAR_ANCHO, IMAGEN_REINICIAR_ALTO, ruta_imagen_triste_reiniciar)
dict_imagen_triste_reiniciar["pos"] = [300, 70]

ruta_imagen_bandera = "C:/Users/Pato/Downloads/recursos/bandera.gif"
dict_bandera_dificil = crear_imagen(0, 0, ruta_imagen_bandera, False)

IMAGEN_BANDERA_ANCHO_MEDIO = dict_bandera_dificil["superficie"].get_width() * 2
IMAGEN_BANDERA_ALTO_MEDIO = dict_bandera_dificil["superficie"].get_height() * 2
dict_bandera_medio = crear_imagen_transformada(IMAGEN_BANDERA_ANCHO_MEDIO, IMAGEN_BANDERA_ALTO_MEDIO, ruta_imagen_bandera)

IMAGEN_BANDERA_ANCHO_FACIL = dict_bandera_dificil["superficie"].get_width() * 4
IMAGEN_BANDERA_ALTO_FACIL = dict_bandera_dificil["superficie"].get_height() * 4
dict_bandera_facil = crear_imagen_transformada(IMAGEN_BANDERA_ANCHO_FACIL, IMAGEN_BANDERA_ALTO_FACIL, ruta_imagen_bandera)

dict_casillero = {}
dict_cantidad_minas = {}
dict_tiempo = {}
dict_puntaje_juego = {}

dict_fin = crear_texto(620, 70, ruta_fuente_pixel, "PERDISTE", TAMANIO_FUENTE_CASILLEROS_FACIL, COLOR_ROJO)

dict_gana = {}


ruta_musica_buscaminas = "C:/Users/Pato/Downloads/recursos/buscaminas.mp3"
pg.mixer.music.load(ruta_musica_buscaminas)
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play(-1)

ruta_efecto_explosion = "C:/Users/Pato/Downloads/recursos/segundo_parcial_recursos_explosion.mp3"
explosion = pg.mixer.Sound(ruta_efecto_explosion)        
explosion.set_volume(0.25)
ruta_efecto_descubrimiento = "C:/Users/Pato/Downloads/recursos/descubrimiento.mp3"
descubrimiento = pg.mixer.Sound(ruta_efecto_descubrimiento)
descubrimiento.set_volume(0.25)

reloj = pg.time.Clock()


#inicializar_matriz = Carga una matriz con valores iniciales (filas y columnas)  retorna matriz.
#a traves de parametro segun dificultad pone una cantidad específica de minas aleatoriamente dentro de la matriz

matriz = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
establecer_cantidad_minas(matriz, CANTIDAD_MINAS_FACIL)
botones_buscaminas = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
bandera_matriz_descubierta = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
bandera_matriz_marcada = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)


establecer_minas_contiguas(matriz)#->Toma la matriz que se genero con la cantidad de minas y recorre los 8 espacios para contabilizar cuantas minas hay
mostrar_matriz(matriz)

bandera_identificarse = False
estado_juego = "inicio"
nivel = "facil"
lista_claves = ["nombre", "puntaje", "activo"]


#RUTA IMAGEN PLAY Y PAUSA PARA MUSICA
imagen_play = pg.image.load("C:/Users/Pato/Downloads/recursos/play.png") 
imagen_pause = pg.image.load("C:/Users/Pato/Downloads/recursos/pausa.png")
imagen_play = pg.transform.scale(imagen_play, (50, 50))
imagen_pause = pg.transform.scale(imagen_pause, (50, 50))

#Codigo y coordenadas para boton de play/pausa
musica_corriendo = True
imagen_actual_musica = imagen_pause
boton_rect = imagen_actual_musica.get_rect(center=(900, 50))


corriendo = True


#Acá se  carga y ordena la lista de jugadores desde un archivo JSON existente.
#Se eligió usar "try" y "except" para que corra el juego aunque no este el archivo

try:
    lista_jugadores = cargar_archivo_json("C:/Users/Pato/OneDrive/Escritorio/Facu/UTN/01_programacion_1/Juego/lista_jugadores.json")
    criterio = "desc"
    ordenar_jugadores(lista_jugadores, criterio)
except:
    lista_jugadores = []
    guardar_archivo_json("C:/Users/Pato/OneDrive/Escritorio/Facu/UTN/01_programacion_1/Juego/lista_jugadores.json", lista_jugadores)#CAMBIAR RUTA

#BUCLE PRINCIPAL DEL JUEGO (WHILE Y  "corriendo" como variable para poder aplicar en boton salir)
while corriendo == True:

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
            
        if evento.type == pg.MOUSEBUTTONDOWN:
                #EVENTOS DEL JUEGO AL INICIO
            if evento.button == 1:
                if estado_juego == "inicio":
                    if boton_nivel.collidepoint(evento.pos) == True:
                        estado_juego = "nivel"
                    elif boton_jugar.collidepoint(evento.pos) == True:
                        estado_juego = "jugando"
                    elif boton_puntajes.collidepoint(evento.pos) == True:
                        estado_juego = "puntajes"
                    elif boton_salir.collidepoint(evento.pos) == True:
                        corriendo = False
                    #BOTON DE MUSICA CREADO ARRIBA
                if boton_rect.collidepoint(evento.pos):
                    if musica_corriendo:
                        pg.mixer.music.pause()  #PAUSA
                        musica_corriendo = False
                        imagen_actual_musica = imagen_play  #PONE IMAGEN DE PLAY
                    else:
                        pg.mixer.music.unpause()  # VUELVE LA MUSICA Y CAMBIA DE IMAGEN
                        musica_corriendo = True
                        imagen_actual_musica = imagen_pause 
                    
                    #inicializar_matriz = Carga una matriz con valores iniciales (filas y columnas)  retorna matriz.

                elif estado_juego == "nivel":
                    if bandera_boton_nivel == True:
                        if boton_nivel_facil.collidepoint(evento.pos) == True:
                            bandera_matriz_descubierta = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                            bandera_matriz_marcada = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                            botones_buscaminas = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
                            matriz = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
                            establecer_cantidad_minas(matriz, CANTIDAD_MINAS_FACIL)
                            establecer_minas_contiguas(matriz)
                            print("\n")
                            mostrar_matriz(matriz)
                            nivel = "facil"
                            estado_juego = "jugando"
                        if boton_nivel_medio.collidepoint(evento.pos) == True:
                            bandera_matriz_descubierta = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                            bandera_matriz_marcada = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                            botones_buscaminas = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, 0)
                            matriz = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, 0)
                            establecer_cantidad_minas(matriz, CANTIDAD_MINAS_MEDIO)
                            establecer_minas_contiguas(matriz)
                            print("\n")
                            mostrar_matriz(matriz)
                            nivel = "medio"
                            estado_juego = "jugando"
                        if boton_nivel_dificil.collidepoint(evento.pos) == True:
                            bandera_matriz_descubierta = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                            bandera_matriz_marcada = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                            botones_buscaminas = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, 0)
                            matriz = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, 0)
                            establecer_cantidad_minas(matriz, CANTIDAD_MINAS_DIFICIL)
                            establecer_minas_contiguas(matriz)
                            print("\n")
                            mostrar_matriz(matriz)
                            nivel = "dificil"
                            estado_juego = "jugando"
                
                elif estado_juego == "jugando":
                    if boton_reiniciar.collidepoint(evento.pos) == True:
                        bandera_fin = False
                        bandera_tiempo_inicial = False
                        bandera_boton_buscaminas = False
                        bandera_boton_nivel = False
                        bandera_identificarse = False
                        bandera_campo_texto = False
                        bandera_inicio = False
                        bandera_mina = False
                        cantidad_minas_facil = str(CANTIDAD_MINAS_FACIL)
                        cantidad_minas_medio = str(CANTIDAD_MINAS_MEDIO)
                        cantidad_minas_dificil = str(CANTIDAD_MINAS_DIFICIL)
                        nombre_ingresado = ""
                        tiempo_inicial = 0
                        tiempo_transcurrido_minutos = 0
                        tiempo_transcurrido_segundos = "0".zfill(2)
                        contador_puntaje = 0
                        if nivel == "facil":
                            bandera_matriz_descubierta = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                            bandera_matriz_marcada = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                            matriz = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
                            establecer_cantidad_minas(matriz, CANTIDAD_MINAS_FACIL)
                        elif nivel == "medio":
                            bandera_matriz_descubierta = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                            bandera_matriz_marcada = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                            matriz = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, 0)
                            establecer_cantidad_minas(matriz, CANTIDAD_MINAS_MEDIO)
                        elif nivel == "dificil":
                            bandera_matriz_descubierta = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                            bandera_matriz_marcada = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                            matriz = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, 0)
                            establecer_cantidad_minas(matriz, CANTIDAD_MINAS_DIFICIL)
                        establecer_minas_contiguas(matriz)
                        print("\n")
                        mostrar_matriz(matriz)
                        bandera_boton_buscaminas = True

                    """
                    Se verifica que el boton este activo, recorre todas las filas y luego las columnas
                    verifica si se hizo clic en casillero actual [i;j] con colisiones detecta donde ocurre
                    inicia el tiempo y se pasa al match para verificar si hay o no una mina """    
                    if bandera_boton_buscaminas == True:                
                        for i in range(len(matriz)):
                            for j in range(len(matriz[i])):
                                if botones_buscaminas[i][j].collidepoint(evento.pos) == True:
                                    if bandera_tiempo_inicial == False:
                                        tiempo_inicial = time.time()
                                        bandera_tiempo_inicial = True
                                    if bandera_matriz_marcada[i][j] == False:
                                        match(matriz[j][i]):
                                            case -1:
                                                explosion.play()
                                                if bandera_matriz_descubierta[i][j] == False:
                                                    bandera_matriz_descubierta[i][j] = True
                                                    bandera_fin = True
                                            case _:
                                                for x in range(j - 1, j + 2):
                                                    for y in range(i - 1, i + 2):
                                                        if 0 <= x and x < len(matriz) and 0 <= y and y < len(matriz[x]):
                                                            if matriz[x][y] != -1:
                                                                if bandera_matriz_descubierta[y][x] == False:
                                                                    contador_puntaje += 1
                                                                    bandera_matriz_descubierta[y][x] = True
                                                
                                                if bandera_matriz_descubierta[i][j] == False:
                                                    descubrimiento.play()
                                                    contador_puntaje += 1
                                                    bandera_matriz_descubierta[i][j] = True
                    if bandera_inicio == True:
                        if boton_volver.collidepoint(evento.pos):
                            bandera_tiempo_inicial = False
                            bandera_boton_buscaminas = False
                            bandera_boton_nivel = False
                            bandera_identificarse = False
                            bandera_campo_texto = False
                            bandera_inicio = False
                            bandera_mina = False
                            bandera_fin = False
                            cantidad_minas_facil = str(CANTIDAD_MINAS_FACIL)
                            cantidad_minas_medio = str(CANTIDAD_MINAS_MEDIO)
                            cantidad_minas_dificil = str(CANTIDAD_MINAS_DIFICIL)
                            nombre_ingresado = ""
                            tiempo_inicial = 0
                            tiempo_transcurrido_minutos = 0
                            tiempo_transcurrido_segundos = "0".zfill(2)
                            contador_puntaje = 0
                            if nivel == "facil":
                                bandera_matriz_descubierta = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                                bandera_matriz_marcada = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                                matriz = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
                                establecer_cantidad_minas(matriz, CANTIDAD_MINAS_FACIL)
                            elif nivel == "medio":
                                bandera_matriz_descubierta = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                                bandera_matriz_marcada = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                                matriz = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, 0)
                                establecer_cantidad_minas(matriz, CANTIDAD_MINAS_MEDIO)
                            elif nivel == "dificil":
                                bandera_matriz_descubierta = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                                bandera_matriz_marcada = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                                matriz = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, 0)
                                establecer_cantidad_minas(matriz, CANTIDAD_MINAS_DIFICIL)
                            establecer_minas_contiguas(matriz)
                            print("\n")
                            mostrar_matriz(matriz)
                            estado_juego ="inicio"
                elif estado_juego == "identificarse":
                    if campo_texto.collidepoint(evento.pos) == True:
                        bandera_campo_texto = True
                    else:
                        bandera_campo_texto = False
                elif estado_juego == "puntajes":
                    if bandera_inicio == True:
                        if boton_inicio.collidepoint(evento.pos):
                            estado_juego ="inicio"
            elif evento.button == 3:
                if estado_juego == "jugando":
                    for i in range(len(matriz)):
                        for j in range(len(matriz[i])):
                            if botones_buscaminas[i][j].collidepoint(evento.pos) == True:
                                if bandera_boton_buscaminas == True:
                                    if bandera_matriz_descubierta[i][j] == False:
                                        if bandera_matriz_marcada[i][j] == False:
                                            if nivel == "facil" and int(cantidad_minas_facil) > 0:
                                                cantidad_minas_facil = str(int(cantidad_minas_facil) - 1)
                                                bandera_matriz_marcada[i][j] = True
                                            elif nivel == "medio" and int(cantidad_minas_medio) > 0:
                                                cantidad_minas_medio = str(int(cantidad_minas_medio) - 1)
                                                bandera_matriz_marcada[i][j] = True
                                            elif nivel == "dificil" and int(cantidad_minas_dificil) > 0:
                                                cantidad_minas_dificil = str(int(cantidad_minas_dificil) - 1)
                                                bandera_matriz_marcada[i][j] = True
                                        else:
                                            bandera_matriz_marcada[i][j] = False
                                            if nivel == "facil":
                                                cantidad_minas_facil = str(int(cantidad_minas_facil) + 1)
                                            elif nivel == "medio":
                                                cantidad_minas_medio = str(int(cantidad_minas_medio) + 1)
                                            else:
                                                cantidad_minas_dificil = str(int(cantidad_minas_dificil) + 1)
               
        
        if evento.type == pg.KEYDOWN:
            if estado_juego == "identificarse":
                actualizar_pantalla(dict_fondo_nombre_usuario , "superficie", pantalla)
                if bandera_campo_texto == True:
                    if evento.key == pg.K_RETURN:
                        if len(nombre_ingresado) >= 3:
                            tiempo_fin = time.time()
                            jugador = cargar_jugador(lista_claves, nombre_ingresado, puntaje, "activo")
                            lista_jugadores.append(jugador)
                            ordenar_jugadores(lista_jugadores, criterio)
                            guardar_archivo_json("C:/Users/Pato/OneDrive/Escritorio/Facu/UTN/01_programacion_1/Juego/lista_jugadores.json", lista_jugadores)
                            bandera_identificarse = True
                    elif evento.key == pg.K_BACKSPACE:
                        nombre_ingresado = nombre_ingresado[0:-1]
                    else:
                        if len(nombre_ingresado) < 15 and (evento.unicode == "_" or evento.unicode == " " or evento.unicode.isalnum() == True):
                            nombre_ingresado += evento.unicode
                    dict_nombre_ingresado["texto"] = fuente_inicio.render(nombre_ingresado, True, COLOR_ROJO)            
    pantalla.fill(color_fondo)
    if estado_juego == "inicio":
        actualizar_pantalla(dict_explosion, "superficie", pantalla)
        #actualizar_pantalla(dict_bucaminas, "superficie", pantalla)
        actualizar_pantalla(dict_nivel, "texto", pantalla)
        actualizar_pantalla(dict_jugar, "texto", pantalla)
        actualizar_pantalla(dict_puntajes, "texto", pantalla)
        actualizar_pantalla(dict_salir, "texto", pantalla)
        coordenadas_boton_nivel = (50, 50, 200, 75)
        coordenadas_boton_jugar = (50, 150, 200, 75)
        coordenadas_boton_puntajes = (50, 250, 200, 75)
        coordenadas_boton_salir = (50, 350, 200, 75)
        boton_nivel = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_nivel, width=10, border_radius=15)
        boton_jugar = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_jugar, width=10, border_radius=15)
        boton_puntajes = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_puntajes, width=10, border_radius=15)
        boton_salir = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_salir, width=10, border_radius=15)
    elif estado_juego == "nivel":
        actualizar_pantalla(dict_elige_nivel , "superficie", pantalla)
        actualizar_pantalla(dict_nivel_facil, "texto", pantalla)
        actualizar_pantalla(dict_nivel_medio, "texto", pantalla)
        actualizar_pantalla(dict_nivel_dificil, "texto", pantalla)
        coordenadas_boton_facil = (330, 290, 300, 100)
        coordenadas_boton_medio = (330, 490, 300, 100)
        coordenadas_boton_dificil = (325, 690, 300, 100)
        boton_nivel_facil = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_facil, width=10, border_radius=15)
        boton_nivel_medio = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_medio, width=10, border_radius=15)
        boton_nivel_dificil = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_dificil, width=10, border_radius=15)
        bandera_boton_nivel = True
    elif estado_juego == "jugando":
        pg.mixer.music.set_volume(0.2)
        actualizar_pantalla(dict_fondo_tablero_juego, "superficie", pantalla)
        if nivel == "facil":
            dict_cantidad_minas["texto"] = fuente_jugando.render(cantidad_minas_facil, True, COLOR_ROJO)
        elif nivel == "medio":
            dict_cantidad_minas["texto"] = fuente_jugando.render(cantidad_minas_medio, True, COLOR_ROJO)
        else:
            dict_cantidad_minas["texto"] = fuente_jugando.render(cantidad_minas_dificil, True, COLOR_ROJO)
        dict_cantidad_minas["pos"] = [70, 70]
        if bandera_tiempo_inicial == True:
            tiempo_transcurrido_minutos = int(time.time() - tiempo_inicial) // 60
            tiempo_transcurrido_segundos = str(int(time.time() - tiempo_inicial) % 60).zfill(2)
        dict_tiempo["texto"] = fuente_jugando.render(f"{tiempo_transcurrido_minutos}:{tiempo_transcurrido_segundos}", True, COLOR_ROJO)
        dict_tiempo["pos"] = [400, 70]
        puntaje = str(contador_puntaje).zfill(4)
        dict_puntaje_juego["texto"] = fuente_jugando.render(puntaje, True, COLOR_ROJO)
        dict_puntaje_juego["pos"] = [500, 70]
        actualizar_pantalla(dict_cantidad_minas, "texto", pantalla)
        if bandera_fin == False:
            boton_reiniciar = actualizar_pantalla(dict_imagen_reiniciar, "superficie", pantalla)
        actualizar_pantalla(dict_tiempo, "texto", pantalla)
        actualizar_pantalla(dict_puntaje_juego, "texto", pantalla)
        posicion_casillero_inicial = [70, 140]
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if nivel == "dificil":
                    posicion_casillero = (posicion_casillero_inicial[0] + i * 16, posicion_casillero_inicial[1] + j * 16)
                    dict_mina_dificil["pos"] = posicion_casillero
                    dict_blanco_dificil["pos"] = posicion_casillero
                    dict_bandera_dificil["pos"] = posicion_casillero
                elif nivel == "medio":
                    posicion_casillero = (posicion_casillero_inicial[0] + i * 33, posicion_casillero_inicial[1] + j * 33)
                    dict_mina_medio["pos"] = posicion_casillero
                    dict_blanco_medio["pos"] = posicion_casillero
                    dict_bandera_medio["pos"] = posicion_casillero
                elif nivel == "facil":
                    posicion_casillero = (posicion_casillero_inicial[0] + i * 65, posicion_casillero_inicial[1] + j * 65)
                    dict_mina_facil["pos"] = posicion_casillero
                    dict_blanco_facil["pos"] = posicion_casillero
                    dict_bandera_facil["pos"] = posicion_casillero
                dict_casillero["pos"] = posicion_casillero
                if bandera_matriz_descubierta[i][j] == False:
                    if bandera_matriz_marcada[i][j] == False:
                        if nivel == "dificil":
                            botones_buscaminas[i][j] = actualizar_pantalla(dict_blanco_dificil, "superficie", pantalla)
                        elif nivel == "medio":
                            botones_buscaminas[i][j] = actualizar_pantalla(dict_blanco_medio, "superficie", pantalla)
                        elif nivel == "facil":
                            botones_buscaminas[i][j] = actualizar_pantalla(dict_blanco_facil, "superficie", pantalla)
                    else:
                        if nivel == "dificil":
                            botones_buscaminas[i][j] = actualizar_pantalla(dict_bandera_dificil, "superficie", pantalla)
                        elif nivel == "medio":
                            botones_buscaminas[i][j] = actualizar_pantalla(dict_bandera_medio, "superficie", pantalla)
                        elif nivel == "facil":
                            botones_buscaminas[i][j] = actualizar_pantalla(dict_bandera_facil, "superficie", pantalla)
                elif matriz[j][i] > 0 or matriz[j][i] == -1:
                    match matriz[j][i]:
                        case -1:
                            if nivel == "dificil":
                                botones_buscaminas[i][j] = actualizar_pantalla(dict_mina_dificil, "superficie", pantalla)
                            elif nivel == "medio":
                                botones_buscaminas[i][j] = actualizar_pantalla(dict_mina_medio, "superficie", pantalla)
                            elif nivel == "facil":
                                botones_buscaminas[i][j] = actualizar_pantalla(dict_mina_facil, "superficie", pantalla)
                        case 1:
                            if nivel == "dificil":
                                dict_casillero["texto"] = fuente_casilleros_dificil.render(f"{matriz[j][i]}", True, "blue1")
                            elif nivel == "medio":
                                dict_casillero["texto"] = fuente_casilleros_medio.render(f"{matriz[j][i]}", True, "blue1")
                            elif nivel == "facil":
                                dict_casillero["texto"] = fuente_casilleros_facil.render(f"{matriz[j][i]}", True, "blue1")
                        case 2:
                            if nivel == "dificil":
                                dict_casillero["texto"] = fuente_casilleros_dificil.render(f"{matriz[j][i]}", True, "chartreuse4")
                            elif nivel == "medio":
                                dict_casillero["texto"] = fuente_casilleros_medio.render(f"{matriz[j][i]}", True, "chartreuse4")
                            elif nivel == "facil":
                                dict_casillero["texto"] = fuente_casilleros_facil.render(f"{matriz[j][i]}", True, "chartreuse4")
                        case 3:
                            if nivel == "dificil":
                                dict_casillero["texto"] = fuente_casilleros_dificil.render(f"{matriz[j][i]}", True, "red1")
                            elif nivel == "medio":
                                dict_casillero["texto"] = fuente_casilleros_medio.render(f"{matriz[j][i]}", True, "red1")
                            elif nivel == "facil":
                                dict_casillero["texto"] = fuente_casilleros_facil.render(f"{matriz[j][i]}", True, "red1")
                        case 4:
                            if nivel == "dificil":
                                dict_casillero["texto"] = fuente_casilleros_dificil.render(f"{matriz[j][i]}", True, "blue4")
                            elif nivel == "medio":
                                dict_casillero["texto"] = fuente_casilleros_medio.render(f"{matriz[j][i]}", True, "blue4")
                            elif nivel == "facil":
                                dict_casillero["texto"] = fuente_casilleros_facil.render(f"{matriz[j][i]}", True, "blue4")
                        case 5:
                            if nivel == "dificil":
                                dict_casillero["texto"] = fuente_casilleros_dificil.render(f"{matriz[j][i]}", True, "darkred")
                            elif nivel == "medio":
                                dict_casillero["texto"] = fuente_casilleros_medio.render(f"{matriz[j][i]}", True, "darkred")
                            elif nivel == "facil":
                                dict_casillero["texto"] = fuente_casilleros_facil.render(f"{matriz[j][i]}", True, "darkred")
                        case 6:
                            if nivel == "dificil":
                                dict_casillero["texto"] = fuente_casilleros_dificil.render(f"{matriz[j][i]}", True, "aquamarine4")
                            elif nivel == "medio":
                                dict_casillero["texto"] = fuente_casilleros_medio.render(f"{matriz[j][i]}", True, "aquamarine4")
                            elif nivel == "facil":
                                dict_casillero["texto"] = fuente_casilleros_facil.render(f"{matriz[j][i]}", True, "aquamarine4")
                        case 7:
                            if nivel == "dificil":
                                dict_casillero["texto"] = fuente_casilleros_dificil.render(f"{matriz[j][i]}", True, "black")
                            elif nivel == "medio":
                                dict_casillero["texto"] = fuente_casilleros_medio.render(f"{matriz[j][i]}", True, "black")
                            elif nivel == "facil":
                                dict_casillero["texto"] = fuente_casilleros_facil.render(f"{matriz[j][i]}", True, "black")
                        case 8:
                            if nivel == "dificil":
                                dict_casillero["texto"] = fuente_casilleros_dificil.render(f"{matriz[j][i]}", True, "azure4")
                            elif nivel == "medio":
                                dict_casillero["texto"] = fuente_casilleros_medio.render(f"{matriz[j][i]}", True, "azure4")
                            elif nivel == "facil":
                                dict_casillero["texto"] = fuente_casilleros_facil.render(f"{matriz[j][i]}", True, "azure4")
                    if matriz[j][i] != -1:
                        actualizar_pantalla(dict_casillero, "texto", pantalla)
                if bandera_fin == False:    
                    bandera_boton_buscaminas = True
        if bandera_fin == True:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[j][i] == -1:
                        bandera_matriz_descubierta[i][j] = True
            bandera_boton_buscaminas = False
            bandera_tiempo_inicial = False
            boton_reiniciar = actualizar_pantalla(dict_imagen_triste_reiniciar, "superficie", pantalla)
            actualizar_pantalla(dict_fin, "texto", pantalla)
        if nivel == "facil" and puntaje == "0054" or nivel == "medio" and puntaje == "0216" or nivel == "dificil" and puntaje == "0380":
            estado_juego = "identificarse"

        actualizar_pantalla(dict_volver, "texto", pantalla)
        coordenadas_boton_volver = (240, 750, 200, 75)
        boton_volver = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_volver, width=10, border_radius=15)
        bandera_inicio = True
    elif estado_juego == "identificarse":
        actualizar_pantalla(dict_fondo_nombre_usuario , "superficie", pantalla)
        dict_nombre_ingresado["texto"] = fuente_inicio.render(f"{nombre_ingresado}", True, COLOR_ROJO)
        actualizar_pantalla(dict_nombre_usuario, "texto", pantalla)
        actualizar_pantalla(dict_nombre_ingresado, "texto", pantalla)
        coordenadas_campo_texto = (330, 390, 300, 80)
        if bandera_campo_texto == False:
            campo_texto = pg.draw.rect(pantalla, COLOR_ROJO, coordenadas_campo_texto, width=10, border_radius=15)
        else:
            campo_texto = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_campo_texto, width=10, border_radius=15)
        if bandera_identificarse == True:
            estado_juego = "fin"
    elif estado_juego == "puntajes":

        actualizar_pantalla(dict_fondo_lista_puntajes, "superficie", pantalla)
        if len(lista_jugadores) > 0:
            dict_nombre["pos"] = [350, 200]
            dict_puntaje["pos"] = [550, 200]
            contador_mostrar_puntajes = 0
            for clave_encabezado in lista_claves:
                if clave_encabezado == "nombre":
                    dict_nombre["texto"] = fuente_inicio.render(f"{clave_encabezado.upper()}", True, COLOR_ROJO)
                    actualizar_pantalla(dict_nombre, "texto", pantalla)
                elif clave_encabezado == "puntaje":
                    dict_puntaje["texto"] = fuente_inicio.render(f"{clave_encabezado.upper()}", True, COLOR_ROJO)
                    actualizar_pantalla(dict_puntaje, "texto", pantalla)                    
            for puntaje_jugador in lista_jugadores:
                if puntaje_jugador["activo"] == True:
                    if contador_mostrar_puntajes < 3:
                        for clave in puntaje_jugador:
                            if clave == "nombre":
                                dict_nombre["texto"] = fuente_inicio.render(f"{puntaje_jugador[clave]}", True, COLOR_ROJO)
                                dict_nombre["pos"][1] += 40
                                actualizar_pantalla(dict_nombre, "texto", pantalla)
                            elif clave == "puntaje":
                                dict_puntaje["texto"] =  fuente_inicio.render(f"{puntaje_jugador[clave]}", True, COLOR_ROJO)
                                dict_puntaje["pos"][1] += 40
                                actualizar_pantalla(dict_puntaje, "texto", pantalla)
                    else:
                        break
                    contador_mostrar_puntajes += 1
        actualizar_pantalla(dict_inicio, "texto", pantalla)
        coordenadas_boton_inicio = (410, 925, 200, 75)
        boton_inicio = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_inicio, width=10, border_radius=15)
        bandera_inicio = True
    elif estado_juego == "fin":
        actualizar_pantalla(dict_fondo_ganaste, "superficie", pantalla)
        dict_gana["texto"] = fuente_inicio.render(".", True, COLOR_GRIS_OSCURO)
        dict_gana["pos"] = (pantalla.get_width() // 2 - dict_gana["texto"].get_width() // 2, pantalla.get_height() // 2)
        actualizar_pantalla(dict_gana, "texto", pantalla)
        if int(time.time() - tiempo_fin) >= 5:
            bandera_tiempo_inicial = False
            bandera_boton_buscaminas = False
            bandera_boton_nivel = False
            bandera_identificarse = False
            bandera_campo_texto = False
            bandera_inicio = False
            bandera_mina = False
            bandera_fin = False
            cantidad_minas_facil = str(CANTIDAD_MINAS_FACIL)
            cantidad_minas_medio = str(CANTIDAD_MINAS_MEDIO)
            cantidad_minas_dificil = str(CANTIDAD_MINAS_DIFICIL)
            nombre_ingresado = ""
            tiempo_inicial = 0
            tiempo_transcurrido_minutos = 0
            tiempo_transcurrido_segundos = "0".zfill(2)
            contador_puntaje = 0
            if nivel == "facil":
                bandera_matriz_descubierta = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                bandera_matriz_marcada = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                matriz = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
                establecer_cantidad_minas(matriz, CANTIDAD_MINAS_FACIL)
            elif nivel == "medio":
                bandera_matriz_descubierta = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                bandera_matriz_marcada = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                matriz = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, 0)
                establecer_cantidad_minas(matriz, CANTIDAD_MINAS_MEDIO)
            elif nivel == "dificil":
                bandera_matriz_descubierta = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                bandera_matriz_marcada = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                matriz = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, 0)
                establecer_cantidad_minas(matriz, CANTIDAD_MINAS_DIFICIL)
            establecer_minas_contiguas(matriz)
            print("\n")
            mostrar_matriz(matriz)
            estado_juego = "inicio"
    pantalla.blit(imagen_actual_musica, boton_rect)

    reloj.tick(30)
   
    
    pg.display.flip()
pg.quit()