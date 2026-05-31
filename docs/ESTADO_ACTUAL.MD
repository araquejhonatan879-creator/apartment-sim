# APARTMENT SIM — ESTADO ACTUAL
### Última actualización: 31/05/2026

---

## FASE ACTUAL: FASE 1 — Core jugable (en progreso)

---

## ✅ COMPLETADO

### Diseño y documentación
- [x] GDD_CORE.md v2.1 — visión, stack, saves, game over, pantalla título, idiomas
- [x] GDD_PERSONAJES.md — protagonista + 3 personajes con rutinas detalladas
- [x] GDD_SISTEMAS.md — 21 sistemas detallados con números y mecánicas
- [x] GDD_NARRATIVA.md — día 1 + 5 actos por personaje completos + eventos grupales
- [x] GDD_ASSETS.md — sprites, fondos, prompts SD, audio
- [x] protagonist.json — silueta/sombra, nombre elegible, stats iniciales
- [x] celine.json v2 — rutinas detalladas semana/fin de semana
- [x] roxy.json v2 — rutinas detalladas semana/fin de semana
- [x] luna.json v2 — rutinas detalladas semana/fin de semana

### Arquitectura
- [x] VARIABLES_GLOBALES.md v1.0 — verificado contra Ren'Py 8.5.3 docs oficiales
- [x] ESTANDARES.md v1.0 — nomenclatura, estructura y reglas completas

### Repositorio y entorno
- [x] Repo GitHub: araquejhonatan879-creator/apartment-sim (público)
- [x] VS Code conectado al repo con Git inicializado
- [x] Carpeta del proyecto: C:\Proyectos\apartmentsimrenpy\
- [x] Estructura de carpetas creada: game/systems/ y game/characters/

### Dev Core — Fase 1 (COMPLETADO EN SESIÓN 31/05/2026)
- [x] `game/script.rpy` v1.0
  - define nar, define pro (con [prot_nombre] interpolado)
  - default mem_decisiones
  - label start — setup nombre protagonista con renpy.input()
  - label start_dia1 — placeholder para Dev Narrativa
  - label map_salon — placeholder temporal hasta que Dev UI cree map.rpy
  - label after_load — migraciones + validación de mem_decisiones
  - Funciones: fn_mem_agregar(), fn_mem_tiene()
- [x] `game/systems/stats.rpy` v1.0
  - Variables: stats de 3 personajes, stats protagonista, personalidad, acceso cuartos
  - Funciones: fn_stats_modificar(), fn_stats_verificar_acceso(), fn_debug_log()
  - Define: DEBUG_MODE
- [x] `game/systems/time.rpy` v1.0
  - Variables: time_dia, time_franja, time_dia_semana, time_es_finde, time_total_franjas
  - Funciones: fn_tiempo_avanzar_franja(), fn_tiempo_calcular_dia_semana(),
    fn_tiempo_es_disponible(), fn_tiempo_es_disponible_finde(),
    fn_tiempo_obtener_label_franja()
- [x] `game/systems/mood.rpy` v1.0
  - Variables: mood_celine, mood_roxy, mood_luna
  - Funciones: fn_mood_calcular(), fn_mood_calcular_todos(), fn_mood_obtener_sprite()
- [x] `game/systems/jealousy.rpy` v1.0
  - Variables: apt_armonia, celos_*_activo, celos_*_intensidad (7 variables)
  - Funciones: fn_celos_evaluar(), fn_celos_aplicar_impacto_armonia(),
    fn_celos_resetear_dia(), fn_celos_recuperar_armonia()
- [x] `game/systems/economy.rpy` v1.0
  - Variables: item_camara
  - Funciones: fn_economia_pagar(), fn_economia_cobrar(),
    fn_economia_tiene_saldo(), fn_economia_comprar_item(), fn_economia_dar_regalo()
- [x] `game/characters/celine.rpy` v1.0
  - define cel = Character("Celine", color="#E8A0BF")
  - 20 diálogos cotidianos (5 franjas × 4-5 moods)
  - label dial_celine_cotidiano (dispatcher automático)
- [x] `game/characters/roxy.rpy` v1.0
  - define rox = Character("Roxy", color="#FF6B6B")
  - 20 diálogos cotidianos
  - label dial_roxy_cotidiano (dispatcher automático)
- [x] `game/characters/luna.rpy` v1.0
  - define lun = Character("Luna", color="#A8D8EA")
  - 20 diálogos cotidianos
  - label dial_luna_cotidiano (dispatcher automático)

---

## 🔄 EN PROCESO

- [ ] Push a GitHub de los 7 archivos .rpy generados (pendiente confirmar)

---

## ❌ PENDIENTE (en orden)

### FASE 1 — Inmediato (próxima sesión)

**Dev UI** (puede empezar ahora que Core está listo):
- [ ] `game/hud.rpy` — scr_hud básico
  - Mostrar: time_franja (con tilde via fn_tiempo_obtener_label_franja()),
    time_dia, time_dia_semana, prot_energia_actual/prot_energia_max, prot_dinero
  - Indicadores de mood: mood_celine, mood_roxy, mood_luna
  - Indicador de armonía: apt_armonia
