import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from edge_impulse_linux.runner import ImpulseRunner

# =======================
# CONFIGURACIÓN STREAMLIT
# =======================
st.set_page_config(
    page_title="BioGest EMG – Clasificación de Gestos",
    page_icon="🧠",
    layout="centered"
)

# ===== ESTILO (corregido para modo oscuro) =====
st.markdown("""
<style>
.big-title {
    font-size: 32px;
    text-align: center;
    font-weight: bold;
    color: #b8a8ff;
    margin-bottom: 0.3rem;
}
.sub-title {
    text-align: center;
    color: #dddddd;
    margin-bottom: 1.5rem;
}
.card {
    padding: 0.9rem 1rem;
    border-radius: 0.8rem;
    border: 1px solid #6e6e8a;
    background-color: rgba(255,255,255,0.08);
    color: #ffffff;
    font-size: 0.95rem;
    line-height: 1.35rem;
}
</style>
""", unsafe_allow_html=True)

# =======================
# CABECERA / INTRO
# =======================
st.markdown('<p class="big-title">BioGest EMG – Seguimiento motor post-ictus</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-title">'
    'Esta herramienta permite cargar ventanas de señal EMG de antebrazo y clasificarlas en tres gestos: '
    '<b>extensión</b>, <b>grip</b> y <b>desviación ulnar</b>, usando el modelo entrenado en Edge Impulse.'
    '</p>',
    unsafe_allow_html=True
)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            '<div class="card"><b>Objetivo</b><br/>'
            'Apoyar el seguimiento de la recuperación motora en pacientes post-ictus, '
            'automatizando la clasificación de gestos de mano en base a EMG.</div>',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            '<div class="card"><b>Entrada</b><br/>'
            'Ventana de 10 s de EMG multicanal combinada en una sola señal (RMS / magnitud) en formato CSV.</div>',
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            '<div class="card"><b>Salida</b><br/>'
            'Gesto predicho y distribución de probabilidades para cada clase.</div>',
            unsafe_allow_html=True
        )

st.markdown("---")

st.markdown("### 🧪 Demo interactiva")
st.write(
    "Sigue estos pasos: "
    "**1)** carga una ventana EMG en formato CSV, "
    "**2)** visualiza la señal y "
    "**3)** clasifica el gesto usando la red neuronal entrenada."
)

# =======================
# CARGAR MODELO EIM
# =======================
MODEL_PATH = "model/emg-hand-gestures-linux-x86_64-v5.eim"

runner = ImpulseRunner(MODEL_PATH)
model_info = runner.init()

LABELS = model_info["model_parameters"]["labels"]
INPUT_LEN = model_info["model_parameters"]["input_features_count"]

# ============ FUNCIÓN DE PREDICCIÓN ============
def predict_eim(signal: np.ndarray):

    # Ajustar longitud requerida
    if len(signal) > INPUT_LEN:
        signal = signal[:INPUT_LEN]
    elif len(signal) < INPUT_LEN:
        padding = np.zeros(INPUT_LEN - len(signal))
        signal = np.concatenate([signal, padding])

    signal = np.array(signal, dtype=np.float32).flatten()

    # Importante: usar solo el vector
    res = runner.classify(signal)

    scores = res["result"]["classification"]
    pred_label = max(scores, key=scores.get)
    probs = [scores[lbl] for lbl in LABELS]

    return pred_label, probs


# =======================
# PASO 1: SUBIR CSV
# =======================
st.markdown("### 1️⃣ Cargar ventana EMG (CSV)")
uploaded_file = st.file_uploader(
    "Sube un archivo CSV con tu ventana de EMG combinada.",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Vista previa del archivo:")
    st.dataframe(df.head())

    try:
        signal = df.iloc[:, -1].astype(float).values
    except Exception:
        st.error("⚠️ La última columna no contiene valores numéricos. Revisa tu archivo CSV.")
        st.stop()

    # =======================
    # PASO 2: GRAFICAR SEÑAL
    # =======================
    st.markdown("### 2️⃣ Visualizar señal EMG")

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(signal, color="#b8a8ff")
    ax.set_title("Ventana EMG cargada")
    ax.set_xlabel("Muestra")
    ax.set_ylabel("Magnitud")
    st.pyplot(fig)

    # =======================
    # PASO 3: CLASIFICAR GESTO
    # =======================
    st.markdown("### 3️⃣ Clasificar gesto")

    st.write("Presiona el botón para ejecutar el modelo sobre esta ventana:")

    if st.button("🔮 Clasificar gesto"):
        pred, probs = predict_eim(signal)

        st.success(f"### Gesto predicho: **{pred.upper()}**")

        prob_df = pd.DataFrame({
            "Clase": LABELS,
            "Probabilidad": probs
        }).set_index("Clase")

        st.subheader("Distribución de probabilidades")
        st.bar_chart(prob_df)

else:
    st.info("⬆️ Sube un archivo CSV para habilitar los pasos 2 y 3.")
