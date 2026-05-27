import os
from dotenv import load_dotenv
from google import genai

# Cargamos la llave secreta
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Inicializamos el cliente de IA
client = genai.Client(api_key=api_key)

def generar_sesion_cneb(grado, curso, tema):
    """
    Función mejorada con Prompt Engineering Avanzado.
    Fuerza a Gemini a entregar formatos consistentes, tablas y dinámicas de alto impacto.
    """
    
    prompt = f"""
    Actúa como un Diseñador Pedagógico de Élite, experto en el Currículo Nacional de la Educación Básica (CNEB) del MINEDU Perú, con un enfoque moderno, ágil e innovador, opuesto a la educación tradicional memorística.
    
    Tu objetivo es crear una sesión de aprendizaje para:
    - Grado: {grado}
    - Curso/Área: {curso}
    - Tema: {tema}
    
    Debes estructurar tu respuesta de forma obligatoria siguiendo este formato EXACTO en Markdown. No improvises otros títulos:
    
    # SESIÓN DE APRENDIZAJE: {tema}
    
    ## 1. DATOS INFORMATIVOS
    * **Grado:** {grado}
    * **Área:** {curso}
    * **Tema del día:** {tema}
    * **Duración:** 90 minutos (45 min de teoría/organización + 45 min de proyecto práctico)
    
    ## 2. PROPÓSITOS DE APRENDIZAJE (Formato Tabla)
    Presenta esta sección ÚNICAMENTE en una tabla con las siguientes columnas:
    | Competencia CNEB | Capacidades | Desempeño Precajonado/Precisado | Evidencia de Aprendizaje |
    | :--- | :--- | :--- | :--- |
    | (Inserta la competencia oficial del CNEB para este curso) | (Inserta las capacidades que se movilizan) | (El desempeño adaptado al tema '{tema}') | (Qué producto o acción medible hará el alumno) |
    
    ## 3. SECUENCIA PEDAGÓGICA (Los 90 minutos)
    * **Inicio (15 min):** Motivación (¡Prohibido empezar dictando!), recuperación de saberes previos y conflicto cognitivo usando un dilema o caso real.
    * **Desarrollo (20 min):** Gestión y acompañamiento del conocimiento básico necesario. Explicación ágil y participativa.
    * **Cierre (10 min):** Metacognición (¿Qué aprendimos hoy? ¿Para qué nos sirve en la vida real?) y evaluación rápida.
    
    ## 4. PROYECTO PRÁCTICO "CERO TAREAS VACÍAS" (45 minutos)
    Diseña un reto innovador para realizar por completo DENTRO del aula (en equipos). 
    
    **REGLAS ESTRICTAS PARA EL PROYECTO:**
    1. **Contexto Peruano Actual:** Debe conectar con los intereses de un adolescente de {grado} en el Perú de hoy (ej. crear un micro-emprendimiento, usar analítica de TikTok/Instagram, resolver un problema de tráfico/basura de su distrito, gamificación con dinámicas de retos, etc.).
    2. **Estructura del Proyecto:**
       * **Nombre del Reto:** (Un nombre atractivo).
       * **Misión:** (Qué deben resolver en 45 minutos).
       * **Reglas del Juego:** (Instrucciones claras para evitar que las bromas desvíen el aprendizaje. El juego TIENE que obligar a usar el tema '{tema}' para poder ganar).
       * **Entregable final:** (Qué le presentan al profesor al sonar el timbre).
    
    Genera la respuesta directamente en texto Markdown limpio, sin introducciones ni comentarios adicionales fuera de la estructura.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Error al conectar con la IA: {str(e)}"