# ============================================================
# APARTMENT SIM — script.rpy
# Día 1: Llegada al apartamento + Tutorial HUD
# ============================================================

# ----------------------------------------------------------
# INICIO DEL JUEGO — Pantalla de nombre
# ----------------------------------------------------------
label start:

    scene black with fade

    $ mc_nombre = renpy.input("¿Cuál es tu nombre?", default="Mateo", length=20)
    $ mc_nombre = mc_nombre.strip()
    if mc_nombre == "":
        $ mc_nombre = "Mateo"

    jump dia1_llegada


# ----------------------------------------------------------
# DÍA 1 — LLEGADA AL APARTAMENTO
# ----------------------------------------------------------
label dia1_llegada:

    $ dia_actual = 1
    $ dia_nombre = "Lunes"
    $ franja_actual = "tarde"
    $ acciones_restantes = 2

    scene bg_pasillo_exterior with fade

    narrator "Cuarto piso. Edificio B. Vallanova."
    narrator "La maleta pesa más de lo que debería para alguien que dice que no trajo mucho."
    narrator "El ascensor no funciona."

    pause 1.0
    narrator "Toco el timbre."
    pause 1.5

    scene bg_puerta_apartamento with dissolve
    show celine neutral at center with dissolve

    c "El cuarto es el del fondo."
    c "No hagas ruido después de las 11."

    hide celine with dissolve

    narrator "Eso es todo. Sin bienvenida. Sin pregunta de si tuve buen viaje."
    narrator "Celine siempre fue así — economía de palabras, eficiencia de hielo."

    pause 0.5

    scene bg_cocina_dia with dissolve
    show roxy feliz at center with dissolve

    r "¡LLEGASTE!"
    r "Pensé que era mañana. ¿Comiste?"
    narrator "Tiene una cuchara en la mano. Una mancha de algo en la camiseta."
    r "Estoy haciendo algo que podría ser pasta. O podría ser un error de cálculo. Ya vemos."
    narrator "Me abraza sin preguntar. Un abrazo de esos que no esperabas y que igual te descolocan."

    hide roxy with dissolve

    narrator "Roxy. Siempre Roxy. Caos en forma de persona."
    pause 0.5

    scene bg_sala_dia with dissolve
    show luna neutral at left with dissolve

    narrator "En el sofá, con un libro, está Luna."
    narrator "Levanta la vista. Me mira exactamente tres segundos."
    pause 1.5

    l "Hola."

    narrator "Vuelve al libro."
    hide luna with dissolve
    narrator "Tres segundos y una palabra. Para Luna, eso es una conversación completa."
    pause 0.5

    scene bg_cuarto_mc_dia with dissolve

    narrator "El cuarto del fondo. Cama. Escritorio. Una ventana que da a la calle."
    narrator "Desde aquí se escucha a Roxy cantando algo mal en la cocina."
    pause 0.8
    narrator "Dejo la maleta en el suelo."
    pause 0.5
    narrator "Esto es real. Voy a vivir aquí."
    narrator "Con Celine. Con Roxy. Con Luna."
    narrator "Con tres personas que conozco desde que era un crío y que de alguna forma terminaron todas en el mismo piso."
    pause 1.0
    narrator "Bien."

    jump tutorial_hud


# ----------------------------------------------------------
# TUTORIAL HUD
# ----------------------------------------------------------
label tutorial_hud:

    scene bg_cuarto_mc_dia with dissolve
    $ hud_visible = True
    pause 0.5

    show screen tutorial_box("FRANJAS HORARIAS", "El dia se divide en 4 franjas:\nManana - Tarde - Noche - Madrugada\n\nCada franja tienes acciones disponibles.\nCuando se acaban, avanza la franja.")
    pause 0.2
    $ renpy.input("", default="", length=0)
    hide screen tutorial_box

    show screen tutorial_box("ACCIONES", "Los circulos junto al reloj son tu energia.\nCada accion que tomes gasta uno.\n\nDormir bien recupera todo para el dia siguiente.")
    pause 0.2
    $ renpy.input("", default="", length=0)
    hide screen tutorial_box

    show screen tutorial_box("STATS DE PERSONAJES", "Cada chica tiene tres barras:\n\nAfecto - que tanto le importas\nConfianza - que tanto cree en ti\nCorrupcion - que tan abierta esta a escalar")
    pause 0.2
    $ renpy.input("", default="", length=0)
    hide screen tutorial_box

    show screen tutorial_box("ARMONIA DEL APARTAMENTO", "La barra azul abajo es la Armonia global.\nRepresenta el ambiente entre todas.\n\nSi baja mucho, las cosas se complican.")
    pause 0.2
    $ renpy.input("", default="", length=0)
    hide screen tutorial_box

    show screen tutorial_box("DINERO", "Empiezas con $500.\nPuedes trabajar, completar quests o salir con ellas.\n\nLos regalos correctos importan mas que los caros.")
    pause 0.2
    $ renpy.input("", default="", length=0)
    hide screen tutorial_box

    jump fin_dia1


