# APARTMENT SIM — GDD SISTEMAS
### Versión 2.0 | Actualizado: 30/05/2026

---

## S01 — STATS POR PERSONAJE

Tres barras independientes por personaje (0-100 cada una):

**Afecto:** Qué tanto le importas. Sube con tiempo compartido, conversaciones, regalos, quests completadas. Baja si la ignoras varios días seguidos o tomas decisiones que la lastiman.

**Confianza:** Qué tanto cree en ti. Sube siendo consistente, cumpliendo promesas, guardando secretos. Baja si mientes, fallas, o usas información en su contra. Es la barra más difícil de recuperar.

**Corrupción:** Qué tan abierta está a escalar la relación físicamente. Requiere mínimos de Afecto y Confianza para poder subir. No sube sola — requiere acciones específicas del jugador.

### Requisitos mínimos para subir Corrupción
| Nivel Corrupción destino | Afecto mínimo | Confianza mínima |
|--------------------------|---------------|------------------|
| 0→20 | 15 | 10 |
| 20→45 | 35 | 25 |
| 45→70 | 55 | 45 |
| 70→90 | 75 | 60 |
| 90→100 | 90 | 75 |

### Umbrales de Corrupción por personaje
| Nivel | Celine | Roxy | Luna |
|-------|--------|------|------|
| 0-20 | Rechaza todo contacto | Coquetea pero para | Ignora insinuaciones |
| 21-45 | Acepta cercanía mínima | Besos impulsivos que "no cuentan" | Permite cercanía en silencio |
| 46-70 | Besos tensos con vergüenza visible | Escenas íntimas con humor | Acción inesperada sin explicación |
| 71-90 | Pierde el control, después actúa como si no pasó | Completamente desinhibida, sin chistes | Se entrega en silencio absoluto |
| 91-100 | Sin barreras, sigue siendo ella — fría y directa | Sin límites, lo vive como aventura | Dice en voz alta lo que nunca dijo |

### Velocidad de cambio base
| Acción | Afecto | Confianza | Corrupción |
|--------|--------|-----------|------------|
| Conversación cotidiana exitosa | +2 | +0 | +0 |
| Conversación profunda | +5 | +3 | +0 |
| Regalo pequeño | +3 | +0 | +0 |
| Regalo significativo | +8 | +2 | +0 |
| Salida (cita) | +10-15 | +5-8 | +0 |
| Quest completada | +15-20 | +10-15 | +0 |
| Evento narrativo completado | +20 | +10 | +5-10 |
| Ignorar un día | -1 | +0 | +0 |
| Ignorar 3 días seguidos | -5 | -2 | +0 |
| Mentira descubierta | -5 | -15 | +0 |
| Usar secreto en contra | -10 | -25 | +0 |

---

## S02 — STATS DEL PROTAGONISTA

**Encanto (0-100):** Mejora opciones de diálogo disponibles y su efectividad. Con Encanto alto aparecen opciones de conversación únicas que no existen con Encanto bajo.

| Encanto | Efecto |
|---------|--------|
| 0-25 | Diálogos básicos. Sin opciones especiales. |
| 26-50 | +1 opción de diálogo en conversaciones importantes |
| 51-75 | +2 opciones. Probabilidad de eventos espontáneos positivos +10% |
| 76-100 | +3 opciones. Sistema voyeur sube a 85% éxito. Algunas chicas inician conversación primero. |

**Energía máxima (base 6, máx 10):** Acciones disponibles por día. Sube haciendo ejercicio en la mañana (5 días consecutivos = +1).

**Dinero:** Sin máximo. Empieza en $500. La moneda es genérica (créditos/billetes) — no se especifica divisa para evitar anclaje cultural.

### Cómo sube Encanto
- Leer un libro: +2 (máx 1 vez por libro)
- Conversación particularmente exitosa: +1
- Quest completada con resultado óptimo: +3-5
- Salida completada: +2

---

## S03 — PERSONALIDAD DEL JUGADOR

Las elecciones del jugador acumulan puntos en 3 arquetipos. El arquetipo dominante afecta cómo reaccionan los personajes.

| Arquetipo | Elecciones que lo suben | Personaje que lo prefiere |
|-----------|------------------------|--------------------------|
| Romántico | Gestos dulces, paciencia, escuchar activamente, recordar detalles | Luna |
| Atrevido | Directo, toma iniciativa, propone cosas, no espera permiso explícito | Roxy |
| Respetuoso | Nunca presiona, espera señales claras, pide antes de actuar | Celine |

