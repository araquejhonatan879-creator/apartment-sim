## =============================================================
## APARTMENT SIM — hud.rpy
## HUD siempre visible: día, franja, energía, dinero y stats
## Paleta de colores del GDD_CORE.md sección 12
## =============================================================

init python:

    # Colores de cada personaje (del GDD_CORE paleta UI)
    COLOR_CELINE = "#818cf8"
    COLOR_ROXY   = "#fb923c"
    COLOR_LUNA   = "#c084fc"
    COLOR_TEXTO  = "#e2e8f0"
    COLOR_PANEL  = "#13131a"
    COLOR_FONDO  = "#0d0d0f"

    # Iconos de estado de ánimo — texto simple para no depender de imágenes
    MOOD_ICONO = {
        "normal":    "●",
        "feliz":     "▲",
        "cansada":   "▼",
        "estresada": "!",
        "traviesa":  "♦",
    }

    MOOD_COLOR = {
        "normal":    "#94a3b8",
        "feliz":     "#4ade80",
        "cansada":   "#60a5fa",
        "estresada": "#f87171",
        "traviesa":  "#f472b6",
    }


## =============================================================
## PANTALLA HUD PRINCIPAL
## Se muestra siempre durante el juego libre (not in_event)
## =============================================================

screen hud():

    ## El HUD solo se muestra cuando no hay evento narrativo activo
    if not renpy.get_screen("evento_activo"):

        ## -------------------------------------------------
        ## PANEL SUPERIOR — Día, franja, energía, dinero
        ## -------------------------------------------------
        frame:
            xalign 0.5
            yalign 0.0
            yoffset 8
            xpadding 20
            ypadding 8
            background "#13131acc"

            hbox:
                spacing 30

                ## Día y día de la semana
                vbox:
                    spacing 2
                    text "DÍA [dia_actual]" style "hud_label"
                    text "[dia_semana()]" style "hud_valor"

                ## Separador
                text "│" style "hud_sep"

                ## Franja horaria actual
                vbox:
                    spacing 2
                    text "FRANJA" style "hud_label"
                    text "[franja_actual.upper()]" style "hud_valor"

                ## Separador
                text "│" style "hud_sep"

                ## Energía (acciones restantes / máximo)
                vbox:
                    spacing 2
                    text "ENERGÍA" style "hud_label"
                    hbox:
                        spacing 4
                        ## Dibuja un círculo por cada acción disponible
                        for i in range(energia_actual):
                            text "◉" style "hud_energia_on"
                        for i in range(acciones_por_franja() - energia_actual):
                            text "◉" style "hud_energia_off"

                ## Separador
                text "│" style "hud_sep"

                ## Dinero
                vbox:
                    spacing 2
                    text "DINERO" style "hud_label"
                    text "$[mc_dinero]" style "hud_dinero"

        ## -------------------------------------------------
        ## PANEL LATERAL DERECHO — Stats de los 3 personajes
        ## -------------------------------------------------
        frame:
            xalign 1.0
            yalign 0.5
            xoffset -8
            xpadding 14
            ypadding 12
            background "#13131acc"

            vbox:
                spacing 12

                ## Celine
                vbox:
                    spacing 3
                    hbox:
                        spacing 6
                        text "CELINE" style "hud_nombre_celine"
                        text "[MOOD_ICONO.get(celine_mood, '●')]" color "[MOOD_COLOR.get(celine_mood, '#94a3b8')]" size 12
                    hbox:
                        spacing 4
                        text "AFE" style "hud_stat_label"
                        bar value celine_afecto range 100 xsize 80 style "hud_bar_celine"
                        text "[celine_afecto]" style "hud_stat_num"
                    hbox:
                        spacing 4
                        text "CON" style "hud_stat_label"
                        bar value celine_confianza range 100 xsize 80 style "hud_bar_celine"
                        text "[celine_confianza]" style "hud_stat_num"
                    hbox:
                        spacing 4
                        text "COR" style "hud_stat_label"
                        bar value celine_corrupcion range 100 xsize 80 style "hud_bar_corrupcion"
                        text "[celine_corrupcion]" style "hud_stat_num"

                ## Separador
                null height 2

                ## Roxy
                vbox:
                    spacing 3
                    hbox:
                        spacing 6
                        text "ROXY" style "hud_nombre_roxy"
                        text "[MOOD_ICONO.get(roxy_mood, '●')]" color "[MOOD_COLOR.get(roxy_mood, '#94a3b8')]" size 12
                    hbox:
                        spacing 4
                        text "AFE" style "hud_stat_label"
                        bar value roxy_afecto range 100 xsize 80 style "hud_bar_roxy"
                        text "[roxy_afecto]" style "hud_stat_num"
                    hbox:
                        spacing 4
                        text "CON" style "hud_stat_label"
                        bar value roxy_confianza range 100 xsize 80 style "hud_bar_roxy"
                        text "[roxy_confianza]" style "hud_stat_num"
                    hbox:
                        spacing 4
                        text "COR" style "hud_stat_label"
                        bar value roxy_corrupcion range 100 xsize 80 style "hud_bar_corrupcion"
                        text "[roxy_corrupcion]" style "hud_stat_num"

                ## Separador
                null height 2

                ## Luna
                vbox:
                    spacing 3
                    hbox:
                        spacing 6
                        text "LUNA" style "hud_nombre_luna"
                        text "[MOOD_ICONO.get(luna_mood, '●')]" color "[MOOD_COLOR.get(luna_mood, '#94a3b8')]" size 12
                    hbox:
                        spacing 4
                        text "AFE" style "hud_stat_label"
                        bar value luna_afecto range 100 xsize 80 style "hud_bar_luna"
                        text "[luna_afecto]" style "hud_stat_num"
                    hbox:
                        spacing 4
                        text "CON" style "hud_stat_label"
                        bar value luna_confianza range 100 xsize 80 style "hud_bar_luna"
                        text "[luna_confianza]" style "hud_stat_num"
                    hbox:
                        spacing 4
                        text "COR" style "hud_stat_label"
                        bar value luna_corrupcion range 100 xsize 80 style "hud_bar_corrupcion"
                        text "[luna_corrupcion]" style "hud_stat_num"

        ## -------------------------------------------------
        ## INDICADOR DE ARMONÍA — esquina inferior izquierda
        ## -------------------------------------------------
        frame:
            xalign 0.0
            yalign 1.0
            xoffset 8
            yoffset -8
            xpadding 12
            ypadding 8
            background "#13131acc"

            hbox:
                spacing 8
                text "ARMONÍA" style "hud_label"
                bar value armonia range 100 xsize 100 style "hud_bar_armonia"
                text "[armonia]" style "hud_stat_num"


