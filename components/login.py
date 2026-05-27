import streamlit as st

def render_login():
    """
    Dibuja una pantalla de inicio de sesión elegante.
    Retorna el rol del usuario ('director', 'profesor') si el ingreso es correcto.
    """
    st.markdown("<h2 style='text-align: center;'>🔐 Acceso al Sistema Escolar SaaS</h2>", unsafe_allow_html=True)
    st.write("Introduce tus credenciales simuladas de prueba para acceder a tu panel correspondiente.")
    
    # Creamos un contenedor visual centrado para el formulario
    with st.container(border=True):
        usuario = st.text_input("Correo electrónico o Usuario:", placeholder="ejemplo@colegio.edu.pe")
        contrasena = st.text_input("Contraseña:", type="password", placeholder="••••••••")
        
        st.write("💡 *Cuentas de prueba para el MVP:*")
        st.caption("• Para entrar como Director usa: **director** / **123**")
        st.caption("• Para entrar como Profesor usa: **profesor** / **123**")
        
        st.divider()
        
        # Botón de ingreso
        if st.button("Ingresar a la Plataforma", use_container_width=True):
            if usuario == "director" and contrasena == "123":
                st.success("¡Acceso concedido como Director!")
                return "director"
            elif usuario == "profesor" and contrasena == "123":
                st.success("¡Acceso concedido como Profesor!")
                return "profesor"
            else:
                st.error("Credenciales incorrectas. Inténtalo de nuevo.")
                return None
    return None