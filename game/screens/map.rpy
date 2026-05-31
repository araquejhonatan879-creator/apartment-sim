## =============================================================
## APARTMENT SIM — map.rpy
## Mapa navegable del apartamento
## CORREGIDO v2: label dormir sincroniza energia_actual
## =============================================================

screen mapa_apartamento():

    tag menu

    if renpy.loadable("images/backgrounds/bg_mapa.png"):
        add "images/backgrounds/bg_mapa.png"
    else:
        add "#0d0d0f"

    use hud()

    frame:
        xalign 0.5
        yalign 0.08
        xpadding 16
        ypadding 6
        background "#13131acc"
        text "APARTAMENTO — [franja_actual.upper()] — DÍA [dia_actual]" style "mapa_titulo"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12

        ## Fila 1: Sala — Cocina — Balcón
        hbox:
            spacing 16
            xalign 0.5

            button:
                action Jump("ir_sala")
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    xalign 0.5
                    yalign 0.5
                    text "SALA" style "mapa_habitacion"
                    text "[personajes_en('sala')]" style "mapa_ocupantes"

            button:
                action Jump("ir_cocina")
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    xalign 0.5
                    yalign 0.5
                    text "COCINA" style "mapa_habitacion"
                    text "[personajes_en('cocina')]" style "mapa_ocupantes"

            button:
                action Jump("ir_balcon")
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    xalign 0.5
                    yalign 0.5
                    text "BALCÓN" style "mapa_habitacion"
                    text "[personajes_en('balcon')]" style "mapa_ocupantes"

        ## Fila 2: Cuartos de las chicas
        hbox:
            spacing 16
            xalign 0.5

            if celine_cuarto_desbloqueado:
                button:
                    action Jump("ir_cuarto_celine")
                    style "mapa_boton"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        xalign 0.5
                        yalign 0.5
                        text "CUARTO CELINE" style "mapa_habitacion_celine"
                        text "[personajes_en('cuarto_celine')]" style "mapa_ocupantes"
            else:
                frame:
                    style "mapa_boton_bloqueado"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        xalign 0.5
                        yalign 0.5
                        text "CUARTO CELINE" style "mapa_habitacion_bloqueada"
                        text "Afecto [celine_afecto]/35" style "mapa_requisito"

            if roxy_cuarto_desbloqueado:
                button:
                    action Jump("ir_cuarto_roxy")
                    style "mapa_boton"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        xalign 0.5
                        yalign 0.5
                        text "CUARTO ROXY" style "mapa_habitacion_roxy"
                        text "[personajes_en('cuarto_roxy')]" style "mapa_ocupantes"
            else:
                frame:
                    style "mapa_boton_bloqueado"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        xalign 0.5
                        yalign 0.5
                        text "CUARTO ROXY" style "mapa_habitacion_bloqueada"
                        text "Afecto [roxy_afecto]/20" style "mapa_requisito"

            if luna_cuarto_desbloqueado:
                button:
                    action Jump("ir_cuarto_luna")
                    style "mapa_boton"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        xalign 0.5
                        yalign 0.5
                        text "CUARTO LUNA" style "mapa_habitacion_luna"
                        text "[personajes_en('cuarto_luna')]" style "mapa_ocupantes"
            else:
                frame:
                    style "mapa_boton_bloqueado"
                    xsize 200
                    ysize 100
                    vbox:
                        spacing 4
                        xalign 0.5
                        yalign 0.5
                        text "CUARTO LUNA" style "mapa_habitacion_bloqueada"
                        text "Afecto [luna_afecto]/45" style "mapa_requisito"

        ## Fila 3: Tu cuarto — Baño — Afuera
        hbox:
            spacing 16
            xalign 0.5

            button:
                action Jump("ir_mi_cuarto")
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    xalign 0.5
                    yalign 0.5
                    text "TU CUARTO" style "mapa_habitacion"
                    text "Descansar / Leer / Trabajar" style "mapa_ocupantes"

            button:
                action Jump("ir_bano")
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    xalign 0.5
                    yalign 0.5
                    text "BAÑO" style "mapa_habitacion"
                    text "Evento espontáneo posible" style "mapa_ocupantes"

            button:
                action Jump("ir_afuera")
                style "mapa_boton"
                xsize 200
                ysize 100
                vbox:
                    spacing 4
                    xalign 0.5
                    yalign 0.5
                    text "SALIR" style "mapa_habitacion"
                    text "Tienda / Salidas / Trabajo" style "mapa_ocupantes"

    vbox:
        xalign 1.0
        yalign 1.0
        xoffset -16
        yoffset -16
        spacing 8

        textbutton "Teléfono"     action Jump("abrir_telefono") style "mapa_accion_btn"
        textbutton "Guardar"      action ShowMenu("save")       style "mapa_accion_btn"
        textbutton "Pasar tiempo" action Jump("pasar_tiempo")   style "mapa_accion_btn"


