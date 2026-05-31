## =============================================================
## APARTMENT SIM — phone.rpy
## Sistema de mensajes de texto
## Reglas del GDD_SISTEMAS.md S17
## =============================================================

## =============================================================
## PANTALLA PRINCIPAL DEL TELÉFONO
## =============================================================

screen pantalla_telefono():
    modal True

    add "#0d0d0f"

    ## Cabecera
    frame:
        xalign 0.5
        yalign 0.06
        xpadding 20
        ypadding 8
        background "#13131acc"
        text "MENSAJES" style "phone_titulo"

    ## Lista de conversaciones
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 8
        xsize 600

        ## CELINE
        button:
            action SetVariable("phone_contacto", "celine")
            style "phone_contacto_btn"
            xsize 600
            ysize 80
            hbox:
                spacing 16
                xalign 0.0
                yalign 0.5
                ## Indicador de mensajes sin leer
                if phone_sin_leer("celine"):
                    text "●" color "#818cf8" size 14 yalign 0.5
                else:
                    text "○" color "#334155" size 14 yalign 0.5
                vbox:
                    yalign 0.5
                    spacing 4
                    text "Celine" style "phone_nombre_celine"
                    text "[phone_ultimo_mensaje('celine')]" style "phone_preview"

        ## ROXY
        button:
            action SetVariable("phone_contacto", "roxy")
            style "phone_contacto_btn"
            xsize 600
            ysize 80
            hbox:
                spacing 16
                xalign 0.0
                yalign 0.5
                if phone_sin_leer("roxy"):
                    text "●" color "#fb923c" size 14 yalign 0.5
                else:
                    text "○" color "#334155" size 14 yalign 0.5
                vbox:
                    yalign 0.5
                    spacing 4
                    text "Roxy" style "phone_nombre_roxy"
                    text "[phone_ultimo_mensaje('roxy')]" style "phone_preview"

        ## LUNA
        button:
            action SetVariable("phone_contacto", "luna")
            style "phone_contacto_btn"
            xsize 600
            ysize 80
            hbox:
                spacing 16
                xalign 0.0
                yalign 0.5
                if phone_sin_leer("luna"):
                    text "●" color "#c084fc" size 14 yalign 0.5
                else:
                    text "○" color "#334155" size 14 yalign 0.5
                vbox:
                    yalign 0.5
                    spacing 4
                    text "Luna" style "phone_nombre_luna"
                    text "[phone_ultimo_mensaje('luna')]" style "phone_preview"

    ## Conversación abierta
    if phone_contacto != "":
        use phone_conversacion(phone_contacto)

    ## Volver
    textbutton "← Volver":
        xalign 0.0
        yalign 1.0
        xoffset 16
        yoffset -16
        action Return()
        style "accion_btn_volver"


## =============================================================
## PANTALLA DE CONVERSACIÓN
## =============================================================

screen phone_conversacion(contacto):

    frame:
        xalign 0.5
        yalign 0.5
        xsize 580
        ysize 520
        xpadding 16
        ypadding 16
        background "#0d1117"

        vbox:
            spacing 8

            ## Nombre del contacto
            text "[phone_nombre_display(contacto)]" style "phone_chat_nombre"
            null height 4

            ## Historial de mensajes
            viewport:
                ysize 360
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 10
                    for msg in phone_mensajes_de(contacto):
                        if msg["de"] == "ellas":
                            ## Mensaje de ella — izquierda
                            hbox:
                                xalign 0.0
                                frame:
                                    background "#1e293b"
                                    xpadding 12
                                    ypadding 8
                                    xmaximum 380
                                    text msg["texto"] style "phone_msg_ellas"
                        else:
                            ## Mensaje del MC — derecha
                            hbox:
                                xalign 1.0
                                frame:
                                    background "#1e3a5f"
                                    xpadding 12
                                    ypadding 8
                                    xmaximum 380
                                    text msg["texto"] style "phone_msg_mc"

            null height 8

            ## Opciones de respuesta si hay mensaje sin leer
            if phone_sin_leer(contacto):
                vbox:
                    spacing 6
                    text "Responder:" style "phone_label_responder"
                    for opcion in phone_opciones_respuesta(contacto):
                        textbutton opcion["texto"]:
                            action [
                                Function(phone_responder, contacto, opcion["tipo"]),
                                ScreenVariableValue("phone_contacto", contacto)
                            ]
                            style "phone_respuesta_btn"
            else:
                text "No hay mensajes nuevos." style "phone_sin_mensajes"


