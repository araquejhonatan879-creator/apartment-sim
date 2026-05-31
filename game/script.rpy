# ============================================================
# APARTMENT SIM — script.rpy
# Día 1: Llegada al apartamento + Tutorial HUD
# ============================================================
# ESTRUCTURA:
#   - label start          : punto de entrada, nombre del MC
#   - label dia1_llegada   : secuencia narrativa lineal del Día 1
#   - label tutorial_hud   : explicación interactiva de la interfaz
#   - label fin_dia1       : cierre del día, stats iniciales, paso al juego libre
#   - label game_loop      : bucle principal post-día-1
# ============================================================

# ----------------------------------------------------------
# INICIO DEL JUEGO — Pantalla de nombre
# ----------------------------------------------------------
label start:

    # Música de título (placeholder hasta tener assets)
    # play music "audio/menu_theme.ogg" fadein 2.0

    scene black with fade

    # Pantalla para elegir nombre del protagonista
    $ mc_nombre = renpy.input(
        "¿Cuál es tu nombre?",
        default="Mateo",
        length=20
    )
    $ mc_nombre = mc_nombre.strip()
    if mc_nombre == "":
        $ mc_nombre = "Mateo"

    # Guardamos el nombre en la variable del sistema
    $ mc_nombre = mc_nombre

    jump dia1_llegada


# ----------------------------------------------------------
# DÍA 1 — LLEGADA AL APARTAMENTO
# Secuencia lineal sin acciones libres — solo narrativa
# ----------------------------------------------------------
label dia1_llegada:

    # Inicializamos el día 1 manualmente (time.rpy lo gestiona desde día 2)
    $ dia_actual = 1
    $ dia_nombre = "Lunes"
    $ franja_actual = "tarde"
    $ acciones_restantes = 2

    # ----------------------------------------------------------
    # ESCENA 1 — La puerta del apartamento
    # ----------------------------------------------------------
    scene bg_pasillo_exterior with fade
    # (bg_pasillo_exterior: placeholder — fondo del pasillo antes de entrar)

    show music_ambient  # placeholder visual hasta tener audio

    narrator "Cuarto piso. Edificio B. Vallanova."
    narrator "La maleta pesa más de lo que debería para alguien que dice que no trajo mucho."
    narrator "El ascensor no funciona."

    pause 1.0

    narrator "Toco el timbre."

    # Pausa dramática
    pause 1.5

    scene bg_puerta_apartamento with dissolve

    # Celine abre la puerta
    show celine neutral at center with dissolve

    c "El cuarto es el del fondo."
    c "No hagas ruido después de las 11."

    # Se da vuelta y desaparece — efecto de movimiento
    hide celine with dissolve

    narrator "Eso es todo. Sin bienvenida. Sin pregunta de si tuve buen viaje."
    narrator "Celine siempre fue así — economía de palabras, eficiencia de hielo."

    pause 0.5

    # ----------------------------------------------------------
    # ESCENA 2 — La cocina / Roxy
    # ----------------------------------------------------------
    scene bg_cocina_dia with dissolve

    # Roxy sale de la cocina
    show roxy feliz at center with dissolve

    r "¡LLEGASTE!"
    r "Pensé que era mañana. ¿Comiste?"

    narrator "Tiene una cuchara en la mano. Una mancha de algo en la camiseta. Sonríe como si llevara semanas esperando este momento."

    r "Estoy haciendo algo que podría ser pasta. O podría ser un error de cálculo. Ya vemos."

    # Abrazo sin pedir permiso — descrito por narrador
    narrator "Me abraza sin preguntar. Un abrazo de esos que no esperabas y que igual te descolocan."

    hide roxy with dissolve

    narrator "Roxy. Siempre Roxy."
    narrator "Caos en forma de persona."

    pause 0.5

    # ----------------------------------------------------------
    # ESCENA 3 — La sala / Luna
    # ----------------------------------------------------------
    scene bg_sala_dia with dissolve

    show luna neutral at left with dissolve

    narrator "En el sofá, con un libro, está Luna."
    narrator "Levanta la vista."
    narrator "Me mira exactamente tres segundos."

    pause 1.5

    l "Hola."

    narrator "Vuelve al libro."

    hide luna with dissolve

    narrator "Tres segundos y una palabra. Para Luna, eso es una conversación completa."

    pause 0.5

    # ----------------------------------------------------------
    # ESCENA 4 — El cuarto del protagonista
    # ----------------------------------------------------------
    scene bg_cuarto_mc_dia with dissolve

    narrator "El cuarto del fondo."
    narrator "Cama. Escritorio. Una ventana que da a la calle."
    narrator "Desde aquí se escucha a Roxy cantando algo mal en la cocina."

    pause 0.8

    narrator "Dejo la maleta en el suelo."

    pause 0.5

    narrator "Esto es real. Voy a vivir aquí."
    narrator "Con Celine. Con Roxy. Con Luna."
    narrator "Con tres personas que conozco desde que era un crío y que de alguna forma terminaron todas en el mismo piso."

    pause 1.0

    narrator "Bien."

    # Transición al tutorial
    jump tutorial_hud


