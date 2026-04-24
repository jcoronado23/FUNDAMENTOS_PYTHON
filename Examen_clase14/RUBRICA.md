# Rúbrica Docente — Examen Final Caso Emisiones

**Examen asociado:** `EXAMEN_FINAL - Caso Emisiones ESTUDIANTE.ipynb`  
**Dataset asociado:** `Estimaciones_Emisiones_Dioxido_Carbono.csv`

## Escala fija

| Nivel | Valor |
|---|---:|
| No logrado | 0 |
| Inicial | 1 |
| Intermedio | 4 |
| Logrado | 5 |

### Regla de uso
- Cada criterio solo puede recibir `0`, `1`, `4` o `5`.
- No usar valores intermedios distintos.
- Redondear el puntaje final de cada bloque a `1 decimal`.

## Fórmula de conversión por bloque

`puntaje_bloque = (suma_criterios / puntaje_maximo_bruto) * puntaje_del_bloque`

## Definición operativa de la escala

- `0`: no hay evidencia suficiente o existe error conceptual grave.
- `1`: hay intento visible, pero incompleto, débil o parcialmente incorrecto.
- `4`: el criterio está mayormente logrado, con pequeñas debilidades o falta de profundidad.
- `5`: el criterio está cumplido con claridad, corrección y buena justificación.

---

## Bloque 1 — Comprensión del dataset (10 pts)

**Máximo bruto:** `20`

| Criterio | 0 | 1 | 4 | 5 |
|---|---|---|---|---|
| Carga y exploración básica del dataset | No carga el archivo o no muestra evidencia usable | Carga parcial o exploración incompleta | Carga correcta y muestra la mayoría de los elementos pedidos | Carga correcta y muestra todos los elementos pedidos con claridad |
| Identificación de estructura real del archivo | No reconoce columnas, años o tipos | Reconoce solo parte de la estructura | Describe correctamente la estructura general | Describe correctamente la estructura y la comunica con claridad |
| Explicación de diferencia entre total y per cápita | Confunde ambas métricas | Intuye la diferencia, pero la explica mal | Distingue correctamente ambas métricas | Distingue correctamente y lo expresa con precisión |
| Explicación del impacto analítico de esa diferencia | No explica impacto o lo hace de forma errónea | Explicación muy general | Explica por qué mezclar métricas afecta el análisis | Explica claramente el impacto y da una razón analítica defendible |

**Conversión:** `(suma / 20) * 10`

---

## Bloque 2 — Normalización y preparación analítica (10 pts)

**Máximo bruto:** `20`

| Criterio | 0 | 1 | 4 | 5 |
|---|---|---|---|---|
| Renombrar columnas al español correctamente | No renombra o renombra mal la mayoría | Renombra parcialmente | Renombra correctamente las columnas principales | Renombra correctamente y deja una estructura clara y consistente |
| Separar correctamente `df_totales_es` y `df_per_capita_es` | Filtra mal o mezcla métricas | Separa con errores menores o inconsistencias | Separa correctamente ambos subconjuntos | Separa correctamente y demuestra control claro del criterio de filtrado |
| Mostrar evidencia de preparación correcta | No muestra evidencia | Muestra evidencia insuficiente o confusa | Muestra columnas y shapes suficientes | Muestra evidencia clara y útil para validar la preparación |
| Reflexión sobre utilidad analítica de la normalización | No reflexiona o lo hace sin sentido | Reflexión superficial | Explica por qué ayuda al análisis | Explica con claridad cómo mejora legibilidad y evita errores analíticos |

**Conversión:** `(suma / 20) * 10`

---

## Bloque 3 — Python base (22 pts)

**Máximo bruto:** `30`

| Criterio | 0 | 1 | 4 | 5 |
|---|---|---|---|---|
| Construcción de `registros_totales` | No crea la estructura o es inutilizable | La crea con errores importantes | La crea correctamente | La crea correctamente y la usa con claridad en el bloque |
| Implementación de `resumen_pais(registros, pais)` | No funciona o no cumple lo pedido | Funciona parcialmente | Retorna la mayor parte de la información correcta | Retorna correctamente toda la información solicitada |
| Resolución de países únicos y máximo global | Respuestas ausentes o erróneas | Resuelve solo una parte | Resuelve correctamente la mayoría | Resuelve con precisión y sin inconsistencias |
| Resolución del caso Costa Rica | No obtiene el año correcto o no muestra procedimiento | Hay intento, pero con error de lógica | Resuelve correctamente | Resuelve correctamente con procedimiento claro |
| Construcción de `reporte_centroamerica_base` | No construye el reporte o es ilegible | Construcción parcial o con errores de estructura | Construye el reporte correctamente | Construye el reporte correctamente y con estructura muy clara |
| Comparación entre predicción inicial y evidencia | No compara o no hay relación con la evidencia | Comparación superficial | Compara la predicción con la evidencia de forma suficiente | Compara claramente intuición vs evidencia y extrae aprendizaje |

