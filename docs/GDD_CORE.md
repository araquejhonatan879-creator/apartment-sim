# APARTMENT SIM — GDD CORE
### Versión 2.1 | Actualizado: 30/05/2026

---

## 1. VISIÓN DEL PROYECTO

**Nombre:** Apartment Sim
**Género:** Visual Novel Adulto / Simulador Social Sandbox
**Plataforma:** Windows (exportable a Mac/Linux/Android)
**Audiencia:** Adultos 18+
**Idioma:** Español (v1.0) — Inglés (v1.1 para distribución)
**Motor:** Ren'Py 8.x
**Ciudad:** Vallanova — ciudad universitaria ficticia, tamaño mediano, costera

### Concepto central
Simulador de vida en apartamento compartido con 3 compañeras de piso en Vallanova. Sin límite de tiempo. El jugador construye relaciones reales a través de tiempo, gestos, decisiones y dinero. El contenido adulto se desbloquea de forma progresiva y natural. Las 3 historias se cruzan y se afectan entre sí. La dinámica central es única: el protagonista vive con su prima (Celine) y dos amigas de infancia (Roxy y Luna) — todos se conocen desde niños, lo que crea capas de historia real debajo de cada interacción.

### Referentes
| Juego | Qué tomamos |
|-------|-------------|
| Summer Memories | Sistema de días, rutinas, eventos por franja |
| Teaching Feeling | Sandbox libre, interacciones en cualquier momento |
| Harem Hotel | Economía, quests por personaje, historias cruzadas |
| Milfy City | Stats del protagonista, mensajes de texto, voyeur, silueta del MC |
| Being a DIK | Personalidad del jugador, elecciones que definen al MC |
| Corrupted Kingdoms | Sistema de celos, stats trust/love/corruption |

---

## 2. STACK TÉCNICO

### Motor: Ren'Py 8.x
- Sistema de saves, galería y stats integrados
- Exporta a Windows, Mac, Linux y Android
- Python como base — potente y familiar
- Agregar personaje nuevo = 1 archivo .rpy + sprites
- No necesita servidor — todo corre local

### Arte y generación visual
- Sprites y fondos: Stable Diffusion Forge
- Ubicación SD Forge: `D:\Proyectos\stable-diffusion-forge`
- Modelo requerido: **Pony Diffusion v6 XL** (HAY QUE DESCARGAR)
- Modelo actual: realisticVisionV51 — NO sirve para anime
- Edición: GIMP o Krita
- Estilo objetivo: Anime 2D, líneas limpias, colores vibrantes

### Software necesario (todo gratuito)
- Ren'Py 8.x — renpy.org
- Stable Diffusion Forge — ya instalado
- GIMP o Krita — edición sprites
- VS Code — código
- Git — control de versiones

---

## 3. EL PROTAGONISTA

**Nombre:** Elegible por el jugador al inicio (default: Kai)
**Edad:** 22 | **Carrera:** Ingeniería de Sistemas (primer año)
**Visual:** Silueta/sombra en escenas grupales. Sin sprite definido en diálogos — perspectiva primera persona.

### Relaciones de entrada (todos se conocen desde niños)
| Personaje | Vínculo |
|-----------|---------|
| Celine | Prima — historia sin resolver |
| Roxy | Amiga de infancia / ex-algo sin nombre |
| Luna | Conocida del grupo — siempre lo observó diferente |

### Stats iniciales
- Encanto: 10
- Energía máxima: 6 acciones/día
- Dinero: $500

---

## 4. SISTEMA DE SAVES

- **Slots manuales:** 10
- **Autosave:** Automático por franja horaria (sobreescribe el anterior)
- **Acceso:** Desde el menú en cualquier momento

---

## 5. GAME OVER

**No existe game over.**
Si Confianza llega a 0 con un personaje: se vuelve hostil/fría de forma permanente pero sigue en el juego. El jugador puede intentar recuperar la relación — es muy difícil pero no imposible.

---

## 6. PANTALLA DE TÍTULO

- Fondo animado: el apartamento de noche con lluvia suave
- Las 3 siluetas visibles desde la ventana (sin detalle, solo presencia)
- Música: tema ambiente nocturno
- Menú: Nuevo juego / Continuar / Galería / Configuración / Salir

---

## 7. IDIOMAS

- **v1.0:** Español completo (toda la UI, diálogos y contenido)
- **v1.1 futura:** Inglés — pensado para distribución en itch.io y F95zone
- Implementación: sistema de traducción integrado de Ren'Py (archivo .rpy por idioma)

---

## 8. MAPA DEL APARTAMENTO