## =============================================================
## FUNCIONES DEL SISTEMA DE MENSAJES
## =============================================================

init python:

    ## ---------------------------------------------------------
    ## BANCO DE MENSAJES ESPONTÁNEOS
    ## Por personaje, organizados por nivel de Afecto
    ## Tono coherente con cada personaje del GDD
    ## ---------------------------------------------------------

    MENSAJES_CELINE = {
        "bajo": [  ## Afecto 0-30
            {"texto": "No uses mis cosas de la cocina sin preguntar.", "tipo": "neutro"},
            {"texto": "El ruido de la ducha a las 7am no es necesario.", "tipo": "neutro"},
            {"texto": "Si vas a usar la sala esta noche avísame.", "tipo": "neutro"},
        ],
        "medio": [  ## Afecto 31-60
            {"texto": "Roxy dice que compraste café. La próxima vez pregunta si alguien más quiere.", "tipo": "positivo"},
            {"texto": "¿Tienes los apuntes de lógica argumentativa de la semana pasada?", "tipo": "positivo"},
            {"texto": "Hay comida en el refrigerador si no comiste.", "tipo": "positivo"},
            {"texto": "No llegues tarde esta noche. El ascensor no funciona después de las 11.", "tipo": "neutro"},
        ],
        "alto": [  ## Afecto 61-100
            {"texto": "No puedo dormir. Nada importante.", "tipo": "positivo"},
            {"texto": "¿Sigues despierto?", "tipo": "positivo"},
            {"texto": "Mañana hay clases temprano. Por si acaso.", "tipo": "positivo"},
            {"texto": "El libro que dejé en la mesa es tuyo si quieres leerlo.", "tipo": "positivo"},
        ],
    }

    MENSAJES_ROXY = {
        "bajo": [
            {"texto": "oye conoces algún buen lugar para comer por aquí??? pregunto por preguntarrr", "tipo": "positivo"},
            {"texto": "ESPERA llevas cuánto tiempo viviendo aquí y nunca has visto Evangelion????", "tipo": "positivo"},
            {"texto": "https://youtu.be/dQw [meme de algo random]", "tipo": "positivo"},
        ],
        "medio": [
            {"texto": "oye si quieres ver una peli esta noche avísame no tengo nada que hacer jaja", "tipo": "positivo"},
            {"texto": "hice demasiada pasta otra vez. por si quieres. no es obligatorio. bueno sí un poco sí", "tipo": "positivo"},
            {"texto": "Luna dice que no hablas mucho. yo le dije que eso es mentira. tengo razón no?", "tipo": "positivo"},
            {"texto": "oye oye oye tengo una idea. no te asustes. igual te va a gustar", "tipo": "positivo"},
        ],
        "alto": [
            {"texto": "no puedo dormir y estoy dibujando cosas raras. nada importante. qué estás haciendo", "tipo": "positivo"},
            {"texto": "oye. gracias por lo de antes. ya sé que no fue gran cosa pero bueno", "tipo": "positivo"},
            {"texto": "sigues despierto? hago café si quieres. o té si eres de esos", "tipo": "positivo"},
            {"texto": "acabo de acordarme de algo de cuando éramos chicos y me dio mucha risa. luego te cuento", "tipo": "positivo"},
        ],
    }

    MENSAJES_LUNA = {
        "bajo": [
            {"texto": ".", "tipo": "neutro"},
            {"texto": "Hay leche en el refrigerador.", "tipo": "neutro"},
            {"texto": "El libro de la mesa no es mío.", "tipo": "neutro"},
        ],
        "medio": [
            {"texto": "¿Leíste algo bueno últimamente?", "tipo": "positivo"},
            {"texto": "Hay luz en tu cuarto a las 2am. ¿Bien?", "tipo": "positivo"},
            {"texto": "El balcón estará libre esta noche si quieres aire.", "tipo": "positivo"},
        ],
        "alto": [
            {"texto": "Pensé en algo que dijiste el otro día. Tenías razón.", "tipo": "positivo"},
            {"texto": "¿Sigues despierto?", "tipo": "positivo"},
            {"texto": "Hay una frase en el libro que no puedo sacarme de la cabeza.", "tipo": "positivo"},
            {"texto": "No es nada. Solo quería escribirte.", "tipo": "positivo"},
        ],
    }

    BANCO_MENSAJES = {
        "celine": MENSAJES_CELINE,
        "roxy":   MENSAJES_ROXY,
        "luna":   MENSAJES_LUNA,
    }

    ## ---------------------------------------------------------
    ## OPCIONES DE RESPUESTA
    ## 3 opciones por mensaje: bien, mal, ignorar (no responder)
    ## ---------------------------------------------------------

    RESPUESTAS_CELINE = {
        "neutro": [
            {"texto": "Entendido.",                              "tipo": "bien"},
            {"texto": "¿Y si no quiero?",                       "tipo": "mal"},
            {"texto": "(No responder)",                         "tipo": "ignorar"},
        ],
        "positivo": [
            {"texto": "Gracias por avisar.",                    "tipo": "bien"},
            {"texto": "No me interesa.",                        "tipo": "mal"},
            {"texto": "(No responder)",                         "tipo": "ignorar"},
        ],
    }

    RESPUESTAS_ROXY = {
        "neutro": [
            {"texto": "jajaja qué?",                            "tipo": "bien"},
            {"texto": "no tengo tiempo para esto",              "tipo": "mal"},
            {"texto": "(No responder)",                         "tipo": "ignorar"},
        ],
        "positivo": [
            {"texto": "cuenta cuenta",                          "tipo": "bien"},
            {"texto": "paso, gracias",                          "tipo": "mal"},
            {"texto": "(No responder)",                         "tipo": "ignorar"},
        ],
    }

    RESPUESTAS_LUNA = {
        "neutro": [
            {"texto": "Ok.",                                    "tipo": "bien"},
            {"texto": "...",                                    "tipo": "mal"},
            {"texto": "(No responder)",                         "tipo": "ignorar"},
        ],
        "positivo": [
            {"texto": "Sigo despierto. ¿Tú también?",          "tipo": "bien"},
            {"texto": "Mañana hablamos.",                       "tipo": "mal"},
            {"texto": "(No responder)",                         "tipo": "ignorar"},
        ],
    }

    BANCO_RESPUESTAS = {
        "celine": RESPUESTAS_CELINE,
        "roxy":   RESPUESTAS_ROXY,
        "luna":   RESPUESTAS_LUNA,
    }

    ## ---------------------------------------------------------
    ## GENERAR MENSAJES DEL DÍA
    ## Llamado desde time.rpy nuevo_dia()
    ## Probabilidad según nivel de Afecto (GDD S17)
    ## ---------------------------------------------------------
    def phone_generar_mensajes_dia():
        import random
        personajes = ["celine", "roxy", "luna"]
        for p in personajes:
            afecto = getattr(store, p + "_afecto", 0)

            ## Probabilidad de recibir mensaje según afecto
            if afecto <= 30:
                prob = 40    ## 0-1 mensajes/día → 40% de recibir uno
            elif afecto <= 60:
                prob = 70    ## 1-2 mensajes/día → 70%
            else:
                prob = 95    ## 2-4 mensajes/día → casi siempre

            if random.randint(1, 100) <= prob:
                ## Elegir banco según nivel de afecto
                if afecto <= 30:
                    nivel = "bajo"
                elif afecto <= 60:
                    nivel = "medio"
                else:
                    nivel = "alto"

                banco = BANCO_MENSAJES.get(p, {}).get(nivel, [])
                if banco:
                    msg = random.choice(banco)
                    ## Agregar a la bandeja sin leer
                    bandeja = getattr(store, "phone_bandeja_" + p, [])
                    bandeja.append({
                        "texto": msg["texto"],
                        "tipo":  msg["tipo"],
                        "de":    "ellas",
                        "leido": False,
                    })
                    setattr(store, "phone_bandeja_" + p, bandeja)

    ## ---------------------------------------------------------
    ## RESPONDER MENSAJE
    ## tipo: "bien" → +2 Afecto / "mal" → -3 Afecto / "ignorar" → -1 Afecto
    ## ---------------------------------------------------------
    def phone_responder(contacto, tipo_respuesta):
        ## Marcar mensajes como leídos
        bandeja = getattr(store, "phone_bandeja_" + contacto, [])
        for msg in bandeja:
            msg["leido"] = True
        setattr(store, "phone_bandeja_" + contacto, bandeja)

        ## Aplicar efecto según tipo de respuesta
        if tipo_respuesta == "bien":
            cambiar_stat(contacto, "afecto", 2)
            ## Agregar respuesta del MC al historial
            respuestas_mc = {
                "celine": "Entendido.",
                "roxy":   "cuenta cuenta",
                "luna":   "Sigo despierto.",
            }
            bandeja.append({
                "texto": respuestas_mc.get(contacto, "Ok."),
                "tipo":  "bien",
                "de":    "mc",
                "leido": True,
            })
        elif tipo_respuesta == "mal":
            cambiar_stat(contacto, "afecto", -3)
        elif tipo_respuesta == "ignorar":
            cambiar_stat(contacto, "afecto", -1)

        registrar_interaccion(contacto)

    ## ---------------------------------------------------------
    ## AUXILIARES DE PANTALLA
    ## ---------------------------------------------------------
    def phone_sin_leer(contacto):
        bandeja = getattr(store, "phone_bandeja_" + contacto, [])
        return any(not msg["leido"] for msg in bandeja if msg["de"] == "ellas")

    def phone_ultimo_mensaje(contacto):
        bandeja = getattr(store, "phone_bandeja_" + contacto, [])
        if bandeja:
            return bandeja[-1]["texto"][:40] + "..." if len(bandeja[-1]["texto"]) > 40 else bandeja[-1]["texto"]
        return "Sin mensajes"

    def phone_mensajes_de(contacto):
        return getattr(store, "phone_bandeja_" + contacto, [])

    def phone_nombre_display(contacto):
        nombres = {"celine": "Celine", "roxy": "Roxy", "luna": "Luna"}
        return nombres.get(contacto, "")

    def phone_opciones_respuesta(contacto):
        ## Busca el último mensaje sin leer y devuelve sus opciones
        bandeja = getattr(store, "phone_bandeja_" + contacto, [])
        for msg in reversed(bandeja):
            if not msg["leido"] and msg["de"] == "ellas":
                tipo = msg.get("tipo", "neutro")
                return BANCO_RESPUESTAS.get(contacto, {}).get(tipo, [])
        return []


