# APARTMENT SIM — GDD ASSETS
### Versión 2.0 | Actualizado: 30/05/2026

---

## 1. MODELO DE STABLE DIFFUSION

**Modelo requerido:** Pony Diffusion v6 XL  
**Modelo actual (cambiar):** realisticVisionV51 — NO sirve para anime  
**SD Forge ubicación:** D:\Proyectos\stable-diffusion-forge  
**Endpoint local:** http://localhost:7860  

**Por qué Pony Diffusion v6 XL:**
- Estilo anime 2D limpio, colores vibrantes
- Excelente para personajes consistentes
- Compatible con LoRA de estilos y personajes
- Estándar en VNs adultos generados con IA

---

## 2. SPRITES DE PERSONAJES

### Cantidad total
- 3 personajes × ~30 sprites = **90 imágenes**

### Expresiones base por personaje (5)
1. Neutral
2. Feliz / Sonriente
3. Sorprendida
4. Enojada / Molesta
5. Sonrojada / Avergonzada

### Outfits por personaje (4)
- Outfit 1: Ropa de diario (se ve en el 80% del juego)
- Outfit 2: Ropa de casa relajada (más casual)
- Outfit 3: Revelador (noche/madrugada, Corrupción >50)
- Outfit 4: Mínimo (Corrupción >80, contexto de interacción libre)

**Cada outfit necesita las 5 expresiones = 20 sprites por outfit × 4 = 20 imágenes de expresión**
**Total sprites por personaje: ~25-30 imágenes**

---

## 3. PROMPTS BASE POR PERSONAJE

### CELINE — Prompts base

**Positivo base:**
```
score_9, score_8_up, score_7_up, anime style, 1girl, solo, 
black hair, hime cut, straight bangs, long hair to shoulders, 
ice grey eyes, sharp gaze, pale skin, tall, voluptuous figure,
composed expression, elegant posture,
indoor apartment background
```

**Outfit 1 (diario):**
```
[base] + white button shirt, dark slacks, formal wear, neat appearance
```

**Outfit 2 (casa relajada):**
```
[base] + oversized sweater, simple shorts, hair slightly loose
```

**Outfit 3 (noche, Corrupción >50):**
```
[base] + thin camisole, shorts, slightly disheveled hair
```

**Outfit 4 (Corrupción >80):**
```
[base] + lingerie, seductive pose, detailed
```

**Negativo universal:**
```
bad anatomy, bad hands, extra fingers, deformed, ugly, 
watermark, text, blurry, low quality, realistic photo, 3d render
```

---

### ROXY — Prompts base

**Positivo base:**
```
score_9, score_8_up, score_7_up, anime style, 1girl, solo,
orange red hair, twin tails, asymmetric pigtails, amber eyes,
expressive eyes, athletic build, energetic posture,
colorful clothes, casual wear
```

**Outfit 1 (diario):**
```
[base] + graphic tee, jeans, sneakers, pins on bag, layered clothing
```

**Outfit 2 (casa relajada):**
```
[base] + crop top, sweatpants, hair slightly messy
```

**Outfit 3 (noche, Corrupción >50):**
```
[base] + loose tank top, underwear visible, relaxed at home
```

**Outfit 4 (Corrupción >80):**
```
[base] + lingerie, playful expression, seductive
```

---

### LUNA — Prompts base

**Positivo base:**
```
score_9, score_8_up, score_7_up, anime style, 1girl, solo,
silver lavender hair, long straight hair, violet eyes,
pale skin, slender figure, calm expression,
always holding a book or notebook
```

**Outfit 1 (diario):**
```
[base] + soft layered clothes, cardigan, long skirt, muted tones
```

**Outfit 2 (casa relajada):**
```
[base] + loose oversized shirt, soft pants, hair down
```

**Outfit 3 (noche, Corrupción >50):**
```
[base] + thin nightgown, hair loose, dreamy expression
```

**Outfit 4 (Corrupción >80):**
```
[base] + lingerie, quiet seductive expression, intimate setting
```

---

## 4. FONDOS DEL APARTAMENTO

### Lista de cuartos y variantes necesarias
Cada cuarto necesita 3 versiones de iluminación + 1 lluvia para cuartos principales.

| Cuarto | Día | Tarde | Noche | Lluvia |
|--------|-----|-------|-------|--------|
| Sala | ✓ | ✓ | ✓ | ✓ |
| Cocina | ✓ | ✓ | ✓ | ✓ |
| Cuarto Celine | ✓ | ✓ | ✓ | — |
| Cuarto Roxy | ✓ | ✓ | ✓ | — |
| Cuarto Luna | ✓ | ✓ | ✓ | — |
| Cuarto protagonista | ✓ | ✓ | ✓ | — |
| Baño | ✓ | — | ✓ | — |
| Balcón | ✓ | ✓ | ✓ | ✓ |