## =============================================================
## FUNCIONES AUXILIARES
## =============================================================

init python:

    def personajes_en(ubicacion):
        presentes = []
        personajes = ["celine", "roxy", "luna"]
        nombres    = {"celine": "Celine", "roxy": "Roxy", "luna": "Luna"}
        for p in personajes:
            if ubicacion_probable(p) == ubicacion:
                if esta_disponible(p):
                    mood  = getattr(store, p + "_mood", "normal")
                    icono = MOOD_ICONO.get(mood, "●")
                    presentes.append(nombres[p] + " " + icono)
        return "  ".join(presentes) if presentes else "Vacío"

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

    def registrar_ubicacion_actual(ubicacion):
        store.ubicacion_actual = ubicacion

    def tomar_cafe():
        maximo = acciones_por_franja()
        if store.energia_actual < maximo:
            store.energia_actual += 1
        usar_accion()


## =============================================================
## LABELS DE NAVEGACIÓN
## =============================================================

label mapa_principal:
    call screen mapa_apartamento
    jump mapa_loop

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

label mapa_loop:
    $ verificar_desbloqueos()
    call screen mapa_apartamento


## =============================================================
## PANTALLAS DE ACCIONES
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
            if ubicacion_probable("celine") == "sala" and esta_disponible("celine"):
                textbutton "Hablar con Celine" action Jump("hablar_celine") style "accion_btn"
            if ubicacion_probable("roxy") == "sala" and esta_disponible("roxy"):
                textbutton "Hablar con Roxy" action Jump("hablar_roxy") style "accion_btn"
            if ubicacion_probable("luna") == "sala" and esta_disponible("luna"):
                textbutton "Hablar con Luna" action Jump("hablar_luna") style "accion_btn"
            textbutton "Ver televisión"        action [Function(usar_accion), Return()] style "accion_btn"
            textbutton "Descansar en el sofá"  action [Function(usar_accion), Return()] style "accion_btn"
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
            textbutton "Preparar algo de comer"   action [Function(usar_accion), Return()] style "accion_btn"
            textbutton "Tomar café (+1 energía)"  action [Function(tomar_cafe), Return()]  style "accion_btn"
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
            textbutton "Tomar aire" action [Function(usar_accion), Return()] style "accion_btn"
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
            textbutton "Dormir (siguiente día)"      action Jump("dormir")          style "accion_btn"
            textbutton "Leer un libro (+2 Encanto)"  action Jump("leer_libro")      style "accion_btn"
            textbutton "Trabajar online (+$50-150)"  action Jump("trabajar")        style "accion_btn"
            textbutton "Hacer ejercicio"             action Jump("hacer_ejercicio") style "accion_btn"
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
            textbutton "Mirar el cuarto" action Jump("explorar_cuarto_celine") style "accion_btn"
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
            textbutton "Mirar el cuarto" action Jump("explorar_cuarto_roxy") style "accion_btn"
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
            textbutton "Mirar el cuarto" action Jump("explorar_cuarto_luna") style "accion_btn"
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
            textbutton "Tienda (regalos)"           action Jump("abrir_tienda") style "accion_btn"
            textbutton "Trabajar fuera (+$50-150)"  action Jump("trabajar")     style "accion_btn"
            if celine_afecto >= 25 or roxy_afecto >= 25 or luna_afecto >= 25:
                null height 4
                text "— Salidas —" style "accion_subtitulo"
                if celine_afecto >= 25:
                    textbutton "Salir con Celine" action Jump("salida_celine") style "accion_btn"
                if roxy_afecto >= 25:
                    textbutton "Salir con Roxy"   action Jump("salida_roxy")   style "accion_btn"
                if luna_afecto >= 25:
                    textbutton "Salir con Luna"   action Jump("salida_luna")   style "accion_btn"
            null height 8
            textbutton "← Volver al mapa" action Return() style "accion_btn_volver"