### Efectos del arquetipo dominante
- Si tu arquetipo coincide con la preferencia del personaje: +20% a todos los puntos de Afecto
- Si tu arquetipo es opuesto: -10% (no bloquea, solo reduce)
- Puedes cambiar de arquetipo — no está fijo, se recalcula cada semana según elecciones recientes

---

## S04 — SISTEMA DE DÍAS Y TIEMPO

**4 franjas por día:**
- Mañana (6am-12pm)
- Tarde (12pm-6pm)
- Noche (6pm-12am)
- Madrugada (12am-6am)

**Acciones por franja:** 2 base (ampliable con Energía máxima del protagonista)

**Días de semana vs fin de semana:**
- Lunes-Viernes tarde: disponibilidad reducida (ellas tienen clase o estudio)
- Sábado-Domingo: disponibilidad completa, probabilidad de eventos especiales +25%

### Rutinas por franja
| Franja | Celine | Roxy | Luna |
|--------|--------|------|------|
| Mañana | Cocina o su cuarto | Cocina o sala | Cocina |
| Tarde | Su cuarto o biblioteca | Sala o afuera | Su cuarto o sala |
| Noche | Sala o su cuarto | Sala o su cuarto | Sala o balcón |
| Madrugada | Su cuarto (guardia baja) | Sala (rara vez duerme) | Cocina o ventana |

**Nota:** Las rutinas no son absolutas — el estado de ánimo diario puede cambiarlas.

---

## S05 — ECONOMÍA Y REGALOS

**Moneda:** Genérica (se muestra como símbolo $)

**Fuentes de ingreso:**
- Trabajar: 1 acción = $50-150 (aleatorio con distribución normal centrada en $90)
- Quests completadas: $50-300 según complejidad
- Eventos especiales: variable

**Tienda (accesible desde el teléfono o sala):**
| Regalo | Precio | Efecto | Notas |
|--------|--------|--------|-------|
| Café favorito | $20 | +3 Afecto | Diferente por personaje — hay que descubrirlo |
| Flores | $40 | +5 Afecto | Luna: +8 (le gustan más) |
| Libro específico | $80 | +8 Afecto +3 Confianza | Requiere saber qué le gusta |
| Ropa | $120 | +5 Afecto + desbloquea outfit | Solo si Afecto >30 |
| Joya | $200 | +15 Afecto | Solo si Afecto >50 para que no resulte raro |
| Cámara compacta | $150 | Desbloquea sistema voyeur | Item de jugador, no regalo |
| Regalo secreto | Variable | Efecto único | Solo disponible si descubriste su secreto correspondiente |

**Café favorito por personaje (hay que descubrirlo interactuando):**
- Celine: Americano negro sin azúcar
- Roxy: Matcha latte con mucho azúcar
- Luna: Té earl grey (no es café — si le compras café sube 0)

---

## S06 — EVENTOS NARRATIVOS (ver GDD_NARRATIVA.md)

5 eventos únicos por personaje desbloqueados por nivel de Afecto (20/40/60/80/100).
Cada evento tiene decisiones internas que afectan stats y narrativa.
Detalle completo en GDD_NARRATIVA.md.

---

## S07 — INTERACCIONES LIBRES SANDBOX

Disponibles una vez desbloqueadas. Se accede desde el mapa cuando el personaje está en ubicación compatible.

### Cómo se desbloquean
Cada interacción requiere nivel mínimo de Corrupción + Afecto. Algunas también requieren Confianza.

### Lista de interacciones por nivel de Corrupción

**Nivel 1 (Corrupción 20+):**
- Abrazo (cualquier lugar): +2 Afecto. Requiere Afecto >25.
- Masaje de hombros (sala/cuarto): +3 Afecto. Puede rechazarse si estado de ánimo es Cansada.
- Ver película juntos en el sofá (sala, noche): +4 Afecto +1 Confianza.

**Nivel 2 (Corrupción 40+):**
- Beso (requiere estar solos): +5 Afecto +5 Corrupción. Primera vez tiene escena especial.
- Dormir en el mismo cuarto (noche): +6 Afecto. Requiere que ella lo proponga o Afecto >60.
- Bailar en sala (noche, música): +5 Afecto +3 Confianza.

