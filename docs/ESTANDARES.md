# APARTMENT SIM — ESTÁNDARES DE DESARROLLO
### Versión: 1.0 — Definido por El Arquitecto
### Motor: Ren'Py 8.5.3 | Python: 3.12
### Última actualización: 31/05/2026
### Fuentes: renpy.org/doc/html/ · python.html · dialogue.html · language_basics.html

---

## 0. VERSIÓN Y STACK — NO CAMBIAR

| Item | Versión | Notas |
|------|---------|-------|
| Motor | Ren'Py **8.5.3** | Descargar de renpy.org exactamente esta versión |
| Python | **3.12** | Incluido en Ren'Py desde v8.4. No instalar Python aparte |
| SDK | Ren'Py SDK | Proyecto en `D:\Proyectos\apartment-sim-renpy` |
| Arte | SD Forge local | `D:\Proyectos\stable-diffusion-forge` |
| Idioma código | **Español** | Comentarios, variables, labels — todo en español |
| Idioma interfaz | Español v1.0, Inglés v1.1 | |

---

## 1. NOMENCLATURA DE VARIABLES

### Regla general: snake_case, sin tildes, sin espacios

| Prefijo | Módulo | Ejemplos |
|---------|--------|---------|
| `stats_` | Stats de personajes | `stats_celine_afecto`, `stats_roxy_confianza` |
| `prot_` | Stats del protagonista | `prot_nombre`, `prot_energia_actual` |
| `pers_` | Personalidad del jugador | `pers_romantico`, `pers_atrevido` |
| `time_` | Sistema de tiempo | `time_dia`, `time_franja` |
| `mood_` | Estado de ánimo | `mood_celine`, `mood_luna` |
| `apt_` | Estado del apartamento | `apt_armonia` |
| `celos_` | Sistema de celos | `celos_roxy_activo`, `celos_celine_intensidad` |
| `acceso_` | Acceso a cuartos | `acceso_cuarto_celine` |
| `ev_` | Flags de eventos/actos | `ev_celine_acto1_done` |
| `quest_` | Flags de quests | `quest_roxy_2_done` |
| `sec_` | Secretos descubiertos | `sec_luna_1` |
| `item_` | Inventario del jugador | `item_camara` |
| `mem_` | Memoria de decisiones | `mem_decisiones` |
| `ui_` | Variables de UI temporales | `ui_menu_abierto` |
| `tmp_` | Variables temporales de label | `tmp_resultado_dado` |
| `persistent.galeria_` | Galería persistente | `persistent.galeria_escenas` |
| `DEBUG_` | Flags de desarrollo | `DEBUG_MODE` |

### Reglas adicionales:
- Nombres de personajes en variables: siempre en minúscula (`celine`, `roxy`, `luna`)
- Booleanos de completado: siempre terminan en `_done` o `_activo`
- Contadores numéricos: pueden terminar en `_total`, `_actual`, `_max`
- Sin abreviaturas ambiguas: `confianza` nunca `conf`, `afecto` nunca `af`

---

## 2. NOMENCLATURA DE LABELS

### Formato general: `modulo_accion_contexto`

