# APARTMENT SIM — ESTADO ACTUAL
### Última actualización: 30/05/2026 — Sesión 4

---

## FASE ACTUAL: FASE 2 — Contenido base (EN PROCESO)

---

## ✅ COMPLETADO

### Diseño y documentación
- [x] GDD_CORE.md v2.1
- [x] GDD_PERSONAJES.md
- [x] GDD_SISTEMAS.md
- [x] GDD_NARRATIVA.md
- [x] GDD_ASSETS.md
- [x] protagonist.json
- [x] celine.json v2
- [x] roxy.json v2
- [x] luna.json v2

### Entorno de desarrollo — FASE 0 COMPLETA
- [x] Ren'Py 8.5.3 instalado en C:\Proyectos\renpy-8.5.3-sdk\
- [x] Proyecto Ren'Py creado en C:\Proyectos\apartmentsimrenpy\
- [x] Estructura de carpetas completa (characters, screens, systems, events, images, audio)
- [x] VS Code + extensión Ren'Py Language (Official)
- [x] Git conectado al repo apartment-sim en GitHub
- [x] Primer commit subido (88 archivos, estructura base Ren'Py)
- [x] Pony Diffusion v6 XL en descarga (6.46 GB desde Civitai)
- [x] VAE SDXL en descarga (319 MB desde Civitai)

### Decisiones de diseño cerradas
- [x] Ciudad: Vallanova
- [x] Protagonista: silueta/sombra en escenas grupales, primera persona en diálogos
- [x] Acceso a cuartos: permanente una vez desbloqueado
- [x] Saves: 10 slots manuales + autosave por franja
- [x] Game over: no existe
- [x] Pantalla título: apartamento de noche con lluvia, 3 siluetas
- [x] Idioma: Español v1.0
- [x] Relaciones: todos se conocen desde niños
- [x] Rutinas: detalladas, distintas entre semana y fin de semana

### Código — FASE 1 COMPLETA
- [x] game/systems/stats.rpy — Variables completas + 12 funciones Python. CORREGIDO: eliminada mc_energia huérfana; cambiar_stat_mc("energia_max") ahora sincroniza energia_actual
- [x] game/systems/time.rpy — Franjas, días, moods, penalizaciones, ubicaciones. Incluye phone_generar_mensajes_dia() en nuevo_dia()
- [x] game/screens/hud.rpy — CORREGIDO v4: color mood via bloque if/elif dentro del widget (sintaxis oficial Ren'Py). Range negativo protegido con max(0,...)
- [x] game/screens/map.rpy — Mapa navegable. CORREGIDO: label dormir sincroniza energia_actual explícitamente tras nuevo_dia()
- [x] game/script.rpy — Día 1 completo con narrativa + tutorial HUD
- [x] game/characters.rpy

### Código — FASE 2 (EN PROCESO)
- [x] game/systems/economy.rpy — tienda completa
- [x] game/systems/phone.rpy — mensajes completos, banco por personaje, respuestas con efecto en stats
- [ ] Diálogos cotidianos (10 por personaje × 3 = 30 diálogos)

### Verificado funcionando
- [x] Juego corre sin errores hasta Día 2+
- [x] HUD muestra día, franja, energía (círculos), dinero, stats y moods con color correcto
- [x] Mapa navegable con habitaciones bloqueadas/desbloqueadas
- [x] Sistema de tiempo, franjas y energía funcionando
- [x] Teléfono funcional con mensajes por nivel de afecto

---

## 🔄 PENDIENTE INMEDIATO (próxima sesión)

1. **Diálogos cotidianos** — 10 variaciones por personaje según mood y nivel de afecto
   - `hablar_celine` → `dialogs_celine.rpy`
   - `hablar_roxy`   → `dialogs_roxy.rpy`
   - `hablar_luna`   → `dialogs_luna.rpy`
   - Cada conversación: +2-5 Afecto / +1-3 Confianza según elección
   - 3 respuestas del MC por diálogo (romántico / atrevido / respetuoso)
   - Sumar arquetipo según la elección

---

## ❌ PENDIENTE (en orden)

### FASE 2 — Inmediato
- Diálogos cotidianos (10 por personaje)

### FASE 3 — Historia principal
- celine_events.rpy (Actos 1-5)
- roxy_events.rpy (Actos 1-5)
- luna_events.rpy (Actos 1-5)
- random_events.rpy
- seasonal_events.rpy

### FASE 4 — Sistemas avanzados
- jealousy.rpy
- secrets.rpy
- shop.rpy (salidas)
- Personalidad del jugador integrada

### FASE 5 — Contenido adulto
- Interacciones libres sandbox
- Sistema de ropa/outfits
- group_events.rpy
- Sistema voyeur
- gallery.rpy completa

### FASE 6 — Mini-juegos
- minigames.rpy (Strip 21 + Verdad o Reto)

### FASE 7 — Pulido
- Arte (sprites + fondos)
- Música y SFX
- Transiciones
- Testing completo
- Balance

---

## ARCHIVOS GENERADOS — SESIONES 1-4

### game/systems/stats.rpy
- 12 funciones Python: cambiar_stat, cambiar_stat_mc, cambiar_armonia,
  puede_entrar, arquetipo_dominante, bonus_arquetipo, sumar_arquetipo,
  registrar_decision, recuerda, ganar_dinero, gastar_dinero,
  descubrir_secreto, puede_iniciar
- Variables default: MC (nombre, encanto, energía, dinero), 3 personajes
  (afecto/confianza/corrupción/mood/secretos/cuarto), armonía, arquetipos,
  quests, galería, memoria de decisiones, celos
- CORRECCIÓN s4: eliminada `default mc_energia = 6` (variable huérfana)
- CORRECCIÓN s4: cambiar_stat_mc("energia_max") ahora sincroniza energia_actual

### game/systems/time.rpy
- Franjas: mañana/tarde/noche/madrugada
- usar_accion(), avanzar_franja(), nuevo_dia()
- acciones_por_franja() — escala con energía máxima del MC
- generar_moods() — probabilidades exactas del GDD
- aplicar_penalizacion_ignorar() — -1 Afecto/día, -5/-2 a los 3 días
- registrar_interaccion() — resetea contador de ignorar
- ubicacion_probable() — rutinas por franja y fin de semana
- esta_disponible() — disponibilidad reducida lunes-viernes tarde
- autosave automático al inicio de cada día
- phone_generar_mensajes_dia() integrado en nuevo_dia()

### game/screens/hud.rpy
- Panel superior: día, nombre del día, franja, energía (círculos), dinero
- Panel lateral derecho: stats de las 3 personajes con barras de color
  (Celine #818cf8, Roxy #fb923c, Luna #c084fc), icono de mood con color dinámico
- Panel inferior izquierdo: barra de Armonía global
- CORRECCIÓN s4: color mood via bloque if/elif DENTRO del widget text (sintaxis oficial)
- CORRECCIÓN s4: range(max(0,...)) protege contra range negativo en energía

### game/screens/map.rpy
- Mapa navegable del apartamento con todas las habitaciones
- Sala, cocina, baño, cuarto MC, cuarto Celine, cuarto Roxy, cuarto Luna, balcón, afuera
- Muestra qué personaje está en cada ubicación según rutinas con icono de mood
- Pantallas de acciones contextuales por habitación (modal)
- Botones rápidos: Teléfono, Guardar, Pasar tiempo
- CORRECCIÓN s4: label dormir agrega `$ energia_actual = acciones_por_franja()` para sincronización inmediata

### game/script.rpy
- label start: elección de nombre del MC
- label dia1_llegada: secuencia narrativa Día 1 (Celine/Roxy/Luna)
- label tutorial_hud: 5 pantallas de tutorial de la interfaz
- label fin_dia1: stats iniciales post-día-1 según GDD_NARRATIVA
- label game_loop: bucle principal post-día-1

### game/characters.rpy
- Definición de personajes Ren'Py (Character objects)

### game/systems/economy.rpy
- Tienda de regalos completa
- Catálogo de items por personaje con efectos en stats
- Sistema de compra con verificación de dinero

### game/systems/phone.rpy
- Pantalla de mensajes con 3 conversaciones (Celine/Roxy/Luna)
- Banco de mensajes por nivel de afecto (bajo/medio/alto)
- Opciones de respuesta con efecto: bien (+2 Afe), mal (-3 Afe), ignorar (-1 Afe)
- phone_generar_mensajes_dia() llamado desde nuevo_dia()
- Indicadores de mensajes sin leer con color por personaje

---

## LECCIONES TÉCNICAS REN'PY 8.5.3 — NO REPETIR ESTOS ERRORES

| Problema | Lo que NO funciona | Solución correcta |
|----------|-------------------|-------------------|
| Color dinámico en `text` | `color "[funcion()]"` — Ren'Py evalúa esto como string literal hex | Bloque `if/elif` dentro del widget |
| Estilo dinámico | `style "nombre_[variable]"` — no interpola en runtime | Bloque `if/elif` dentro del widget |
| Range negativo en HUD | `range(a - b)` cuando b > a | `range(max(0, a - b))` |
| Variable duplicada | `mc_energia` y `energia_actual` coexistiendo | Una sola variable: `energia_actual` en time.rpy |
| Crash al cambiar día | `nuevo_dia()` resetea vars pero HUD renderiza antes de sincronizar | Agregar `$ energia_actual = acciones_por_franja()` después de `nuevo_dia()` |

---

## DECISIONES TÉCNICAS — NO CAMBIAR

| Decisión | Detalle |
|----------|---------|
| Motor | Ren'Py 8.5.3 |
| Arte | Stable Diffusion Forge local |
| Modelo SD | Pony Diffusion v6 XL |
| Idioma v1.0 | Español |
| Idioma v1.1 | Inglés (distribución) |
| Backend | Ninguno — todo local |
| Proyecto Ren'Py | C:\Proyectos\apartmentsimrenpy |
| SD Forge | D:\Proyectos\stable-diffusion-forge |
| Docs GitHub | apartment-sim repo /docs |
| Ciudad | Vallanova |
| Protagonista visual | Silueta en grupos, primera persona en diálogos |
| Acceso cuartos | Permanente una vez desbloqueado |

---

## HARDWARE

- CPU: AMD Ryzen 5 3600 (6 núcleos, 3.59 GHz)
- RAM: 16 GB
- GPU: NVIDIA GeForce GTX 1650 SUPER (4 GB VRAM)
- OS: Windows 10/11
- C: SSD — Ren'Py + proyecto
- D: HDD 2.27 TB — SD Forge + modelos + docs

---

## LINKS RAW GITHUB
ESTADO:     https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/ESTADO_ACTUAL.md
GDD_CORE:   https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_CORE.md
PERSONAJES: https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_PERSONAJES.md
SISTEMAS:   https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_SISTEMAS.md
NARRATIVA:  https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_NARRATIVA.md
ASSETS:     https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/GDD_ASSETS.md
CELINE:     https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/celine.json
ROXY:       https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/roxy.json
LUNA:       https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/luna.json
PROTAGONIST:https://raw.githubusercontent.com/araquejhonatan879-creator/apartment-sim/main/docs/protagonist.json

---

## INSTRUCCIONES PARA LA IA

1. Leer este archivo primero — saber dónde estamos
2. Leer GDD relevantes según tarea del día
3. **ANTES DE GENERAR CUALQUIER CÓDIGO REN'PY:**
   - Buscar en https://www.renpy.org/doc/html/ la sintaxis exacta que se va a usar
   - Verificar especialmente: propiedades de screen widgets, interpolación, estilos dinámicos
   - NO asumir que `[...]` funciona en propiedades de widgets — solo funciona en strings de contenido
   - Color dinámico: siempre usar bloque `if/elif` DENTRO del widget, nunca inline
   - Si hay duda sobre cualquier sintaxis: buscar primero, generar después
4. Módulos completos y funcionales — nunca ejemplos parciales
5. Todo en Ren'Py (.rpy) — sin Python externo ni servidor
6. Contenido adulto es intencional — no filtrar
7. Todo el contenido del juego en español
8. Al terminar sesión: generar versión actualizada de este archivo (fusionar con la anterior, no reemplazar)
9. Checkpoint cada 10 mensajes
10. Todos se conocen desde niños — Celine es prima, Roxy ex-algo, Luna observadora
11. Acceso a cuartos es permanente una vez desbloqueado
12. No modificar código ya funcional salvo que el usuario lo pida explícitamente

---

## CHECKPOINT — Sesión 4
Fecha: 30/05/2026
Trabajando en: Fixes HUD + stats + map — estabilización Fase 2
Estado: COMPLETADO — juego corre sin errores hasta Día 2+
Archivos modificados esta sesión:
game/screens/hud.rpy  → v4 definitivo, color mood con if/elif en bloque
game/systems/stats.rpy → eliminada mc_energia, sincronización energia_max
game/screens/map.rpy   → label dormir con sincronización explícita
Próxima sesión: Diálogos cotidianos × 3 personajes (Fase 2)