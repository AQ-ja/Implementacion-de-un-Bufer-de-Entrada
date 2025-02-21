def cargar_buffer(entrada, inicio, tamano_buffer):

    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer

def procesar_buffer(entrada, tamano_buffer):

    inicio = 0
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    avance = 0
    lexema = ""
    
    while True:
        # Si se llegó al final del búfer, recargar nuevos datos
        if avance >= len(buffer):
            inicio += tamano_buffer
            buffer = cargar_buffer(entrada, inicio, tamano_buffer)
            avance = 0
        
        char = buffer[avance]
        avance += 1

        if char == "eof":
            # Si hay un lexema pendiente, imprimirlo y terminar
            if lexema:
                print("Lexema procesado:", lexema)
            break
        elif char == " ":
            # Cuando se encuentra un espacio y existe un lexema acumulado, se imprime
            if lexema:
                print("Lexema procesado:", lexema)
                lexema = ""
        else:
            # Acumular el carácter en el lexema actual
            lexema += char


entrada = list("Esto es un ejemplo de entrada con eof")
#entrada = list("Tarea de diseño de compiladores")
tamano_buffer = 10
procesar_buffer(entrada, tamano_buffer)
