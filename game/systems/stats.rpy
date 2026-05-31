##############################################################################
# APARTMENT SIM — SISTEMA DE STATS
# Archivo: game/systems/stats.rpy
# Módulo: Stats de personajes, stats del protagonista, personalidad y acceso
# Versión: 1.0
# Última modificación: 31/05/2026
# Dependencias: ninguna — este módulo es la base de todos los demás
# Descripción:
#   Declara todas las variables de stats (personajes + protagonista +
#   personalidad + acceso a cuartos) y define las funciones centrales
#   fn_stats_modificar() y fn_stats_verificar_acceso().
#   NINGÚN otro archivo debe modificar stats directamente — siempre
#   a través de fn_stats_modificar().
##############################################################################


##############################################################################
# FUNCIONES PYTHON DEL MÓDULO
# Definidas en init python: para que estén disponibles antes del label start.
# Priority 0 (default) — no hay dependencias previas.
##############################################################################

init python:

    def fn_stats_modificar(personaje, stat, delta):
        """
        Modifica el stat de un personaje aplicando los límites 0-100.

        Parámetros:
            personaje (str): "celine", "roxy" o "luna"
            stat (str):      "afecto", "confianza" o "corrupcion"
            delta (int):     cantidad a sumar (positivo) o restar (negativo)

        Retorna:
            int: el valor nuevo del stat después de aplicar el cambio

        Uso desde labels de evento:
            $ fn_stats_modificar("celine", "afecto", 5)
            $ fn_stats_modificar("roxy", "confianza", -3)

        NUNCA hacer:
            $ stats_celine_afecto += 5  ← incorrecto, no usa límites
        """

        # Construir el nombre de la variable (ej: "stats_celine_afecto")
        nombre_var = "stats_" + personaje + "_" + stat

        # Leer el valor actual desde el store global de Ren'Py
        valor_actual = getattr(store, nombre_var, 0)

        # Aplicar el delta y clampear entre 0 y 100
        valor_nuevo = max(0, min(100, valor_actual + delta))

        # Escribir el valor nuevo en el store (esto activa el guardado)
        setattr(store, nombre_var, valor_nuevo)

        # Log en consola si estamos en modo debug
        fn_debug_log(
            "[stats] {} {} {} → {} ({:+d})".format(
                personaje, stat, valor_actual, valor_nuevo, delta
            )
        )

        return valor_nuevo


    def fn_stats_verificar_acceso(personaje):
        """
        Verifica si el protagonista ha alcanzado el afecto necesario para
        desbloquear el acceso al cuarto de un personaje. Si se cumple la
        condición Y el acceso aún no estaba activo, lo activa.

        Umbrales definidos en VARIABLES_GLOBALES.md sección 7:
            Roxy  → afecto >= 20
            Celine → afecto >= 35
            Luna  → afecto >= 45

        Parámetros:
            personaje (str): "celine", "roxy" o "luna"

        Retorna:
            bool: True si el acceso quedó desbloqueado (nuevo o ya existía)
                  False si el afecto aún no alcanza el umbral

        Uso recomendado: llamar al final de cada evento de personaje.
            $ fn_stats_verificar_acceso("roxy")
        """

        # Umbrales de afecto para desbloqueo de cuarto
        umbrales = {
            "roxy":   20,
            "celine": 35,
            "luna":   45,
        }

        # Si el personaje no está en la tabla, avisar y salir
        if personaje not in umbrales:
            fn_debug_log(
                "[stats] fn_stats_verificar_acceso: personaje desconocido '{}'".format(
                    personaje
                )
            )
            return False

        # Leer el afecto actual del personaje
        afecto_actual = getattr(store, "stats_" + personaje + "_afecto", 0)

        # Leer si el acceso ya estaba activo (una vez True, nunca vuelve a False)
        nombre_acceso = "acceso_cuarto_" + personaje
        acceso_actual = getattr(store, nombre_acceso, False)

        # Si ya tenía acceso, no hace falta nada más
        if acceso_actual:
            return True

        # Verificar si alcanzó el umbral
        if afecto_actual >= umbrales[personaje]:
            # Desbloquear el acceso — setattr activa el guardado
            setattr(store, nombre_acceso, True)
            fn_debug_log(
                "[stats] Acceso desbloqueado: cuarto de {} (afecto={})".format(
                    personaje, afecto_actual
                )
            )
            return True

        # Umbral no alcanzado
        return False


    def fn_debug_log(mensaje):
        """
        Imprime un mensaje en la consola de Ren'Py solo si DEBUG_MODE es True.
        Usar para trazabilidad durante desarrollo — no afecta builds de release.

        Parámetros:
            mensaje (str): texto a mostrar en consola

        Nota: DEBUG_MODE está definido en este mismo archivo como define.
        """
        if DEBUG_MODE:
            renpy.log(mensaje)


