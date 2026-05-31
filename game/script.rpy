##############################################################################
# APARTMENT SIM — SCRIPT PRINCIPAL
# Archivo: game/script.rpy
# Módulo: Punto de entrada del juego, setup inicial, hooks de Ren'Py
# Versión: 1.0
# Última modificación: 31/05/2026
# Dependencias:
#   game/systems/stats.rpy    (prot_nombre, fn_stats_verificar_acceso)
#   game/systems/time.rpy     (time_franja, fn_tiempo_avanzar_franja)
#   game/systems/mood.rpy     (fn_mood_calcular_todos)
#   game/systems/jealousy.rpy (fn_celos_evaluar)
#   game/characters/celine.rpy (cel)
#   game/characters/roxy.rpy   (rox)
#   game/characters/luna.rpy   (lun)
# Descripción:
#   Contiene el label start obligatorio (punto de entrada de Ren'Py),
#   el setup inicial del protagonista (nombre, primer estado del juego),
#   la memoria de decisiones, el label after_load para migraciones,
#   y los defines del narrador y protagonista que dependen de prot_nombre.
#   Dev Narrativa escribe los diálogos del día 1 a partir del label
#   start_dia1 que está al final de este archivo.
##############################################################################


##############################################################################
# DEFINES DE PERSONAJES QUE DEPENDEN DE ESTE ARCHIVO
# nar y pro se definen aquí porque:
#   - nar no tiene nombre visible (narrador puro)
#   - pro usa [prot_nombre] que es una variable del store
# cel, rox, lun están en sus respectivos archivos de personaje.
# Fuente: renpy.org/doc/html/dialogue.html — interpolación de variables
##############################################################################

# Narrador — sin nombre visible en pantalla
define nar = Character(None)

# Protagonista — el nombre se interpola desde la variable prot_nombre del store
# Ren'Py actualiza [prot_nombre] automáticamente cuando la variable cambia
define pro = Character("[prot_nombre]", color="#FFFFFF")


##############################################################################
# VARIABLE DE MEMORIA DE DECISIONES
# Declarada aquí porque script.rpy es su módulo responsable
# según VARIABLES_GLOBALES.md sección 12.
# ADVERTENCIA: usar siempre reasignación — NUNCA .append()
##############################################################################

# Lista de strings con decisiones clave para diálogos futuros
# Máximo 20 items — las más antiguas se descartan si se supera el límite
default mem_decisiones = []


##############################################################################
# LABEL START — PUNTO DE ENTRADA OBLIGATORIO
# Ren'Py siempre busca este label al iniciar una partida nueva.
# NO renombrar. NO mover a otro archivo.
##############################################################################

label start:

    # Inicializar el estado base del juego antes de cualquier diálogo
    # Recalcular moods con los valores iniciales de stats
    $ fn_mood_calcular_todos()

    # Evaluar celos iniciales (todos en 0 con stats iniciales, pero
    # es buena práctica inicializar el sistema desde el primer momento)
    $ fn_celos_evaluar()

    # --- Setup del nombre del protagonista ---
    # renpy.input() pausa el juego y muestra un campo de texto.
    # El jugador puede dejar el nombre por defecto "Kai" o escribir el suyo.
    # strip() elimina espacios al inicio/fin. Si queda vacío, usar "Kai".
    # Fuente doc: renpy.org/doc/html/input.html

    $ nombre_ingresado = renpy.input(
        "¿Cómo te llamas?",
        default="Kai",
        length=20
    ).strip()

    # Si el jugador borró todo y dejó vacío, usar el nombre por defecto
    if nombre_ingresado == "":
        $ prot_nombre = "Kai"
    else:
        $ prot_nombre = nombre_ingresado

    # Limpiar variable temporal — no necesitamos guardarla
    $ del nombre_ingresado

    # --- Pantalla negra de transición antes del día 1 ---
    scene black with fade

    # Saltar al día 1 — Dev Narrativa escribe desde aquí
    jump start_dia1


##############################################################################
# LABEL START_DIA1 — INICIO DEL DÍA 1
# Dev Narrativa escribe los diálogos a partir de aquí.
# Cuando terminen los diálogos de presentación del día 1,
# hacer jump al mapa: jump map_salon
#
# Contexto del día 1 según GDD_NARRATIVA.md:
#   - El protagonista acaba de llegar al apartamento
#   - Conoce (o reencuentra) a Celine, Roxy y Luna
#   - Primera franja: mañana, día 1, lunes
##############################################################################