| Patrón | Ejemplo | Uso |
|--------|---------|-----|
| `ev_personaje_actoN` | `ev_celine_acto1` | Escena principal de acto |
| `ev_personaje_actoN_fin` | `ev_celine_acto1_fin` | Cierre de un acto |
| `ev_personaje_actoN_alt` | `ev_celine_acto1_alt` | Rama alternativa de acto |
| `quest_personaje_N` | `quest_roxy_1` | Inicio de quest |
| `quest_personaje_N_entrega` | `quest_luna_2_entrega` | Entrega/resolución de quest |
| `dial_personaje_contexto` | `dial_celine_cocina_manana` | Diálogo cotidiano situacional |
| `dial_personaje_mood` | `dial_roxy_feliz` | Diálogo según estado de ánimo |
| `ev_grupal_N` | `ev_grupal_cena_1` | Evento con múltiples personajes |
| `ev_random_N` | `ev_random_lluvia` | Evento aleatorio |
| `sec_personaje_N` | `sec_celine_1` | Descubrimiento de secreto |
| `mini_juego_nombre` | `mini_strip21` | Mini-juego |
| `map_salon` | `map_salon` | Hub de mapa, sala principal |
| `map_cocina` | `map_cocina` | Hub de mapa, cocina |
| `start` | `start` | Label obligatorio de inicio (Ren'Py lo requiere) |
| `after_load` | `after_load` | Hook de Ren'Py post-carga de save |
| `splashscreen` | `splashscreen` | Pantalla splash (hook de Ren'Py) |

### Reglas adicionales:
- Todo en minúscula
- Palabras separadas por `_`
- Sin tildes ni caracteres especiales en los nombres de labels
- Los números van sin cero a la izquierda: `acto1` no `acto01` (a menos que sean más de 9)

---

## 3. NOMENCLATURA DE SCREENS

### Formato: `scr_nombre`

| Screen | Uso |
|--------|-----|
| `scr_hud` | HUD principal (stats, tiempo, energía) |
| `scr_mapa` | Mapa del apartamento para navegar |
| `scr_stats` | Pantalla detalle de stats de personajes |
| `scr_inventario` | Items del jugador |
| `scr_galeria` | Galería de CG desbloqueados |
| `scr_telefono` | Interfaz del teléfono del protagonista |
| `scr_confirmacion` | Popup genérico de confirmación |
| `scr_notificacion` | Toast/notificación temporal en pantalla |
| `scr_titulo` | Pantalla de título principal |
| `scr_creditos` | Pantalla de créditos |
| `scr_config` | Configuración del juego |

### Reglas adicionales:
- Todo en minúscula con `scr_` obligatorio
- Un archivo por screen compleja (`hud.rpy`, `map.rpy`)
- Screens simples pueden agruparse en un solo archivo

---

## 4. NOMENCLATURA DE FUNCIONES PYTHON

### Formato: `fn_modulo_accion`

| Función | Módulo | Descripción |
|---------|--------|-------------|
| `fn_stats_modificar(personaje, stat, delta)` | stats.rpy | Modifica un stat con límites 0–100 |
| `fn_stats_verificar_acceso(personaje)` | stats.rpy | Verifica y desbloquea acceso a cuarto si aplica |
| `fn_tiempo_avanzar_franja()` | time.rpy | Avanza la franja horaria y aplica consecuencias |
| `fn_tiempo_es_disponible(personaje, franja)` | time.rpy | Verifica si personaje está disponible en franja |
| `fn_mood_calcular(personaje)` | mood.rpy | Recalcula el mood según stats actuales |
| `fn_celos_evaluar()` | jealousy.rpy | Evalúa y actualiza celos de todos |
| `fn_economia_pagar(monto)` | economy.rpy | Deduce dinero, retorna True si hay saldo |
| `fn_galeria_desbloquear(id_escena)` | gallery.rpy | Agrega escena a galería persistente |
| `fn_mem_agregar(decision)` | script.rpy | Agrega decisión a mem_decisiones (patrón correcto) |
| `fn_debug_log(mensaje)` | stats.rpy | Solo imprime si DEBUG_MODE es True |

### Reglas adicionales:
- Todas las funciones se definen en `init python:` o `init 1 python:` blocks
- Retornan valores cuando es necesario — nunca efectos secundarios silenciosos
- Parámetros en snake_case
- Todo comentado en español explicando qué hace, qué recibe y qué devuelve

---

## 5. NOMENCLATURA DE PERSONAJES EN CÓDIGO

### Definición oficial (verificado en renpy.org/doc/html/dialogue.html):
```renpy
# En characters.rpy — usar define (son constantes, no se guardan)
define cel = Character("Celine", color="#E8A0BF")
define rox = Character("Roxy",   color="#FF6B6B")
define lun = Character("Luna",   color="#A8D8EA")
define nar = Character(None)          # Narrador — sin nombre visible
define pro = Character("[prot_nombre]", color="#FFFFFF")  # Protagonista con nombre dinámico
```

### Alias en código:
| Alias | Personaje | Color referencial |
|-------|-----------|------------------|
| `cel` | Celine (prima, académica) | `#E8A0BF` (rosa suave) |
| `rox` | Roxy (ex-algo, artista) | `#FF6B6B` (coral) |
| `lun` | Luna (observadora, misteriosa) | `#A8D8EA` (azul claro) |
| `nar` | Narrador (sin nombre) | sin color |
| `pro` | Protagonista (nombre dinámico) | `#FFFFFF` |

**Nota sobre pro:** El `[prot_nombre]` en el string se interpola automáticamente por Ren'Py
usando el valor de la variable del store. Esto es comportamiento oficial documentado.

**NUNCA usar:**
- Nombres completos como variable: `celine "texto"` ← incorrecto
- `not Character()`: el alias siempre apunta a un `Character()` correcto

---

## 6. ESTRUCTURA DE ARCHIVOS .RPY

### Encabezado obligatorio en cada archivo:
```renpy
##############################################################################
# APARTMENT SIM — [NOMBRE DEL MÓDULO]
# Archivo: [nombre_archivo.rpy]
# Módulo: [qué sistema maneja]
# Versión: 1.0
# Última modificación: [fecha]
# Dependencias: [lista de archivos que este necesita]
# Descripción:
#   [Qué hace este archivo en 2-3 líneas]
##############################################################################
```

### Orden de bloques dentro de cada .rpy:
```
1. Encabezado (comentario)
2. init python: — funciones del módulo
3. default [variables] — declaración de variables (si el módulo es responsable)
4. define [constantes] — constantes del módulo (si aplica)
5. screen scr_nombre: — screens del módulo (si aplica)
6. label nombre_label: — labels del módulo
```

### Archivos y sus responsabilidades:

| Archivo | Contiene | Estado |
|---------|---------|--------|
| `characters.rpy` | Solo defines de Character() | Fase 1 |
| `stats.rpy` | Variables de stats + fn_stats_* | Fase 1 |
| `time.rpy` | Variables de tiempo + fn_tiempo_* | Fase 1 |
| `mood.rpy` | Variables de mood + fn_mood_* | Fase 2 |
| `economy.rpy` | Variables económicas + fn_economia_* | Fase 2 |
| `jealousy.rpy` | Variables de celos + fn_celos_* | Fase 4 |
| `secrets.rpy` | Flags de secretos | Fase 4 |
| `hud.rpy` | scr_hud + scr_notificacion | Fase 1 |
| `map.rpy` | scr_mapa + labels map_* | Fase 1 |
| `phone.rpy` | scr_telefono | Fase 2 |
| `gallery.rpy` | persistent.galeria_* + scr_galeria | Fase 5 |
| `script.rpy` | label start, setup inicial, mem_decisiones | Fase 1 |
| `celine_events.rpy` | Todos los labels ev_celine_* y quest_celine_* | Fase 3 |
| `roxy_events.rpy` | Todos los labels ev_roxy_* y quest_roxy_* | Fase 3 |
| `luna_events.rpy` | Todos los labels ev_luna_* y quest_luna_* | Fase 3 |
| `random_events.rpy` | Labels ev_random_* | Fase 3 |
| `seasonal_events.rpy` | Eventos estacionales | Fase 3 |
| `group_events.rpy` | Labels ev_grupal_* | Fase 5 |
| `minigames.rpy` | Mini-juegos | Fase 6 |
| `options.rpy` | Config del proyecto (generado por SDK, editar) | Fase 1 |
| `gui.rpy` | Estilos de GUI (generado por SDK, editar) | Fase 1 |

---

## 7. REGLAS DE COMENTARIOS

### Todo en español. Sin excepción.

```renpy
##############################################################################
# Encabezado de sección — doble línea de hashes
##############################################################################

# -- Subsección menor -- solo un hash y guiones

# Comentario de una línea: explica el QUÉ y el POR QUÉ, no el cómo obvio

# MAL: $ stats_celine_afecto += 5  # suma 5 a afecto
# BIEN: $ fn_stats_modificar("celine", "afecto", 5)  # Celine reacciona bien al regalo

# Comentario antes de bloque de choices: explica qué impacto tienen las opciones
# menu:
#     # Opción romántica — suma pers_romantico
#     "...":

# Comentario de TODO pendiente:
# TODO: implementar animación de transición aquí (Fase 7)

# Comentario de advertencia:
# ADVERTENCIA: no usar .append() en listas — ver VARIABLES_GLOBALES.md sección 12
```

---

## 8. REGLAS DE ESTILO DE CÓDIGO

### Variables:
```renpy
# Siempre usar fn_ para modificar stats — nunca modificar directamente desde eventos
# MAL:
$ stats_celine_afecto += 10

# BIEN:
$ fn_stats_modificar("celine", "afecto", 10)
```

### Condicionales:
```renpy
# Comentar el propósito de cada condicional complejo
if stats_celine_afecto >= 50 and ev_celine_acto2_done:
    # Celine está lista para el acto 3 — mostrar opción especial
    jump ev_celine_acto3
```

### Choices (menús de decisión):
```renpy
# Cada choice que afecta personalidad debe comentar qué arquetipo suma
menu:
    # Opción romántica
    "Te sonrío suavemente.":
        $ fn_stats_modificar("celine", "afecto", 3)
        $ pers_romantico += 1
        jump dial_celine_respuesta_romantica

    # Opción atrevida
    "Le guiño un ojo.":
        $ fn_stats_modificar("celine", "afecto", 1)
        $ fn_stats_modificar("celine", "confianza", -1)
        $ pers_atrevido += 1
        jump dial_celine_respuesta_atrevida
```

### Avance de tiempo:
```renpy
# Siempre avanzar tiempo a través de la función, nunca modificar time_franja directo
$ fn_tiempo_avanzar_franja()
```

---

## 9. REGLAS DE IMÁGENES Y ASSETS

### Nombres de sprites:
```
[personaje]_[outfit]_[emocion]_[variante]
Ejemplos:
  celine_outfit1_normal
  celine_outfit1_feliz
  roxy_outfit2_traviesa
  luna_outfit1_cansada_alt
```

### Nombres de fondos:
```
bg_[ubicacion]_[momento]
Ejemplos:
  bg_salon_dia
  bg_salon_noche
  bg_cocina_manana
  bg_cuarto_celine_tarde
```

### Nombres de CG (escenas de galería):
```
cg_[personaje]_[acto]_[numero]
Ejemplos:
  cg_celine_acto3_01
  cg_grupal_verano_01
```

### Carpetas de assets:
```
game/
├── images/
│   ├── sprites/
│   │   ├── celine/
│   │   ├── roxy/
│   │   └── luna/
│   ├── backgrounds/
│   └── cg/
├── audio/
│   ├── music/
│   └── sfx/
└── fonts/
```

---

## 10. REGLAS DE SAVES Y ROLLBACK

### Lo que SIEMPRE se guarda (usar para gameplay):
- Variables declaradas con `default`
- Objetos alcanzables desde variables `default`

### Lo que NUNCA se guarda (solo para constantes):
- Variables declaradas con `define`
- Variables asignadas en `init python:` blocks

### Lo que se guarda entre partidas (persistente):
- Todo lo accesible desde el objeto `persistent`

### Patrón obligatorio para listas en saves:
```renpy
# NUNCA (no activa el guardado):
$ mem_decisiones.append("elegí ayudar a Celine")

# SIEMPRE (reasignar la variable activa el guardado):
$ mem_decisiones = mem_decisiones + ["elegí ayudar a Celine"]

# Lo mismo para persistent:
$ persistent.galeria_escenas = persistent.galeria_escenas + ["cg_celine_acto1_01"]
```

---

## 11. REGLAS DE CONSISTENCIA NARRATIVA

*(Para que Dev Narrativa no rompa la lógica del juego)*

- Celine es **prima** del protagonista — relación cercana pero con barreras
- Roxy es **ex-algo** — hay tensión no resuelta, historia compartida
- Luna es **la observadora** — conoce más de lo que dice, relación más lenta
- Los tres personajes **se conocen entre sí desde niños**
- El protagonista llegó recientemente al apartamento
- La ciudad es **Vallanova** — universitaria, mediana, costera, ficticia
- Sin Game Over: Confianza 0 = hostilidad permanente pero recuperable
- Acceso a cuartos: una vez desbloqueado, **NUNCA se bloquea de nuevo**

---

## 12. REGLAS PARA EL HUD

- El HUD se muestra en todas las pantallas de gameplay excepto durante escenas de acto
- Durante escenas de acto (label `ev_*`): ocultar HUD con `hide screen scr_hud`
- Al volver al mapa: mostrar HUD con `show screen scr_hud`
- El HUD siempre refleja los valores actuales (usa las variables directamente, no copies)

---

## CHECKLIST ANTES DE HACER PUSH A GITHUB

- [ ] ¿Todas las variables nuevas están en VARIABLES_GLOBALES.md?
- [ ] ¿Las variables de gameplay usan `default`?
- [ ] ¿Las constantes usan `define`?
- [ ] ¿Las listas se reasignan en lugar de `.append()`?
- [ ] ¿Los labels siguen el patrón de nomenclatura?
- [ ] ¿Los comentarios están en español?
- [ ] ¿Se usó `fn_stats_modificar()` en lugar de modificar stats directamente?
- [ ] ¿El encabezado del .rpy está completo?
- [ ] ¿ESTADO_ACTUAL.md fue actualizado?


---

## 13. NOMBRES RESERVADOS — LO QUE NUNCA SE PUEDE USAR
*(Fuente: renpy.org/doc/html/reserved.html — leído directamente)*

### 13.1 Nombres de ARCHIVOS prohibidos
```
❌ Cualquier archivo que empiece con "00"  → reservado para Ren'Py interno
❌ Cualquier archivo que empiece con "_"   → reservado para Ren'Py interno
❌ Archivos que no empiecen con letra o número

✅ Nuestros archivos: stats.rpy, time.rpy, hud.rpy, map.rpy, script.rpy, etc.
   Todos empiezan con letra — CORRECTO
```

### 13.2 Nombres de VARIABLES prohibidos
```
❌ Cualquier nombre que empiece con _ (un guión bajo)
   → Ren'Py los reserva para uso interno
   → Rompería el juego en versiones futuras

❌ Nombres de Python built-ins — causan bugs oscuros y silenciosos:
   list, dict, set, tuple, str, int, float, bool, type, object, input,
   print, range, map, filter, sorted, zip, sum, min, max, id, len,
   format, hash, open, exit, quit, help, vars, dir, globals, locals,
   compile, eval, exec, repr, iter, next, any, all, abs, round...
   (lista completa en reserved.html — son ~80 nombres)

❌ Nombres de Python exceptions:
   Exception, Error, TypeError, ValueError, KeyError, IndexError,
   AttributeError, RuntimeError, NameError, ImportError,
   FileNotFoundError, True, False, None...

❌ Nombres de typing module que Ren'Py importa en todos los stores:
   Any, Callable, Literal, Self, cast, final, overload, override

❌ Nombres propios de Ren'Py — causan conflicto silencioso:
   renpy, config, persistent, style, gui, store, ui, audio, anim,
   narrator, menu, say, dissolve, fade, move, left, right, center,
   topleft, topright, truecenter, reset, color, default, define,
   Character, Image, Text, Transform, Gallery, Show, Hide, Jump,
   Call, Return, Function, Preference, FileSave, FileLoad...
   (lista completa de ~200 nombres en reserved.html)

❌ Keywords del lenguaje Ren'Py (no se pueden usar en NINGÚN contexto):
   at, call, elif, else, expression, hide, if, image, init,
   jump, label, menu, onlayer, pass, python, return, scene,
   set, show, with, while

⚠ NOMBRES PELIGROSOS EN NUESTRO PROYECTO — verificar:
   "set"   → keyword de Ren'Py y built-in de Python ← NUNCA usar como variable
   "list"  → built-in Python ← NUNCA usar como variable
   "input" → built-in Python (tenemos prot_nombre con renpy.input()) ← OK porque no la guardamos como variable
   "color" → reservado Ren'Py ← NUNCA usar como variable o screen
   "map"   → built-in Python ← CUIDADO: nuestro archivo se llama map.rpy pero las VARIABLES dentro deben ser map_salon, no "map"
```

### 13.3 Nombres de LABELS prohibidos o especiales
```
LABELS ESPECIALES (Ren'Py los intercepta automáticamente — solo usar si es intencional):
  start          → punto de inicio del juego — OBLIGATORIO que exista en script.rpy
  splashscreen   → se ejecuta UNA VEZ antes del menú principal al arrancar
  main_menu      → reemplaza el menú principal completo si existe
  before_main_menu → se ejecuta antes de mostrar el menú principal
  after_load     → se ejecuta cada vez que el jugador carga un save
  before_load    → se ejecuta justo ANTES de cargar (contexto nuevo, cambios se pierden)
  quit           → se ejecuta cuando el jugador cierra el juego

REGLA: Si creas un label que se llame igual que uno de estos, Ren'Py lo va a ejecutar
       automáticamente aunque no lo llames tú. Esto puede romper el juego silenciosamente.

NUESTRO USO DE LABELS ESPECIALES:
  start          → en script.rpy — contiene setup inicial
  after_load     → en script.rpy — migraciones de datos entre versiones
  splashscreen   → en script.rpy — pantalla de carga/intro (Fase 7)
  Los demás: NO usar por ahora
```

### 13.4 Nombres de SCREENS prohibidos o especiales
```
SCREENS ESPECIALES (Ren'Py los llama automáticamente — solo usar si es intencional):
  main_menu      → pantalla del menú principal
  game_menu      → wrapper del menú de juego
  save           → pantalla de guardado
  load           → pantalla de carga
  preferences    → pantalla de preferencias
  confirm        → popup de confirmación genérico
  notify         → notificación temporal
  skip_indicator → indicador de modo skip
  nvl            → para modo NVL
  choice         → reemplaza los menús de choices del juego

NUESTROS SCREENS usan prefijo scr_ por diseño → NUNCA colisionan con estos:
  scr_hud, scr_mapa, scr_stats, scr_galeria, etc. → SEGUROS
```

---

## 14. QUÉ NO SE PUEDE GUARDAR EN SAVES (PicklingError)
*(Fuente: renpy.org/doc/html/save_load_rollback.html — verificado)*

Si alguno de estos tipos termina en el store (accesible desde variables `default`),
el juego lanza `PicklingError` al intentar guardar y el jugador pierde su partida.

```
❌ NO GUARDAR NUNCA:
   - Archivos abiertos (open(), renpy.open_file()) ← error real documentado
   - Sockets de red
   - Iteradores (resultado de iter(), zip(), map(), filter(), range() no asignado)
   - Generadores (funciones con yield)
   - Coroutines / async functions / await / futures
   - Lambda functions almacenadas en variables del store
   - Funciones internas (inner functions, closures)
   - Objetos Render de Ren'Py

✅ SÍ SE PUEDE GUARDAR (pickle-safe):
   - bool, int, float, str, None
   - list, tuple, dict, set (siempre que su CONTENIDO también sea pickle-safe)
   - Clases definidas en init python: con nombre fijo que no cambie entre versiones
   - Character, Displayable, Transform (pero ya están en define, no en default)

REGLA PRÁCTICA para Apartment Sim:
Solo guardamos tipos básicos: int, str, bool, list de strings, list de bools.
Eso es todo lo que necesitamos. Sin clases, sin objetos complejos, sin archivos.
```

---

## 15. REGLAS DE INIT PRIORITY
*(Fuente: renpy.org/doc/html/lifecycle.html — verificado)*

```
Rango reservado Ren'Py:  por debajo de -999 y por encima de 999 → NO tocar
Rango para librerías:    -999 a -100
Rango para nosotros:     -99 a 99  (recomendación oficial)
Default si no se pone:   0

NUESTRO PROYECTO:
  init 0 python:   → funciones de módulos (fn_stats_*, fn_tiempo_*, etc.)
  init -1 python:  → si una función depende de otra ya definida (raro, evitar)
  Sin número:      → equivale a init 0, usar para define y default normales

REGLA: Los defaults se procesan DESPUÉS de todos los init blocks.
Esto significa que las variables default están disponibles desde el inicio del juego,
pero las funciones definidas en init python: se ejecutan ANTES.
```

---

## 16. EL PROBLEMA DEL .RPYC FANTASMA
*(Fuente: renpy.org/doc/html/language_basics.html — verificado)*

```
Ren'Py compila .rpy → .rpyc al iniciar.
Si eliminas o renombras un .rpy SIN eliminar su .rpyc:
  → El .rpyc SIGUE siendo ejecutado
  → El código del archivo eliminado sigue corriendo
  → Puede causar labels duplicados, variables duplicadas, bugs imposibles de rastrear

REGLA OBLIGATORIA:
Cuando renombres o elimines un .rpy → TAMBIÉN elimina el .rpyc correspondiente.
El .rpyc está en la misma carpeta que el .rpy.

CHECKLIST AÑADIDO: antes de cada sesión de trabajo, verificar que no haya .rpyc huérfanos.
```

---

## 17. VARIABLES DINÁMICAS CON renpy.dynamic()
*(Para saber cuándo usarlo)*

```renpy
# renpy.dynamic() crea variables locales al contexto actual.
# Se usan para variables temporales dentro de labels complejos
# que NO deben guardarse ni afectar al estado global.

# Ejemplo de uso correcto en nuestro proyecto:
label ev_celine_acto1:
    $ renpy.dynamic("tmp_resultado")  # variable solo vive en este label
    $ tmp_resultado = "positivo"
    # ...
    return
    # Al hacer return, tmp_resultado desaparece

# NO usar para stats ni flags de progreso — esos siempre son default globales
```

---

## 18. AFTER_LOAD — MIGRACIÓN DE DATOS ENTRE VERSIONES

```renpy
# Si en una actualización del juego CAMBIAS el nombre de una variable
# o AÑADES una variable que los saves antiguos no tienen,
# el jugador con save antiguo puede tener crash o comportamiento raro.
#
# SOLUCIÓN: usar label after_load para migrar datos.
# Ren'Py re-ejecuta default statements al cargar, pero solo si la variable
# genuinamente no existe en el save. Si existe con valor antiguo, lo respeta.

label after_load:
    # Ejemplo: en v1.1 renombramos stats_celine_amor → stats_celine_afecto
    # Un jugador con save de v1.0 tiene stats_celine_amor pero no stats_celine_afecto
    python:
        # Verificar si existe el nombre viejo y migrar
        if hasattr(store, "stats_celine_amor"):
            stats_celine_afecto = store.stats_celine_amor
            del store.stats_celine_amor
        renpy.block_rollback()  # OBLIGATORIO si cambias datos aquí
    return

# REGLA: cada vez que cambies el nombre de una variable en VARIABLES_GLOBALES.md,
# añadir la migración correspondiente en after_load.
# Documentar la migración en ESTADO_ACTUAL.md con la versión.
```
