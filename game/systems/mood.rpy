##############################################################################
# APARTMENT SIM — SISTEMA DE ESTADO DE ÁNIMO
# Archivo: game/systems/mood.rpy
# Módulo: Estado de ánimo diario por personaje
# Versión: 1.0
# Última modificación: 31/05/2026
# Dependencias:
#   game/systems/stats.rpy  (stats_*_afecto, stats_*_confianza)
#   game/systems/time.rpy   (time_es_finde, time_franja)
# Descripción:
#   Calcula y almacena el estado de ánimo de cada personaje (mood_*).
#   El mood depende de sus stats actuales, la franja horaria y si es
#   fin de semana. Se recalcula llamando fn_mood_calcular() desde
#   fn_tiempo_avanzar_franja() o al inicio de cada label de evento.
#   El mood afecta qué sprite se muestra y qué diálogos están disponibles.
##############################################################################


##############################################################################
# FUNCIONES PYTHON DEL MÓDULO
##############################################################################

init python:

    def fn_mood_calcular(personaje):
        """
        Recalcula el estado de ánimo de un personaje y lo guarda en mood_*.

        El mood se determina por una combinación de:
            - Afecto actual (principal)
            - Confianza actual (modificador)
            - Franja horaria (contexto)
            - Si es fin de semana (modificador positivo general)

        Valores posibles de mood:
            "normal"    → estado base, sin modificadores especiales
            "feliz"     → afecto alto + franja favorable
            "cansada"   → franja de madrugada o noche con afecto bajo
            "estresada" → confianza baja + afecto bajo
            "traviesa"  → afecto alto + confianza alta + noche/finde

        Parámetros:
            personaje (str): "celine", "roxy" o "luna"

        Retorna:
            str: el mood calculado (también lo guarda en store.mood_*)

        Uso recomendado: llamar al avanzar franja o al inicio de un evento.
            $ fn_mood_calcular("celine")
            $ fn_mood_calcular("roxy")
            $ fn_mood_calcular("luna")
        """

        # Leer stats necesarios desde el store
        afecto     = getattr(store, "stats_" + personaje + "_afecto",    0)
        confianza  = getattr(store, "stats_" + personaje + "_confianza", 0)
        franja     = store.time_franja
        es_finde   = store.time_es_finde

        # --- Algoritmo de mood ---
        # Se evalúan condiciones en orden de prioridad (la primera que se
        # cumpla determina el mood). Orden: traviesa > feliz > estresada >
        # cansada > normal.

        mood_resultado = "normal"

        # Traviesa: afecto y confianza altos, en contexto nocturno o finde
        # Representa que el personaje está cómodo y en modo coqueto/juguetón
        if (afecto >= 60 and confianza >= 50 and
                (franja in ("noche", "madrugada") or es_finde)):
            mood_resultado = "traviesa"

        # Feliz: afecto alto, cualquier franja, especialmente finde o tarde
        elif afecto >= 50 and (es_finde or franja in ("tarde", "noche")):
            mood_resultado = "feliz"

        # Feliz también con afecto moderado-alto en cualquier contexto
        elif afecto >= 65:
            mood_resultado = "feliz"

        # Estresada: confianza muy baja — no se fía del protagonista
        elif confianza <= 15 and afecto <= 30:
            mood_resultado = "estresada"

        # Cansada: madrugada siempre cansa (si no es traviesa), o afecto
        # bajo combinado con franja de mañana (aún no se despabila)
        elif franja == "madrugada":
            mood_resultado = "cansada"

        elif franja == "manana" and afecto <= 25:
            mood_resultado = "cansada"

        # Normal: todo lo demás
        # (ya está asignado como valor por defecto arriba)

        # Guardar en el store — esto activa el guardado automático
        setattr(store, "mood_" + personaje, mood_resultado)

        fn_debug_log(
            "[mood] {} → {} (afecto={}, confianza={}, franja={}, finde={})".format(
                personaje, mood_resultado, afecto, confianza, franja, es_finde
            )
        )

        return mood_resultado


    def fn_mood_calcular_todos():
        """
        Recalcula el mood de los tres personajes de una sola vez.
        Llamar desde fn_tiempo_avanzar_franja() al cambiar de franja.

        Retorna:
            dict: {"celine": mood, "roxy": mood, "luna": mood}

        Uso:
            $ fn_mood_calcular_todos()
        """

        resultado = {}
        for personaje in ("celine", "roxy", "luna"):
            resultado[personaje] = fn_mood_calcular(personaje)

        fn_debug_log("[mood] Recálculo completo: {}".format(resultado))
        return resultado


    def fn_mood_obtener_sprite(personaje):
        """
        Retorna el nombre de imagen del sprite correspondiente al mood
        actual del personaje, siguiendo la convención de nombres de assets
        definida en ESTANDARES.md sección 9.

        Formato: personaje_outfit1_mood
        (outfit1 es el outfit base — expandir en Fase 5 con sistema de outfits)

        Parámetros:
            personaje (str): "celine", "roxy" o "luna"

        Retorna:
            str: nombre de imagen para usar en show/scene
                 ej: "celine_outfit1_normal", "roxy_outfit1_feliz"

        Uso en labels:
            $ nombre_sprite = fn_mood_obtener_sprite("celine")
            show expression nombre_sprite
        """

        mood_actual = getattr(store, "mood_" + personaje, "normal")

        # Formato de nombre definido en ESTANDARES.md sección 9:
        # [personaje]_[outfit]_[emocion]
        nombre_sprite = "{}_outfit1_{}".format(personaje, mood_actual)

        return nombre_sprite


##############################################################################
# VARIABLES DEL MÓDULO
# Keyword: default — se guardan en save, participan en rollback
# Valores válidos: "normal" | "feliz" | "cansada" | "estresada" | "traviesa"
##############################################################################

# Estado de ánimo de Celine — se recalcula en cada avance de franja
default mood_celine = "normal"

# Estado de ánimo de Roxy — se recalcula en cada avance de franja
default mood_roxy   = "normal"

# Estado de ánimo de Luna — se recalcula en cada avance de franja
default mood_luna   = "normal"
