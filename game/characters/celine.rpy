##############################################################################
# APARTMENT SIM — PERSONAJE CELINE
# Archivo: game/characters/celine.rpy
# Módulo: Definición de Character + diálogos cotidianos de Celine
# Versión: 1.0
# Última modificación: 31/05/2026
# Dependencias:
#   game/systems/stats.rpy   (stats_celine_*, prot_nombre)
#   game/systems/time.rpy    (time_franja, time_es_finde)
#   game/systems/mood.rpy    (mood_celine)
# Descripción:
#   Define el Character() de Celine con su alias "cel".
#   Contiene los diálogos cotidianos situacionales (dial_celine_*)
#   que el mapa llama según franja horaria y mood.
#   NO contiene eventos narrativos ni actos — eso va en celine_events.rpy.
#   Perfil: prima del protagonista, estudiante universitaria, disciplinada,
#   se sonroja fácil, barrera emocional alta pero se rompe lento.
##############################################################################


##############################################################################
# DEFINICIÓN DEL PERSONAJE
# Usar define — Character() es una constante, no se guarda en saves.
# Fuente: renpy.org/doc/html/dialogue.html
# Color rosa suave — definido en ESTANDARES.md sección 5.
##############################################################################

define cel = Character("Celine", color="#E8A0BF")


##############################################################################
# DIÁLOGOS COTIDIANOS — MAÑANA
# Llamados desde map.rpy cuando time_franja == "manana"
# Entre semana Celine no está disponible en mañana (universidad),
# estos labels se usan solo en finde o si un evento la retiene en casa.
##############################################################################

label dial_celine_manana_normal:
    cel "Mmh... ¿ya te levantaste? Yo todavía estoy medio dormida."
    cel "¿Quieres café? Puse a calentar agua hace un rato."
    return

label dial_celine_manana_feliz:
    cel "¡Buenos días! Hoy me desperté con ganas de hacer algo rico para desayunar."
    cel "¿Tienes hambre? Puedo hacer tostadas con lo que quedó ayer."
    return

label dial_celine_manana_cansada:
    cel "..."
    cel "No me hables todavía. Necesito mi café primero."
    return

label dial_celine_manana_estresada:
    cel "Tengo entrega hoy. No puedo distraerme, por favor."
    return

label dial_celine_manana_traviesa:
    cel "Oye... ¿a qué hora te dormiste anoche? Te escuché llegar tarde."
    cel "No te estaba esperando, ¿eh? Solo... no pude dormir bien."
    return


##############################################################################
# DIÁLOGOS COTIDIANOS — TARDE
# Entre semana Celine está en la universidad — solo disponible en finde.
##############################################################################

label dial_celine_tarde_normal:
    cel "Acabo de llegar. La tarde estuvo larga."
    cel "Voy a revisar mis apuntes un rato. ¿Necesitas algo?"
    return

label dial_celine_tarde_feliz:
    cel "¡Oye! El profesor anuló el parcial de mañana. Me siento libre por primera vez en semanas."
    cel "Casi nunca tengo tardes libres. No sé ni qué hacer conmigo misma."
    return

label dial_celine_tarde_cansada:
    cel "Cuatro horas de clase seguidas. Cuatro."
    cel "No me preguntes nada importante ahora mismo, por favor."
    return

label dial_celine_tarde_estresada:
    cel "Tengo que estudiar. No es personal, es que... tengo mucho encima."
    cel "Ya hablamos después, ¿sí?"
    return

label dial_celine_tarde_traviesa:
    cel "¿Sabes cuánto tiempo llevo sin hacer algo que no sea estudiar?"
    cel "A veces pienso que necesito que alguien me obligue a tomar un descanso."
    return


##############################################################################
# DIÁLOGOS COTIDIANOS — NOCHE
# Franja principal de disponibilidad de Celine entre semana.
##############################################################################

label dial_celine_noche_normal:
    cel "Estaba leyendo. ¿Qué pasa?"
    return

label dial_celine_noche_feliz:
    cel "Hoy fue un buen día, la verdad. No pasa seguido."
    cel "¿Tú cómo estás? No te pregunto mucho eso, lo sé."
    return

label dial_celine_noche_cansada:
    cel "Estoy agotada pero no me da sueño. Qué cosa más rara."
    cel "Me pasa cuando tengo muchas cosas en la cabeza."
    return

label dial_celine_noche_estresada:
    cel "No puedo dejar de pensar en la defensa del jueves."
    cel "Sé que voy a estar bien pero... no me lo termino de creer."
    return

label dial_celine_noche_traviesa:
    cel "¿Qué haces despierto tan tarde?"
    cel "Yo tampoco debería estarlo, pero aquí estamos."
    return


##############################################################################
# DIÁLOGOS COTIDIANOS — MADRUGADA
# Celine raramente está disponible — si aparece, hay algo pasando.
##############################################################################

label dial_celine_madrugada_normal:
    cel "¿No puedes dormir?"
    cel "Yo tampoco. A veces la cabeza no para."
    return

label dial_celine_madrugada_cansada:
    cel "Son las... no quiero ni ver la hora."
    cel "Mañana me voy a arrepentir de esto."
    return

label dial_celine_madrugada_traviesa:
    cel "Nos vamos a ver muy mal mañana, ¿sabes?"
    cel "Y aun así sigo aquí. Qué raro."
    return


##############################################################################
# LABEL DISPATCHER — DIÁLOGOS COTIDIANOS
# map.rpy llama a este label para obtener el diálogo correcto según
# la franja y el mood actuales. No hay que buscar el label manualmente.
##############################################################################

label dial_celine_cotidiano:
    # Construir el nombre del label según franja y mood actuales
    # Formato: dial_celine_[franja]_[mood]
    $ tmp_label_celine = "dial_celine_{}_{}".format(time_franja, mood_celine)

    # Verificar que el label existe antes de hacer jump
    # Si no existe (combinación no implementada), usar el normal de esa franja
    if renpy.has_label(tmp_label_celine):
        call expression tmp_label_celine
    else:
        $ tmp_label_celine_fallback = "dial_celine_{}_normal".format(time_franja)
        if renpy.has_label(tmp_label_celine_fallback):
            call expression tmp_label_celine_fallback
        else:
            # Fallback final — nunca debería llegar aquí
            cel "Hola."

    return