**Total fondos: 8 cuartos × 3 = 24 base + 4 lluvia = 28 fondos**

### Prompts base para fondos

**Sala (día):**
```
score_9, anime background, cozy apartment living room, 
natural daylight, warm tones, sofa, coffee table, bookshelf,
plants, large window, no people, detailed interior
```

**Cocina (noche):**
```
score_9, anime background, small apartment kitchen,
warm kitchen light, counter, stove, small table, cups,
cozy night atmosphere, no people
```

**Cuarto Celine (tarde):**
```
score_9, anime background, neat organized bedroom,
bookshelves full of law books, desk with papers,
afternoon light through curtains, dark blue color accents,
minimal but elegant, no people
```

**Cuarto Roxy (día):**
```
score_9, anime background, creative messy bedroom,
art supplies, sketchbooks, posters on walls, 
bright colors, morning light, organized chaos, no people
```

**Cuarto Luna (noche):**
```
score_9, anime background, peaceful minimalist bedroom,
books stacked everywhere, dim lamp light, 
lavender color accents, moon visible through window, no people
```

**Balcón (noche):**
```
score_9, anime background, small apartment balcony,
city lights in distance, night sky, railing, 
atmospheric night mood, stars, no people
```

---

## 5. IMÁGENES DE EVENTOS NARRATIVOS

~50 imágenes para los 15 actos narrativos + eventos especiales.

### Distribución aproximada
- 3-4 imágenes por acto narrativo (15 actos × 3 = ~45)
- 5 imágenes para eventos grupales
- Total: ~50 imágenes

### Tipos de escenas a generar
- Escenas de conversación (personaje en contexto del evento)
- Momentos emocionales clave (expresión especial + fondo)
- Primer contacto físico por personaje
- Escenas de descubrimiento de secretos

---

## 6. IMÁGENES DE CONTENIDO ADULTO

**15 imágenes por personaje = 45 total**

### Distribución por personaje
| Tipo | Cantidad | Trigger |
|------|----------|---------|
| Interacción libre nivel 1 | 3 | Corrupción 40+ |
| Interacción libre nivel 2 | 3 | Corrupción 60+ |
| Interacción libre nivel 3 | 3 | Corrupción 80+ |
| Escenas voyeur (3) | 3 | Sistema S15 |
| Acto 5 narrativo | 3 | Afecto 100 |

---

## 7. FOTOS COLECCIONABLES

8-10 fotos por personaje = ~27 fotos total

### Tipos de fotos coleccionables
- Fotos cotidianas en momentos naturales (mayor parte)
- Fotos posadas (Corrupción >60, pedirle que pose)
- Fotos de eventos especiales (cumpleaños, San Valentín)

---

## 8. ELEMENTOS UI

### HUD (siempre visible)
- Barras de stats: Afecto / Confianza / Corrupción para cada personaje
- Dinero actual
- Franja horaria actual
- Día actual
- Energía disponible

### Pantalla del teléfono
- App de mensajes con las 3 personajes
- App de tienda
- App de galería (fotos coleccionables)

### Mapa del apartamento
- Vista top-down simple
- Puntos de interacción por cuarto
- Indicador de dónde está cada personaje

---

## 9. AUDIO

### Música por franja (4 temas)
| Franja | Mood | Referencia |
|--------|------|------------|
| Mañana | Optimista, tranquilo | Lo-fi con piano suave |
| Tarde | Activo, cálido | Lo-fi beats moderados |
| Noche | Íntimo, melancólico | Ambient con guitarra |
| Madrugada | Silencioso, tenso | Minimal ambient |

### Temas especiales
- Tema de Celine: Piano clásico frío
- Tema de Roxy: Synth pop energético
- Tema de Luna: Ambient con cuerdas
- Tema de eventos adultos: Ambient sensual
- Tema de tensión/celos: Strings tensos

### Efectos de sonido
- Notificación de mensaje (diferente por personaje)
- Puerta abriéndose/cerrándose
- Lluvia (loop)
- Ambiente de cocina
- Ambiente de sala
- Click de cámara (S16)

**Fuente recomendada:** Packs royalty-free de itch.io o freesound.org

---

## 10. ORDEN DE GENERACIÓN RECOMENDADO

### Fase 0 (mínimo para empezar a probar)
1. Sprite neutral Outfit 1 de las 3 personajes
2. Fondo sala día y noche
3. Fondo cocina día

### Fase 1 (para tener el core visual)
4. Las 5 expresiones de Outfit 1 por personaje (15 sprites)
5. Fondos de todos los cuartos en variante día

### Fase 2 (para contenido completo)
6. Outfit 2 y 3 con expresiones
7. Fondos variante noche y tarde
8. Imágenes de eventos narrativos por orden de los actos

### Fase final
9. Outfit 4 + imágenes adultas
10. Fotos coleccionables
11. Elementos UI finales
