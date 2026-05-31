##############################################################################
# APARTMENT SIM — SISTEMA DE CELOS Y ARMONÍA
# Archivo: game/systems/jealousy.rpy
# Módulo: Celos por personaje y armonía global del apartamento
# Versión: 1.0
# Última modificación: 31/05/2026
# Dependencias:
#   game/systems/stats.rpy  (stats_*_afecto, stats_*_confianza)
#   game/systems/time.rpy   (time_dia — para reset diario)
# Descripción:
#   Evalúa los celos de cada personaje en función de la diferencia de
#   atención que reciben del protagonista. Gestiona la armonía global
#   del apartamento (apt_armonia). Los celos se resetean al iniciar
#   cada nuevo día. La armonía es persistente entre días.
#   Si apt_armonia llega a 0, se activa modo conflicto global.
##############################################################################


##############################################################################
# FUNCIONES PYTHON DEL MÓDULO
##############################################################################

init python:

    def fn_celos_evaluar():
        """
        Evalúa los celos de los tres personajes comparando su afecto entre
        sí. Si alguna tiene una diferencia grande respecto a las demás,
        desarrolla celos proporcionales a esa diferencia.

        Lógica:
            - Calcular el afecto promedio de los tres personajes
            - Si el afecto de un personaje está muy por encima del promedio,
              las OTRAS dos sienten celos de ella
            - La intensidad de los celos (0-3) depende de la diferencia:
                0 → diferencia < 10  (sin celos)
                1 → diferencia 10-19 (celos leves)
                2 → diferencia 20-34 (celos moderados)
                3 → diferencia >= 35 (celos intensos)
            - Si alguna tiene celos activos, la armonía baja

        Retorna:
            dict: estado de celos de cada personaje
                  {"celine": intensidad, "roxy": intensidad, "luna": intensidad}

        Uso recomendado: llamar al avanzar franja o al final de eventos
        importantes donde se modificó el afecto de alguien.
            $ fn_celos_evaluar()
        """

        personajes = ["celine", "roxy", "luna"]

        # Leer afectos actuales
        afectos = {}
        for p in personajes:
            afectos[p] = getattr(store, "stats_" + p + "_afecto", 0)

        # Calcular promedio
        promedio = sum(afectos.values()) / len(personajes)

        # Evaluar celos de cada personaje
        resultado = {}
        hubo_celos = False

        for p in personajes:
            # Los celos de P se basan en qué tan POR DEBAJO del promedio está P
            # Si P tiene menos afecto que las demás, siente celos
            diferencia = promedio - afectos[p]

            # Determinar intensidad
            if diferencia < 10:
                intensidad = 0
            elif diferencia < 20:
                intensidad = 1
            elif diferencia < 35:
                intensidad = 2
            else:
                intensidad = 3

            # Guardar en store
            nombre_activo     = "celos_" + p + "_activo"
            nombre_intensidad = "celos_" + p + "_intensidad"

            setattr(store, nombre_intensidad, intensidad)
            setattr(store, nombre_activo, intensidad > 0)

            if intensidad > 0:
                hubo_celos = True

            resultado[p] = intensidad

            fn_debug_log(
                "[jealousy] {} → intensidad={} (afecto={}, promedio={:.1f}, diff={:.1f})".format(
                    p, intensidad, afectos[p], promedio, diferencia
                )
            )

        # Impacto en armonía si hay celos activos
        if hubo_celos:
            fn_celos_aplicar_impacto_armonia(resultado)

        return resultado


    def fn_celos_aplicar_impacto_armonia(resultado_celos):
        """
        Reduce la armonía del apartamento según la intensidad total de celos.
        La armonía no puede bajar de 0.

        Tabla de impacto por franja (acumulativo entre personajes):
            intensidad 1 → -2 puntos de armonía por personaje celosa
            intensidad 2 → -5 puntos de armonía por personaje celosa
            intensidad 3 → -10 puntos de armonía por personaje celosa

        Parámetros:
            resultado_celos (dict): output de fn_celos_evaluar()

        Nota: función interna — llamada solo desde fn_celos_evaluar().
        No llamar directamente desde labels.
        """

        impacto_por_intensidad = {0: 0, 1: 2, 2: 5, 3: 10}

        impacto_total = 0
        for p, intensidad in resultado_celos.items():
            impacto_total += impacto_por_intensidad.get(intensidad, 0)

        if impacto_total > 0:
            armonia_actual = store.apt_armonia
            armonia_nueva  = max(0, armonia_actual - impacto_total)
            store.apt_armonia = armonia_nueva

            fn_debug_log(
                "[jealousy] Armonía: {} → {} (impacto -{})".format(
                    armonia_actual, armonia_nueva, impacto_total
                )
            )

            # Advertir si la armonía llegó a 0 (modo conflicto global)
            if armonia_nueva == 0:
                fn_debug_log(
                    "[jealousy] ALERTA: apt_armonia llegó a 0 — activar modo conflicto"
                )


    def fn_celos_resetear_dia():
        """
        Resetea los celos activos de todos los personajes al inicio de un
        nuevo día. La ARMONÍA no se resetea — es persistente entre días.

        Llamar desde fn_tiempo_avanzar_franja() cuando nuevo_dia == True.

        Uso:
            $ fn_celos_resetear_dia()
        """

        for p in ("celine", "roxy", "luna"):
            setattr(store, "celos_" + p + "_activo",     False)
            setattr(store, "celos_" + p + "_intensidad", 0)

        fn_debug_log("[jealousy] Celos reseteados al iniciar nuevo día")


    def fn_celos_recuperar_armonia(puntos):
        """
        Incrementa la armonía del apartamento (máximo 100).
        Llamar desde eventos grupales positivos o acciones de reconciliación.

        Parámetros:
            puntos (int): cantidad de armonía a recuperar (positivo)

        Retorna:
            int: valor nuevo de apt_armonia

        Uso desde labels:
            $ fn_celos_recuperar_armonia(5)
        """

        armonia_actual = store.apt_armonia
        armonia_nueva  = min(100, armonia_actual + puntos)
        store.apt_armonia = armonia_nueva

        fn_debug_log(
            "[jealousy] Armonía recuperada: {} → {} (+{})".format(
                armonia_actual, armonia_nueva, puntos
            )
        )

        return armonia_nueva


##############################################################################
# VARIABLES DEL MÓDULO
# Keyword: default — se guardan en save, participan en rollback
##############################################################################

# Armonía global del apartamento — persistente entre días, rango 0-100
# Si llega a 0: modo conflicto global (todas hostiles entre sí)
default apt_armonia = 70

# --- Celos de Celine ---
default celos_celine_activo     = False   # True si tiene celos activos hoy
default celos_celine_intensidad = 0       # 0=ninguno 1=leve 2=moderado 3=intenso

# --- Celos de Roxy ---
default celos_roxy_activo       = False
default celos_roxy_intensidad   = 0

# --- Celos de Luna ---
default celos_luna_activo       = False
default celos_luna_intensidad   = 0
