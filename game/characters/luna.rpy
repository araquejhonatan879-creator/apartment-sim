##############################################################################
# APARTMENT SIM — PERSONAJE LUNA
# Archivo: game/characters/luna.rpy
# Módulo: Definición de Character + diálogos cotidianos de Luna
# Versión: 1.0
# Última modificación: 31/05/2026
# Dependencias:
#   game/systems/stats.rpy   (stats_luna_*, prot_nombre)
#   game/systems/time.rpy    (time_franja, time_es_finde)
#   game/systems/mood.rpy    (mood_luna)
# Descripción:
#   Define el Character() de Luna con su alias "lun".
#   Contiene los diálogos cotidianos situacionales (dial_luna_*)
#   que el mapa llama según franja horaria y mood.
#   NO contiene eventos narrativos ni actos — eso va en luna_events.rpy.
#   Perfil: la observadora, trabaja remoto, lectora compulsiva,
#   habla poco pero cada frase tiene peso, conoce más de todos de lo
#   que aparenta, su relación con el protagonista es la más lenta
#   pero potencialmente la más profunda.
##############################################################################


##############################################################################
# DEFINICIÓN DEL PERSONAJE
# Color azul claro — definido en ESTANDARES.md sección 5.
##############################################################################

define lun = Character("Luna", color="#A8D8EA")


##############################################################################
# DIÁLOGOS COTIDIANOS — MAÑANA
# Luna trabaja remoto en mañana — modo enfocado, no interrumpir.
# Disponible en finde o si el afecto es suficientemente alto.
##############################################################################

label dial_luna_manana_normal:
    lun "Estoy en medio de algo."
    lun "¿Puedes volver en un rato?"
    return

label dial_luna_manana_feliz:
    lun "Terminé temprano hoy."
    lun "¿Quieres té? Puse la tetera hace un momento."
    return

label dial_luna_manana_cansada:
    lun "No dormí bien."
    lun "Voy a intentar trabajar de todas formas."
    return

label dial_luna_manana_estresada:
    lun "Tengo una entrega en dos horas. Por favor."
    return

label dial_luna_manana_traviesa:
    lun "Llevas un rato parado ahí."
    lun "¿Querías decirme algo o solo pasabas?"
    return


##############################################################################
# DIÁLOGOS COTIDIANOS — TARDE
# Franja de pausa de Luna — la más disponible del día entre semana.
##############################################################################

label dial_luna_tarde_normal:
    lun "Me tomé un descanso."
    lun "¿Cómo va tu día?"
    return

label dial_luna_tarde_feliz:
    lun "Hoy el trabajo fluyó bien. Esas tardes son raras."
    lun "Iba a salir a caminar. ¿Quieres venir?"
    return

label dial_luna_tarde_cansada:
    lun "Llevo horas frente a la pantalla."
    lun "Necesito aire pero no tengo energía para salir. Paradójico."
    return

label dial_luna_tarde_estresada:
    lun "Tuve una llamada difícil. Dame un momento."
    return

label dial_luna_tarde_traviesa:
    lun "Te noto diferente hoy."
    lun "No lo digo como crítica. Solo... lo noté."
    return


##############################################################################
# DIÁLOGOS COTIDIANOS — NOCHE
# Luna lee por las noches — disponible y más abierta que durante el día.
##############################################################################

label dial_luna_noche_normal:
    lun "Estaba leyendo."
    lun "¿Qué necesitas?"
    return

label dial_luna_noche_feliz:
    lun "Este libro es bueno. Hacía tiempo que no encontraba uno así."
    lun "¿Tú lees mucho?"
    return

label dial_luna_noche_cansada:
    lun "Debería dormir pero el libro no me deja."
    lun "Es un problema que tengo."
    return

label dial_luna_noche_estresada:
    lun "Estoy intentando desconectarme con esto."
    lun "¿Podemos hablar mañana?"
    return

label dial_luna_noche_traviesa:
    lun "Las noches aquí son raras. Todo el mundo despierto a esta hora."
    lun "Aunque supongo que yo no tengo excusa para quejarme."
    return


##############################################################################
# DIÁLOGOS COTIDIANOS — MADRUGADA
# Luna raramente está despierta — si lo está, algo la mantiene en vela.
##############################################################################

label dial_luna_madrugada_normal:
    lun "No puedo dormir."
    lun "Tú tampoco, al parecer."
    return

label dial_luna_madrugada_cansada:
    lun "Voy a intentarlo otra vez."
    lun "Buenas noches."
    return

label dial_luna_madrugada_traviesa:
    lun "¿Sabes qué hora es?"
    lun "Sí, yo también lo sé. Y aquí seguimos."
    return


##############################################################################
# LABEL DISPATCHER — DIÁLOGOS COTIDIANOS
##############################################################################

label dial_luna_cotidiano:
    $ tmp_label_luna = "dial_luna_{}_{}".format(time_franja, mood_luna)

    if renpy.has_label(tmp_label_luna):
        call expression tmp_label_luna
    else:
        $ tmp_label_luna_fallback = "dial_luna_{}_normal".format(time_franja)
        if renpy.has_label(tmp_label_luna_fallback):
            call expression tmp_label_luna_fallback
        else:
            lun "..."

    return