label start_dia1:

    # TODO: Dev Narrativa — escribir diálogos del día 1 aquí
    # Siguiendo GDD_NARRATIVA.md — llegada al apartamento + presentaciones
    # Usar aliases: cel, rox, lun, nar, pro — NUNCA nombres completos
    # Al terminar: jump map_salon

    # Placeholder temporal — reemplazar con el día 1 real
    scene black with fade

    nar "Vallanova. Por fin."
    nar "Hacía tiempo que no volvía. O quizás era la primera vez que volvía así."

    # Al terminar el día 1 narrativo, ir al mapa
    jump map_salon


##############################################################################
# LABEL MAP_SALON — PLACEHOLDER
# Placeholder temporal hasta que Dev UI cree map.rpy con el label real.
# Una vez map.rpy exista, este label desaparece — el de map.rpy toma el control.
# IMPORTANTE: cuando Dev UI cree map.rpy, eliminar este placeholder
# Y también eliminar el .rpyc de script (ver ESTANDARES.md sección 16).
##############################################################################

label map_salon:

    # TODO: Dev UI — reemplazar este placeholder con el mapa real en map.rpy
    # Cuando map.rpy esté listo, BORRAR este label y su .rpyc

    nar "[prot_nombre] mira el salón del apartamento."
    nar "(El mapa está pendiente — Dev UI lo implementa en map.rpy)"

    # Ciclo temporal para que el juego no crashee sin el mapa real
    jump map_salon


##############################################################################
# LABEL AFTER_LOAD — HOOK DE MIGRACIÓN
# Ren'Py ejecuta este label automáticamente cada vez que el jugador
# carga un save. Usar para migrar variables entre versiones del juego.
# Fuente: ESTANDARES.md sección 18 — renpy.org/doc/html/label.html
##############################################################################

label after_load:

    python:
        # --- Migraciones v1.0 → futuras versiones ---
        # Por ahora no hay migraciones (primera versión).
        # Cuando se renombre una variable en el futuro, agregar aquí:
        #
        # Ejemplo de migración futura:
        # if hasattr(store, "nombre_variable_vieja"):
        #     nueva_variable = store.nombre_variable_vieja
        #     del store.nombre_variable_vieja
        #
        # OBLIGATORIO al final si se modificaron datos:
        # renpy.block_rollback()

        # Verificar que mem_decisiones existe y es lista (compatibilidad)
        if not hasattr(store, "mem_decisiones"):
            store.mem_decisiones = []

        # Verificar que no superó el límite de 20 decisiones
        # (podría pasar en saves muy antiguos con versiones anteriores)
        if hasattr(store, "mem_decisiones") and len(store.mem_decisiones) > 20:
            store.mem_decisiones = store.mem_decisiones[-20:]

        renpy.block_rollback()

    return


##############################################################################
# FUNCIÓN AUXILIAR — MEMORIA DE DECISIONES
# Definida aquí porque script.rpy es el módulo responsable de mem_decisiones.
# Sigue el patrón obligatorio de reasignación de listas (ESTANDARES.md sección 10).
##############################################################################

init python:

    def fn_mem_agregar(decision):
        """
        Agrega una decisión a la memoria de decisiones del protagonista.
        Mantiene un máximo de 20 items — descarta el más antiguo si se supera.

        Parámetros:
            decision (str): texto corto que describe la decisión tomada
                            ej: "ayude_a_celine_apuntes"
                                "rechace_oferta_roxy"
                                "encontre_diario_luna"

        IMPORTANTE: usa reasignación de lista — NUNCA .append()
        Ver VARIABLES_GLOBALES.md sección 12 y ESTANDARES.md sección 10.

        Uso desde labels de evento:
            $ fn_mem_agregar("ayude_a_celine_apuntes")
        """

        # Reasignar la lista completa — esto activa el guardado automático
        nueva_lista = store.mem_decisiones + [decision]

        # Mantener máximo 20 items — conservar los más recientes
        if len(nueva_lista) > 20:
            nueva_lista = nueva_lista[-20:]

        store.mem_decisiones = nueva_lista

        fn_debug_log(
            "[script] Decisión guardada: '{}' (total: {})".format(
                decision, len(store.mem_decisiones)
            )
        )


    def fn_mem_tiene(decision):
        """
        Verifica si una decisión específica está en la memoria.
        Útil para diálogos que referencian decisiones pasadas.

        Parámetros:
            decision (str): decisión a buscar

        Retorna:
            bool: True si la decisión está en mem_decisiones

        Uso en condiciones de diálogo:
            if fn_mem_tiene("ayude_a_celine_apuntes"):
                cel "Todavía me acuerdo de eso."
        """

        return decision in store.mem_decisiones
