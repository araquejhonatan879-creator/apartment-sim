# APARTMENT SIM — VARIABLES GLOBALES
### Versión: 1.0 — Verificado por El Arquitecto contra documentación oficial
### Motor: Ren'Py 8.5.3 | Python: 3.12 (desde Ren'Py 8.4+)
### Última actualización: 31/05/2026
### Fuentes: renpy.org/doc/html/python.html · /save_load_rollback.html · /persistent.html

---

## REGLAS FUNDAMENTALES DE VARIABLES EN REN'PY 8.5.3
*(Verificado en documentación oficial — crítico para saves y rollback)*

| Keyword | Comportamiento | Uso correcto |
|---------|---------------|--------------|
| `default` | Siempre se guarda en save. Si ya existe un valor guardado, NO sobreescribe. | **Toda variable de gameplay** (stats, flags, progreso) |
| `define` | Constante. NO se guarda. NO participa en rollback. | Solo constantes fijas (colores, nombres de personajes) |
| `init python:` vars | NO se guardan si se asignan en init. | Solo para clases, funciones y config |
| `persistent.x` | Se guarda entre partidas distintas (no ligado a save slot). | Galería, achievements, ajustes del jugador |

**ADVERTENCIA CRÍTICA sobre listas:**
Según la doc oficial: *"changes to fields in objects will not cause those objects to be saved — the variable itself must change"*.
Esto significa que hacer `lista.append(x)` NO activa el save automático.
**Solución obligatoria:** reasignar siempre → `lista = lista + [nuevo_item]`
O usar `default` con listas y reasignar. Documentado en cada variable lista de este archivo.

---

## 1. STATS POR PERSONAJE
**Módulo responsable:** `stats.rpy`
**Keyword:** `default` (se guardan, participan en rollback)

| Variable | Tipo | Valor inicial | Rango | Quién modifica | Descripción |
|----------|------|--------------|-------|----------------|-------------|
| `stats_celine_afecto` | `int` | `15` | 0–100 | stats.rpy, celine_events.rpy | Afecto de Celine hacia el protagonista |
| `stats_celine_confianza` | `int` | `10` | 0–100 | stats.rpy, celine_events.rpy | Confianza de Celine en el protagonista |
| `stats_celine_corrupcion` | `int` | `5` | 0–100 | celine_events.rpy | Nivel de corrupción de Celine |
| `stats_roxy_afecto` | `int` | `25` | 0–100 | stats.rpy, roxy_events.rpy | Afecto de Roxy hacia el protagonista |
| `stats_roxy_confianza` | `int` | `15` | 0–100 | stats.rpy, roxy_events.rpy | Confianza de Roxy en el protagonista |
| `stats_roxy_corrupcion` | `int` | `15` | 0–100 | roxy_events.rpy | Nivel de corrupción de Roxy |
| `stats_luna_afecto` | `int` | `20` | 0–100 | stats.rpy, luna_events.rpy | Afecto de Luna hacia el protagonista |
| `stats_luna_confianza` | `int` | `10` | 0–100 | stats.rpy, luna_events.rpy | Confianza de Luna en el protagonista |
| `stats_luna_corrupcion` | `int` | `10` | 0–100 | luna_events.rpy | Nivel de corrupción de Luna |

**Nota arquitectura:** Los stats nunca se modifican directamente desde labels de evento.
Siempre usar la función `fn_stats_modificar(personaje, stat, delta)` definida en stats.rpy.
Esto garantiza que se apliquen los límites 0–100 y se actualice el HUD.

---

## 2. STATS DEL PROTAGONISTA
**Módulo responsable:** `stats.rpy` (energía: `time.rpy`, dinero: `economy.rpy`)
**Keyword:** `default`

| Variable | Tipo | Valor inicial | Rango | Quién modifica | Descripción |
|----------|------|--------------|-------|----------------|-------------|
| `prot_nombre` | `str` | `"Kai"` | — | script.rpy (una vez) | Nombre elegido en el setup inicial |
| `prot_encanto` | `int` | `10` | 0–100 | stats.rpy | Mejora opciones de diálogo disponibles |
| `prot_energia_max` | `int` | `6` | 6–10 | stats.rpy | Acciones máximas por franja horaria |
| `prot_energia_actual` | `int` | `6` | 0–`prot_energia_max` | time.rpy | Acciones disponibles en la franja actual |
| `prot_dinero` | `int` | `500` | 0–sin límite | economy.rpy | Dinero disponible en pesos de Vallanova |

**Nota sobre prot_nombre:**
Se inicializa con `default prot_nombre = "Kai"`.
En script.rpy, al inicio del juego, se reemplaza con input del jugador:
`$ prot_nombre = renpy.input("¿Cómo te llamas?", default="Kai")` — verificar sintaxis en docs.
Una vez asignado, la variable ya está en el store y se guarda normalmente.

