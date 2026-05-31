## =============================================================
## APARTMENT SIM — economy.rpy
## Sistema de economía: tienda, regalos, items
## Integrado con stats.rpy (gastar_dinero, cambiar_stat)
## Números del GDD_SISTEMAS.md S05
## =============================================================

## =============================================================
## PANTALLA PRINCIPAL DE TIENDA
## =============================================================

screen pantalla_tienda():
    modal True

    add "#0d0d0f"

    ## Título
    frame:
        xalign 0.5
        yalign 0.06
        xpadding 20
        ypadding 8
        background "#13131acc"
        text "TIENDA" style "tienda_titulo"

    ## Saldo actual
    frame:
        xalign 1.0
        yalign 0.06
        xoffset -16
        xpadding 16
        ypadding 8
        background "#13131acc"
        text "Saldo: $[mc_dinero]" style "tienda_saldo"

    ## Navegación de categorías
    hbox:
        xalign 0.5
        yalign 0.14
        spacing 8

        textbutton "Regalos":
            action SetVariable("tienda_categoria", "regalos")
            style "tienda_tab"
        textbutton "Items":
            action SetVariable("tienda_categoria", "items")
            style "tienda_tab"
        textbutton "Salidas":
            action SetVariable("tienda_categoria", "salidas")
            style "tienda_tab"

    ## Contenido según categoría
    frame:
        xalign 0.5
        yalign 0.55
        xsize 700
        ysize 500
        xpadding 24
        ypadding 20
        background "#13131a"

        if tienda_categoria == "regalos":
            use tienda_regalos()
        elif tienda_categoria == "items":
            use tienda_items()
        elif tienda_categoria == "salidas":
            use tienda_salidas()

    ## Botón volver
    textbutton "← Volver":
        xalign 0.0
        yalign 1.0
        xoffset 16
        yoffset -16
        action Return()
        style "accion_btn_volver"


## =============================================================
## CATEGORÍA: REGALOS
## =============================================================

screen tienda_regalos():

    vbox:
        spacing 10

        text "— REGALOS —" style "tienda_seccion"
        null height 4

        ## Para quién es el regalo
        hbox:
            spacing 8
            xalign 0.5
            text "Para:" style "tienda_label"
            textbutton "Celine" action SetVariable("tienda_destinatario", "celine") style "tienda_dest_btn"
            textbutton "Roxy"   action SetVariable("tienda_destinatario", "roxy")   style "tienda_dest_btn"
            textbutton "Luna"   action SetVariable("tienda_destinatario", "luna")   style "tienda_dest_btn"

        text "Destinatario: [tienda_destinatario_nombre()]" style "tienda_seleccion"

        null height 8

        ## Lista de regalos
        ## Café favorito — $20
        hbox:
            spacing 12
            xfill True
            vbox:
                xsize 420
                text "Café favorito  —  $20" style "tienda_item_nombre"
                text "+3 Afecto  (el favorito de cada una vale más)" style "tienda_item_desc"
            textbutton "Comprar":
                action Function(comprar_regalo, "cafe", 20, 3)
                style "tienda_comprar_btn"

        ## Flores — $40
        hbox:
            spacing 12
            xfill True
            vbox:
                xsize 420
                text "Flores  —  $40" style "tienda_item_nombre"
                text "+5 Afecto  (+8 para Luna)" style "tienda_item_desc"
            textbutton "Comprar":
                action Function(comprar_regalo, "flores", 40, 5)
                style "tienda_comprar_btn"

        ## Libro específico — $80
        hbox:
            spacing 12
            xfill True
            vbox:
                xsize 420
                text "Libro  —  $80" style "tienda_item_nombre"
                text "+8 Afecto  +3 Confianza  (requiere saber qué le gusta)" style "tienda_item_desc"
            textbutton "Comprar":
                action Function(comprar_regalo, "libro", 80, 8)
                style "tienda_comprar_btn"

        ## Ropa — $120
        hbox:
            spacing 12
            xfill True
            vbox:
                xsize 420
                text "Ropa  —  $120" style "tienda_item_nombre"
                text "+5 Afecto  Desbloquea outfit  (requiere Afecto >30)" style "tienda_item_desc"
            textbutton "Comprar":
                if tienda_destinatario != "" and getattr(store, tienda_destinatario + "_afecto", 0) >= 30:
                    action Function(comprar_regalo, "ropa", 120, 5)
                else:
                    action NullAction()
                style "tienda_comprar_btn"

        ## Joya — $200
        hbox:
            spacing 12
            xfill True
            vbox:
                xsize 420
                text "Joya  —  $200" style "tienda_item_nombre"
                text "+15 Afecto  (requiere Afecto >50)" style "tienda_item_desc"
            textbutton "Comprar":
                if tienda_destinatario != "" and getattr(store, tienda_destinatario + "_afecto", 0) >= 50:
                    action Function(comprar_regalo, "joya", 200, 15)
                else:
                    action NullAction()
                style "tienda_comprar_btn"

        ## Regalo secreto — solo si descubriste el secreto
        if tienda_destinatario != "" and getattr(store, tienda_destinatario + "_secreto_1", False):
            hbox:
                spacing 12
                xfill True
                vbox:
                    xsize 420
                    text "Regalo secreto  —  variable" style "tienda_item_nombre"
                    text "Efecto único según personaje" style "tienda_item_desc"
                textbutton "Comprar":
                    action Function(comprar_regalo_secreto, tienda_destinatario)
                    style "tienda_comprar_btn"


