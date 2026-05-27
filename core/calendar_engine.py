import pandas as pd

def optimizar_calendario(temario_original, festividades_directores):
    """
    Recibe una lista de temas (temario) y una lista de semanas con feriados.
    Reorganiza el temario para que no se pierdan horas de clase.
    """
    # Creamos un calendario base de 8 semanas para el bimestre
    semanas = [f"Semana {i}" for i in range(1, 9)]
    
    # Creamos un diccionario (tabla) inicial relacionando cada semana con su tema
    cronograma = []
    tema_index = 0
    
    for semana in semanas:
        # Si el director marcó esta semana como festividad/actuación
        if semana in festividades_directores:
            evento = festividades_directores[semana]
            cronograma.append({
                "Semana": semana,
                "Estado": f"🚫 INTERRUMPIDA ({evento})",
                "Tema a Dictar": "No hay clases (Se recupera la siguiente semana)"
            })
        else:
            # Si hay clases, asignamos el tema correspondiente si aún quedan temas
            if tema_index < len(temario_original):
                cronograma.append({
                    "Semana": semana,
                    "Estado": "✅ Clase Efectiva",
                    "Tema a Dictar": temario_original[tema_index]
                })
                tema_index += 1
            else:
                cronograma.append({
                    "Semana": semana,
                    "Estado": "🎉 Temario Completado",
                    "Tema a Dictar": "Repaso o Evaluaciones finales"
                })
                
    # Convertimos los datos en una tabla de Pandas para manejarlo profesionalmente
    df_resultado = pd.DataFrame(cronograma)
    return df_resultado