---

## 3. PERSONALIDAD DEL JUGADOR
**Módulo responsable:** `stats.rpy`
**Keyword:** `default`
**Descripción general:** Sistema de arquetipo acumulativo. Al final de cada jornada se
determina el arquetipo dominante comparando los tres valores. No hay límite superior —
lo que importa es cuál es mayor.

| Variable | Tipo | Valor inicial | Quién modifica | Descripción |
|----------|------|--------------|----------------|-------------|
| `pers_romantico` | `int` | `0` | stats.rpy (desde choices) | Puntos acumulados arquetipo romántico |
| `pers_atrevido` | `int` | `0` | stats.rpy (desde choices) | Puntos acumulados arquetipo atrevido |
| `pers_respetuoso` | `int` | `0` | stats.rpy (desde choices) | Puntos acumulados arquetipo respetuoso |

---

## 4. SISTEMA DE TIEMPO
**Módulo responsable:** `time.rpy`
**Keyword:** `default`

| Variable | Tipo | Valor inicial | Quién modifica | Descripción |
|----------|------|--------------|----------------|-------------|
| `time_dia` | `int` | `1` | time.rpy | Día actual del juego (empieza en día 1) |
| `time_franja` | `str` | `"manana"` | time.rpy | Franja activa: `"manana"` / `"tarde"` / `"noche"` / `"madrugada"` |
| `time_dia_semana` | `str` | `"lunes"` | time.rpy | Día de la semana en texto |
| `time_es_finde` | `bool` | `False` | time.rpy | `True` si `time_dia_semana` es `"sabado"` o `"domingo"` |
| `time_total_franjas` | `int` | `0` | time.rpy | Contador total de franjas transcurridas (para eventos temporales) |

**Valores válidos para time_franja:**
`"manana"` → `"tarde"` → `"noche"` → `"madrugada"` → avanza día → `"manana"`
Sin tildes en el valor para evitar problemas de encoding en comparaciones.

**Valores válidos para time_dia_semana:**
`"lunes"` `"martes"` `"miercoles"` `"jueves"` `"viernes"` `"sabado"` `"domingo"`
Sin tildes por la misma razón.

---

## 5. ESTADO DE ÁNIMO DIARIO
**Módulo responsable:** `mood.rpy`
**Keyword:** `default`
**Descripción:** Se recalcula cada vez que avanza la franja. Depende de stats y eventos recientes.

| Variable | Tipo | Valor inicial | Quién modifica | Valores válidos |
|----------|------|--------------|----------------|-----------------|
| `mood_celine` | `str` | `"normal"` | mood.rpy | `"normal"` `"feliz"` `"cansada"` `"estresada"` `"traviesa"` |
| `mood_roxy` | `str` | `"normal"` | mood.rpy | `"normal"` `"feliz"` `"cansada"` `"estresada"` `"traviesa"` |
| `mood_luna` | `str` | `"normal"` | mood.rpy | `"normal"` `"feliz"` `"cansada"` `"estresada"` `"traviesa"` |

**Nota:** El mood afecta qué sprite se muestra y qué diálogos cotidianos están disponibles.
Se lee en hud.rpy para mostrar indicador visual.

---

## 6. ARMONÍA Y CELOS
**Módulo responsable:** `jealousy.rpy`
**Keyword:** `default`

| Variable | Tipo | Valor inicial | Rango | Quién modifica | Descripción |
|----------|------|--------------|-------|----------------|-------------|
| `apt_armonia` | `int` | `70` | 0–100 | jealousy.rpy | Armonía global del apartamento |
| `celos_celine_activo` | `bool` | `False` | — | jealousy.rpy | True si Celine tiene celos activos hoy |
| `celos_roxy_activo` | `bool` | `False` | — | jealousy.rpy | True si Roxy tiene celos activos hoy |
| `celos_luna_activo` | `bool` | `False` | — | jealousy.rpy | True si Luna tiene celos activos hoy |
| `celos_celine_intensidad` | `int` | `0` | 0–3 | jealousy.rpy | 0=ninguno 1=leve 2=moderado 3=intenso |
| `celos_roxy_intensidad` | `int` | `0` | 0–3 | jealousy.rpy | 0=ninguno 1=leve 2=moderado 3=intenso |
| `celos_luna_intensidad` | `int` | `0` | 0–3 | jealousy.rpy | 0=ninguno 1=leve 2=moderado 3=intenso |

**Nota:** Los celos se resetean al avanzar de día. La armonía es persistente.
Si `apt_armonia` llega a 0, se activa modo conflicto global.

---

## 7. ACCESO A CUARTOS
**Módulo responsable:** `stats.rpy` (verificación), `map.rpy` (uso)
**Keyword:** `default`
**Regla de diseño:** Una vez `True`, NUNCA vuelve a `False`.

