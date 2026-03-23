
# ── Tu reporte clínico — responde al menos 2 preguntas ────────────────────
# Usa los comentarios de la celda anterior como guía si te quedas en blanco.
# Reporte clínico 
# Pregunta 1: Que sintoma aparece asociado a más enfermedades distintas?

for sintoma, cantidad in conteo_sintomas.items():
    enfermedades_con_sintoma = set()
    for p in pacientes:
        if sintoma in p["sintomas"]:
            enfermedades_con_sintoma.add(p["enfermedad"])
    print(f"{sintoma:<25}: {len(enfermedades_con_sintoma)} enfermedades distintas")
    
# Pregunta 2: Cual es le top 5 de personas con más síntomas distintos?
pacientes_con_cantidad_sintomas = []
for p in pacientes[:5]:
    cantidad_sintomas = len(set(p["sintomas"]))
    pacientes_con_cantidad_sintomas.append((p["nombre"], cantidad_sintomas))