# ----------------------------------------------------------
# TUTORIAL HUD — Explicación interactiva de la interfaz
# Se interrumpe la narrativa con cajas de texto especiales
# ----------------------------------------------------------
label tutorial_hud:

    scene bg_cuarto_mc_dia with dissolve

    # Activamos el HUD explícitamente para que sea visible
    $ hud_visible = True

    pause 0.5

    # --- TUTORIAL: FRANJAS HORARIAS ---
    show screen tutorial_box("⏰ FRANJAS HORARIAS",
        "El día se divide en 4 franjas:\nMañana · Tarde · Noche · Madrugada\n\nCada franja tienes acciones disponibles.\nCuando se acaban, avanza la franja.")

    pause 0.2
    $ renpy.input("", default="", length=0)  # espera click
    hide screen tutorial_box

    # --- TUTORIAL: ACCIONES ---
    show screen tutorial_box("⚡ ACCIONES",
        "Los círculos junto al reloj son tu energía.\nCada acción que tomes gasta uno.\n\nDormir bien recupera todo para el día siguiente.")

    pause 0.2
    $ renpy.input("", default="", length=0)
    hide screen tutorial_box

    # --- TUTORIAL: STATS DE PERSONAJES ---
    show screen tutorial_box("💜 STATS DE PERSONAJES",
        "Cada chica tiene tres barras:\n\nAfecto — qué tanto le importas\nConfianza — qué tanto cree en ti\nCorrupción — qué tan abierta está a escalar")

    pause 0.2
    $ renpy.input("", default="", length=0)
    hide screen tutorial_box

    # --- TUTORIAL: ARMONÍA ---
    show screen tutorial_box("🏠 ARMONÍA DEL APARTAMENTO",
        "La barra verde abajo es la Armonía global.\nRepresenta el ambiente entre todas.\n\nSi baja mucho, las cosas se complican.\nSi se mantiene alta, los eventos grupales aparecen.")

    pause 0.2
    $ renpy.input("", default="", length=0)
    hide screen tutorial_box

    # --- TUTORIAL: DINERO ---
    show screen tutorial_box("💵 DINERO",
        "Empiezas con $500.\nPuedes trabajar, completar quests o salir con ellas.\n\nLos regalos correctos importan más que los caros.")

    pause 0.2
    $ renpy.input("", default="", length=0)
    hide screen tutorial_box

    jump fin_dia1


# ----------------------------------------------------------
# FIN DEL DÍA 1 — Cierre narrativo y stats iniciales
# ----------------------------------------------------------
label fin_dia1:

    scene bg_cuarto_mc_noche with fade

    narrator "La noche llega sin avisar."
    narrator "Desde la sala se escucha el televisor. Voces bajas. El apartamento ya no está en silencio."
    narrator "Hay algo extraño en estar en un lugar nuevo que de alguna forma ya conocías."

    pause 0.8

    narrator "Mañana empieza de verdad."

    # Aplicamos los stats iniciales del Día 1 según GDD_NARRATIVA
    python:
        # Stats iniciales post-día-1 (definidos en GDD_NARRATIVA)
        celine_afecto    = 5
        celine_confianza = 5
        celine_corrupcion = 0

        roxy_afecto      = 15
        roxy_confianza   = 10
        roxy_corrupcion  = 0

        luna_afecto      = 5
        luna_confianza   = 5
        luna_corrupcion  = 0

        # MC stats iniciales
        mc_encanto       = 10
        mc_energia_max   = 6
        mc_energia       = 6
        mc_dinero        = 500

        # Armonía inicial
        armonia          = 70

        # Día completado
        dia_actual       = 2
        franja_actual    = "mañana"
        acciones_restantes = acciones_por_franja()

        # Autosave del fin del día 1
        renpy.save_persistent()

    # Mensaje de autosave visual
    show screen notificacion_hud("Partida guardada automáticamente — Día 1 completado")
    pause 1.5
    hide screen notificacion_hud

    scene black with fade

    pause 1.0

    # Fade al título del día siguiente
    show text "Día 2 — Mañana" with dissolve
    pause 1.5
    hide text with dissolve

    jump game_loop


# ----------------------------------------------------------
# GAME LOOP — Bucle principal del juego libre (post-día-1)
# Aquí arranca la jugabilidad sandbox
# ----------------------------------------------------------
label game_loop:

    # Generamos moods del día actual
    python:
        generar_moods()
        # Autosave al inicio de cada día (también lo hace time.rpy)
        renpy.save(renpy.slot_name_for_autosave())

    # Mostramos la pantalla de inicio de día
    call screen pantalla_inicio_dia

    # Después del intro del día, vamos al mapa
    jump mapa_principal


