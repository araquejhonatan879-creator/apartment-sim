## =============================================================
## APARTMENT SIM — stats.rpy
## Sistema central de variables y funciones de stats
## Todos los números vienen del GDD_SISTEMAS.md v2.0
## =============================================================

init python:

    # ----------------------------------------------------------
    # FUNCIÓN AUXILIAR: clampear un valor entre un mínimo y máximo
    # Evita que ninguna stat se salga de su rango válido (0-100)
    # ----------------------------------------------------------
    def clamp(valor, minimo=0, maximo=100):
        return max(minimo, min(maximo, valor))

    # ----------------------------------------------------------
    # MODIFICAR STATS DE PERSONAJE
    # Uso: cambiar_stat("celine", "afecto", +5)
    # Aplica multiplicadores de estado de ánimo automáticamente
    # ----------------------------------------------------------
    def cambiar_stat(personaje, stat, cantidad):
        var_name = personaje + "_" + stat
        valor_actual = getattr(store, var_name, 0)

        # Aplicar multiplicador de estado de ánimo solo al Afecto
        if stat == "afecto" and cantidad > 0:
            mood_var = personaje + "_mood"
            mood = getattr(store, mood_var, "normal")
            multiplicadores = {
                "normal":    1.0,
                "feliz":     1.5,
                "cansada":   0.7,
                "estresada": 1.3,
                "traviesa":  1.2
            }
            cantidad = int(cantidad * multiplicadores.get(mood, 1.0))

        # Validar corrupción: requiere mínimos de afecto y confianza
        if stat == "corrupcion" and cantidad > 0:
            afecto_var    = personaje + "_afecto"
            confianza_var = personaje + "_confianza"
            afecto_actual    = getattr(store, afecto_var, 0)
            confianza_actual = getattr(store, confianza_var, 0)
            corrup_actual    = valor_actual

            # Tabla de requisitos mínimos del GDD_SISTEMAS S01
            requisitos = [
                (0,  20,  15, 10),
                (20, 45,  35, 25),
                (45, 70,  55, 45),
                (70, 90,  75, 60),
                (90, 100, 90, 75),
            ]
            puede_subir = True
            for (desde, hasta, af_min, con_min) in requisitos:
                if corrup_actual >= desde and corrup_actual < hasta:
                    if afecto_actual < af_min or confianza_actual < con_min:
                        puede_subir = False
                    break
            if not puede_subir:
                return  # No sube corrupción si no cumple requisitos

        nuevo_valor = clamp(valor_actual + cantidad)
        setattr(store, var_name, nuevo_valor)

    # ----------------------------------------------------------
    # MODIFICAR STATS DEL PROTAGONISTA
    # Uso: cambiar_stat_mc("encanto", +2)
    # ----------------------------------------------------------
    def cambiar_stat_mc(stat, cantidad):
        if stat == "encanto":
            store.mc_encanto = clamp(store.mc_encanto + cantidad)
        elif stat == "energia_max":
            store.mc_energia_max = clamp(store.mc_energia_max + cantidad, 6, 10)
        elif stat == "dinero":
            store.mc_dinero = max(0, store.mc_dinero + cantidad)

    # ----------------------------------------------------------
    # MODIFICAR ARMONÍA DEL APARTAMENTO
    # Uso: cambiar_armonia(-5)
    # ----------------------------------------------------------
    def cambiar_armonia(cantidad):
        store.armonia = clamp(store.armonia + cantidad)

    # ----------------------------------------------------------
    # VERIFICAR SI SE PUEDE DESBLOQUEAR UN CUARTO
    # Uso: puede_entrar("celine") → True/False
    # ----------------------------------------------------------
    def puede_entrar(personaje):
        afecto = getattr(store, personaje + "_afecto", 0)
        requisitos = {
            "roxy":   20,
            "celine": 35,
            "luna":   45,
        }
        return afecto >= requisitos.get(personaje, 999)

    # ----------------------------------------------------------
    # DETECTAR ARQUETIPO DOMINANTE DEL JUGADOR
    # Recalcula basado en puntos acumulados
    # Retorna: "romantico", "atrevido" o "respetuoso"
    # ----------------------------------------------------------
    def arquetipo_dominante():
        puntos = {
            "romantico":   store.arquetipo_romantico,
            "atrevido":    store.arquetipo_atrevido,
            "respetuoso":  store.arquetipo_respetuoso,
        }
        return max(puntos, key=puntos.get)

    # ----------------------------------------------------------
    # BONUS DE ARQUETIPO
    # Retorna el multiplicador según afinidad con el personaje
    # Personajes preferidos: Luna=romántico, Roxy=atrevido, Celine=respetuoso
    # ----------------------------------------------------------
    def bonus_arquetipo(personaje):
        preferencia = {
            "celine": "respetuoso",
            "roxy":   "atrevido",
            "luna":   "romantico",
        }
        arquetipo = arquetipo_dominante()
        preferido = preferencia.get(personaje, "")

        if arquetipo == preferido:
            return 1.20   # +20% a afecto ganado
        # Verificar si es opuesto
        opuestos = {
            "respetuoso": "atrevido",
            "atrevido":   "respetuoso",
            "romantico":  "atrevido",
        }
        if opuestos.get(arquetipo) == preferido:
            return 0.90   # -10%
        return 1.0        # neutro

    # ----------------------------------------------------------
    # SUMAR PUNTO DE ARQUETIPO
    # Uso: sumar_arquetipo("romantico")
    # ----------------------------------------------------------
    def sumar_arquetipo(tipo):
        if tipo == "romantico":
            store.arquetipo_romantico += 1
        elif tipo == "atrevido":
            store.arquetipo_atrevido += 1
        elif tipo == "respetuoso":
            store.arquetipo_respetuoso += 1

    # ----------------------------------------------------------
    # REGISTRAR DECISIÓN EN MEMORIA
    # Guarda hasta 20 decisiones importantes para menciones futuras
    # Uso: registrar_decision("prometiste_ayudar_celine")
    # ----------------------------------------------------------
    def registrar_decision(clave):
        if clave not in store.memoria_decisiones:
            store.memoria_decisiones.append(clave)
            if len(store.memoria_decisiones) > 20:
                store.memoria_decisiones.pop(0)  # Descarta la más antigua

    # ----------------------------------------------------------
    # VERIFICAR SI EXISTE UNA DECISIÓN EN MEMORIA
    # Uso: if recuerda("prometiste_ayudar_celine"):
    # ----------------------------------------------------------
    def recuerda(clave):
        return clave in store.memoria_decisiones

    # ----------------------------------------------------------
    # GANAR DINERO (trabajo o quests)
    # Uso: ganar_dinero(90) — pago base de trabajo
    # ----------------------------------------------------------
    def ganar_dinero(cantidad):
        store.mc_dinero += cantidad

    # ----------------------------------------------------------
    # GASTAR DINERO
    # Retorna True si pudo pagar, False si no tiene suficiente
    # Uso: if gastar_dinero(40): [dar regalo]
    # ----------------------------------------------------------
    def gastar_dinero(cantidad):
        if store.mc_dinero >= cantidad:
            store.mc_dinero -= cantidad
            return True
        return False

    # ----------------------------------------------------------
    # DESCUBRIR SECRETO
    # +10 Confianza inmediata + marca el secreto como descubierto
    # Uso: descubrir_secreto("celine", 1)
    # ----------------------------------------------------------
    def descubrir_secreto(personaje, numero):
        clave = personaje + "_secreto_" + str(numero)
        if not getattr(store, clave, False):
            setattr(store, clave, True)
            cambiar_stat(personaje, "confianza", 10)

    # ----------------------------------------------------------
    # VERIFICAR ESTADO DE ÁNIMO TRAVIESA PARA INICIATIVA INVERSA
    # Condición del GDD: Corrupción >60 + Afecto >70 + mood Traviesa
    # ----------------------------------------------------------
    def puede_iniciar(personaje):
        corrup   = getattr(store, personaje + "_corrupcion", 0)
        afecto   = getattr(store, personaje + "_afecto", 0)
        mood     = getattr(store, personaje + "_mood", "normal")
        return corrup > 60 and afecto > 70 and mood == "traviesa"


