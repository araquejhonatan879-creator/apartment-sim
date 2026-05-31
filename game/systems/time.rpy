## =============================================================
## APARTMENT SIM — time.rpy
## Sistema de días, franjas horarias y energía
## Números y reglas del GDD_SISTEMAS.md S04
## =============================================================

init python:

    # ----------------------------------------------------------
    # FRANJAS HORARIAS
    # Orden del día: mañana → tarde → noche → madrugada → (nuevo día)
    # ----------------------------------------------------------
    FRANJAS = ["mañana", "tarde", "noche", "madrugada"]

    # Etiquetas legibles para el HUD
    FRANJA_LABEL = {
        "mañana":    "Mañana  6am – 12pm",
        "tarde":     "Tarde   12pm – 6pm",
        "noche":     "Noche   6pm – 12am",
        "madrugada": "Madrugada  12am – 6am",
    }

    # ----------------------------------------------------------
    # AVANZAR FRANJA
    # Consume 1 acción. Si se agotan las acciones, avanza la franja.
    # Si era madrugada, avanza al nuevo día.
    # ----------------------------------------------------------
    def usar_accion():
        store.energia_actual -= 1
        if store.energia_actual <= 0:
            avanzar_franja()

    def avanzar_franja():
        idx_actual = FRANJAS.index(store.franja_actual)
        if idx_actual < len(FRANJAS) - 1:
            store.franja_actual = FRANJAS[idx_actual + 1]
            store.energia_actual = acciones_por_franja()
        else:
            # Era madrugada — nuevo día
            nuevo_dia()

    # ----------------------------------------------------------
    # ACCIONES POR FRANJA
    # Base: 2 acciones por franja
    # La energía máxima del MC expande esto proporcionalmente:
    # energia_max 6  → 2 acciones por franja  (2×3 franjas activas = 6)
    # energia_max 8  → 2-3 según franja
    # energia_max 10 → 3 acciones por franja
    # Madrugada siempre da 1 acción (franja de bajo rendimiento)
    # ----------------------------------------------------------
    def acciones_por_franja():
        if store.franja_actual == "madrugada":
            return 1
        base = 2
        extra = (store.mc_energia_max - 6) // 2
        return base + extra

    # ----------------------------------------------------------
    # NUEVO DÍA
    # Avanza el contador, resetea energía, genera estados de ánimo,
    # aplica penalizaciones por ignorar personajes
    # ----------------------------------------------------------
    def nuevo_dia():
        store.dia_actual += 1
        store.franja_actual = "mañana"
        store.energia_actual = acciones_por_franja()

        # Generar estado de ánimo del día para cada personaje
        generar_moods()

        # Penalización por ignorar personajes (GDD S01)
        aplicar_penalizacion_ignorar()

        # Reducir celos activos si el jugador atendió al personaje celoso
        actualizar_celos()

        # Autosave al inicio de cada nuevo día
        renpy.save("auto", "Autosave — Día {}".format(store.dia_actual))

    # ----------------------------------------------------------
    # ES FIN DE SEMANA
    # Sábado = día % 7 == 6, Domingo = día % 7 == 0
    # El juego empieza en lunes (día 1)
    # ----------------------------------------------------------
    def es_fin_de_semana():
        return store.dia_actual % 7 in (0, 6)

    # ----------------------------------------------------------
    # GENERAR ESTADOS DE ÁNIMO DIARIOS
    # Probabilidades del GDD_SISTEMAS S08:
    # Normal 40%, Feliz 20%, Cansada 15%, Estresada 15%, Traviesa 10%
    # ----------------------------------------------------------
    def generar_moods():
        import random
        tabla = [
            ("normal",    40),
            ("feliz",     20),
            ("cansada",   15),
            ("estresada", 15),
            ("traviesa",  10),
        ]
        personajes = ["celine", "roxy", "luna"]
        for p in personajes:
            tirada = random.randint(1, 100)
            acumulado = 0
            for (mood, probabilidad) in tabla:
                acumulado += probabilidad
                if tirada <= acumulado:
                    setattr(store, p + "_mood", mood)
                    break

    # ----------------------------------------------------------
    # PENALIZACIÓN POR IGNORAR
    # Ignorar 1 día: -1 Afecto
    # Ignorar 3 días seguidos: -5 Afecto -2 Confianza (GDD S01)
    # Se rastrea con contadores de días sin interacción
    # ----------------------------------------------------------
    def aplicar_penalizacion_ignorar():
        personajes = ["celine", "roxy", "luna"]
        for p in personajes:
            contador_var = p + "_dias_sin_interaccion"
            contador = getattr(store, contador_var, 0)
            contador += 1
            setattr(store, contador_var, contador)

            if contador >= 3:
                cambiar_stat(p, "afecto", -5)
                cambiar_stat(p, "confianza", -2)
            elif contador >= 1:
                cambiar_stat(p, "afecto", -1)

    def registrar_interaccion(personaje):
        """Llama esto cada vez que el jugador interactúa con un personaje.
        Resetea el contador de días sin interacción."""
        setattr(store, personaje + "_dias_sin_interaccion", 0)

    # ----------------------------------------------------------
    # CELOS — bajar nivel si el jugador atendió al personaje celoso
    # Si lleva 3 días de acciones dirigidas al personaje celoso: se resuelve
    # ----------------------------------------------------------
    def actualizar_celos():
        personajes = ["celine", "roxy", "luna"]
        for p in personajes:
            if getattr(store, p + "_celosa", False):
                contador_var = p + "_dias_atendido_celos"
                contador = getattr(store, contador_var, 0)
                # Si el jugador interactuó ayer con este personaje
                if getattr(store, p + "_dias_sin_interaccion", 0) == 0:
                    contador += 1
                    setattr(store, contador_var, contador)
                    if contador >= 3:
                        setattr(store, p + "_celosa", False)
                        setattr(store, contador_var, 0)
                else:
                    setattr(store, contador_var, 0)

    # ----------------------------------------------------------
    # DÓNDE ESTÁ CADA PERSONAJE en la franja actual
    # Devuelve la ubicación probable según rutinas del GDD S04
    # No es absoluto — el mood puede cambiarlo en eventos especiales
    # ----------------------------------------------------------
    def ubicacion_probable(personaje):
        franja = store.franja_actual
        finde  = es_fin_de_semana()

        rutinas = {
            "celine": {
                "mañana":    "cocina",
                "tarde":     "cuarto" if not finde else "sala",
                "noche":     "sala",
                "madrugada": "cuarto",
            },
            "roxy": {
                "mañana":    "cocina",
                "tarde":     "sala" if not finde else "afuera",
                "noche":     "sala",
                "madrugada": "sala",
            },
            "luna": {
                "mañana":    "cocina",
                "tarde":     "cuarto",
                "noche":     "balcon",
                "madrugada": "cocina",
            },
        }
        return rutinas.get(personaje, {}).get(franja, "cuarto")

    # ----------------------------------------------------------
    # VERIFICAR SI UN PERSONAJE ESTÁ DISPONIBLE para interactuar
    # Lunes-Viernes tarde: disponibilidad reducida (clase/estudio)
    # ----------------------------------------------------------
    def esta_disponible(personaje):
        if store.franja_actual == "tarde" and not es_fin_de_semana():
            # Celine y Luna estudian más, Roxy a veces también
            probabilidad_ausente = {
                "celine": 70,
                "luna":   60,
                "roxy":   40,
            }
            import random
            return random.randint(1, 100) > probabilidad_ausente.get(personaje, 50)
        return True

    # ----------------------------------------------------------
    # TEXTO DEL DÍA DE LA SEMANA
    # ----------------------------------------------------------
    def dia_semana():
        dias = ["Lunes", "Martes", "Miércoles", "Jueves",
                "Viernes", "Sábado", "Domingo"]
        return dias[(store.dia_actual - 1) % 7]


## =============================================================
## VARIABLES DE TIEMPO
## =============================================================

default dia_actual     = 1
default franja_actual  = "mañana"
default energia_actual = 2   # Se recalcula al inicio con acciones_por_franja()

# Contadores de días sin interacción por personaje
default celine_dias_sin_interaccion = 0
default roxy_dias_sin_interaccion   = 0
default luna_dias_sin_interaccion   = 0

# Contadores para resolver celos
default celine_dias_atendido_celos = 0
default roxy_dias_atendido_celos   = 0
default luna_dias_atendido_celos   = 0