## =============================================================
## LABELS DE ACCIONES
## =============================================================

label dormir:
    ## nuevo_dia() ya resetea franja_actual y energia_actual internamente.
    ## La línea extra sincroniza el valor visible ANTES de que el HUD
    ## re-renderice, evitando el crash de range negativo en el primer frame.
    $ nuevo_dia()
    $ energia_actual = acciones_por_franja()
    "Cierras los ojos. Mañana es otro día en Vallanova."
    jump mapa_loop

label leer_libro:
    $ usar_accion()
    $ cambiar_stat_mc("encanto", 2)
    "Lees durante un rato. Tu cabeza trabaja mejor."
    jump mapa_loop

label trabajar:
    python:
        import random
        pago = random.randint(50, 150)
        ganar_dinero(pago)
        usar_accion()
    "Trabajas un rato. Ganas $[pago]."
    jump mapa_loop

label hacer_ejercicio:
    python:
        store.ejercicio_streak = getattr(store, "ejercicio_streak", 0) + 1
        if store.ejercicio_streak >= 5:
            cambiar_stat_mc("energia_max", 1)
            store.ejercicio_streak = 0
            renpy.notify("¡Energía máxima aumentada!")
        usar_accion()
    "Haces ejercicio. [store.ejercicio_streak]/5 días para más energía."
    jump mapa_loop

label evento_bano_check:
    python:
        import random
        tiene_evento_bano = random.randint(1, 100) <= 15
    if tiene_evento_bano:
        jump evento_bano_espontaneo
    else:
        $ usar_accion()
        "El baño está vacío."
        jump mapa_loop

label evento_bano_espontaneo:
    $ usar_accion()
    "La puerta estaba entreabierta..."
    jump mapa_loop

label hablar_celine:
    $ registrar_interaccion("celine")
    $ usar_accion()
    "[ Diálogos de Celine — Fase 2 ]"
    jump mapa_loop

label hablar_roxy:
    $ registrar_interaccion("roxy")
    $ usar_accion()
    "[ Diálogos de Roxy — Fase 2 ]"
    jump mapa_loop

label hablar_luna:
    $ registrar_interaccion("luna")
    $ usar_accion()
    "[ Diálogos de Luna — Fase 2 ]"
    jump mapa_loop

label interaccion_celine:
    $ usar_accion()
    "[ Interacción libre Celine — Fase 5 ]"
    jump mapa_loop

label interaccion_roxy:
    $ usar_accion()
    "[ Interacción libre Roxy — Fase 5 ]"
    jump mapa_loop

label interaccion_luna:
    $ usar_accion()
    "[ Interacción libre Luna — Fase 5 ]"
    jump mapa_loop

label explorar_cuarto_celine:
    $ usar_accion()
    "[ Exploración cuarto Celine — Fase 4 ]"
    jump mapa_loop

label explorar_cuarto_roxy:
    $ usar_accion()
    "[ Exploración cuarto Roxy — Fase 4 ]"
    jump mapa_loop

label explorar_cuarto_luna:
    $ usar_accion()
    "[ Exploración cuarto Luna — Fase 4 ]"
    jump mapa_loop

label salida_celine:
    $ usar_accion()
    "[ Salida con Celine — Fase 3 ]"
    jump mapa_loop

label salida_roxy:
    $ usar_accion()
    "[ Salida con Roxy — Fase 3 ]"
    jump mapa_loop

label salida_luna:
    $ usar_accion()
    "[ Salida con Luna — Fase 3 ]"
    jump mapa_loop


## =============================================================
## ESTILOS
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

## Variables de tracking
default ubicacion_actual = "sala"
default ejercicio_streak = 0