# ----------------------------------------------------------
# FIN DEL DÍA 1
# ----------------------------------------------------------
label fin_dia1:

    scene bg_cuarto_mc_noche with fade

    narrator "La noche llega sin avisar."
    narrator "Desde la sala se escucha el televisor. Voces bajas."
    narrator "Hay algo extraño en estar en un lugar nuevo que de alguna forma ya conocias."
    pause 0.8
    narrator "Manana empieza de verdad."

    python:
        store.celine_afecto     = 5
        store.celine_confianza  = 5
        store.celine_corrupcion = 0
        store.roxy_afecto       = 15
        store.roxy_confianza    = 10
        store.roxy_corrupcion   = 0
        store.luna_afecto       = 5
        store.luna_confianza    = 5
        store.luna_corrupcion   = 0
        store.mc_encanto        = 10
        store.mc_energia_max    = 6
        store.mc_energia        = 6
        store.mc_dinero         = 500
        store.armonia           = 70
        store.dia_actual        = 2
        store.franja_actual     = "manana"
        store.acciones_restantes = acciones_por_franja()

    show screen notificacion_hud("Partida guardada automaticamente - Dia 1 completado")
    pause 1.5
    hide screen notificacion_hud

    scene black with fade
    pause 1.0
    show text "Dia 2 - Manana" with dissolve
    pause 1.5
    hide text with dissolve

    jump game_loop


# ----------------------------------------------------------
# GAME LOOP
# ----------------------------------------------------------
label game_loop:

    python:
        generar_moods()

    call screen pantalla_inicio_dia
    jump mapa_principal


# ----------------------------------------------------------
# SCREENS AUXILIARES
# ----------------------------------------------------------
screen pantalla_inicio_dia():
    modal True
    zorder 200

    add "#0d0d0f"

    vbox:
        xalign 0.5
        yalign 0.4
        spacing 20

        text "[dia_nombre], Dia [dia_actual]":
            xalign 0.5
            size 52
            color "#e2e8f0"
            bold True

        text "Estado de animo hoy:":
            xalign 0.5
            size 24
            color "#94a3b8"

        hbox:
            xalign 0.5
            spacing 40

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

        textbutton "Empezar el dia":
            xalign 0.5
            action Return()
            style "confirm_button"


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

            text "[[ Haz clic para continuar ]]":
                xalign 1.0
                size 14
                color "#64748b"


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
# LABEL AUXILIAR — avance de franja
# ----------------------------------------------------------
label nueva_franja:

    python:
        resultado = avanzar_franja()

    if resultado == "nuevo_dia":
        $ nuevo_dia()
        jump game_loop
    else:
        jump mapa_principal

    return


# ----------------------------------------------------------
# LABELS DE ACCIONES BÁSICAS
# (interaccion_celine/roxy/luna viven en map.rpy)
# ----------------------------------------------------------
label accion_trabajar:
    python:
        import random
        ganancia = int(random.gauss(90, 20))
        ganancia = max(50, min(150, ganancia))
        ganar_dinero(ganancia)
        usar_accion()
    narrator "Unas horas de trabajo freelance."
    "Ganaste $[ganancia]."
    return

label accion_descansar:
    python:
        store.mc_energia = min(store.mc_energia + 2, store.mc_energia_max)
        usar_accion()
    narrator "Una siesta corta. El cuerpo lo agradece."
    return