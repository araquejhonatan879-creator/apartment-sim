##############################################################################
# APARTMENT SIM — SISTEMA DE TIEMPO
# Archivo: game/systems/time.rpy
# Módulo: Días, franjas horarias, energía del protagonista, rutinas
# Versión: 1.0
# Última modificación: 31/05/2026
# Dependencias: game/systems/stats.rpy (prot_energia_actual, prot_energia_max)
# Descripción:
#   Gestiona el avance del tiempo en franjas horarias (mañana → tarde →
#   noche → madrugada → nuevo día), recalcula energía al cambiar franja,
#   actualiza el día de la semana y expone utilidades de consulta de
#   disponibilidad de personajes según sus rutinas.
##############################################################################


##############################################################################
# FUNCIONES PYTHON DEL MÓDULO
##############################################################################

init python:

    def fn_tiempo_avanzar_franja():
        """
        Avanza el tiempo una franja horaria y aplica todas las consecuencias:
            - Ciclo: manana → tarde → noche → madrugada → (nuevo día) → manana
            - Al iniciar un nuevo día: incrementa time_dia, actualiza
              time_dia_semana, time_es_finde y restaura energía al máximo.
            - Siempre incrementa time_total_franjas.
            - NUNCA modificar time_franja directamente desde un label —
              siempre llamar esta función.

        Retorna:
            bool: True si al avanzar se inició un nuevo día, False si no.

        Uso desde labels:
            $ fn_tiempo_avanzar_franja()
        """

        # Orden oficial de franjas — sin tildes para evitar problemas de encoding
        orden_franjas = ["manana", "tarde", "noche", "madrugada"]

        # Leer franja actual
        franja_actual = store.time_franja

        # Buscar posición actual en el ciclo
        if franja_actual in orden_franjas:
            indice_actual = orden_franjas.index(franja_actual)
        else:
            # Si el valor es inválido, resetear a mañana con log de advertencia
            fn_debug_log(
                "[time] ADVERTENCIA: time_franja inválida '{}' — reseteando a manana".format(
                    franja_actual
                )
            )
            indice_actual = 0

        # Calcular siguiente franja
        indice_siguiente = (indice_actual + 1) % len(orden_franjas)
        franja_siguiente = orden_franjas[indice_siguiente]

        # Detectar si se completa el ciclo (madrugada → manana = nuevo día)
        nuevo_dia = (franja_siguiente == "manana")

        # Aplicar la nueva franja
        store.time_franja = franja_siguiente

        # Incrementar contador total de franjas
        store.time_total_franjas = store.time_total_franjas + 1

        # --- Lógica de nuevo día ---
        if nuevo_dia:
            store.time_dia = store.time_dia + 1
            store.time_dia_semana = fn_tiempo_calcular_dia_semana(store.time_dia)
            store.time_es_finde = store.time_dia_semana in ("sabado", "domingo")

            # Restaurar energía al máximo al comenzar el día
            store.prot_energia_actual = store.prot_energia_max

            fn_debug_log(
                "[time] Nuevo día: {} ({}) — energía restaurada a {}".format(
                    store.time_dia,
                    store.time_dia_semana,
                    store.prot_energia_max
                )
            )
        else:
            # Entre franjas del mismo día: reducir energía en 1 si queda
            if store.prot_energia_actual > 0:
                store.prot_energia_actual = store.prot_energia_actual - 1

        fn_debug_log(
            "[time] Franja: {} → {} | Día {} | Energía: {}/{}".format(
                franja_actual,
                franja_siguiente,
                store.time_dia,
                store.prot_energia_actual,
                store.prot_energia_max
            )
        )

        return nuevo_dia


    def fn_tiempo_calcular_dia_semana(numero_dia):
        """
        Calcula el día de la semana a partir del número de día del juego.
        El día 1 es lunes (primer día del juego).

        Parámetros:
            numero_dia (int): número de día absoluto del juego (empieza en 1)

        Retorna:
            str: nombre del día sin tildes
                 "lunes", "martes", "miercoles", "jueves",
                 "viernes", "sabado", "domingo"

        Nota: función pura — no lee ni escribe el store.
        """

        dias = [
            "lunes",
            "martes",
            "miercoles",
            "jueves",
            "viernes",
            "sabado",
            "domingo",
        ]

        # (numero_dia - 1) porque el día 1 debe dar índice 0 (lunes)
        indice = (numero_dia - 1) % 7
        return dias[indice]


    def fn_tiempo_es_disponible(personaje, franja):
        """
        Consulta si un personaje está disponible para interactuar en una
        franja horaria dada, según sus rutinas base definidas en los GDD.

        Esta función codifica las rutinas de SEMANA. Para fines de semana
        usa fn_tiempo_es_disponible_finde().

        Parámetros:
            personaje (str): "celine", "roxy" o "luna"
            franja (str):    "manana", "tarde", "noche" o "madrugada"

        Retorna:
            bool: True si el personaje está en el apartamento y disponible.

        Fuente de rutinas: GDD_PERSONAJES.md — celine.json, roxy.json, luna.json

        IMPORTANTE: esta función solo consulta disponibilidad BASE.
        Los eventos narrativos pueden overridear la disponibilidad temporalmente.
        Eso es responsabilidad de cada *_events.rpy.
        """

        # Si es fin de semana, usar la tabla de finde
        if store.time_es_finde:
            return fn_tiempo_es_disponible_finde(personaje, franja)

        # --- Rutinas de SEMANA (lunes a viernes) ---
        # True = está en el apartamento y disponible para interactuar
        # False = está fuera o dormida / no disponible
        rutinas_semana = {
            "celine": {
                "manana":    False,   # universidad (clases de mañana)
                "tarde":     False,   # universidad (clases/biblioteca)
                "noche":     True,    # en casa, estudiando o cocinando
                "madrugada": False,   # dormida
            },
            "roxy": {
                "manana":    True,    # en casa (trabaja tarde/noche)
                "tarde":     False,   # trabajo en bar / galería
                "noche":     False,   # trabajo nocturno
                "madrugada": True,    # vuelve a casa, disponible brevemente
            },
            "luna": {
                "manana":    False,   # trabajo remoto enfocado (no interrumpir)
                "tarde":     True,    # pausa / cocina / disponible
                "noche":     True,    # lectura, disponible
                "madrugada": False,   # dormida
            },
        }

        if personaje not in rutinas_semana:
            fn_debug_log(
                "[time] fn_tiempo_es_disponible: personaje desconocido '{}'".format(
                    personaje
                )
            )
            return False

        if franja not in rutinas_semana[personaje]:
            fn_debug_log(
                "[time] fn_tiempo_es_disponible: franja inválida '{}'".format(franja)
            )
            return False

        return rutinas_semana[personaje][franja]


    def fn_tiempo_es_disponible_finde(personaje, franja):
        """
        Versión de fin de semana de fn_tiempo_es_disponible().
        Las rutinas del finde son distintas — todos están más en casa.

        Parámetros:
            personaje (str): "celine", "roxy" o "luna"
            franja (str):    "manana", "tarde", "noche" o "madrugada"

        Retorna:
            bool: True si está disponible en fin de semana.

        Fuente: GDD_PERSONAJES.md — rutinas fin de semana de cada personaje.
        """

        # --- Rutinas de FIN DE SEMANA (sábado y domingo) ---
        rutinas_finde = {
            "celine": {
                "manana":    True,    # duerme hasta tarde, pero disponible
                "tarde":     True,    # compras, cafetería, en casa
                "noche":     True,    # salidas o queda en casa
                "madrugada": False,   # dormida
            },
            "roxy": {
                "manana":    False,   # duerme hasta tarde (trabajó de noche)
                "tarde":     True,    # disponible, más relajada
                "noche":     True,    # salidas o en casa pintando
                "madrugada": True,    # vuelve tarde, disponible brevemente
            },
            "luna": {
                "manana":    True,    # paseo matutino, disponible al volver
                "tarde":     True,    # lectura, disponible
                "noche":     True,    # más abierta que entre semana
                "madrugada": False,   # dormida
            },
        }

        if personaje not in rutinas_finde:
            fn_debug_log(
                "[time] fn_tiempo_es_disponible_finde: personaje desconocido '{}'".format(
                    personaje
                )
            )
            return False

        if franja not in rutinas_finde[personaje]:
            return False

        return rutinas_finde[personaje][franja]


    def fn_tiempo_obtener_label_franja(franja):
        """
        Retorna el texto visible al jugador para una franja horaria.
        Usado por el HUD para mostrar la hora del día con tilde.

        Parámetros:
            franja (str): valor interno sin tilde ("manana", "tarde", etc.)

        Retorna:
            str: texto con tilde para mostrar en pantalla

        Nota: las variables internas no llevan tilde (evita bugs de encoding),
        pero el HUD sí puede mostrar texto con tilde al jugador.
        """

        etiquetas = {
            "manana":    "Mañana",
            "tarde":     "Tarde",
            "noche":     "Noche",
            "madrugada": "Madrugada",
        }

        return etiquetas.get(franja, franja)


##############################################################################
# VARIABLES DEL MÓDULO
# Keyword: default — se guardan en save, participan en rollback
##############################################################################

# Día actual del juego — empieza en 1 (lunes)
default time_dia          = 1

# Franja horaria activa — ciclo: manana → tarde → noche → madrugada → manana
# Sin tildes para evitar problemas de encoding en comparaciones
default time_franja       = "manana"

# Día de la semana en texto — sin tildes
# Valores válidos: "lunes" "martes" "miercoles" "jueves" "viernes" "sabado" "domingo"
default time_dia_semana   = "lunes"

# True si time_dia_semana es "sabado" o "domingo"
# Se recalcula en fn_tiempo_avanzar_franja() al cambiar de día
default time_es_finde     = False

# Contador total de franjas transcurridas desde el inicio
# Útil para eventos temporales ("3 franjas después de X")
default time_total_franjas = 0