**Nivel 3 (Corrupción 60+):**
- Escena íntima nivel 1 (cuarto, noche/madrugada): desbloqueada y guardada en galería.
- Ducha compartida (baño): probabilidad base 40%, sube con Encanto.
- Sesión de fotos (si Corrupción >60): ella posa, fotos guardadas en colección.

**Nivel 4 (Corrupción 80+):**
- Escena íntima nivel 2: más explícita, múltiples variantes según personalidad.
- Proponer outfit (requiere Confianza >70): ella se cambia con variantes según Corrupción.
- Iniciativa nocturna: el jugador puede ir a su cuarto — puede aceptar o rechazar según estado de ánimo.

**Nivel 5 (Corrupción 95+):**
- Escena íntima nivel 3: sin restricciones, variante final de cada personaje.
- Interacciones grupales (requiere Armonía >60 y Corrupción >70 en 2+ personajes).

### Iniciativa inversa
Si Corrupción >60 y Afecto >70 y estado de ánimo es Traviesa (10% probabilidad):
El personaje puede proponer una interacción libre por su cuenta.
- Celine: lo hace de forma indirecta — "si quisieras... podría ser..." seguido de silencio
- Roxy: directo, sin rodeos, con un chiste por encima
- Luna: aparece en tu cuarto sin decir nada y espera

---

## S08 — ESTADO DE ÁNIMO DIARIO

Se determina al inicio de cada día para cada personaje. No cambia dentro del día salvo por eventos narrativos.

| Estado | Probabilidad | Efecto en Afecto ganado | Efecto especial |
|--------|-------------|------------------------|-----------------|
| Normal | 40% | x1 | Ninguno |
| Feliz | 20% | x1.5 | Confianza también x1.3 |
| Cansada | 15% | x0.7 | Rechaza interacciones físicas de nivel 1-2 |
| Estresada | 15% | x1.3 positivas / x0.3 negativas | Si la presionas: -10 Afecto extra |
| Traviesa | 10% | x1.2 | Puede proponer interacción libre si Corrupción >60 |

**Cómo saber el estado de ánimo:**
- Observable visualmente (expresión del sprite)
- Mensajes de texto del día lo insinúan
- Encanto >50: el jugador puede "leer" el estado al llegar a la sala

---

## S09 — SECRETOS DESCUBRIBLES

Cada personaje tiene 3 secretos. Se descubren explorando su cuarto, teléfono, o estando en el lugar correcto a la hora correcta.

**Descubrir un secreto:**
- +10 Confianza inmediato
- Desbloquea diálogos únicos relacionados
- Desbloquea el "Regalo secreto" en tienda

**Usar un secreto en su contra:**
- -20 Confianza permanente
- Bloquea 1 quest relacionada
- Ella lo recuerda — menciones futuras negativas

**Usar un secreto para acercarte (opción positiva):**
- Diálogo único de vulnerabilidad
- +15 Afecto +10 Confianza adicionales

### Secretos por personaje
**Celine:**
1. Diario con entradas sobre ti (cajón izquierdo escritorio, requiere estar en su cuarto con Afecto >35)
2. Conversación que tuvo con Roxy sobre ti (escuchar desde el pasillo, tarde, semana 2+)
3. Llora sola a veces de madrugada (estar despierto en madrugada, semana 3+)

**Roxy:**
1. Bocetos tuyos en su sketchbook (ver el libro cuando lo deja en sala)
2. Fotos de los dos que no tiró (cajón de su cuarto, Afecto >40)
3. Le habla a Luna de ti (escuchar conversación, noche, semana 2+)

**Luna:**
1. Página con tu nombre en su cuaderno (ver el cuaderno — solo si ella lo deja olvidado)
2. Cartas que no envió (fondo del cajón, solo en madrugada con Afecto >45)
3. La encuentras llorando en cocina a las 3am (estar en cocina en madrugada, semana 3+)

---

## S10 — EVENTOS ESPONTÁNEOS

**Probabilidad:** 15% por franja de que ocurra uno. No se repite el mismo en la misma semana.

