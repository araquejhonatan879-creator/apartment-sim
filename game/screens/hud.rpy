## =============================================================
## APARTMENT SIM — hud.rpy
## HUD siempre visible: día, franja, energía, dinero y stats
## CORREGIDO v4: color mood via bloque de propiedades (sintaxis oficial)
## =============================================================

init python:

    COLOR_CELINE = "#818cf8"
    COLOR_ROXY   = "#fb923c"
    COLOR_LUNA   = "#c084fc"
    COLOR_TEXTO  = "#e2e8f0"
    COLOR_PANEL  = "#13131a"
    COLOR_FONDO  = "#0d0d0f"

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


screen hud():

    if not renpy.get_screen("evento_activo"):

        ## -------------------------------------------------
        ## PANEL SUPERIOR
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

                vbox:
                    spacing 2
                    text "DÍA [dia_actual]" style "hud_label"
                    text "[dia_semana()]" style "hud_valor"

                text "│" style "hud_sep"

                vbox:
                    spacing 2
                    text "FRANJA" style "hud_label"
                    text "[franja_actual.upper()]" style "hud_valor"

                text "│" style "hud_sep"

                vbox:
                    spacing 2
                    text "ENERGÍA" style "hud_label"
                    hbox:
                        spacing 4
                        for i in range(max(0, energia_actual)):
                            text "◉" style "hud_energia_on"
                        for i in range(max(0, acciones_por_franja() - energia_actual)):
                            text "◉" style "hud_energia_off"

                text "│" style "hud_sep"

                vbox:
                    spacing 2
                    text "DINERO" style "hud_label"
                    text "$[mc_dinero]" style "hud_dinero"

        ## -------------------------------------------------
        ## PANEL LATERAL DERECHO
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

                ## CELINE
                ## El icono usa un bloque de propiedades con if/elif —
                ## esta es la sintaxis oficial de Ren'Py para color dinámico
                vbox:
                    spacing 3
                    hbox:
                        spacing 6
                        text "CELINE" style "hud_nombre_celine"
                        text "[MOOD_ICONO.get(celine_mood, '●')]":
                            if celine_mood == "feliz":
                                color "#4ade80"
                            elif celine_mood == "cansada":
                                color "#60a5fa"
                            elif celine_mood == "estresada":
                                color "#f87171"
                            elif celine_mood == "traviesa":
                                color "#f472b6"
                            else:
                                color "#94a3b8"
                            size 12
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

                null height 2

                ## ROXY
                vbox:
                    spacing 3
                    hbox:
                        spacing 6
                        text "ROXY" style "hud_nombre_roxy"
                        text "[MOOD_ICONO.get(roxy_mood, '●')]":
                            if roxy_mood == "feliz":
                                color "#4ade80"
                            elif roxy_mood == "cansada":
                                color "#60a5fa"
                            elif roxy_mood == "estresada":
                                color "#f87171"
                            elif roxy_mood == "traviesa":
                                color "#f472b6"
                            else:
                                color "#94a3b8"
                            size 12
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

                null height 2

                ## LUNA
                vbox:
                    spacing 3
                    hbox:
                        spacing 6
                        text "LUNA" style "hud_nombre_luna"
                        text "[MOOD_ICONO.get(luna_mood, '●')]":
                            if luna_mood == "feliz":
                                color "#4ade80"
                            elif luna_mood == "cansada":
                                color "#60a5fa"
                            elif luna_mood == "estresada":
                                color "#f87171"
                            elif luna_mood == "traviesa":
                                color "#f472b6"
                            else:
                                color "#94a3b8"
                            size 12
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
        ## ARMONÍA
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
## ESTILOS
## =============================================================

style hud_label:
    color "#64748b"
    size 10

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

style hud_bar_corrupcion:
    left_bar  Frame("#f43f5e", 0, 0)
    right_bar Frame("#1f0a12", 0, 0)
    ysize 6
    yalign 0.5

style hud_bar_armonia:
    left_bar  Frame("#38bdf8", 0, 0)
    right_bar Frame("#0c1a2e", 0, 0)
    ysize 6
    yalign 0.5