# APARTMENT SIM — VARIABLES GLOBALES
### Versión: BORRADOR — El Arquitecto debe completar y verificar con documentación oficial
### Ren'Py: 8.5.3 | Python: 3.12
### Última actualización: 30/05/2026

---

## INSTRUCCIÓN PARA EL ARQUITECTO
Este archivo es un borrador base. Tu trabajo es:
1. Verificar cada variable contra la documentación de Ren'Py 8.5.3
2. Agregar las que falten
3. Definir los tipos correctos según Python 3.12
4. Crear el archivo stats.rpy base con los `default` statements
5. Documentar qué módulo es responsable de modificar cada variable

---

## 1. STATS POR PERSONAJE

| Variable | Tipo | Valor inicial | Rango | Módulo responsable | Descripción |
|----------|------|--------------|-------|-------------------|-------------|
| stats_celine_afecto | int | 15 | 0-100 | stats.rpy | Afecto hacia el protagonista |
| stats_celine_confianza | int | 10 | 0-100 | stats.rpy | Confianza en el protagonista |
| stats_celine_corrupcion | int | 5 | 0-100 | stats.rpy | Nivel de corrupción |
| stats_roxy_afecto | int | 25 | 0-100 | stats.rpy | Afecto hacia el protagonista |
| stats_roxy_confianza | int | 15 | 0-100 | stats.rpy | Confianza en el protagonista |
| stats_roxy_corrupcion | int | 15 | 0-100 | stats.rpy | Nivel de corrupción |
| stats_luna_afecto | int | 20 | 0-100 | stats.rpy | Afecto hacia el protagonista |
| stats_luna_confianza | int | 10 | 0-100 | stats.rpy | Confianza en el protagonista |
| stats_luna_corrupcion | int | 10 | 0-100 | stats.rpy | Nivel de corrupción |

---

## 2. STATS DEL PROTAGONISTA

| Variable | Tipo | Valor inicial | Rango | Módulo responsable | Descripción |
|----------|------|--------------|-------|-------------------|-------------|
| prot_nombre | str | "Kai" | — | script.rpy | Nombre elegido por el jugador |
| prot_encanto | int | 10 | 0-100 | stats.rpy | Mejora opciones de diálogo |
| prot_energia_max | int | 6 | 6-10 | stats.rpy | Acciones máximas por franja |
| prot_energia_actual | int | 6 | 0-prot_energia_max | time.rpy | Acciones disponibles hoy |
| prot_dinero | int | 500 | 0-∞ | economy.rpy | Dinero disponible |

---

## 3. PERSONALIDAD DEL JUGADOR

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| pers_romantico | int | 0 | stats.rpy | Puntos arquetipo romántico |
| pers_atrevido | int | 0 | stats.rpy | Puntos arquetipo atrevido |
| pers_respetuoso | int | 0 | stats.rpy | Puntos arquetipo respetuoso |

---

## 4. SISTEMA DE TIEMPO

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| time_dia | int | 1 | time.rpy | Día actual del juego |
| time_franja | str | "manana" | time.rpy | Franja actual: manana/tarde/noche/madrugada |
| time_dia_semana | str | "lunes" | time.rpy | Día de la semana |
| time_es_finde | bool | False | time.rpy | True si es sábado o domingo |

---

## 5. ESTADO DE ÁNIMO DIARIO

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| mood_celine | str | "normal" | mood.rpy | normal/feliz/cansada/estresada/traviesa |
| mood_roxy | str | "normal" | mood.rpy | normal/feliz/cansada/estresada/traviesa |
| mood_luna | str | "normal" | mood.rpy | normal/feliz/cansada/estresada/traviesa |

---

## 6. ARMONÍA Y CELOS

| Variable | Tipo | Valor inicial | Rango | Módulo responsable | Descripción |
|----------|------|--------------|-------|-------------------|-------------|
| apt_armonia | int | 70 | 0-100 | jealousy.rpy | Armonía global del apartamento |
| celos_celine_activo | bool | False | jealousy.rpy | True si Celine tiene celos activos |
| celos_roxy_activo | bool | False | jealousy.rpy | True si Roxy tiene celos activos |
| celos_luna_activo | bool | False | jealousy.rpy | True si Luna tiene celos activos |

---

