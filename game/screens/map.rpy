## =============================================================
## APARTMENT SIM — map.rpy
## Mapa navegable del apartamento — pantalla principal de juego libre
## Ubicaciones, personajes presentes, acciones disponibles
## Reglas de acceso del GDD_CORE sección 8
## =============================================================

## =============================================================
## PANTALLA PRINCIPAL DEL MAPA
## Se llama con: call screen mapa_apartamento
## =============================================================

screen mapa_apartamento():

    tag menu

    ## Fondo del mapa — placeholder hasta tener el arte
    add "images/backgrounds/bg_mapa.png" if renpy.loadable("images/backgrounds/bg_mapa.png") else "#0d0d0f"

    ## HUD siempre visible encima del mapa
    use hud()

    ## -------------------------------------------------
    ## TÍTULO DE UBICACIÓN ACTUAL
    ## -------------------------------------------------
    frame:
        xalign 0.5
        yalign 0.08
        xpadding 16
        ypadding 6
        background "#13131acc"
        text "APARTAMENTO — [franja_actual.upper()] — DÍA [dia_actual]" style "mapa_titulo"

    ## -------------------------------------------------
    ## BOTONES DE NAVEGACIÓN POR HABITACIÓN
    ## Cada botón muestra la habitación y quién está ahí
    ## -------------------------------------------------
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12

        ## Fila 1: Sala — Cocina — Balcón
        hbox:
            spacing 16
            xalign 0.5

            ## SALA
            textbutton "" action Jump("ir_sala"):
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    text "SALA" style "mapa_habitacion"
                    text "[personajes_en('sala')]" style "mapa_ocupantes"

            ## COCINA
            textbutton "" action Jump("ir_cocina"):
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    text "COCINA" style "mapa_habitacion"
                    text "[personajes_en('cocina')]" style "mapa_ocupantes"

            ## BALCÓN
            textbutton "" action Jump("ir_balcon"):
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    text "BALCÓN" style "mapa_habitacion"
                    text "[personajes_en('balcon')]" style "mapa_ocupantes"

        ## Fila 2: Cuartos de las chicas
        hbox:
            spacing 16
            xalign 0.5

            ## CUARTO CELINE
            if celine_cuarto_desbloqueado:
                textbutton "" action Jump("ir_cuarto_celine"):
                    style "mapa_boton"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        text "CUARTO CELINE" style "mapa_habitacion_celine"
                        text "[personajes_en('cuarto_celine')]" style "mapa_ocupantes"
            else:
                frame:
                    style "mapa_boton_bloqueado"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        text "CUARTO CELINE" style "mapa_habitacion_bloqueada"
                        text "Afecto [celine_afecto]/35" style "mapa_requisito"

            ## CUARTO ROXY
            if roxy_cuarto_desbloqueado:
                textbutton "" action Jump("ir_cuarto_roxy"):
                    style "mapa_boton"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        text "CUARTO ROXY" style "mapa_habitacion_roxy"
                        text "[personajes_en('cuarto_roxy')]" style "mapa_ocupantes"
            else:
                frame:
                    style "mapa_boton_bloqueado"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        text "CUARTO ROXY" style "mapa_habitacion_bloqueada"
                        text "Afecto [roxy_afecto]/20" style "mapa_requisito"

            ## CUARTO LUNA
            if luna_cuarto_desbloqueado:
                textbutton "" action Jump("ir_cuarto_luna"):
                    style "mapa_boton"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        text "CUARTO LUNA" style "mapa_habitacion_luna"
                        text "[personajes_en('cuarto_luna')]" style "mapa_ocupantes"
            else:
                frame:
                    style "mapa_boton_bloqueado"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        text "CUARTO LUNA" style "mapa_habitacion_bloqueada"
                        text "Afecto [luna_afecto]/45" style "mapa_requisito"

        ## Fila 3: Tu cuarto — Baño — Afuera
        hbox:
            spacing 16
            xalign 0.5

            ## TU CUARTO
            textbutton "" action Jump("ir_mi_cuarto"):
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    text "TU CUARTO" style "mapa_habitacion"
                    text "Descansar / Leer / Trabajar" style "mapa_ocupantes"

            ## BAÑO
            textbutton "" action Jump("ir_bano"):
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    text "BAÑO" style "mapa_habitacion"
                    text "Evento espontáneo posible" style "mapa_ocupantes"

            ## SALIR (tienda / salidas)
            textbutton "" action Jump("ir_afuera"):
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    text "SALIR" style "mapa_habitacion"
                    text "Tienda / Salidas / Trabajo" style "mapa_ocupantes"

    ## -------------------------------------------------
    ## BOTONES DE ACCIÓN RÁPIDA — esquina inferior derecha
    ## -------------------------------------------------
    vbox:
        xalign 1.0
        yalign 1.0
        xoffset -16
        yoffset -16
        spacing 8

        ## Teléfono
        textbutton "📱 Teléfono" action Jump("abrir_telefono"):
            style "mapa_accion_btn"

        ## Guardar
        textbutton "💾 Guardar" action ShowMenu("save"):
            style "mapa_accion_btn"

        ## Avanzar franja (pasar el tiempo sin hacer nada)
        textbutton "⏩ Pasar tiempo" action Jump("pasar_tiempo"):
            style "mapa_accion_btn"