# ----------------------------------------------------------
# PANTALLA DE INICIO DE DÍA (screen auxiliar inline)
# Se define aquí para no depender de un archivo separado
# hasta que map.rpy y screens adicionales estén listos
# ----------------------------------------------------------
screen pantalla_inicio_dia():
    modal True
    zorder 200

    add "gui/overlay/confirm.png"  # fondo semitransparente

    vbox:
        xalign 0.5
        yalign 0.4
        spacing 20

        text "[dia_nombre], Día [dia_actual]":
            xalign 0.5
            size 52
            color "#e2e8f0"
            bold True

        text "Estado de ánimo hoy:":
            xalign 0.5
            size 24
            color "#94a3b8"

        hbox:
            xalign 0.5
            spacing 40

            # Celine
            vbox:
                xalign 0.5
                text "Celine":
                    xalign 0.5
                    size 18
                    color "#818cf8"
                text "[celine_mood]":
                    xalign 0.5
                    size 22
                    color "#e2e8f0"

            # Roxy
            vbox:
                xalign 0.5
                text "Roxy":
                    xalign 0.5
                    size 18
                    color "#fb923c"
                text "[roxy_mood]":
                    xalign 0.5
                    size 22
                    color "#e2e8f0"

            # Luna
            vbox:
                xalign 0.5
                text "Luna":
                    xalign 0.5
                    size 18
                    color "#c084fc"
                text "[luna_mood]":
                    xalign 0.5
                    size 22
                    color "#e2e8f0"

        textbutton "Empezar el día":
            xalign 0.5
            action Return()
            style "confirm_button"


# ----------------------------------------------------------
# SCREEN — Tutorial box (usado en tutorial_hud)
# Caja flotante centrada con título y texto
# ----------------------------------------------------------
screen tutorial_box(titulo, contenido):
    zorder 300

    frame:
        xalign 0.5
        yalign 0.85
        xsize 760
        padding (30, 20)
        background "#1e293bdd"

        vbox:
            spacing 12

            text titulo:
                size 22
                color "#f8fafc"
                bold True

            text contenido:
                size 18
                color "#cbd5e1"
                line_leading 6

            text "[ Haz clic para continuar ]":
                xalign 1.0
                size 14
                color "#64748b"


# ----------------------------------------------------------
# SCREEN — Notificación HUD (usada en fin_dia1 y otros)
# Mensaje temporal en esquina inferior
# ----------------------------------------------------------
screen notificacion_hud(mensaje):
    zorder 400

    frame:
        xalign 0.5
        yalign 0.95
        xsize 500
        padding (20, 10)
        background "#0f172acc"

        text mensaje:
            xalign 0.5
            size 16
            color "#94a3b8"


# ----------------------------------------------------------
# LABEL AUXILIAR — Llamado desde map.rpy cuando termina
# una franja o el jugador decide dormir
# ----------------------------------------------------------
label nueva_franja():

    python:
        resultado = avanzar_franja()

    if resultado == "nuevo_dia":
        # Autosave y transición al nuevo día
        $ nuevo_dia()
        jump game_loop
    else:
        # Seguimos en el mismo día, nueva franja
        jump mapa_principal

    return


# ----------------------------------------------------------
# LABEL AUXILIAR — Interacción cotidiana genérica
# Se llama desde map.rpy para conversaciones simples
# Reemplazar con diálogos reales en Fase 2
# ----------------------------------------------------------
label interaccion_celine():
    # Placeholder — diálogos reales en Fase 2
    $ cambiar_stat("celine", "afecto", 2)
    $ registrar_interaccion("celine")
    c "..."
    narrator "(Hace falta más tiempo juntos para que esto fluya.)"
    return

label interaccion_roxy():
    $ cambiar_stat("roxy", "afecto", 2)
    $ registrar_interaccion("roxy")
    r "¿Qué onda?"
    narrator "(Roxy siempre tiene algo que decir. A veces incluso tiene sentido.)"
    return

label interaccion_luna():
    $ cambiar_stat("luna", "afecto", 2)
    $ registrar_interaccion("luna")
    l "..."
    narrator "(El silencio de Luna tiene peso propio.)"
    return


# ----------------------------------------------------------
# LABEL — Trabajar (fuente de ingresos básica)
# ----------------------------------------------------------
label accion_trabajar():
    python:
        import random
        # Distribución centrada en $90, rango $50-150
        ganancia = int(random.gauss(90, 20))
        ganancia = max(50, min(150, ganancia))
        ganar_dinero(ganancia)

    narrator "Unas horas de trabajo freelance. El dinero es modesto pero alcanza."
    "[mc_nombre] ganó $[ganancia]."

    $ usar_accion()
    return


# ----------------------------------------------------------
# LABEL — Descansar (recupera energía a mitad de día)
# Costo: 1 acción. Ganancia: +2 energía (no supera el máx)
# ----------------------------------------------------------
label accion_descansar():
    python:
        mc_energia = min(mc_energia + 2, mc_energia_max)

    narrator "Una siesta corta. El cuerpo lo agradece."
    $ usar_accion()
    return


# ----------------------------------------------------------
# FIN DE ARCHIVO
# Siguiente: map.rpy (navegación del apartamento)
# ============================================================