## =============================================================
## ESTILOS DEL HUD
## =============================================================

style hud_label:
    color "#64748b"
    size 10
    font "gui/font/RobotoCondensed-Regular.ttf" if renpy.loadable("gui/font/RobotoCondensed-Regular.ttf") else "DejaVuSans.ttf"

style hud_valor:
    color "#e2e8f0"
    size 13
    bold True

style hud_sep:
    color "#334155"
    size 18
    yalign 0.5

style hud_dinero:
    color "#fbbf24"
    size 13
    bold True

style hud_energia_on:
    color "#4ade80"
    size 12

style hud_energia_off:
    color "#1e3a2f"
    size 12

## Nombres de personajes con su color
style hud_nombre_celine:
    color "#818cf8"
    size 11
    bold True

style hud_nombre_roxy:
    color "#fb923c"
    size 11
    bold True

style hud_nombre_luna:
    color "#c084fc"
    size 11
    bold True

style hud_stat_label:
    color "#64748b"
    size 10
    xminimum 24

style hud_stat_num:
    color "#e2e8f0"
    size 10
    xminimum 22

## Barras de Afecto/Confianza por personaje
style hud_bar_celine:
    left_bar  Frame("#818cf8", 0, 0)
    right_bar Frame("#1e1b4b", 0, 0)
    ysize 6
    yalign 0.5

style hud_bar_roxy:
    left_bar  Frame("#fb923c", 0, 0)
    right_bar Frame("#431407", 0, 0)
    ysize 6
    yalign 0.5

style hud_bar_luna:
    left_bar  Frame("#c084fc", 0, 0)
    right_bar Frame("#2e1065", 0, 0)
    ysize 6
    yalign 0.5

## Barra de Corrupción — igual para todos, color rojizo
style hud_bar_corrupcion:
    left_bar  Frame("#f43f5e", 0, 0)
    right_bar Frame("#1f0a12", 0, 0)
    ysize 6
    yalign 0.5

## Barra de Armonía — verde/azul
style hud_bar_armonia:
    left_bar  Frame("#38bdf8", 0, 0)
    right_bar Frame("#0c1a2e", 0, 0)
    ysize 6
    yalign 0.5
