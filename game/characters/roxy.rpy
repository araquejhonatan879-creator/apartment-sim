##############################################################################
# APARTMENT SIM — PERSONAJE ROXY
# Archivo: game/characters/roxy.rpy
# Módulo: Definición de Character + diálogos cotidianos de Roxy
# Versión: 1.0
# Última modificación: 31/05/2026
# Dependencias:
#   game/systems/stats.rpy   (stats_roxy_*, prot_nombre)
#   game/systems/time.rpy    (time_franja, time_es_finde)
#   game/systems/mood.rpy    (mood_roxy)
# Descripción:
#   Define el Character() de Roxy con su alias "rox".
#   Contiene los diálogos cotidianos situacionales (dial_roxy_*)
#   que el mapa llama según franja horaria y mood.
#   NO contiene eventos narrativos ni actos — eso va en roxy_events.rpy.
#   Perfil: ex-algo del protagonista, artista, trabaja en bar de noche,
#   fachada ruda que esconde inseguridad, directa y sarcástica,
#   tensión no resuelta con el protagonista desde el primer día.
##############################################################################


##############################################################################
# DEFINICIÓN DEL PERSONAJE
# Color coral — definido en ESTANDARES.md sección 5.
##############################################################################

define rox = Character("Roxy", color="#FF6B6B")


##############################################################################
# DIÁLOGOS COTIDIANOS — MAÑANA
# Roxy está disponible en mañana (duerme de día cuando no trabaja).
# Entre semana trabaja tarde/noche — la mañana es su tiempo libre.
##############################################################################

label dial_roxy_manana_normal:
    rox "¿Qué quieres?"
    rox "Es temprano. No esperes mucha conversación de mi parte."
    return

label dial_roxy_manana_feliz:
    rox "Ey. Hoy no trabajo hasta las seis. Es raro tener mañana libre."
    rox "No me mires así, solo estoy de buen humor. Pasa a veces."
    return

label dial_roxy_manana_cansada:
    rox "Llegué hace dos horas. No me hables."
    return

label dial_roxy_manana_estresada:
    rox "Tengo cosas que resolver. Ahora no es buen momento."
    return

label dial_roxy_manana_traviesa:
    rox "Mira quién madrugó."
    rox "¿O no dormiste? Porque tienes esa cara."
    return


##############################################################################
# DIÁLOGOS COTIDIANOS — TARDE
# Entre semana Roxy se está preparando para el trabajo — disponibilidad baja.
# En finde es su franja más relajada.
##############################################################################

label dial_roxy_tarde_normal:
    rox "Estoy a punto de salir. ¿Necesitas algo rápido?"
    return

label dial_roxy_tarde_feliz:
    rox "Hoy no hay prisa. Raro pero bienvenido."
    rox "¿Tienes algún plan o solo estás dando vueltas?"
    return

label dial_roxy_tarde_cansada:
    rox "No dormí suficiente. Y tengo que trabajar en tres horas. Genial."
    return

label dial_roxy_tarde_estresada:
    rox "Oye, ahora no. En serio."
    return

label dial_roxy_tarde_traviesa:
    rox "¿Vas a quedarte mirándome o me vas a decir algo?"
    return


##############################################################################
# DIÁLOGOS COTIDIANOS — NOCHE
# Roxy está trabajando entre semana — disponible solo en finde.
# Si aparece disponible en noche entre semana es por evento especial.
##############################################################################

label dial_roxy_noche_normal:
    rox "Creí que ya estarías dormido."
    rox "¿Qué haces despierto?"
    return

label dial_roxy_noche_feliz:
    rox "Hoy salí temprano del bar. El dueño cerró antes."
    rox "No me acostumbro a tener noches libres."
    return

label dial_roxy_noche_cansada:
    rox "Siete horas de pie. Los pies me matan."
    rox "No me pidas nada."
    return

label dial_roxy_noche_estresada:
    rox "Tuve una noche de mierda. No es cosa tuya."
    rox "Solo... dame un rato."
    return

label dial_roxy_noche_traviesa:
    rox "Qué coincidencia encontrarte aquí a estas horas."
    rox "¿O no es tan coincidencia?"
    return


##############################################################################
# DIÁLOGOS COTIDIANOS — MADRUGADA
# Roxy llega del trabajo — es cuando más está en casa entre semana.
##############################################################################

label dial_roxy_madrugada_normal:
    rox "Acabo de llegar. El bar estuvo lleno toda la noche."
    rox "¿Por qué sigues despierto?"
    return

label dial_roxy_madrugada_feliz:
    rox "Buenas propinas hoy. No pasa seguido."
    rox "¿Tienes algo de comer? Tengo hambre."
    return

label dial_roxy_madrugada_cansada:
    rox "No puedo más. Me caigo de sueño."
    rox "Hablamos mañana."
    return

label dial_roxy_madrugada_traviesa:
    rox "Llevas despierto esperándome, ¿verdad?"
    rox "No tienes que negarlo. Es tarde para mentiras."
    return


##############################################################################
# LABEL DISPATCHER — DIÁLOGOS COTIDIANOS
##############################################################################

label dial_roxy_cotidiano:
    $ tmp_label_roxy = "dial_roxy_{}_{}".format(time_franja, mood_roxy)

    if renpy.has_label(tmp_label_roxy):
        call expression tmp_label_roxy
    else:
        $ tmp_label_roxy_fallback = "dial_roxy_{}_normal".format(time_franja)
        if renpy.has_label(tmp_label_roxy_fallback):
            call expression tmp_label_roxy_fallback
        else:
            rox "..."

    return
