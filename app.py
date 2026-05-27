import streamlit as st
from core.ia_engine import generar_sesion_cneb
from components.optimizador_cal import render_optimizador
from components.login import render_login

# Configuración global de la página
st.set_page_config(page_title="SaaS Educativo Perú", page_icon="🇵🇪", layout="wide")

# Inicializamos la memoria de sesión
if "rol_usuario" not in st.session_state:
    st.session_state["rol_usuario"] = None

# --- CONTROL DE FLUJO ---
if st.session_state["rol_usuario"] is None:
    rol_detectado = render_login()
    if rol_detectado:
        st.session_state["rol_usuario"] = rol_detectado
        st.rerun()

# Si el usuario ya está logueado
else:
    rol = st.session_state["rol_usuario"]
    
    # Barra lateral de navegación
    st.sidebar.title("🇵🇪 Menú Sistema")
    st.sidebar.write(f"Conectado como: **{rol.capitalize()}**")
    
    if rol == "director":
        opciones_menu = ["Dashboard Principal", "Módulo Directores (Calendario)"]
    else:
        opciones_menu = ["Dashboard Principal", "Módulo Profesores (IA)"]
        
    opcion_menu = st.sidebar.radio("Selecciona un Módulo:", opciones_menu, key="menu_navegacion")
    
    if st.sidebar.button("🚪 Cerrar Sesión"):
        st.session_state["rol_usuario"] = None
        st.rerun()

    st.divider()

    # --- CONTENEDORES INDEPENDIENTES PARA EVITAR EL ERROR DE JAVASCRIPT ---
    if opcion_menu == "Dashboard Principal":
        st.title("🏫 Panel de Control Escolar Inteligente")
        st.write(f"Bienvenido de nuevo al ecosistema SaaS. Tienes permisos de nivel: **{rol.upper()}**.")
        st.info("Utiliza el panel izquierdo para gestionar las herramientas activas de tu cuenta.")

    elif opcion_menu == "Módulo Profesores (IA)":
        st.title("🤖 Generador de Sesiones de Aprendizaje")
        col1, col2 = st.columns(2)
        with col1:
            grado_seleccionado = st.selectbox("Grado:", ["1° de Sec.", "2° de Sec.", "3° de Sec.", "4° de Sec.", "5° de Sec."])
        with col2:
            curso_seleccionado = st.selectbox("Curso:", ["Matemática", "Comunicación", "Ciencia y Tecnología"])
            
        tema_ingresado = st.text_input("Tema de la clase:")
        
        if st.button("✨ Generar Sesión Completa", use_container_width=True):
            if tema_ingresado.strip() == "":
                st.warning("Escribe un tema.")
            else:
                with st.spinner("Generando..."):
                    resultado_ia = generar_sesion_cneb(grado_seleccionado, curso_seleccionado, tema_ingresado)
                    st.markdown(resultado_ia)

    elif opcion_menu == "Módulo Directores (Calendario)":
        # Al meterlo en su propio bloque limpio, el renderizado no se cruzará con nada
        st.empty()
        render_optimizador()