### Acceso a cuartos
**Una vez desbloqueado el cuarto con el nivel de Afecto requerido, el acceso es PERMANENTE.**
No se necesita volver a ganarlo. El jugador puede entrar cuando quiera dentro de los horarios disponibles.

| Cuarto | Afecto para desbloquear | Disponibilidad tras desbloqueo |
|--------|------------------------|-------------------------------|
| Sala / Cocina | 0 | Siempre |
| Cuarto Roxy | 20 | Disponible cuando ella está ahí |
| Cuarto Celine | 35 | Disponible cuando ella lo permite (guardia baja) |
| Cuarto Luna | 45 | Disponible en momentos específicos de su rutina |
| Baño | Sin requisito | Evento espontáneo — probabilidad por franja |
| Balcón | 0 | Siempre (Luna aquí de noche frecuentemente) |

---

## 9. ESTRUCTURA DE ARCHIVOS REN'PY

```
apartment-sim-renpy/          ← D:\Proyectos\apartment-sim-renpy
├── game/
│   ├── script.rpy            ← narrativa principal, día 1, inicio
│   ├── characters/
│   │   ├── celine.rpy
│   │   ├── roxy.rpy
│   │   └── luna.rpy
│   ├── screens/
│   │   ├── hud.rpy           ← barras de stats siempre visibles
│   │   ├── map.rpy           ← mapa navegable del apartamento
│   │   ├── phone.rpy         ← mensajes de texto
│   │   ├── gallery.rpy       ← galería de escenas
│   │   └── shop.rpy          ← tienda de regalos
│   ├── systems/
│   │   ├── stats.rpy         ← variables y funciones de stats
│   │   ├── time.rpy          ← franjas horarias y días
│   │   ├── mood.rpy          ← estado de ánimo diario
│   │   ├── jealousy.rpy      ← celos entre personajes
│   │   ├── secrets.rpy       ← secretos descubribles
│   │   ├── minigames.rpy     ← Strip 21 y Verdad o Reto
│   │   └── economy.rpy       ← dinero, regalos, tienda
│   ├── events/
│   │   ├── celine_events.rpy
│   │   ├── roxy_events.rpy
│   │   ├── luna_events.rpy
│   │   ├── group_events.rpy
│   │   ├── random_events.rpy
│   │   └── seasonal_events.rpy
│   ├── images/
│   │   ├── sprites/
│   │   ├── backgrounds/
│   │   ├── items/
│   │   └── ui/
│   └── audio/
│       ├── music/
│       └── sfx/
└── saves/
```

---

## 10. LÍMITES Y ESCALABILIDAD

### Scope v1.0
- 3 personajes completos
- 21 sistemas implementados
- Sandbox sin fin definido
- Eventos grupales hasta 3 personajes
- Arte con Stable Diffusion

### Fuera de scope v1.0
- Voces actuadas
- Animaciones de escenas
- Más de 3 personajes principales
- Multijugador

### Escalabilidad
- Nuevo personaje = 1 .rpy + sprites + events archivo
- Stats genéricos para cualquier personaje
- Mini-juegos modulares
- Tienda expandible en 2 líneas de código

---

## 11. ASSETS — RESUMEN

- ~90 sprites (3 personajes × 30)
- ~28 fondos (8 cuartos × 3 horas + variantes lluvia)
- ~50 imágenes de eventos narrativos
- ~45 imágenes de contenido adulto
- ~27 fotos coleccionables
- **Total: ~240 imágenes**

Detalle completo en `GDD_ASSETS.md`

---

## 12. PALETA UI

| Elemento | Color |
|----------|-------|
| Fondo | `#0d0d0f` |
| Paneles | `#13131a` |
| Texto | `#e2e8f0` |
| Celine | `#818cf8` |
| Roxy | `#fb923c` |
| Luna | `#c084fc` |

---

## 13. AUDIO

- 4 temas por franja horaria
- Temas especiales por personaje
- Lo-fi para momentos cotidianos
- Efectos: notificaciones, puertas, lluvia, ambiente
- Fuente: packs royalty-free itch.io / freesound.org

---

## 14. REPOSITORIO GITHUB

```
docs/
├── GDD_CORE.md
├── GDD_PERSONAJES.md
├── GDD_SISTEMAS.md
├── GDD_NARRATIVA.md
├── GDD_ASSETS.md
├── ESTADO_ACTUAL.md
├── celine.json
├── roxy.json
├── luna.json
└── protagonist.json
```

**Instrucción para IA:** Leer `ESTADO_ACTUAL.md` primero. Luego los archivos relevantes para la tarea del día.