| Evento | Franja | Condición | Efecto posible |
|--------|--------|-----------|---------------|
| Puerta del baño sin seguro | Mañana/Noche | Aleatorio | Escena voyeur sin cámara (no guarda) / +5 Corrupción |
| Apagón | Noche | Semana 1+ | Conversación forzada en oscuridad / +5 Afecto +3 Confianza |
| Lluvia intensa | Tarde/Noche | Cualquier semana | Todas en casa, ambiente íntimo / +3 Afecto todas |
| Se rompe algo | Mañana/Tarde | Cualquier semana | Si lo arreglas: +5 Confianza con la afectada |
| Te encuentra durmiendo en el sofá | Mañana | Madrugada previa activa | Reacción según personaje y Afecto actual |
| Pesadilla (ella) | Madrugada | Semana 2+ | Si vas: +8 Afecto +5 Confianza |
| Cocinar juntos sin planear | Mañana | Fin de semana | Minijuego simple / +6 Afecto |
| Encuentras su ropa en secadora | Mañana | Cualquier semana | Decisión moral / varias consecuencias |

---

## S11 — SISTEMA DE ROPA

4 outfits por personaje. Se desbloquean por nivel de Corrupción.

| Outfit | Corrupción req. | Descripción |
|--------|-----------------|-------------|
| Outfit 1 (base) | 0 | Ropa de diario. Siempre disponible. |
| Outfit 2 | 25 | Más casual/cómoda. Ropa de casa relajada. |
| Outfit 3 | 50 | Más revelador. Solo en noche/madrugada. |
| Outfit 4 | 80 | Máxima exposición. Solo en contexto de interacción libre. |

**A Corrupción >75 y Confianza >70:** puedes sugerirle qué ponerse. Acepta con probabilidad del 60% base (sube con Afecto).

---

## S12 — SALIDAS FUERA DEL APARTAMENTO

| Salida | Afecto req. | Costo | Bonus |
|--------|-------------|-------|-------|
| Café | 25 | $30 | +8 Afecto |
| Cine | 40 | $50 | +10 Afecto +5 Confianza |
| Compras | 50 | $80 | +8 Afecto + outfit desbloqueado |
| Cena | 60 | $100 | +12 Afecto +8 Confianza |
| Playa/Parque | 70 | $60 | +10 Afecto +10 Corrupción |
| Noche fuera | 85 | $150 | Evento especial único por personaje |

**Salidas grupales:** Invitar a dos con Afecto >50 en ambas activa evento grupal especial. Baja Armonía si la tercera se entera. Sube celos.

---

## S13 — MEMORIA DE DECISIONES

El juego almacena hasta 20 decisiones importantes. Se mencionan orgánicamente días o semanas después en diálogos.

**Tipos de decisiones recordadas:**
- Promesas hechas (y si se cumplieron)
- Momentos de crueldad o indiferencia
- Momentos de apoyo inesperado
- Secretos descubiertos y cómo se usaron
- Elecciones en eventos narrativos

**Cómo aparece en juego:**
- En diálogos cotidianos: "Eso que hiciste el martes..."
- En momentos de tensión: referencia directa
- En eventos narrativos: cambia opciones disponibles

---

## S14 — GALERÍA DE RECUERDOS

Accesible desde el teléfono del protagonista.

**Contenido:**
- Escenas narrativas desbloqueadas (automático)
- Interacciones libres marcadas como favoritas (el jugador elige)
- Fotos coleccionables (sistema S16)
- Filtros: por personaje / por tipo / por semana del juego

---

## S15 — SISTEMA VOYEUR

**Requisito:** Tener "Cámara compacta" ($150 en tienda).  
**Disponibilidad:** Solo noche y madrugada.  
**Probabilidad de éxito base:** 70% (sube a 85% con Encanto >75).

**Si te pillan:**
- -25 Confianza con esa personaje
- Bloqueado del sistema voyeur con ella esa semana
- Diálogo de confrontación (tono según Afecto actual)

**Si tienes éxito:**
- Escena desbloqueada y guardada en galería
- +15 Corrupción con esa personaje

**3 escenas por personaje, de menor a mayor intensidad:**
| Escena | Corrupción previa req. | Descripción general |
|--------|----------------------|---------------------|
| Voyeur 1 | 20 | Situación cotidiana íntima (cambiarse, ducharse) |
| Voyeur 2 | 50 | Situación más comprometedora |
| Voyeur 3 | 75 | Escena explícita |

---

## S16 — FOTOS COLECCIONABLES

**Cómo funcionan:** En momentos específicos aparece un ícono de cámara en pantalla. El jugador tiene 3-5 segundos para hacer click. Si lo hace: foto guardada en galería.

**A Corrupción >60:** puedes pedirle que pose. Acepta con probabilidad del 50% base.