- [ ] `game/map.rpy` — scr_mapa básico + labels map_salon, map_cocina
  - map_salon: hub principal — opciones de interacción según disponibilidad
  - Usar fn_tiempo_es_disponible(personaje, time_franja) para mostrar/ocultar personajes
  - Llamar dial_*_cotidiano del personaje elegido
  - Botón avanzar tiempo → fn_tiempo_avanzar_franja() + fn_mood_calcular_todos()
    + fn_celos_evaluar() + fn_stats_verificar_acceso() para cada personaje

**Dev Narrativa** (puede empezar ahora):
- [ ] `game/script.rpy` — diálogos del día 1 (primera jornada completa)
  - Seguir GDD_NARRATIVA.md — llegada al apartamento, presentaciones
  - Usar aliases: cel, rox, lun, nar, pro — NUNCA nombres completos
  - Usar fn_stats_modificar() para cualquier cambio de stats

### FASE 2 — Una vez Fase 1 completa
- [ ] `game/systems/phone.rpy` — scr_telefono (mensajes de texto de personajes)
- [ ] Diálogos cotidianos adicionales (10 por personaje, situacionales)
- [ ] Sistema de trabajo del protagonista (fn_economia_cobrar desde events)

### FASE 3 — Historia principal
- [ ] `game/events/celine_events.rpy` — ev_celine_acto1 ... acto5
- [ ] `game/events/roxy_events.rpy`
- [ ] `game/events/luna_events.rpy`
- [ ] `game/events/random_events.rpy`

### FASE 4 — Sistemas avanzados
- [ ] Expandir catálogo tienda en economy.rpy (agregar ítems según GDD_SISTEMAS.md)
- [ ] `game/systems/secrets.rpy` — flags sec_* y mecánica de descubrimiento
- [ ] `game/systems/shop.rpy` — pantalla tienda completa

### FASE 5 — Contenido adulto
- [ ] Sistema de outfits — expandir fn_mood_obtener_sprite() a múltiples outfits
- [ ] `game/events/group_events.rpy` — ev_grupal_*
- [ ] `game/gallery.rpy` — persistent.galeria_escenas, persistent.galeria_fotos

### FASE 6 — Mini-juegos
- [ ] `game/minigames.rpy` — Strip 21 + Verdad o Reto

### FASE 7 — Pulido
- [ ] Música, SFX, transiciones
- [ ] Pantalla título: apartamento de noche con lluvia, 3 siluetas
- [ ] Testing completo + balance de stats

---

## DECISIONES TÉCNICAS — NO CAMBIAR

