import streamlit as st
import json
import pandas as pd
from core.calendar_engine import optimizar_calendario

def render_optimizador():
    st.subheader("📆 Módulo 2: Optimizador de Calendario Escolar (Vista del Director)")
    st.write("Configura el almanaque del bimestre de forma flexible y compacta las clases automáticamente.")
    
    # 1. CARGAR TEMARIOS DESDE EL JSON
    try:
        with open("data/cneb_base.json", "r", encoding="utf-8") as f:
            banco_temarios = json.load(f)
    except Exception as e:
        st.error("No se pudo cargar el banco de temarios.")
        banco_temarios = {"Matemática": []}

    st.divider()

    # 2. SELECTOR DE CURSO
    st.write("📋 **1. Selección de Área Académica:**")
    curso_elegido = st.selectbox("¿Qué curso deseas reorganizar hoy?", list(banco_temarios.keys()))
    temas_profesor = banco_temarios[curso_elegido]
        
    st.divider()
    
    # 3. TABLA INTERACTIVA TIPO EXCEL (CON LLAVE DE ESTABILIZACIÓN)
    st.write("🛠️ **2. Agenda de Suspensiones del Colegio (Feriados, Actuaciones, Aniversarios):**")
    st.write("Modifica o añade filas en la tabla de abajo para registrar las fechas donde no habrá clases:")

    datos_iniciales_feriados = [
        {"Semana": "Semana 3", "Motivo": "Día de la Madre"},
        {"Semana": "Semana 6", "Motivo": "Aniversario del Colegio"},
    ]
    
    # Agregamos 'key=f"editor_{curso_elegido}"' para que el navegador se limpie correctamente
    tabla_editable = st.data_editor(
        datos_iniciales_feriados, 
        num_rows="dynamic",
        use_container_width=True,
        key=f"editor_{curso_elegido}",
        column_config={
            "Semana": st.column_config.SelectboxColumn(
                "Semana Afectada",
                options=[f"Semana {i}" for i in range(1, 9)],
                required=True
            ),
            "Motivo": st.column_config.TextColumn(
                "Nombre de la Festividad / Razón",
                required=True
            )
        }
    )
    
    st.divider()
    
    # 4. PROCESAR LOS DATOS DE LA TABLA EDITABLE
    festividades_mapeadas = {}
    for fila in tabla_editable:
        if isinstance(fila, dict) and fila.get("Semana") and fila.get("Motivo"):
            festividades_mapeadas[fila["Semana"]] = fila["Motivo"]
    
    # 5. BOTÓN PARA RECALCULAR
    if st.button("🔄 Optimizar y Compactar Calendario Escolar", use_container_width=True):
        resultado_tabla = optimizar_calendario(temas_profesor, festividades_mapeadas)
        
        st.success(f"¡Calendario de **{curso_elegido}** recalculado de forma inteligente!")
        st.dataframe(resultado_tabla, use_container_width=True)