## =============================================================
## INTEGRACIÓN CON time.rpy
## Agregar llamada a phone_generar_mensajes_dia() en nuevo_dia()
## INSTRUCCIÓN: en time.rpy, dentro de nuevo_dia(), agregar:
##     phone_generar_mensajes_dia()
## después de generar_moods()
## =============================================================

## =============================================================
## LABEL DE ENTRADA
## Reemplaza el placeholder en map.rpy
## =============================================================

label telefono_main:
    $ phone_contacto = ""
    call screen pantalla_telefono
    jump mapa_loop


## =============================================================
## ESTILOS
## =============================================================

style phone_titulo:
    color "#e2e8f0"
    size 20
    bold True
    xalign 0.5

style phone_contacto_btn:
    background "#13131a"
    hover_background "#1e293b"
    xpadding 16
    ypadding 12

style phone_nombre_celine:
    color "#818cf8"
    size 16
    bold True

style phone_nombre_roxy:
    color "#fb923c"
    size 16
    bold True

style phone_nombre_luna:
    color "#c084fc"
    size 16
    bold True

style phone_preview:
    color "#64748b"
    size 13

style phone_chat_nombre:
    color "#e2e8f0"
    size 16
    bold True
    xalign 0.5

style phone_msg_ellas:
    color "#e2e8f0"
    size 14

style phone_msg_mc:
    color "#bfdbfe"
    size 14

style phone_label_responder:
    color "#64748b"
    size 13

style phone_respuesta_btn:
    background "#1e293b"
    hover_background "#334155"
    color "#e2e8f0"
    size 13
    xpadding 12
    ypadding 6
    xfill True

style phone_sin_mensajes:
    color "#475569"
    size 13
    xalign 0.5

## =============================================================
## VARIABLES
## =============================================================

default phone_contacto      = ""
default phone_bandeja_celine = []
default phone_bandeja_roxy   = []
default phone_bandeja_luna   = []