## =============================================================
## FUNCIÓN AUXILIAR — qué personajes están en una ubicación
## Devuelve string con nombres o "Vacío" si no hay nadie
## =============================================================

init python:

    def personajes_en(ubicacion):
        presentes = []
        personajes = ["celine", "roxy", "luna"]
        nombres    = {"celine": "Celine", "roxy": "Roxy", "luna": "Luna"}

        for p in personajes:
            if ubicacion_probable(p) == ubicacion:
                # Verificar disponibilidad
                if esta_disponible(p):
                    mood = getattr(store, p + "_mood", "normal")
                    icono = MOOD_ICONO.get(mood, "●")
                    presentes.append(nombres[p] + " " + icono)

        if presentes:
            return "  ".join(presentes)
        return "Vacío"

    # Verificar y desbloquear cuartos automáticamente
    def verificar_desbloqueos():
        if store.celine_afecto >= 35 and not store.celine_cuarto_desbloqueado:
            store.celine_cuarto_desbloqueado = True
            renpy.notify("¡Ahora puedes entrar al cuarto de Celine!")
        if store.roxy_afecto >= 20 and not store.roxy_cuarto_desbloqueado:
            store.roxy_cuarto_desbloqueado = True
            renpy.notify("¡Ahora puedes entrar al cuarto de Roxy!")
        if store.luna_afecto >= 45 and not store.luna_cuarto_desbloqueado:
            store.luna_cuarto_desbloqueado = True
            renpy.notify("¡Ahora puedes entrar al cuarto de Luna!")


## =============================================================
## LABELS DE NAVEGACIÓN
## Cada habitación tiene su label con las acciones disponibles
## =============================================================

label ir_sala:
    $ verificar_desbloqueos()
    $ registrar_ubicacion_actual("sala")
    call screen acciones_sala
    jump mapa_loop

label ir_cocina:
    $ verificar_desbloqueos()
    $ registrar_ubicacion_actual("cocina")
    call screen acciones_cocina
    jump mapa_loop

label ir_balcon:
    $ verificar_desbloqueos()
    $ registrar_ubicacion_actual("balcon")
    call screen acciones_balcon
    jump mapa_loop

label ir_cuarto_celine:
    $ verificar_desbloqueos()
    $ registrar_ubicacion_actual("cuarto_celine")
    call screen acciones_cuarto_celine
    jump mapa_loop

label ir_cuarto_roxy:
    $ verificar_desbloqueos()
    $ registrar_ubicacion_actual("cuarto_roxy")
    call screen acciones_cuarto_roxy
    jump mapa_loop

label ir_cuarto_luna:
    $ verificar_desbloqueos()
    $ registrar_ubicacion_actual("cuarto_luna")
    call screen acciones_cuarto_luna
    jump mapa_loop

label ir_mi_cuarto:
    $ verificar_desbloqueos()
    $ registrar_ubicacion_actual("mi_cuarto")
    call screen acciones_mi_cuarto
    jump mapa_loop

label ir_bano:
    $ verificar_desbloqueos()
    $ registrar_ubicacion_actual("bano")
    jump evento_bano_check

label ir_afuera:
    $ verificar_desbloqueos()
    call screen acciones_afuera
    jump mapa_loop

label abrir_telefono:
    jump telefono_main

label pasar_tiempo:
    $ usar_accion()
    "[franja_actual.upper()] — El tiempo pasa."
    jump mapa_loop

## Loop principal del mapa — regresa aquí después de cada acción
label mapa_loop:
    $ verificar_desbloqueos()
    call screen mapa_apartamento


## =============================================================
## PANTALLAS DE ACCIONES POR HABITACIÓN
## Cada una muestra qué puedes hacer en ese lugar
## =============================================================