##############################################################################
# CONSTANTES DEL MÓDULO
# Usar define — NO se guardan en saves. Son valores fijos que nunca cambian.
##############################################################################

# Modo de desarrollo — False en producción, True durante pruebas locales
# ADVERTENCIA sección 14: los define no se guardan. Cambiar aquí directamente.
define DEBUG_MODE = False


##############################################################################
# STATS DE PERSONAJES
# Módulo responsable: stats.rpy (declaración)
# Modificar solo con: fn_stats_modificar(personaje, stat, delta)
# Keyword: default — se guardan en save, participan en rollback
##############################################################################

# --- Celine (prima del protagonista) ---
# Valores iniciales bajos: hay historia familiar pero también distancia reciente
default stats_celine_afecto     = 15   # rango 0-100
default stats_celine_confianza  = 10   # rango 0-100
default stats_celine_corrupcion = 5    # rango 0-100, solo sube desde eventos

# --- Roxy (ex-algo del protagonista) ---
# Afecto y corrupción más altos: hay tensión no resuelta e historia compartida
default stats_roxy_afecto       = 25   # rango 0-100
default stats_roxy_confianza    = 15   # rango 0-100
default stats_roxy_corrupcion   = 15   # rango 0-100

# --- Luna (la observadora) ---
# Valores medios: te conoce más de lo que aparenta, pero guarda distancia
default stats_luna_afecto       = 20   # rango 0-100
default stats_luna_confianza    = 10   # rango 0-100
default stats_luna_corrupcion   = 10   # rango 0-100


##############################################################################
# STATS DEL PROTAGONISTA
# prot_nombre: se asigna en script.rpy durante el setup inicial
# prot_energia_actual: lo gestiona time.rpy al avanzar franjas
# prot_dinero: lo gestiona economy.rpy en compras/trabajo
# Keyword: default
##############################################################################

# Nombre elegible por el jugador — valor por defecto hasta que se ingrese uno
default prot_nombre         = "Kai"

# Encanto: desbloquea opciones de diálogo adicionales al subir
default prot_encanto        = 10    # rango 0-100

# Energía: cuántas acciones puede hacer el protagonista por franja horaria
default prot_energia_max    = 6     # rango 6-10, sube con progreso
default prot_energia_actual = 6     # rango 0-prot_energia_max


# Dinero inicial en pesos de Vallanova
# NOTA: prot_dinero se declara aquí pero economy.rpy es responsable de modificarlo.
# Se declara en stats.rpy porque conceptualmente es un stat del protagonista.
default prot_dinero         = 500   # sin límite superior


##############################################################################
# PERSONALIDAD DEL JUGADOR
# Sistema de arquetipo acumulativo — no tiene límite superior.
# El arquetipo dominante es el que tiene mayor valor al comparar los tres.
# Se suman desde los choices en labels de evento.
# Keyword: default
##############################################################################

# Puntos de arquetipo romántico (opciones tiernas, detallistas, sentimentales)
default pers_romantico    = 0

# Puntos de arquetipo atrevido (opciones directas, coquetas, de riesgo)
default pers_atrevido     = 0

# Puntos de arquetipo respetuoso (opciones prudentes, empáticas, de límites)
default pers_respetuoso   = 0


##############################################################################
# ACCESO A CUARTOS
# Una vez True, NUNCA vuelve a False — ver GDD y VARIABLES_GLOBALES.md sección 7.
# La verificación se hace con fn_stats_verificar_acceso(personaje).
# El uso (entrar al cuarto) está en map.rpy.
# Keyword: default
##############################################################################

# Acceso al cuarto de Roxy — se desbloquea con afecto >= 20
default acceso_cuarto_roxy   = False

# Acceso al cuarto de Celine — se desbloquea con afecto >= 35
default acceso_cuarto_celine = False

# Acceso al cuarto de Luna — se desbloquea con afecto >= 45
default acceso_cuarto_luna   = False