| Decisión | Detalle |
|----------|---------|
| Motor | Ren'Py **8.5.3** |
| Python | **3.12** (incluido en Ren'Py 8.4+) |
| Arte | Stable Diffusion Forge local |
| Modelo SD | Pony Diffusion v6 XL (pendiente descargar) |
| Idioma v1.0 | Español |
| Idioma v1.1 | Inglés (distribución) |
| Backend | Ninguno — todo local |
| Proyecto Ren'Py | C:\Proyectos\apartmentsimrenpy |
| SD Forge | D:\Proyectos\stable-diffusion-forge |
| Ciudad | Vallanova |
| Protagonista visual | Silueta en grupos, primera persona en diálogos |
| Acceso cuartos | Permanente una vez desbloqueado |

---

## HARDWARE

- CPU: AMD Ryzen 5 3600 (6 núcleos, 3.59 GHz)
- RAM: 16 GB
- GPU: NVIDIA GeForce GTX 1650 SUPER (4 GB VRAM)
- OS: Windows 10/11
- Almacenamiento: C:\Proyectos\ (repo local)

---

## ARQUITECTURA DE FUNCIONES — REFERENCIA RÁPIDA

### Cadena de llamadas al avanzar franja (map.rpy debe hacer esto):
```renpy
$ nuevo_dia = fn_tiempo_avanzar_franja()   # avanza tiempo + energía
$ fn_mood_calcular_todos()                  # recalcula moods
$ fn_celos_evaluar()                        # evalúa celos + impacto armonía
if nuevo_dia:
    $ fn_celos_resetear_dia()               # resetea celos al nuevo día
$ fn_stats_verificar_acceso("celine")       # verificar desbloqueo cuartos
$ fn_stats_verificar_acceso("roxy")
$ fn_stats_verificar_acceso("luna")
```

### Modificar stats desde eventos (ÚNICA forma correcta):
```renpy
$ fn_stats_modificar("celine", "afecto", 5)
$ fn_stats_modificar("roxy", "confianza", -2)
$ fn_stats_modificar("luna", "corrupcion", 3)
```

### Dar regalo a personaje:
```renpy
if fn_economia_dar_regalo("celine", "flores"):
    cel "Qué bonitas, gracias."
else:
    nar "No tienes suficiente dinero."
```

### Llamar diálogo cotidiano desde el mapa:
```renpy
call dial_celine_cotidiano   # detecta franja y mood automáticamente
call dial_roxy_cotidiano
call dial_luna_cotidiano
```

### Obtener sprite según mood:
```renpy
$ sprite_actual = fn_mood_obtener_sprite("celine")
show expression sprite_actual
```

---

## ESTRUCTURA DE ARCHIVOS ACTUAL

```
apartmentsimrenpy/
├── docs/                          ← documentación del proyecto
│   ├── ESTADO_ACTUAL.MD           ← este archivo
│   ├── VARIABLES_GLOBALES.md
│   ├── ESTANDARES.md
│   ├── GDD_CORE.md
│   ├── GDD_PERSONAJES.md
│   ├── GDD_SISTEMAS.md
│   ├── GDD_NARRATIVA.md
│   ├── GDD_ASSETS.md
│   ├── celine.json
│   ├── roxy.json
│   ├── luna.json
│   └── protagonist.json
├── game/
│   ├── systems/                   ← Dev Core
│   │   ├── stats.rpy              ✅ v1.0
│   │   ├── time.rpy               ✅ v1.0
│   │   ├── mood.rpy               ✅ v1.0
│   │   ├── jealousy.rpy           ✅ v1.0
│   │   └── economy.rpy            ✅ v1.0
│   ├── characters/                ← Dev Core
│   │   ├── celine.rpy             ✅ v1.0
│   │   ├── roxy.rpy               ✅ v1.0
│   │   └── luna.rpy               ✅ v1.0
│   ├── script.rpy                 ✅ v1.0
│   ├── hud.rpy                    ⏳ PENDIENTE — Dev UI
│   ├── map.rpy                    ⏳ PENDIENTE — Dev UI
│   ├── gui.rpy                    (generado por SDK)
│   └── options.rpy                (generado por SDK)
└── .gitignore
```

---

## LINKS RAW GITHUB

```
ESTADO:    https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/ESTADO_ACTUAL.MD
VARIABLES: https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/VARIABLES_GLOBALES.md
ESTANDARES:https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/ESTANDARES.md
GDD_CORE:  https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_CORE.md
PERSONAJES:https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_PERSONAJES.md
SISTEMAS:  https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_SISTEMAS.md
NARRATIVA: https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_NARRATIVA.md
ASSETS:    https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_ASSETS.md
CELINE:    https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/celine.json
ROXY:      https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/roxy.json
LUNA:      https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/luna.json
PROTAGONIST:https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/protagonist.json
```

---

## LO QUE PUEDE EMPEZAR CADA DEV AHORA

### ✅ Dev Core
Fase 1 al **100% completa**. Próxima tarea: Fase 2 (economy expand, phone.rpy) o apoyar Dev UI/Narrativa.

### ✅ Dev UI (puede empezar YA — Core listo)
1. Leer ESTANDARES.md sección 3 (screens) y sección 12 (HUD)
2. Leer este archivo sección "Cadena de llamadas al avanzar franja"
3. Crear `game/hud.rpy` con scr_hud — variables disponibles:
   - Tiempo: time_dia, time_franja, time_dia_semana, time_es_finde
   - Energía: prot_energia_actual, prot_energia_max
   - Dinero: prot_dinero
   - Moods: mood_celine, mood_roxy, mood_luna
   - Armonía: apt_armonia
   - Celos: celos_*_activo, celos_*_intensidad
4. Crear `game/map.rpy` — usar fn_tiempo_es_disponible() para presencia de personajes

### ✅ Dev Narrativa (puede empezar YA)
1. Leer ESTANDARES.md secciones 7, 8 y 11
2. Leer GDD_NARRATIVA.md — día 1 completo
3. Escribir diálogos del día 1 en `game/script.rpy`
4. Aliases obligatorios: cel, rox, lun, nar, pro
5. NUNCA modificar stats directamente — siempre fn_stats_modificar()
6. NUNCA usar .append() en listas — siempre reasignar

### ⏳ Dev Arte (espera SD Forge + modelo)
1. Revisar GDD_ASSETS.md para prompts base
2. Nombres de sprites según ESTANDARES.md sección 9:
   formato: [personaje]_outfit1_[mood]
   ej: celine_outfit1_normal, roxy_outfit1_feliz, luna_outfit1_traviesa
3. Moods disponibles: normal, feliz, cansada, estresada, traviesa

---

## CHECKPOINT

```
Sesión: 31/05/2026
Trabajando en: Dev Core — Fase 1
Estado: COMPLETADO — 8 archivos .rpy generados y listos para push
Archivos: stats.rpy, time.rpy, mood.rpy, jealousy.rpy, economy.rpy,
          celine.rpy, roxy.rpy, luna.rpy, script.rpy
Siguiente sesión Dev Core: NO HAY — Fase 1 Core 100% completa
Siguiente sesión Dev UI: hud.rpy + map.rpy (Core ya está listo)
```