| Variable | Tipo | Valor inicial | Desbloqueo | Descripción |
|----------|------|--------------|------------|-------------|
| `acceso_cuarto_roxy` | `bool` | `False` | Afecto Roxy ≥ 20 | Puede entrar al cuarto de Roxy |
| `acceso_cuarto_celine` | `bool` | `False` | Afecto Celine ≥ 35 | Puede entrar al cuarto de Celine |
| `acceso_cuarto_luna` | `bool` | `False` | Afecto Luna ≥ 45 | Puede entrar al cuarto de Luna |

---

## 8. PROGRESO — SECRETOS
**Módulo responsable:** `secrets.rpy`
**Keyword:** `default`
**Regla:** Una vez `True`, NUNCA vuelve a `False`.

| Variable | Tipo | Valor inicial | Descripción |
|----------|------|--------------|-------------|
| `sec_celine_1` | `bool` | `False` | Diario de Celine descubierto |
| `sec_celine_2` | `bool` | `False` | Conversación Celine-Roxy escuchada |
| `sec_celine_3` | `bool` | `False` | Celine encontrada llorando |
| `sec_roxy_1` | `bool` | `False` | Bocetos del sketchbook vistos |
| `sec_roxy_2` | `bool` | `False` | Fotos de Roxy encontradas |
| `sec_roxy_3` | `bool` | `False` | Conversación Roxy-Luna escuchada |
| `sec_luna_1` | `bool` | `False` | Página del cuaderno de Luna vista |
| `sec_luna_2` | `bool` | `False` | Cartas de Luna encontradas |
| `sec_luna_3` | `bool` | `False` | Luna encontrada llorando |

---

## 9. PROGRESO — ACTOS NARRATIVOS
**Módulo responsable:** cada personaje en su `*_events.rpy`
**Keyword:** `default`
**Regla:** Una vez `True`, NUNCA vuelve a `False`.

| Variable | Tipo | Valor inicial | Módulo | Descripción |
|----------|------|--------------|--------|-------------|
| `ev_celine_acto1_done` | `bool` | `False` | celine_events.rpy | Acto 1 Celine completado |
| `ev_celine_acto2_done` | `bool` | `False` | celine_events.rpy | Acto 2 Celine completado |
| `ev_celine_acto3_done` | `bool` | `False` | celine_events.rpy | Acto 3 Celine completado |
| `ev_celine_acto4_done` | `bool` | `False` | celine_events.rpy | Acto 4 Celine completado |
| `ev_celine_acto5_done` | `bool` | `False` | celine_events.rpy | Acto 5 Celine completado |
| `ev_roxy_acto1_done` | `bool` | `False` | roxy_events.rpy | Acto 1 Roxy completado |
| `ev_roxy_acto2_done` | `bool` | `False` | roxy_events.rpy | Acto 2 Roxy completado |
| `ev_roxy_acto3_done` | `bool` | `False` | roxy_events.rpy | Acto 3 Roxy completado |
| `ev_roxy_acto4_done` | `bool` | `False` | roxy_events.rpy | Acto 4 Roxy completado |
| `ev_roxy_acto5_done` | `bool` | `False` | roxy_events.rpy | Acto 5 Roxy completado |
| `ev_luna_acto1_done` | `bool` | `False` | luna_events.rpy | Acto 1 Luna completado |
| `ev_luna_acto2_done` | `bool` | `False` | luna_events.rpy | Acto 2 Luna completado |
| `ev_luna_acto3_done` | `bool` | `False` | luna_events.rpy | Acto 3 Luna completado |
| `ev_luna_acto4_done` | `bool` | `False` | luna_events.rpy | Acto 4 Luna completado |
| `ev_luna_acto5_done` | `bool` | `False` | luna_events.rpy | Acto 5 Luna completado |

---

## 10. PROGRESO — QUESTS
**Módulo responsable:** cada personaje en su `*_events.rpy`
**Keyword:** `default`

| Variable | Tipo | Valor inicial | Módulo | Quest |
|----------|------|--------------|--------|-------|
| `quest_celine_1_done` | `bool` | `False` | celine_events.rpy | Los apuntes |
| `quest_celine_2_done` | `bool` | `False` | celine_events.rpy | La defensa |
| `quest_celine_3_done` | `bool` | `False` | celine_events.rpy | El diario |
| `quest_roxy_1_done` | `bool` | `False` | roxy_events.rpy | El sketchbook |
| `quest_roxy_2_done` | `bool` | `False` | roxy_events.rpy | La exposición |
| `quest_roxy_3_done` | `bool` | `False` | roxy_events.rpy | La noche que llora |
| `quest_luna_1_done` | `bool` | `False` | luna_events.rpy | El libro |
| `quest_luna_2_done` | `bool` | `False` | luna_events.rpy | Tres días de silencio |
| `quest_luna_3_done` | `bool` | `False` | luna_events.rpy | El mismo libro |