## =============================================================
## CATEGORÍA: ITEMS
## =============================================================

screen tienda_items():

    vbox:
        spacing 10

        text "— ITEMS —" style "tienda_seccion"
        null height 4

        ## Cámara compacta
        hbox:
            spacing 12
            xfill True
            vbox:
                xsize 420
                text "Camara compacta  —  $150" style "tienda_item_nombre"
                text "Desbloquea el sistema voyeur" style "tienda_item_desc"
            if tiene_camara:
                text "Ya tienes" style "tienda_ya_tienes"
            else:
                textbutton "Comprar":
                    action Function(comprar_item, "camara", 150)
                    style "tienda_comprar_btn"


## =============================================================
## CATEGORÍA: SALIDAS
## =============================================================

screen tienda_salidas():

    vbox:
        spacing 10

        text "— SALIDAS —" style "tienda_seccion"
        text "Accede desde el mapa > Salir" style "tienda_item_desc"
        null height 8

        text "Cafe ($30)  —  Afecto 25 requerido" style "tienda_item_nombre"
        text "Cine ($50)  —  Afecto 40 requerido" style "tienda_item_nombre"
        text "Compras ($80)  —  Afecto 50 requerido" style "tienda_item_nombre"
        text "Cena ($100)  —  Afecto 60 requerido" style "tienda_item_nombre"
        text "Playa/Parque ($60)  —  Afecto 70 requerido" style "tienda_item_nombre"
        text "Noche fuera ($150)  —  Afecto 85 requerido" style "tienda_item_nombre"


## =============================================================
## FUNCIONES DE COMPRA
## =============================================================

init python:

    def tienda_destinatario_nombre():
        nombres = {"celine": "Celine", "roxy": "Roxy", "luna": "Luna", "": "Nadie"}
        return nombres.get(store.tienda_destinatario, "")

    def comprar_regalo(tipo, precio, afecto_base):
        dest = store.tienda_destinatario
        if dest == "":
            renpy.notify("Selecciona a quien va el regalo.")
            return

        if not gastar_dinero(precio):
            renpy.notify("No tienes suficiente dinero.")
            return

        afecto = afecto_base

        ## Cafe favorito — bonus si es el correcto
        if tipo == "cafe":
            favoritos = {
                "celine": True,   ## americano negro
                "roxy":   True,   ## matcha latte
                "luna":   False,  ## luna no toma cafe — vale 0
            }
            if dest == "luna":
                renpy.notify("A Luna no le gusta el cafe. +0 Afecto.")
                return
            afecto = 5  ## bonus por acertar el favorito

        ## Flores — Luna recibe +8
        if tipo == "flores" and dest == "luna":
            afecto = 8

        ## Libro — suma confianza
        if tipo == "libro":
            cambiar_stat(dest, "confianza", 3)

        ## Ropa — desbloquea outfit 2
        if tipo == "ropa":
            outfit_var = dest + "_outfit_desbloqueado"
            setattr(store, outfit_var, max(getattr(store, outfit_var, 1), 2))

        ## Joya
        ## sin efecto extra — solo afecto base

        cambiar_stat(dest, "afecto", afecto)
        renpy.notify("Regalo entregado a {}. +{} Afecto".format(
            tienda_destinatario_nombre(), afecto))

    def comprar_regalo_secreto(dest):
        precios = {"celine": 100, "roxy": 80, "luna": 90}
        precio = precios.get(dest, 100)
        if not gastar_dinero(precio):
            renpy.notify("No tienes suficiente dinero.")
            return
        cambiar_stat(dest, "afecto", 20)
        cambiar_stat(dest, "confianza", 15)
        renpy.notify("Regalo especial entregado. Efecto unico desbloqueado.")

    def comprar_item(tipo, precio):
        if not gastar_dinero(precio):
            renpy.notify("No tienes suficiente dinero.")
            return
        if tipo == "camara":
            store.tiene_camara = True
            renpy.notify("Camara compacta obtenida. Sistema voyeur desbloqueado.")


## =============================================================
## LABEL DE ENTRADA A LA TIENDA
## Llamado desde map.rpy label abrir_tienda
## =============================================================

label abrir_tienda:
    $ tienda_categoria    = "regalos"
    $ tienda_destinatario = ""
    call screen pantalla_tienda
    jump mapa_loop


## =============================================================
## VARIABLES
## =============================================================

default tienda_categoria    = "regalos"
default tienda_destinatario = ""

## Outfits desbloqueados (1 = base, siempre disponible)
default celine_outfit_desbloqueado = 1
default roxy_outfit_desbloqueado   = 1
default luna_outfit_desbloqueado   = 1