screen acciones_sala():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 24
        ypadding 20
        background "#13131a"
        xsize 400

        vbox:
            spacing 12
            text "SALA" style "accion_titulo"
            null height 8

            ## Interactuar con quien esté presente
            if ubicacion_probable("celine") == "sala" and esta_disponible("celine"):
                textbutton "Hablar con Celine" action [Jump("hablar_celine"), Return()]  style "accion_btn"
            if ubicacion_probable("roxy") == "sala" and esta_disponible("roxy"):
                textbutton "Hablar con Roxy" action [Jump("hablar_roxy"), Return()] style "accion_btn"
            if ubicacion_probable("luna") == "sala" and esta_disponible("luna"):
                textbutton "Hablar con Luna" action [Jump("hablar_luna"), Return()] style "accion_btn"

            ## Acciones propias de la sala
            textbutton "Ver televisión (pasar tiempo)" action [Function(usar_accion), Return()] style "accion_btn"
            textbutton "Descansar en el sofá"          action [Function(usar_accion), Return()] style "accion_btn"

            null height 8
            textbutton "← Volver al mapa" action Return() style "accion_btn_volver"

screen acciones_cocina():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 24
        ypadding 20
        background "#13131a"
        xsize 400

        vbox:
            spacing 12
            text "COCINA" style "accion_titulo"
            null height 8

            if ubicacion_probable("celine") == "cocina" and esta_disponible("celine"):
                textbutton "Hablar con Celine" action Jump("hablar_celine") style "accion_btn"
            if ubicacion_probable("roxy") == "cocina" and esta_disponible("roxy"):
                textbutton "Hablar con Roxy" action Jump("hablar_roxy") style "accion_btn"
            if ubicacion_probable("luna") == "cocina" and esta_disponible("luna"):
                textbutton "Hablar con Luna" action Jump("hablar_luna") style "accion_btn"

            textbutton "Preparar algo de comer"      action [Function(usar_accion), Return()] style "accion_btn"
            textbutton "Tomar café (recuperar +1 energía)" action [Function(tomar_cafe), Return()] style "accion_btn"

            null height 8
            textbutton "← Volver al mapa" action Return() style "accion_btn_volver"

screen acciones_balcon():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 24
        ypadding 20
        background "#13131a"
        xsize 400

        vbox:
            spacing 12
            text "BALCÓN" style "accion_titulo"
            null height 8

            if ubicacion_probable("luna") == "balcon" and esta_disponible("luna"):
                textbutton "Hablar con Luna" action Jump("hablar_luna") style "accion_btn"

            textbutton "Tomar aire (pasar tiempo)" action [Function(usar_accion), Return()] style "accion_btn"

            null height 8
            textbutton "← Volver al mapa" action Return() style "accion_btn_volver"

screen acciones_mi_cuarto():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 24
        ypadding 20
        background "#13131a"
        xsize 400

        vbox:
            spacing 12
            text "TU CUARTO" style "accion_titulo"
            null height 8

            textbutton "Dormir (avanzar al siguiente día)" action Jump("dormir") style "accion_btn"
            textbutton "Leer un libro (+2 Encanto)"        action Jump("leer_libro") style "accion_btn"
            textbutton "Trabajar online (+$50-150)"        action Jump("trabajar") style "accion_btn"
            textbutton "Hacer ejercicio (streaks → +Energía)" action Jump("hacer_ejercicio") style "accion_btn"

            null height 8
            textbutton "← Volver al mapa" action Return() style "accion_btn_volver"

screen acciones_cuarto_celine():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 24
        ypadding 20
        background "#13131a"
        xsize 400

        vbox:
            spacing 12
            text "CUARTO DE CELINE" style "accion_titulo_celine"
            null height 8

            if ubicacion_probable("celine") == "cuarto" and esta_disponible("celine"):
                textbutton "Hablar con Celine" action Jump("hablar_celine") style "accion_btn"
                if celine_corrupcion >= 20:
                    textbutton "Interacción libre" action Jump("interaccion_celine") style "accion_btn"

            textbutton "Mirar el cuarto"    action Jump("explorar_cuarto_celine") style "accion_btn"

            null height 8
            textbutton "← Volver al mapa" action Return() style "accion_btn_volver"

