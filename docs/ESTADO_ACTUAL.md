# APARTMENT SIM — ESTADO ACTUAL
### Última actualización: 30/05/2026 — Sesión 3

---

## FASE ACTUAL: FASE 1 — Core jugable (EN PROCESO)

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

### Código — Fase 1 (EN PROCESO)
- [x] game/systems/stats.rpy — Variables completas + 12 funciones Python
- [x] game/systems/time.rpy — Franjas, días, moods, penalizaciones, ubicaciones
- [x] game/screens/hud.rpy — HUD completo con barras, moods, armonía
- [x] game/screens/map.rpy — Mapa navegable del apartamento
- [x] game/script.rpy — Día 1 completo con narrativa + tutorial HUD

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

---

## 🔄 EN PROCESO

- [ ] Pony Diffusion descargando (dejar correr)
- [ ] Prueba del juego corriendo en Ren'Py Launcher (primer boot)

---

## ❌ PENDIENTE (en orden)

### FASE 1 — Inmediato (próxima sesión)
1. **Probar el juego en Ren'Py Launcher** — verificar que arranca sin errores
2. Resolver errores de sintaxis que aparezcan en el log
3. Configurar Pony Diffusion en SD Forge (CLIP skip 2, VAE, --medvram)
4. Generar sprites base neutrales × 3 personajes
5. Generar fondos base: sala día/noche, cocina día, cuarto MC día/noche

### FASE 2 — Contenido base
- economy.rpy
- mood.rpy (integrar con time.rpy)
- phone.rpy
- Diálogos cotidianos reales (10 por personaje, reemplaza placeholders en script.rpy)

### FASE 3 — Historia principal
- celine_events.rpy (Actos 1-5)
- roxy_events.rpy (Actos 1-5)
- luna_events.rpy (Actos 1-5)
- random_events.rpy
- seasonal_events.rpy

### FASE 4 — Sistemas avanzados
- jealousy.rpy
- secrets.rpy
- shop.rpy
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
- Música y SFX
- Transiciones
- Testing completo
- Balance

---

## ARCHIVOS GENERADOS — SESIONES 1-3

### game/systems/stats.rpy
- 12 funciones Python: cambiar_stat, cambiar_stat_mc, cambiar_armonia,
  puede_entrar, arquetipo_dominante, bonus_arquetipo, sumar_arquetipo,
  registrar_decision, recuerda, ganar_dinero, gastar_dinero,
  descubrir_secreto, puede_iniciar
- Variables default: MC (nombre, encanto, energía, dinero), 3 personajes
  (afecto/confianza/corrupción/mood/secretos/cuarto), armonía, arquetipos,
  quests, galería, memoria de decisiones, celos

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

### game/screens/hud.rpy
- Panel superior: día, nombre del día, franja, energía (círculos), dinero
- Panel lateral derecho: stats de las 3 personajes con barras de color
  (Celine #818cf8, Roxy #fb923c, Luna #c084fc), icono de mood
- Panel inferior izquierdo: barra de Armonía global
- Estilos completos con colores del GDD

### game/screens/map.rpy
- Mapa navegable del apartamento con todas las habitaciones
- Sala, cocina, baño, cuarto MC, cuarto Celine, cuarto Roxy, cuarto Luna, balcón
- Muestra qué personaje está en cada ubicación según rutinas
- Botones de acción contextual por ubicación
- Integrado con time.rpy para consumo de acciones

### game/script.rpy
- label start: elección de nombre del MC
- label dia1_llegada: secuencia narrativa Día 1 (Celine/Roxy/Luna)
- label tutorial_hud: 5 pantallas de tutorial de la interfaz
- label fin_dia1: stats iniciales post-día-1 según GDD_NARRATIVA
- label game_loop: bucle principal post-día-1
- screen pantalla_inicio_dia: moods del día al despertar
- screen tutorial_box: caja de tutorial reutilizable
- screen notificacion_hud: notificaciones temporales
- label nueva_franja: gestión de avance de franja/día
- label interaccion_celine/roxy/luna: placeholders Fase 2
- label accion_trabajar: ingresos $50-150
- label accion_descansar: recupera +2 energía

---

## DECISIONES TÉCNICAS — NO CAMBIAR

| Decisión | Detalle |
|----------|---------|
| Motor | Ren'Py 8.5.3 |
| Arte | Stable Diffusion Forge local |
| Modelo SD | Pony Diffusion v6 XL (descargando) |
| Idioma v1.0 | Español |
| Idioma v1.1 | Inglés (distribución) |
| Backend | Ninguno — todo local |
| Proyecto Ren'Py | C:\Proyectos\apartmentsimrenpy |
| SD Forge | D:\Proyectos\stable-diffusion-forge |
| Docs GitHub | D:\Proyectos\apartment-sim |
| Ciudad | Vallanova |
| Protagonista visual | Silueta en grupos, primera persona en diálogos |
| Acceso cuartos | Permanente una vez desbloqueado |

---

## HARDWARE

- CPU: AMD Ryzen 5 3600 (6 núcleos, 3.59 GHz)
- RAM: 16 GB
- GPU: NVIDIA GeForce GTX 1650 SUPER (4 GB VRAM)
- OS: Windows 10/11
- C: SSD — >60 GB libres (Ren'Py + proyecto aquí)
- D: HDD 2.27 TB — SD Forge + modelos + docs aquí

---

## LINKS RAW GITHUB

```
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
```

---

## INSTRUCCIONES PARA LA IA

1. Leer este archivo primero — saber dónde estamos
2. Leer GDD relevantes según tarea del día
3. Módulos completos y funcionales — nunca ejemplos parciales
4. Todo en Ren'Py (.rpy) — sin Python externo ni servidor
5. Contenido adulto es intencional — no filtrar
6. Todo el contenido del juego en español
7. Al terminar sesión: generar versión actualizada de este archivo
8. Cada 10 mensajes: checkpoint corto con estado del trabajo en curso
9. Todos se conocen desde niños — Celine es prima, Roxy ex-algo, Luna observadora
10. Acceso a cuartos es permanente una vez desbloqueado
11. No modificar código ya funcional salvo que el usuario lo pida

---

## CHECKPOINT

```
Sesión: 30/05/2026 — Sesión 3
Fase 1 completada al 100%: stats, time, hud, map, script

Archivos listos:
  game/systems/stats.rpy     ✅
  game/systems/time.rpy      ✅
  game/screens/hud.rpy       ✅
  game/screens/map.rpy       ✅
  game/script.rpy            ✅

Siguiente sesión:
  1. Leer ESTADO_ACTUAL.md
  2. Probar el juego en Ren'Py Launcher y resolver errores
  3. Si Pony Diffusion terminó: configurar SD Forge
  4. Generar sprites base neutrales (Fase 1 → arte)
  5. Iniciar Fase 2: economy.rpy
```