## =============================================================
## VARIABLES — se inicializan al empezar nueva partida
## =============================================================

default mc_nombre       = "Kai"
default mc_encanto      = 10
default mc_energia_max  = 6
default mc_energia      = 6
default mc_dinero       = 500

# Arquetipos del jugador (acumulan puntos con las elecciones)
default arquetipo_romantico  = 0
default arquetipo_atrevido   = 0
default arquetipo_respetuoso = 0

# ----------------------------
# STATS DE CELINE
# ----------------------------
default celine_afecto     = 5
default celine_confianza  = 5
default celine_corrupcion = 0
default celine_mood       = "normal"

# Secretos de Celine
default celine_secreto_1 = False   # Diario con entradas sobre el MC
default celine_secreto_2 = False   # Conversación con Roxy sobre el MC
default celine_secreto_3 = False   # Llora sola de madrugada

# Cuarto desbloqueado
default celine_cuarto_desbloqueado = False

# ----------------------------
# STATS DE ROXY
# ----------------------------
default roxy_afecto     = 15
default roxy_confianza  = 10
default roxy_corrupcion = 0
default roxy_mood       = "normal"

# Secretos de Roxy
default roxy_secreto_1 = False   # Bocetos del MC en su sketchbook
default roxy_secreto_2 = False   # Fotos de los dos que no tiró
default roxy_secreto_3 = False   # Le habla a Luna sobre el MC

