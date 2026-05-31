# APARTMENT SIM — ESTADO ACTUAL
### Última actualización: 30/05/2026

---

## FASE ACTUAL: FASE 0 — Preparación

---

## ✅ COMPLETADO

### Diseño y documentación
- [x] GDD_CORE.md v2.1 — visión, stack, saves, game over, pantalla título, idiomas
- [x] GDD_PERSONAJES.md — protagonista + 3 personajes con rutinas detalladas
- [x] GDD_SISTEMAS.md — 21 sistemas detallados con números y mecánicas
- [x] GDD_NARRATIVA.md — día 1 + 5 actos por personaje completos + eventos grupales
- [x] GDD_ASSETS.md — sprites, fondos, prompts SD, audio
- [x] protagonist.json — silueta/sombra, nombre elegible, stats iniciales
- [x] celine.json v2 — rutinas detalladas semana/fin de semana, coherencia mejorada
- [x] roxy.json v2 — rutinas detalladas semana/fin de semana, coherencia mejorada
- [x] luna.json v2 — rutinas detalladas semana/fin de semana, coherencia mejorada
- [x] Stable Diffusion Forge instalado en D:\Proyectos\stable-diffusion-forge

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

- [ ] Crear repositorio GitHub y subir todos los docs
- [ ] Reemplazar USUARIO en los links raw del repo

---

## ❌ PENDIENTE (en orden)

### FASE 0 — Inmediato
1. Crear repo GitHub: `apartment-sim` (público)
2. Subir carpeta `docs/` completa
3. Actualizar links raw en este archivo
4. Configurar Proyecto Claude con los links
5. Descargar Pony Diffusion v6 XL en SD Forge
6. Instalar Ren'Py 8.x desde renpy.org
7. Generar sprites base neutrales Outfit 1 de las 3 personajes
8. Generar fondos base: sala día/noche, cocina día
9. Crear estructura de carpetas en D:\Proyectos\apartment-sim-renpy

### FASE 1 — Core jugable
- stats.rpy
- time.rpy
- hud.rpy
- map.rpy
- script.rpy (día 1)

### FASE 2 — Contenido base
- economy.rpy
- mood.rpy
- phone.rpy
- Diálogos cotidianos (10 por personaje)

### FASE 3 — Historia principal
- celine_events.rpy
- roxy_events.rpy
- luna_events.rpy
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
- Música y SFX
- Transiciones
- Testing completo
- Balance

---

## DECISIONES TÉCNICAS — NO CAMBIAR

| Decisión | Detalle |
|----------|---------|
| Motor | Ren'Py 8.x |
| Arte | Stable Diffusion Forge local |
| Modelo SD | Pony Diffusion v6 XL (pendiente descargar) |
| Idioma v1.0 | Español |
| Idioma v1.1 | Inglés (distribución) |
| Backend | Ninguno — todo local |
| Proyecto Ren'Py | D:\Proyectos\apartment-sim-renpy |
| SD Forge | D:\Proyectos\stable-diffusion-forge |
| Proyecto anterior | D:\Proyectos\apartment-sim — DESCARTADO |
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

## LINKS RAW GITHUB (completar al crear el repo)

```
ESTADO:     https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/ESTADO_ACTUAL.md
GDD_CORE:   https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/GDD_CORE.md
PERSONAJES: https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/GDD_PERSONAJES.md
SISTEMAS:   https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/GDD_SISTEMAS.md
NARRATIVA:  https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/GDD_NARRATIVA.md
ASSETS:     https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/GDD_ASSETS.md
CELINE:     https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/celine.json
ROXY:       https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/roxy.json
LUNA:       https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/luna.json
PROTAGONIST:https://raw.githubusercontent.com/USUARIO/apartment-sim/main/docs/protagonist.json
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

---

## CHECKPOINT

```
Sesión: 30/05/2026
Trabajando en: GDD completo v2.1 + JSONs actualizados
Estado: COMPLETADO — todos los archivos listos para GitHub
Siguiente sesión: Crear repo GitHub → instalar Ren'Py → descargar modelo SD anime
```
