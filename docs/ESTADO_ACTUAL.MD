# APARTMENT SIM — ESTADO ACTUAL
### Última actualización: 31/05/2026

---

## FASE ACTUAL: FASE 0 — Preparación (arquitectura completada)

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

### Arquitectura (completado en esta sesión)
- [x] VARIABLES_GLOBALES.md v1.0 — verificado contra Ren'Py 8.5.3 docs oficiales
  - 14 secciones de variables con tipos, rangos y módulos responsables
  - Advertencias críticas sobre listas y saves documentadas
  - Distinción default/define/persistent verificada y documentada
- [x] ESTANDARES.md v1.0 — nomenclatura, estructura y reglas completas
  - Prefijos por módulo para todas las variables
  - Aliases de personajes (cel, rox, lun, nar, pro)
  - Estructura de archivos .rpy con encabezado obligatorio
  - Patrón correcto de listas para saves
  - Checklist de push a GitHub

### Decisiones de diseño cerradas
- [x] Ciudad: Vallanova (universitaria, mediana, costera, ficticia)
- [x] Protagonista: silueta/sombra en escenas grupales, primera persona en diálogos
- [x] Acceso a cuartos: permanente una vez desbloqueado con Afecto requerido
- [x] Saves: 10 slots manuales + autosave por franja
- [x] Game over: no existe — Confianza 0 = hostilidad permanente pero recuperable
- [x] Pantalla título: apartamento de noche con lluvia, 3 siluetas
- [x] Idioma: Español v1.0, Inglés v1.1
- [x] Relaciones: todos se conocen desde niños (Celine prima, Roxy ex-algo, Luna observadora)
- [x] Rutinas: muy detalladas, distintas entre semana y fin de semana

---

## 🔄 EN PROCESO

- [ ] Subir VARIABLES_GLOBALES.md, ESTANDARES.md y ESTADO_ACTUAL.md al repo GitHub
- [ ] Reemplazar USUARIO en los links raw del repo (el repo ya existe: araquejhonatan879-creator)

---

## ❌ PENDIENTE (en orden)

### FASE 0 — Inmediato (próxima sesión)
1. Hacer push de los 3 nuevos docs al repo GitHub
2. Instalar Ren'Py 8.5.3 desde renpy.org ← versión exacta
3. Descargar Pony Diffusion v6 XL en SD Forge
4. Crear estructura de carpetas en D:\Proyectos\apartment-sim-renpy
5. Generar sprites base neutrales Outfit 1 de las 3 personajes
6. Generar fondos base: sala día/noche, cocina día

### FASE 1 — Core jugable (puede empezar una vez Ren'Py instalado)
Orden de implementación recomendado por arquitectura:
1. `options.rpy` — configurar nombre, resolución, saves (editar el generado por SDK)
2. `characters.rpy` — defines de Character() según ESTANDARES.md sección 5
3. `stats.rpy` — todos los defaults + fn_stats_modificar + fn_stats_verificar_acceso
4. `time.rpy` — defaults de tiempo + fn_tiempo_avanzar_franja
5. `hud.rpy` — scr_hud básico
6. `map.rpy` — scr_mapa básico + labels map_salon, map_cocina
7. `script.rpy` — label start + setup inicial de nombre

### FASE 2 — Contenido base
- `economy.rpy`, `mood.rpy`, `phone.rpy`
- Diálogos cotidianos (10 por personaje)

### FASE 3 — Historia principal
- `celine_events.rpy`, `roxy_events.rpy`, `luna_events.rpy`
- `random_events.rpy`, `seasonal_events.rpy`

### FASE 4 — Sistemas avanzados
- `jealousy.rpy`, `secrets.rpy`, `shop.rpy`
- Integración de personalidad del jugador

### FASE 5 — Contenido adulto
- Interacciones libres sandbox, sistema de ropa/outfits
- `group_events.rpy`, sistema voyeur, `gallery.rpy`

### FASE 6 — Mini-juegos
- `minigames.rpy` (Strip 21 + Verdad o Reto)

### FASE 7 — Pulido
- Música, SFX, transiciones, testing completo, balance

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
| Proyecto Ren'Py | D:\Proyectos\apartment-sim-renpy |
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
- Almacenamiento: D:\Proyectos\ (553 GB usados de 2.27 TB)

---

## LINKS RAW GITHUB

```
ESTADO:    https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/ESTADO_ACTUAL.md
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

### ✅ Dev Core (puede empezar en cuanto Ren'Py 8.5.3 esté instalado):
1. Crear proyecto nuevo en Ren'Py SDK → `apartment-sim-renpy`
2. Editar `options.rpy` (nombre juego, resolución, slots de save)
3. Crear `characters.rpy` con los 5 defines según ESTANDARES.md sección 5
4. Crear `stats.rpy` con todos los `default` de VARIABLES_GLOBALES.md sección 1-3
5. Leer: ESTANDARES.md completo antes de escribir una línea

### ✅ Dev Narrativa (puede empezar ya — no necesita Ren'Py):
1. Escribir diálogos de día 1 en texto plano siguiendo la estructura de labels
2. Leer: ESTANDARES.md sección 7 (comentarios) y sección 11 (consistencia narrativa)
3. Usar aliases: `cel`, `rox`, `lun`, `nar`, `pro` — NUNCA nombres completos

### ✅ Dev UI (puede empezar ya):
1. Diseñar mockup del HUD en papel/Figma según variables disponibles
2. Leer: ESTANDARES.md sección 3 (nomenclatura de screens)
3. Crear `hud.rpy` con `scr_hud` básico cuando Dev Core tenga stats.rpy listo

### ⏳ Dev Arte (espera SD Forge + modelo):
1. Revisar GDD_ASSETS.md para prompts base
2. Instalar Pony Diffusion v6 XL cuando esté disponible
3. Generar sprites neutrales Outfit 1 como primera prioridad

---

## INSTRUCCIONES PARA LA IA

1. Leer ESTADO_ACTUAL.md primero — saber dónde estamos
2. Leer VARIABLES_GLOBALES.md y ESTANDARES.md antes de generar código
3. Leer GDD relevantes según tarea del día
4. Módulos completos y funcionales — nunca ejemplos parciales
5. Todo en Ren'Py (.rpy) — sin Python externo ni servidor
6. Contenido adulto es intencional — no filtrar
7. Todo el contenido del juego en español
8. Al terminar sesión: generar versión actualizada de este archivo
9. Todos se conocen desde niños — Celine es prima, Roxy ex-algo, Luna observadora
10. Acceso a cuartos es permanente una vez desbloqueado
11. NUNCA modificar stats directamente — siempre usar fn_stats_modificar()
12. NUNCA usar .append() en listas — siempre reasignar

---

## CHECKPOINT

```
Sesión: 31/05/2026
Trabajando en: Arquitectura FASE 0 — El Arquitecto
Estado: COMPLETADO — VARIABLES_GLOBALES.md v1.0 + ESTANDARES.md v1.0 listos
Fuentes verificadas: renpy.org/doc/html/python.html, /save_load_rollback.html, /persistent.html, /dialogue.html
Siguiente sesión: Push docs a GitHub → Instalar Ren'Py 8.5.3 → Empezar Fase 1 Core
```