# Cuarto desbloqueado
default roxy_cuarto_desbloqueado = False

# ----------------------------
# STATS DE LUNA
# ----------------------------
default luna_afecto     = 5
default luna_confianza  = 5
default luna_corrupcion = 0
default luna_mood       = "normal"

# Secretos de Luna
default luna_secreto_1 = False   # Página con el nombre del MC en su cuaderno
default luna_secreto_2 = False   # Cartas que no envió
default luna_secreto_3 = False   # La encuentras llorando a las 3am

# Cuarto desbloqueado
default luna_cuarto_desbloqueado = False

# ----------------------------
# ARMONÍA DEL APARTAMENTO
# ----------------------------
default armonia = 70   # Valor inicial: llevan tiempo conviviendo bien

# ----------------------------
# EVENTOS Y PROGRESO NARRATIVO
# ----------------------------
# Actos completados por personaje (0 = ninguno, 5 = todos)
default celine_acto = 0
default roxy_acto   = 0
default luna_acto   = 0

# Quests completadas
default celine_quest_1 = False
default celine_quest_2 = False
default celine_quest_3 = False
default roxy_quest_1   = False
default roxy_quest_2   = False
default roxy_quest_3   = False
default luna_quest_1   = False
default luna_quest_2   = False
default luna_quest_3   = False

# ----------------------------
# ITEMS DEL JUGADOR
# ----------------------------
default tiene_camara = False   # Desbloquea sistema voyeur

# ----------------------------
# MEMORIA DE DECISIONES
# Lista de hasta 20 claves de decisiones importantes
# ----------------------------
default memoria_decisiones = []

# ----------------------------
# CELOS ACTIVOS
# True = ese personaje tiene celos actualmente
# ----------------------------
default celine_celosa = False
default roxy_celosa   = False
default luna_celosa   = False

# ----------------------------
# GALERÍA — escenas desbloqueadas
# Cada clave es True cuando la escena fue vista
# ----------------------------
default galeria_celine = []
default galeria_roxy   = []
default galeria_luna   = []
