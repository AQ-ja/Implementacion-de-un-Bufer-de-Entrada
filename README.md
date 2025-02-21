# Procesamiento de Lexemas con Buffers

Este código procesa una cadena de entrada en bloques (buffers) de tamaño fijo y extrae lexemas (tokens o palabras) separados por espacios.

## Funciones principales

### `cargar_buffer(entrada, inicio, tamano_buffer)`
- **Descripción**: Carga un segmento de la cadena de entrada desde una posición inicial (`inicio`) con un tamaño máximo (`tamano_buffer`).
- **Detalles**:
  - Si el segmento es más pequeño que el tamaño del buffer, añade `"eof"` (end of file) para indicar el final de la entrada.
  - Retorna el buffer cargado.

### `procesar_buffer(entrada, tamano_buffer)`
- **Descripción**: Procesa la entrada en bloques de tamaño fijo y extrae lexemas separados por espacios.
- **Detalles**:
  - Lee el contenido del buffer carácter por carácter.
  - Si encuentra un espacio, imprime el lexema acumulado y lo reinicia.
  - Si encuentra `"eof"`, imprime el lexema pendiente y termina.
  - Si el buffer se agota, carga un nuevo segmento de la entrada.