screen acciones_cuarto_roxy():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 24
        ypadding 20
        background "#13131a"
        xsize 400

        vbox:
            spacing 12
            text "CUARTO DE ROXY" style "accion_titulo_roxy"
            null height 8

            if ubicacion_probable("roxy") == "cuarto" and esta_disponible("roxy"):
                textbutton "Hablar con Roxy" action Jump("hablar_roxy") style "accion_btn"
                if roxy_corrupcion >= 20:
                    textbutton "Interacción libre" action Jump("interaccion_roxy") style "accion_btn"

            textbutton "Mirar el cuarto"    action Jump("explorar_cuarto_roxy") style "accion_btn"

            null height 8
            textbutton "← Volver al mapa" action Return() style "accion_btn_volver"

screen acciones_cuarto_luna():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 24
        ypadding 20
        background "#13131a"
        xsize 400

        vbox:
            spacing 12
            text "CUARTO DE LUNA" style "accion_titulo_luna"
            null height 8

            if ubicacion_probable("luna") == "cuarto" and esta_disponible("luna"):
                textbutton "Hablar con Luna" action Jump("hablar_luna") style "accion_btn"
                if luna_corrupcion >= 20:
                    textbutton "Interacción libre" action Jump("interaccion_luna") style "accion_btn"

            textbutton "Mirar el cuarto"    action Jump("explorar_cuarto_luna") style "accion_btn"

            null height 8
            textbutton "← Volver al mapa" action Return() style "accion_btn_volver"

screen acciones_afuera():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 24
        ypadding 20
        background "#13131a"
        xsize 400

        vbox:
            spacing 12
            text "SALIR" style "accion_titulo"
            null height 8

            textbutton "Tienda (regalos)"     action Jump("abrir_tienda") style "accion_btn"
            textbutton "Trabajar fuera ($50-150)" action Jump("trabajar") style "accion_btn"

            ## Salidas con personajes — requieren afecto mínimo
            if celine_afecto >= 25 or roxy_afecto >= 25 or luna_afecto >= 25:
                null height 4
                text "— Salidas —" style "accion_subtitulo"
                if celine_afecto >= 25:
                    textbutton "Salir con Celine" action Jump("salida_celine") style "accion_btn"
                if roxy_afecto >= 25:
                    textbutton "Salir con Roxy" action Jump("salida_roxy") style "accion_btn"
                if luna_afecto >= 25:
                    textbutton "Salir con Luna" action Jump("salida_luna") style "accion_btn"

            null height 8
            textbutton "← Volver al mapa" action Return() style "accion_btn_volver"


## =============================================================
## FUNCIONES AUXILIARES DEL MAPA
## =============================================================

init python:

    def registrar_ubicacion_actual(ubicacion):
        store.ubicacion_actual = ubicacion

    def tomar_cafe():
        """Tomar café en cocina: recupera 1 punto de energía, máx acciones de la franja"""
        maximo = acciones_por_franja()
        if store.energia_actual < maximo:
            store.energia_actual += 1
        usar_accion()


## =============================================================
## LABELS DE ACCIONES BÁSICAS DEL CUARTO PROPIO
## =============================================================

label dormir:
    $ nuevo_dia()
    "Cierras los ojos. Mañana es otro día en Vallanova."
    jump mapa_loop

label leer_libro:
    $ usar_accion()
    $ cambiar_stat_mc("encanto", 2)
    "Lees durante un rato. Sientes que tu cabeza trabaja mejor."
    jump mapa_loop

label trabajar:
    python:
        import random
        pago = random.randint(50, 150)
        ganar_dinero(pago)
        usar_accion()
    "Trabajas un rato online. Ganas $[pago]."
    jump mapa_loop

label hacer_ejercicio:
    python:
        store.ejercicio_streak = getattr(store, "ejercicio_streak", 0) + 1
        if store.ejercicio_streak >= 5:
            cambiar_stat_mc("energia_max", 1)
            store.ejercicio_streak = 0
            renpy.notify("¡Energía máxima aumentada!")
        usar_accion()
    "Haces ejercicio. [{store.ejercicio_streak}/5 días para más energía]"
    jump mapa_loop

## Eventos check del baño — probabilidad de evento espontáneo
label evento_bano_check:
    python:
        import random
        prob = random.randint(1, 100)
        tiene_evento_bano = prob <= 15  ## 15% de probabilidad base
    if tiene_evento_bano:
        jump evento_bano_espontaneo
    else:
        $ usar_accion()
        "El baño está vacío."
        jump mapa_loop

label evento_bano_espontaneo:
    ## Placeholder — se desarrolla en random_events.rpy
    $ usar_accion()
    "La puerta estaba entreabierta..."
    jump mapa_loop

