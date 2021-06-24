#!/usr/bin/env python

# La abstraccion de proceso en el OS es representada mediante una PCB
class PCB: # Bloque de Control de Procesos
    def __init__(estado, process_id, parent_id, counter, registers, memory_limit, files_opened)
        # ID del Proceso
        process_id  = 0
        parent_id = 0
        estado = ''
        registers = None # de proposito general
        apuntador_pila = None # Apuntador a pila
        counter = None # contador de programa
        informacion_contable = None

        # Credenciales de Seguridad
        owner_id = 0 # id del usuario propietario
        apuntador_cola_procesos = None # Apuntadores a la cola de procesos
        mascara_senales = None  # Mascara de seniales
        memory_limit = 0 # Administracion de memoria
        files_opened = 0 # Archivos abiertos
    
p1 = PCB(None, 123, 1, 0, [], 100, 0)

# Tablas de Procesos: contiene varios PCBs
tablas_procesos = []
tabla_procesos.append(p1)

# Colas de procesos
# el OS enlaza PCBs en colas (el PCB contiene punteros para ello) 
# de procesos en el mismoe stado
procesos_listos = [] # Algunos OS consideran procesos running en esta lista

# Procesos bloqueados
# 1. Una misma cola para todos 
# 2. Una cola por evento
# 3. Varios eventos por cola (System V)
procesos_bloqueados = []

# Un proceso migra entre distintas colas
cola_listos = []
cola_devices_es = []

# Planificadores
scheduler_long_term = None 
# selecciona procesos en cola_listos
# requerido con poca frecuencia (seg) 
# puede ser lento, controla el grado de multiprogramacion, ej: job sheculder

scheduler_short_term = None
# selecciona proceso siguiente a ejecutarse
# requerido muy frecuentemente (ms)
# debe ser rapido, ej: CPU Scheduler

# Interrupciones
# Es un evento que altera la secuencia en que el procesador ejecuta las instrucciones
# Ej: IA-32 (intel 32bits) tiene una tabla descriptora (IDT) con 256 entradas:
# 32 => 0 a 31 predefinidas y reservadas
# 224 => 32 y 255 definidas por el usuario
# 1. proceso en ejecucion hasta la interrupcion
# 2. Captura el estado, intercambia el control y encuentra la rutina
# 3. Ejecuta la rutina respectiva
# 4. Restaura el proceso interrumpido
# 5. Continua la ejecucion


# Threads 
# Un proceso contiene multiples flujos de ejecucion, llamados threads o procesos ligeros
# El proceso se corresponde con un entorno de ejecucion: 
# - mapa de memoria
# - conjunto de recursos asociados (ficheros, semaforos, ..)
# - Conjunto de threads
# Todo proceso tiene un thread implicito: el flujo de ejecucion inicial
# Los threads de un mismo proceso comparten:
# - Mapa de memoria (codigo, datos, zonas de memoria compartida, ...)
# - Recursos asociados al proceso (ficheros, semaforos, ...)
# Cada thread tiene recursos propios: una pila, estado, y copia del contenido de los registros
# Las colas de listos y bloqueados contienen threads en vez de procesos

# Singlethreading cuando el SO no reconoce el concepto de thread, ej: MS-DOS
# Multithreading cuando el SO soporta multiples threads de ejecucion dentro de un proceso
# ej: Unix tradicionales soportan multiples procesos de usuario, pero solo soporta un thread por proceso. Solares sin embargo soporta multiples threads.