## 7. PROGRESO — SECRETOS

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| sec_celine_1 | bool | False | secrets.rpy | Diario descubierto |
| sec_celine_2 | bool | False | secrets.rpy | Conversación con Roxy escuchada |
| sec_celine_3 | bool | False | secrets.rpy | La encontraste llorando |
| sec_roxy_1 | bool | False | secrets.rpy | Bocetos en sketchbook vistos |
| sec_roxy_2 | bool | False | secrets.rpy | Fotos encontradas |
| sec_roxy_3 | bool | False | secrets.rpy | Conversación con Luna escuchada |
| sec_luna_1 | bool | False | secrets.rpy | Página del cuaderno vista |
| sec_luna_2 | bool | False | secrets.rpy | Cartas encontradas |
| sec_luna_3 | bool | False | secrets.rpy | La encontraste llorando |

---

## 8. PROGRESO — ACTOS NARRATIVOS

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| ev_celine_acto1_done | bool | False | celine_events.rpy | Acto 1 completado |
| ev_celine_acto2_done | bool | False | celine_events.rpy | Acto 2 completado |
| ev_celine_acto3_done | bool | False | celine_events.rpy | Acto 3 completado |
| ev_celine_acto4_done | bool | False | celine_events.rpy | Acto 4 completado |
| ev_celine_acto5_done | bool | False | celine_events.rpy | Acto 5 completado |
| ev_roxy_acto1_done | bool | False | roxy_events.rpy | Acto 1 completado |
| ev_roxy_acto2_done | bool | False | roxy_events.rpy | Acto 2 completado |
| ev_roxy_acto3_done | bool | False | roxy_events.rpy | Acto 3 completado |
| ev_roxy_acto4_done | bool | False | roxy_events.rpy | Acto 4 completado |
| ev_roxy_acto5_done | bool | False | roxy_events.rpy | Acto 5 completado |
| ev_luna_acto1_done | bool | False | luna_events.rpy | Acto 1 completado |
| ev_luna_acto2_done | bool | False | luna_events.rpy | Acto 2 completado |
| ev_luna_acto3_done | bool | False | luna_events.rpy | Acto 3 completado |
| ev_luna_acto4_done | bool | False | luna_events.rpy | Acto 4 completado |
| ev_luna_acto5_done | bool | False | luna_events.rpy | Acto 5 completado |

---

## 9. PROGRESO — QUESTS

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| quest_celine_1_done | bool | False | celine_events.rpy | Quest Los apuntes completada |
| quest_celine_2_done | bool | False | celine_events.rpy | Quest La defensa completada |
| quest_celine_3_done | bool | False | celine_events.rpy | Quest El diario completada |
| quest_roxy_1_done | bool | False | roxy_events.rpy | Quest El sketchbook completada |
| quest_roxy_2_done | bool | False | roxy_events.rpy | Quest La exposición completada |
| quest_roxy_3_done | bool | False | roxy_events.rpy | Quest La noche que llora completada |
| quest_luna_1_done | bool | False | luna_events.rpy | Quest El libro completada |
| quest_luna_2_done | bool | False | luna_events.rpy | Quest Tres días de silencio completada |
| quest_luna_3_done | bool | False | luna_events.rpy | Quest El mismo libro completada |

---

## 10. ACCESO A CUARTOS
(Una vez True, permanece True para siempre)

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| acceso_cuarto_roxy | bool | False | stats.rpy | Desbloqueado con Afecto Roxy ≥20 |
| acceso_cuarto_celine | bool | False | stats.rpy | Desbloqueado con Afecto Celine ≥35 |
| acceso_cuarto_luna | bool | False | stats.rpy | Desbloqueado con Afecto Luna ≥45 |

---

## 11. ITEMS DEL JUGADOR

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| item_camara | bool | False | economy.rpy | Tiene cámara compacta ($150) |

---

## 12. MEMORIA DE DECISIONES
(Lista de hasta 20 decisiones importantes)

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| mem_decisiones | list | [] | script.rpy | Lista de strings con decisiones clave |

---

## 13. GALERÍA

| Variable | Tipo | Valor inicial | Módulo responsable | Descripción |
|----------|------|--------------|-------------------|-------------|
| galeria_escenas | list | [] | gallery.rpy | Escenas desbloqueadas |
| galeria_fotos | list | [] | gallery.rpy | Fotos coleccionables obtenidas |

---

## NOTAS PARA EL ARQUITECTO

1. Todas estas variables van en `default` statements en `stats.rpy` o su módulo correspondiente
2. Las variables `bool` de progreso deben ser `default` (no `define`) para que se guarden
3. `prot_nombre` necesita manejo especial — se define después del input del jugador
4. Las listas (`mem_decisiones`, `galeria_escenas`, etc.) necesitan consideración especial 
   para saves en Ren'Py — verificar documentación de save/load/rollback
5. Verificar en https://www.renpy.org/doc/html/python.html la sección de variables y saves
6. Python 3.12 en Ren'Py 8.5.3 — verificar compatibilidad de tipos