---

## 11. ITEMS DEL JUGADOR
**Módulo responsable:** `economy.rpy`
**Keyword:** `default`

| Variable | Tipo | Valor inicial | Costo | Descripción |
|----------|------|--------------|-------|-------------|
| `item_camara` | `bool` | `False` | $150 | Cámara compacta — habilita mecánica de fotos |

*(Expandir en Fase 4 cuando se implemente la tienda completa)*

---

## 12. MEMORIA DE DECISIONES
**Módulo responsable:** `script.rpy`
**Keyword:** `default`
**⚠ ADVERTENCIA CRÍTICA — LEER ANTES DE IMPLEMENTAR:**
Según la doc oficial de Ren'Py: cambiar un objeto (lista) no activa el guardado automático,
solo cambia la variable sí misma.
**Patrón obligatorio:** `$ mem_decisiones = mem_decisiones + ["nueva_decision"]`
NUNCA usar `.append()` directamente.

| Variable | Tipo | Valor inicial | Límite | Descripción |
|----------|------|--------------|--------|-------------|
| `mem_decisiones` | `list` | `[]` | 20 items | Strings con decisiones clave para diálogos futuros |

---

## 13. GALERÍA
**Módulo responsable:** `gallery.rpy`
**Keyword:** `persistent` (sobrevive entre partidas distintas)
**Fuente doc:** renpy.org/doc/html/persistent.html

**Diferencia crítica con otras variables:**
La galería usa `persistent` porque debe estar disponible en el menú principal,
independientemente de qué partida se cargue.

| Variable | Tipo | Valor inicial | Descripción |
|----------|------|--------------|-------------|
| `persistent.galeria_escenas` | `list` | `None` → inicializar con `default` | Escenas CG desbloqueadas |
| `persistent.galeria_fotos` | `list` | `None` → inicializar con `default` | Fotos coleccionables obtenidas |

**Declaración correcta:**
```renpy
default persistent.galeria_escenas = []
default persistent.galeria_fotos = []
```

**Patrón obligatorio de escritura (misma regla de listas):**
```renpy
$ persistent.galeria_escenas = persistent.galeria_escenas + ["id_escena"]
```

---

## 14. FLAGS DE SESIÓN (NO SE GUARDAN — SOLO DURAN UN ARRANQUE)
**Módulo responsable:** varios
**Keyword:** `define` o variables en `init python:`
**⚠ Estas variables NO se guardan en saves. Se resetean cada vez que el juego arranca.**

| Variable | Tipo | Valor inicial | Descripción |
|----------|------|--------------|-------------|
| `DEBUG_MODE` | `bool` | `False` | Activa logs en consola durante desarrollo |

---

## RESUMEN DE DECLARACIONES POR ARCHIVO

### stats.rpy — declarar con `default`:
```
stats_celine_afecto, stats_celine_confianza, stats_celine_corrupcion
stats_roxy_afecto, stats_roxy_confianza, stats_roxy_corrupcion
stats_luna_afecto, stats_luna_confianza, stats_luna_corrupcion
prot_nombre, prot_encanto, prot_energia_max, prot_energia_actual, prot_dinero
pers_romantico, pers_atrevido, pers_respetuoso
acceso_cuarto_roxy, acceso_cuarto_celine, acceso_cuarto_luna
```

### time.rpy — declarar con `default`:
```
time_dia, time_franja, time_dia_semana, time_es_finde, time_total_franjas
```

### mood.rpy — declarar con `default`:
```
mood_celine, mood_roxy, mood_luna
```

### jealousy.rpy — declarar con `default`:
```
apt_armonia
celos_celine_activo, celos_roxy_activo, celos_luna_activo
celos_celine_intensidad, celos_roxy_intensidad, celos_luna_intensidad
```

### secrets.rpy — declarar con `default`:
```
sec_celine_1/2/3, sec_roxy_1/2/3, sec_luna_1/2/3
```

### celine_events.rpy — declarar con `default`:
```
ev_celine_acto1_done ... ev_celine_acto5_done
quest_celine_1_done, quest_celine_2_done, quest_celine_3_done
```

### roxy_events.rpy — declarar con `default`:
```
ev_roxy_acto1_done ... ev_roxy_acto5_done
quest_roxy_1_done, quest_roxy_2_done, quest_roxy_3_done
```

### luna_events.rpy — declarar con `default`:
```
ev_luna_acto1_done ... ev_luna_acto5_done
quest_luna_1_done, quest_luna_2_done, quest_luna_3_done
```

### economy.rpy — declarar con `default`:
```
item_camara
```

### script.rpy — declarar con `default`:
```
mem_decisiones
```

### gallery.rpy — declarar con `default persistent.`:
```
persistent.galeria_escenas, persistent.galeria_fotos
```
