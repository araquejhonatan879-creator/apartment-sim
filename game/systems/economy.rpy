##############################################################################
# APARTMENT SIM — SISTEMA ECONÓMICO
# Archivo: game/systems/economy.rpy
# Módulo: Dinero, compras, trabajo, regalos e ítems del jugador
# Versión: 1.0
# Última modificación: 31/05/2026
# Dependencias:
#   game/systems/stats.rpy  (prot_dinero — declarado allí, modificado aquí)
# Descripción:
#   Gestiona todas las operaciones económicas del protagonista: pagar,
#   cobrar, verificar saldo, comprar ítems de la tienda y dar regalos
#   a personajes. prot_dinero está declarado en stats.rpy porque
#   conceptualmente es un stat del protagonista, pero economy.rpy es
#   el único módulo autorizado a modificarlo.
##############################################################################


##############################################################################
# FUNCIONES PYTHON DEL MÓDULO
##############################################################################

init python:

    def fn_economia_pagar(monto):
        """
        Deduce dinero del saldo del protagonista si hay suficiente.

        Parámetros:
            monto (int): cantidad a descontar (debe ser positivo)

        Retorna:
            bool: True si el pago se realizó (había saldo)
                  False si no había suficiente dinero (saldo no cambia)

        Uso desde labels:
            if fn_economia_pagar(150):
                "Compraste la cámara."
            else:
                "No tienes suficiente dinero."
        """

        if monto <= 0:
            fn_debug_log(
                "[economy] fn_economia_pagar: monto inválido {}".format(monto)
            )
            return False

        if store.prot_dinero >= monto:
            store.prot_dinero = store.prot_dinero - monto
            fn_debug_log(
                "[economy] Pago: -{} | Saldo: {} → {}".format(
                    monto,
                    store.prot_dinero + monto,
                    store.prot_dinero
                )
            )
            return True
        else:
            fn_debug_log(
                "[economy] Pago fallido: necesita {} pero tiene {}".format(
                    monto, store.prot_dinero
                )
            )
            return False


    def fn_economia_cobrar(monto):
        """
        Agrega dinero al saldo del protagonista (salario, venta, etc.).

        Parámetros:
            monto (int): cantidad a agregar (debe ser positivo)

        Retorna:
            int: saldo nuevo después del cobro

        Uso desde labels:
            $ fn_economia_cobrar(200)
            "Cobraste tu turno en el café."
        """

        if monto <= 0:
            fn_debug_log(
                "[economy] fn_economia_cobrar: monto inválido {}".format(monto)
            )
            return store.prot_dinero

        store.prot_dinero = store.prot_dinero + monto

        fn_debug_log(
            "[economy] Cobro: +{} | Saldo: {}".format(monto, store.prot_dinero)
        )

        return store.prot_dinero


    def fn_economia_tiene_saldo(monto):
        """
        Verifica si el protagonista tiene suficiente dinero sin descontarlo.
        Útil para mostrar/ocultar opciones en menus antes de ejecutarlas.

        Parámetros:
            monto (int): cantidad a verificar

        Retorna:
            bool: True si prot_dinero >= monto

        Uso en condiciones de menu:
            menu:
                "Comprar cámara ($150)" if fn_economia_tiene_saldo(150):
                    $ fn_economia_comprar_item("camara")
        """

        return store.prot_dinero >= monto


    def fn_economia_comprar_item(id_item):
        """
        Intenta comprar un ítem de la tienda. Verifica saldo, descuenta
        el precio y activa el flag item_* correspondiente.

        Catálogo actual (Fase 1-2 — expandir en Fase 4):
            "camara" → $150 → activa item_camara

        Parámetros:
            id_item (str): identificador del ítem ("camara", etc.)

        Retorna:
            bool: True si la compra se realizó
                  False si no hay saldo o el ítem ya estaba comprado

        Uso desde labels:
            if fn_economia_comprar_item("camara"):
                "Ahora tienes una cámara compacta."
            else:
                "No pudiste comprar la cámara."
        """

        # Catálogo: id_item → (precio, nombre_variable_flag)
        catalogo = {
            "camara": (150, "item_camara"),
        }

        if id_item not in catalogo:
            fn_debug_log(
                "[economy] fn_economia_comprar_item: ítem desconocido '{}'".format(
                    id_item
                )
            )
            return False

        precio, nombre_flag = catalogo[id_item]

        # Verificar si ya lo tiene
        if getattr(store, nombre_flag, False):
            fn_debug_log(
                "[economy] fn_economia_comprar_item: '{}' ya estaba comprado".format(
                    id_item
                )
            )
            return False

        # Intentar el pago
        if fn_economia_pagar(precio):
            setattr(store, nombre_flag, True)
            fn_debug_log(
                "[economy] Compra exitosa: {} por ${}".format(id_item, precio)
            )
            return True
        else:
            return False


    def fn_economia_dar_regalo(personaje, id_regalo):
        """
        Da un regalo a un personaje: descuenta el precio del saldo y aplica
        el bonus de afecto/confianza correspondiente usando fn_stats_modificar().

        Catálogo de regalos actual (Fase 2 — expandir en Fase 4):
            "flores"    → $30  → +5 afecto
            "libro"     → $50  → +4 afecto +3 confianza
            "chocolate" → $20  → +3 afecto
            "perfume"   → $80  → +7 afecto +2 confianza

        Parámetros:
            personaje (str): "celine", "roxy" o "luna"
            id_regalo (str): identificador del regalo

        Retorna:
            bool: True si el regalo se entregó con éxito
                  False si no hay saldo o regalo desconocido

        Uso desde labels:
            if fn_economia_dar_regalo("celine", "flores"):
                cel "Ay, qué bonitas. Gracias."
            else:
                "No tienes suficiente dinero para el regalo."
        """

        # Catálogo: id_regalo → (precio, delta_afecto, delta_confianza)
        catalogo_regalos = {
            "flores":    (30,  5, 0),
            "libro":     (50,  4, 3),
            "chocolate": (20,  3, 0),
            "perfume":   (80,  7, 2),
        }

        if id_regalo not in catalogo_regalos:
            fn_debug_log(
                "[economy] fn_economia_dar_regalo: regalo desconocido '{}'".format(
                    id_regalo
                )
            )
            return False

        precio, delta_afecto, delta_confianza = catalogo_regalos[id_regalo]

        # Intentar el pago
        if not fn_economia_pagar(precio):
            return False

        # Aplicar bonus de stats usando la función oficial del módulo stats
        if delta_afecto != 0:
            fn_stats_modificar(personaje, "afecto", delta_afecto)

        if delta_confianza != 0:
            fn_stats_modificar(personaje, "confianza", delta_confianza)

        fn_debug_log(
            "[economy] Regalo '{}' dado a {} por ${} (+afecto={}, +confianza={})".format(
                id_regalo, personaje, precio, delta_afecto, delta_confianza
            )
        )

        return True


##############################################################################
# VARIABLES DEL MÓDULO
# Keyword: default — se guardan en save, participan en rollback
# NOTA: prot_dinero está declarado en stats.rpy — no redeclarar aquí.
##############################################################################

# Cámara compacta — habilita mecánica de fotos (Fase 5)
# Precio: $150 en la tienda del juego
default item_camara = False