**8-10 fotos por personaje**, distribuidas a lo largo del juego en momentos naturales.

---

## S17 — MENSAJES DE TEXTO

Accesible desde el teléfono en cualquier momento. Cada personaje envía mensajes espontáneos según Afecto y estado del día.

**Responder bien:** +2 Afecto  
**Ignorar:** -1 Afecto por día ignorado  
**Responder mal:** -3 Afecto

**Frecuencia de mensajes espontáneos:**
| Afecto | Mensajes por día |
|--------|-----------------|
| 0-30 | 0-1 |
| 31-60 | 1-2 |
| 61-100 | 2-4 |

---

## S18 — QUESTS POR PERSONAJE

3 quests por personaje (9 en total). Revelan historia y dan bonuses grandes.
Detalle completo en GDD_PERSONAJES.md (sección de cada personaje).

**Estructura de quest:**
1. Trigger (condición de Afecto/Confianza)
2. Evento/escena
3. Decisión del jugador
4. Consecuencia inmediata + consecuencia a largo plazo

---

## S19 — REPUTACIÓN DEL APARTAMENTO

**Barra global: Armonía (0-100)**  
Valor inicial: 70 (llevan tiempo conviviendo bien).

| Nivel | Efecto |
|-------|--------|
| >70 | Eventos grupales frecuentes, las tres interactúan naturalmente, ambiente cálido |
| 40-70 | Normal. Sin efectos especiales. |
| <40 | Algunas se evitan entre sí. Menos eventos disponibles. Diálogos más tensos. |
| <20 | Algunas se niegan a estar en el mismo cuarto. Bloquea eventos grupales. |

**Qué sube Armonía:**
- Eventos grupales positivos: +5-10
- Resolver conflictos entre ellas: +10-15
- Cumpleaños exitoso: +10

**Qué baja Armonía:**
- Celos activos: -3 por día
- Conflicto entre personajes sin resolver: -5
- Elecciones que favorecen claramente a una y perjudican a otra: -5-10

---

## S20 — CELOS Y DINÁMICAS

El sistema de celos se activa cuando una personaje detecta que el jugador está subiendo Afecto/Corrupción con otra.

**Umbral de activación:** Diferencia de Afecto >25 entre dos personajes O evento narrativo con otra presenciado.

| Par | Cómo expresan celos |
|-----|---------------------|
| Celine → Roxy | Se vuelve más fría y distante. Más sarcástica de lo normal. |
| Celine → Luna | Silencio activo. Deja de buscar al jugador. |
| Roxy → Celine | Comentarios ácidos con humor. Lo dice como chiste pero no es chiste. |
| Roxy → Luna | Pregunta más, escucha menos. Busca más atención. |
| Luna → cualquiera | Desaparece. Afecto baja solo 1 punto por día hasta que la busques. |

**Resolver celos:** Dedicar 3 días de acciones principalmente a la personaje celosa baja el nivel de celos.

---

## S21 — MINI-JUEGOS

### Strip 21 (Blackjack simplificado)
**Cómo se activa:** Lo propones tú o el personaje si Corrupción >30 y estado de ánimo Traviesa.
**Reglas:**
- Objetivo: llegar a 21 sin pasarse
- Cartas del 1 al 10 + figuras (valen 10)
- Sin dealer — es 1v1
- **Si pierdes:** eliges entre perder una prenda o hacer un reto (generado según nivel de Corrupción)
- **Si ganas:** tú eliges la prenda o el reto para ella

**Efectos:**
- Cada prenda perdida: +5 Corrupción
- Reto completado: +5 Afecto +3 Corrupción
- Reto rechazado: -5 Confianza

### Verdad o Reto
**Cómo se activa:** Lo propones tú o el personaje si Corrupción >20 y Afecto >30.
**Estructura:**
- Preguntas y retos generados según nivel de Corrupción (banco de 30+ por nivel)
- Rechazar una verdad: -3 Confianza
- Rechazar un reto: -5 Confianza
- Respuesta honesta a verdad difícil: +8 Confianza

**Banco de preguntas por nivel de Corrupción:**
- Nivel bajo (0-30): preguntas inocentes / retos tontos
- Nivel medio (31-60): preguntas personales / retos con contacto físico leve
- Nivel alto (61-85): preguntas íntimas / retos explícitos
- Nivel máximo (86-100): sin filtros