## Placeholders de interacciones — se desarrollan en events/*.rpy
label hablar_celine:
    $ registrar_interaccion("celine")
    $ usar_accion()
    "[ Diálogos de Celine — desarrollar en celine_events.rpy ]"
    jump mapa_loop

label hablar_roxy:
    $ registrar_interaccion("roxy")
    $ usar_accion()
    "[ Diálogos de Roxy — desarrollar en roxy_events.rpy ]"
    jump mapa_loop

label hablar_luna:
    $ registrar_interaccion("luna")
    $ usar_accion()
    "[ Diálogos de Luna — desarrollar en luna_events.rpy ]"
    jump mapa_loop

label interaccion_celine:
    $ usar_accion()
    "[ Interacción libre Celine — desarrollar en celine_events.rpy ]"
    jump mapa_loop

label interaccion_roxy:
    $ usar_accion()
    "[ Interacción libre Roxy — desarrollar en roxy_events.rpy ]"
    jump mapa_loop

label interaccion_luna:
    $ usar_accion()
    "[ Interacción libre Luna — desarrollar en luna_events.rpy ]"
    jump mapa_loop

label explorar_cuarto_celine:
    $ usar_accion()
    "[ Exploración cuarto Celine — desarrollar en secrets.rpy ]"
    jump mapa_loop

label explorar_cuarto_roxy:
    $ usar_accion()
    "[ Exploración cuarto Roxy — desarrollar en secrets.rpy ]"
    jump mapa_loop

label explorar_cuarto_luna:
    $ usar_accion()
    "[ Exploración cuarto Luna — desarrollar en secrets.rpy ]"
    jump mapa_loop

label abrir_tienda:
    "[ Tienda — desarrollar en economy.rpy ]"
    jump mapa_loop

label telefono_main:
    "[ Teléfono — desarrollar en phone.rpy ]"
    jump mapa_loop

label salida_celine:
    $ usar_accion()
    "[ Salida con Celine — desarrollar en celine_events.rpy ]"
    jump mapa_loop

label salida_roxy:
    $ usar_accion()
    "[ Salida con Roxy — desarrollar en roxy_events.rpy ]"
    jump mapa_loop

label salida_luna:
    $ usar_accion()
    "[ Salida con Luna — desarrollar en luna_events.rpy ]"
    jump mapa_loop


## =============================================================
## ESTILOS DEL MAPA
## =============================================================

style mapa_titulo:
    color "#94a3b8"
    size 13

style mapa_habitacion:
    color "#e2e8f0"
    size 14
    bold True
    xalign 0.5

style mapa_habitacion_celine:
    color "#818cf8"
    size 14
    bold True
    xalign 0.5

style mapa_habitacion_roxy:
    color "#fb923c"
    size 14
    bold True
    xalign 0.5

style mapa_habitacion_luna:
    color "#c084fc"
    size 14
    bold True
    xalign 0.5

style mapa_habitacion_bloqueada:
    color "#475569"
    size 13
    bold True
    xalign 0.5

style mapa_ocupantes:
    color "#94a3b8"
    size 11
    xalign 0.5

style mapa_requisito:
    color "#f87171"
    size 11
    xalign 0.5

style mapa_boton:
    background "#13131a"
    hover_background "#1e293b"
    xpadding 12
    ypadding 10
    xalign 0.5
    yalign 0.5

style mapa_boton_bloqueado:
    background "#0d0d0f"
    xpadding 12
    ypadding 10

style mapa_accion_btn:
    background "#1e293b"
    hover_background "#334155"
    color "#e2e8f0"
    size 13
    xpadding 12
    ypadding 6

style accion_titulo:
    color "#e2e8f0"
    size 16
    bold True
    xalign 0.5

style accion_titulo_celine:
    color "#818cf8"
    size 16
    bold True
    xalign 0.5

style accion_titulo_roxy:
    color "#fb923c"
    size 16
    bold True
    xalign 0.5

style accion_titulo_luna:
    color "#c084fc"
    size 16
    bold True
    xalign 0.5

style accion_subtitulo:
    color "#64748b"
    size 12
    xalign 0.5

style accion_btn:
    background "#1e293b"
    hover_background "#334155"
    color "#e2e8f0"
    size 14
    xpadding 16
    ypadding 8
    xfill True

style accion_btn_volver:
    background "#0d0d0f"
    hover_background "#1e293b"
    color "#64748b"
    size 13
    xpadding 16
    ypadding 6
    xfill True

## Variable de tracking de ubicación actual
default ubicacion_actual = "sala"
default ejercicio_streak = 0
