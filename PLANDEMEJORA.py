

import streamlit as st
import requests
import random

# Info de la API
API_KEY = ("sk-57fdc94aa828429aad3d0ac614dcbc36")
API_URL = "https://api.deepseek.com/v1/chat/completions"

# Instrucciones del asistente
SYSTEM_PROMPT = """
Eres un asistente educativo especializado únicamente en:

- Ingeniería Aeroespacial
- CubeSats
- Satélites
- Redes espaciales
- Comunicaciones satelitales
- Redes de a bordo
- IoT espacial
- IPv4 e IPv6
- Modelo OSI aplicado al entorno espacial
- Estaciones terrenas
- Constelaciones satelitales
- DTN (Delay Tolerant Networking)
- Protocolos CCSDS
- Telemetría y telecontrol
- Bandas VHF/UHF, S, X o Ka

Normas:

1. Solo puedes responder preguntas relacionadas con estos temas.
2. Si la pregunta no pertenece al área aeroespacial, debes rechazarla educadamente.
3. Responde de forma clara y argumentativa.
4. Utiliza ejemplos cuando sea apropiado.
5. Mantén respuestas cortas y completas para optimizar el consumo de tokens.
6. Limita cada respuesta a aproximadamente 150 palabras brindandolas completas.
"""
#Cosnsumo de tokens
MAX_HISTORIAL = 10
MAX_TOKENS = 200


def preguntar_deepseek(mensaje, historial):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    mensajes = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    mensajes.extend(historial)

    mensajes.append(
        {
            "role": "user",
            "content": mensaje
        }
    )

    payload = {
        "model": "deepseek-chat",
        "messages": mensajes,
        "temperature": 0.3,
        "max_tokens": MAX_TOKENS
    }

    try:

        respuesta = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        respuesta.raise_for_status()

        return respuesta.json()["choices"][0]["message"]["content"]

    except Exception as error:
        return f"Error: {error}"


st.set_page_config(
    page_title="Asistente Educativo Aeroespacial",
    page_icon="🛰️",
    layout="wide"
)

# Diseño visual de la pagina
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background:
    linear-gradient(
        rgba(0,0,0,0.70),
        rgba(0,0,0,0.70)
    ),
    url("https://wallpapercave.com/wp/wp8860763.jpg");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stSidebar"] {
    background:
    linear-gradient(
        rgba(3,10,30,0.45),
        rgba(3,10,30,0.45)
    ),
    url("https://i.pinimg.com/736x/cf/93/93/cf9393c5f65270f2ab8de051ab2e8609.jpg");

    background-size: cover;
    background-position: center;
}

h1, h2, h3 {
    color: white !important;
}

p, label {
    color: #d9e6ff !important;
}

.stTextInput input {
    background-color: rgba(0,0,0,0.80);
    color: white !important;
}

.stButton button {
    background-color: #1565c0;
    color: white;
    border-radius: 10px;
}

.stButton button:hover {
    background-color: #1976d2;
}

</style>
""", unsafe_allow_html=True)

# Encabezado
st.title("🛰️ Asistente Educativo de Ingeniería Aeroespacial")

st.image(
    "https://images-assets.nasa.gov/image/iss070e046860/iss070e046860~medium.jpg",
    use_container_width=True
)

st.caption(
    "Proyecto académico sobre CubeSats, comunicaciones espaciales, "
    "redes satelitales, IoT espacial e IPv6."
)

# Barra lateral
st.sidebar.title("Información del Proyecto")

st.sidebar.info("""
Temas principales:

• CubeSats

• Comunicaciones espaciales

• Constelaciones satelitales

• Modelo OSI

• IPv4 e IPv6

• IoT Espacial

• DTN

• Telemetría y Telecontrol
""")

# Pestañas
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🛰️ Asistente",
    "🌍 Constelación",
    "📡 Modelo OSI",
    "📊 Telemetría",
    "🚀 Arquitectura"
])

# ASISTENTE
with tab1:

    st.header("Asistente Educativo Aeroespacial")

    if "historial" not in st.session_state:
        st.session_state.historial = []

    pregunta = st.text_input(
        "Escribe una pregunta sobre Ingeniería Aeroespacial:"
    )

    if st.button("Consultar"):

        if pregunta:

            respuesta = preguntar_deepseek(
                pregunta,
                st.session_state.historial[-MAX_HISTORIAL:]
            )

            st.session_state.historial.append(
                {
                    "role": "user",
                    "content": pregunta
                }
            )

            st.session_state.historial.append(
                {
                    "role": "assistant",
                    "content": respuesta
                }
            )

            st.subheader("Respuesta")
            st.write(respuesta)

# CONSTELACIÓN
with tab2:

    st.header("Constelación de CubeSats en Órbita LEO")

    cantidad = st.slider(
        "Cantidad de CubeSats",
        min_value=3,
        max_value=12,
        value=5
    )

    for i in range(cantidad):

        ancho_banda = random.randint(20, 100)
        jitter = random.randint(1, 25)
        throughput = random.randint(15, ancho_banda)
        latencia = random.randint(50, 300)

        st.info(
            f"""
🛰️ SAT-{i+1}

Ancho de banda: {ancho_banda} Mbps

Jitter: {jitter} ms

Throughput: {throughput} Mbps

Latencia: {latencia} ms

IPv6: Activo
"""
        )

# MODELO OSI
with tab3:

    st.header("Modelo OSI Aplicado a CubeSats")

    st.markdown("""
### Capa Física
Bandas VHF, UHF, S y X.

### Capa de Enlace
Protocolos AX.25 y CCSDS.

### Capa de Red
IPv4, IPv6 y DTN.

### Capa de Transporte
TCP, UDP y SCPS-TP.

### Capa de Sesión
Gestión de contactos orbitales.

### Capa de Presentación
Compresión, codificación y cifrado.

### Capa de Aplicación
Telemetría, telecontrol y transmisión de imágenes.
""")

# TELEMETRÍA
with tab4:

    st.header("Monitor de Comunicaciones")

    st.metric(
        "Ancho de Banda",
        f"{random.randint(50,100)} Mbps"
    )

    st.metric(
        "Jitter",
        f"{random.randint(1,20)} ms"
    )

    st.metric(
        "Throughput",
        f"{random.randint(40,90)} Mbps"
    )

    st.metric(
        "Pérdida de Paquetes",
        f"{random.uniform(0,3):.2f}%"
    )

    st.success(
        "Valores simulados para una red de CubeSats."
    )

# ARQUITECTURA
with tab5:

    st.header("Arquitectura de Comunicación Espacial")

    st.markdown("""
### Flujo de Comunicación

CubeSat → Constelación → Satélite Relay → Estación Terrena → Centro de Control

### Tecnologías Utilizadas

- IPv6
- DTN
- TCP/IP
- UDP
- CCSDS

### Parámetros de Red

- Throughput
- Jitter
- Latencia
- Pérdida de paquetes

### Objetivo

Simular el intercambio de información entre CubeSats y una estación terrena utilizando conceptos de redes espaciales e Internet de las Cosas (IoT).
""")
