## =============================================================
## APARTMENT SIM — stats.rpy
## Sistema central de variables y funciones de stats
## Todos los números vienen del GDD_SISTEMAS.md v2.0
## CORREGIDO: eliminada mc_energia huérfana
## =============================================================

init python:

    def clamp(valor, minimo=0, maximo=100):
        return max(minimo, min(maximo, valor))

    def cambiar_stat(personaje, stat, cantidad):
        var_name = personaje + "_" + stat
        valor_actual = getattr(store, var_name, 0)

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

        if stat == "corrupcion" and cantidad > 0:
            afecto_actual    = getattr(store, personaje + "_afecto", 0)
            confianza_actual = getattr(store, personaje + "_confianza", 0)
            corrup_actual    = valor_actual
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
                return

        nuevo_valor = clamp(valor_actual + cantidad)
        setattr(store, var_name, nuevo_valor)

    def cambiar_stat_mc(stat, cantidad):
        if stat == "encanto":
            store.mc_encanto = clamp(store.mc_encanto + cantidad)
        elif stat == "energia_max":
            store.mc_energia_max = clamp(store.mc_energia_max + cantidad, 6, 10)
            ## Sincronizar energía actual si subió el máximo
            store.energia_actual = min(store.energia_actual + 1, store.mc_energia_max)
        elif stat == "dinero":
            store.mc_dinero = max(0, store.mc_dinero + cantidad)

    def cambiar_armonia(cantidad):
        store.armonia = clamp(store.armonia + cantidad)

    def puede_entrar(personaje):
        afecto = getattr(store, personaje + "_afecto", 0)
        requisitos = {"roxy": 20, "celine": 35, "luna": 45}
        return afecto >= requisitos.get(personaje, 999)

    def arquetipo_dominante():
        puntos = {
            "romantico":  store.arquetipo_romantico,
            "atrevido":   store.arquetipo_atrevido,
            "respetuoso": store.arquetipo_respetuoso,
        }
        return max(puntos, key=puntos.get)

    def bonus_arquetipo(personaje):
        preferencia = {"celine": "respetuoso", "roxy": "atrevido", "luna": "romantico"}
        arquetipo = arquetipo_dominante()
        preferido = preferencia.get(personaje, "")
        if arquetipo == preferido:
            return 1.20
        opuestos = {"respetuoso": "atrevido", "atrevido": "respetuoso", "romantico": "atrevido"}
        if opuestos.get(arquetipo) == preferido:
            return 0.90
        return 1.0

    def sumar_arquetipo(tipo):
        if tipo == "romantico":
            store.arquetipo_romantico += 1
        elif tipo == "atrevido":
            store.arquetipo_atrevido += 1
        elif tipo == "respetuoso":
            store.arquetipo_respetuoso += 1

    def registrar_decision(clave):
        if clave not in store.memoria_decisiones:
            store.memoria_decisiones.append(clave)
            if len(store.memoria_decisiones) > 20:
                store.memoria_decisiones.pop(0)

    def recuerda(clave):
        return clave in store.memoria_decisiones

    def ganar_dinero(cantidad):
        store.mc_dinero += cantidad

    def gastar_dinero(cantidad):
        if store.mc_dinero >= cantidad:
            store.mc_dinero -= cantidad
            return True
        return False

    def descubrir_secreto(personaje, numero):
        clave = personaje + "_secreto_" + str(numero)
        if not getattr(store, clave, False):
            setattr(store, clave, True)
            cambiar_stat(personaje, "confianza", 10)

    def puede_iniciar(personaje):
        corrup = getattr(store, personaje + "_corrupcion", 0)
        afecto = getattr(store, personaje + "_afecto", 0)
        mood   = getattr(store, personaje + "_mood", "normal")
        return corrup > 60 and afecto > 70 and mood == "traviesa"


## =============================================================
## VARIABLES
## =============================================================

default mc_nombre      = "Kai"
default mc_encanto     = 10
default mc_energia_max = 6
## NOTA: mc_energia eliminada — usar energia_actual de time.rpy
default mc_dinero      = 500

default arquetipo_romantico  = 0
default arquetipo_atrevido   = 0
default arquetipo_respetuoso = 0

## CELINE
default celine_afecto     = 5
default celine_confianza  = 5
default celine_corrupcion = 0
default celine_mood       = "normal"
default celine_secreto_1  = False
default celine_secreto_2  = False
default celine_secreto_3  = False
default celine_cuarto_desbloqueado = False

## ROXY
default roxy_afecto     = 15
default roxy_confianza  = 10
default roxy_corrupcion = 0
default roxy_mood       = "normal"
default roxy_secreto_1  = False
default roxy_secreto_2  = False
default roxy_secreto_3  = False
default roxy_cuarto_desbloqueado = False

## LUNA
default luna_afecto     = 5
default luna_confianza  = 5
default luna_corrupcion = 0
default luna_mood       = "normal"
default luna_secreto_1  = False
default luna_secreto_2  = False
default luna_secreto_3  = False
default luna_cuarto_desbloqueado = False

## APARTAMENTO
default armonia = 70

## PROGRESO NARRATIVO
default celine_acto = 0
default roxy_acto   = 0
default luna_acto   = 0

default celine_quest_1 = False
default celine_quest_2 = False
default celine_quest_3 = False
default roxy_quest_1   = False
default roxy_quest_2   = False
default roxy_quest_3   = False
default luna_quest_1   = False
default luna_quest_2   = False
default luna_quest_3   = False

default tiene_camara       = False
default memoria_decisiones = []

default celine_celosa = False
default roxy_celosa   = False
default luna_celosa   = False

default galeria_celine = []
default galeria_roxy   = []
default galeria_luna   = []