**Conversión:** `(suma / 30) * 22`

---

## Bloque 4 — Análisis con pandas (28 pts)

**Máximo bruto:** `35`

| Criterio | 0 | 1 | 4 | 5 |
|---|---|---|---|---|
| Respuestas analíticas con `df_totales_es` | No responde o responde mal la mayoría | Respuestas parciales | Responde correctamente la mayoría | Responde correctamente todas las pedidas |
| Respuesta del promedio per cápita 2005 | Ausente o incorrecta | Intento parcial | Correcta | Correcta y presentada con claridad |
| Construcción de `reporte_total_centroamerica` | No existe o está mal agrupado | Construcción parcial | Construcción correcta | Construcción correcta y bien presentada |
| Construcción de `reporte_promedio_centroamerica` | No existe o está mal agrupado | Construcción parcial | Construcción correcta | Construcción correcta y bien presentada |
| Construcción de `conversiones_costa_rica` | No existe o tiene errores graves de conversión | Existe, pero con errores parciales | Tabla correcta | Tabla correcta, clara y consistente |
| Implementación de `comparar_paises(df, paises)` | No funciona o no filtra bien | Funciona parcialmente | Funciona correctamente | Funciona correctamente y deja resultado listo para comparar |
| Redacción de `contraste_metricas` | Confunde métricas o no usa evidencia | Explicación superficial | Contraste correcto con al menos un ejemplo | Contraste claro, correcto y bien sustentado con evidencia |

**Conversión:** `(suma / 35) * 28`

---

## Bloque 5 — Visualización (10 pts)

**Máximo bruto:** `25`

| Criterio | 0 | 1 | 4 | 5 |
|---|---|---|---|---|
| Gráfico de líneas | Ausente o ilegible | Presente pero incompleto | Correcto | Correcto, claro y bien rotulado |
| Gráfico de barras | Ausente o ilegible | Presente pero incompleto | Correcto | Correcto, claro y bien rotulado |
| Lectura del gráfico 1 | Ausente o incoherente | Muy superficial | Lectura adecuada | Lectura clara y pertinente |
| Lectura del gráfico 2 | Ausente o incoherente | Muy superficial | Lectura adecuada | Lectura clara y pertinente |
| Interpretación conjunta | No interpreta o lo hace sin relación con los gráficos | Interpretación débil | Interpretación suficiente | Interpretación sólida y conectada al análisis |

**Conversión:** `(suma / 25) * 10`

---

## Bloque 6 — Informe final crítico (20 pts)

**Máximo bruto:** `30`

| Criterio | 0 | 1 | 4 | 5 |
|---|---|---|---|---|
| Dos hallazgos numéricos concretos | No hay cifras o son irrelevantes | Hay una cifra o ambas son débiles | Presenta dos hallazgos numéricos suficientes | Presenta dos hallazgos numéricos claros y bien conectados |
| Limitación real del análisis | Ausente o incorrecta | Muy general | Identifica una limitación real | La explica con claridad y pertinencia |
| Comparación explícita entre total y per cápita | Ausente o confundida | Muy superficial | Comparación correcta | Comparación clara, precisa y analíticamente útil |
| Conclusión final | Ausente o desconectada | Débil o vaga | Conclusión coherente | Conclusión clara y bien sostenida |
| Recomendación o advertencia final | Ausente o sin relación con los datos | Muy general | Relacionada con los resultados | Relacionada con los resultados y bien justificada |
| Coherencia global del informe con la evidencia previa | No hay coherencia | Coherencia parcial | Coherencia suficiente | Integración clara de todo el análisis |

**Conversión:** `(suma / 30) * 20`

---

## Reglas transversales para el docente

- Usar `0` solo cuando falte evidencia suficiente o haya error conceptual importante.
- Usar `1` cuando el estudiante muestre camino correcto pero incompleto.
- Usar `4` cuando el criterio esté sustancialmente bien, aunque no perfecto.
- Usar `5` cuando el criterio esté claramente logrado.
- Dar crédito parcial al razonamiento correcto aunque el resultado final no sea exacto.
- Penalizar fuerte solo estos errores conceptuales:
  - confundir emisiones totales con per cápita,
  - usar mal la métrica en conclusiones,
  - informar sin evidencia numérica,
  - producir gráficos sin sentido analítico.
- No sobrepenalizar errores menores de estilo o nombre si la lógica está clara, salvo cuando el nombre exigido sea necesario para revisar.

## Cierre

Esta pauta busca que la corrección sea más consistente entre docentes y que cada nivel de desempeño tenga evidencia observable en el trabajo del estudiante.
