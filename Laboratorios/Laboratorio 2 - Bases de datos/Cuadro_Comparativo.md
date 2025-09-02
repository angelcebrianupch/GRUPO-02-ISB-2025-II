# ✨ Comparativo de Bases de Datos EMG –  (11 Datasets)

| # | 📂 Dataset / Fuente | 👥 Población | ✋ Gestos | 🎚️ Canales EMG | ⏱️ fs (Hz) | 📆 Sesiones / Días | 📅 Año | 🔒 Licencia | 💾 Tamaño / Archivos | 🛠 Herramientas asociadas | 🧭 Aplicación sugerida | ✅ Pros | ⚠️ Contras | 🎯 Idoneidad |
|---|---------------------|--------------|-----------|----------------|-------------|-------------------|--------|-------------|----------------------|--------------------------|-----------------------|---------|------------|--------------|
| 01 | 🧩 **GRABMyo (PhysioNet 1.1.0)** | 43 sanos (24–35 a) | 16 + reposo | 28 (16 antebrazo + 12 muñeca) | 2048 | 3 días multisesión | 2024 | CC BY 4.0 | 129 grabaciones (~GBs) | Scripts Matlab + Python | Biometría, gestos, prótesis | 🔝 Muchos sujetos, alta fs, robustez multisesión | ⚙️ Complejo (32 canales, pesado) | ⭐⭐⭐⭐ **Alta** |
| 02 | 🤲 **sEMG Basic Hand Movements (UCI)** | 5 sanos (DB1) + 1 sano × 3 días (DB2) | 6 + reposo | 2 | 500 | 3 días (DB2) | 2014 | OA (UCI) | Pequeño (<50 MB) | .mat | Gestos funcionales, control HMI | 🎯 Simple, bajo costo, gestos claros | 👥 Pocos sujetos | ⭐⭐⭐⭐ **Alta** |
| 03 | 📡 **EMG Data for Gestures (UCI Myo)** | 36 sanos | 6–7 + reposo | 8 (Myo armband) | NR | 2 series/sujeto | 2019 | CC BY 4.0 | 73 archivos (~300 MB) | Myo SDK, Python/Matlab | Prototipos rápidos, wearables | 🧑‍🤝‍🧑 Muchos sujetos, portable | ❓ fs no clara, señal cruda | ⭐⭐⭐⭐ **Media–Alta** |
| 04 | 🏆 **Ninapro DB1** | 27 sanos (20 hombres, 7 mujeres) | 52 + reposo | 10 (8 antebrazo + 2 flexor/extensor) | ~100 | 1 sesión, 10 repeticiones/gesto | 2014 | CC BY 4.0 (académico) | 27 .zip (~GBs) | .mat (EMG + Glove + etiquetas) | Control de prótesis, ML robusto | 📚 Benchmark mundial, gran diversidad de gestos | ⚖️ Dataset grande, más gestos de los necesarios | ⭐⭐⭐⭐⭐ **Alta (preferida)** |
| 05 | 🧑‍⚕️ **Hand-to-nose (Figshare)** | 20 post-stroke + sanos | 1 gesto funcional | NR | NR | NR | ~2021 | NR | 3 archivos .mat | Matlab | Rehabilitación clínica (Fugl-Meyer) | 🧠 Incluye clínico + scores FM | ❓ Protocolo poco detallado | ⭐⭐ **Baja–Media** |
| 06 | 🎯 **Reaching 9 dirs (Mendeley)** | 12 sanos + 13 post-stroke | 9 direcciones alcance | 8 (brazo/hombro) | NR | — | 2018 | CC BY 4.0 | Carpetas MVC + targets | Matlab/Python | Comparación sano vs stroke | 🔄 Multicanal, clínico | 🚫 No gestos mano reales | ⭐⭐⭐ **Media** |
| 07 | 🧪 **One-shot ProtoTL (JNER)** | 20 post-stroke | 7 (incl. reposo) | NR (antebrazo) | NR | — | 2024 | CC BY 4.0 | GitHub (código) | Python (PyTorch) | IA clínica (few-shot TL) | 🆕 Innovador (prototypical nets) | 📉 Dataset no público | ⭐⭐ **Exploratoria** |
| 08 | 🧠 **Bilateral Fusion CNN-LSTM (Sensors)** | 25 post-stroke | 7 | 4 regiones | NR | 2 sesiones | 2025 | CC BY 4.0 | Solo artículo | Python (DL) | Rehabilitación post-stroke | 📈 Precisión muy alta | 🚫 Datos no disponibles | ⭐⭐ **Exploratoria** |
| 09 | 🦾 **NeuroLife® HDEMG (JNER)** | 7 post-stroke + 7 sanos | 12 + reposo | hasta 150 | NR | Bloques múltiples | 2024 | Bajo solicitud | Manga HDEMG (~GBs) | Hardware Battelle | Interfaces portátiles clínicas | 🧩 Alta densidad, wearable | 🔒 Acceso restringido, caro | ⭐⭐⭐ **Media** |
| 10 | ⚡ **Fast EMG Classification (Preprint)** | 40 sanos + post-stroke | 6 | 4 (antebrazo) | 2000 | — | 2025 | OA Preprint | ~GB | Matlab + Python | Optimización práctica (ventana 2s, 2ch) | 📝 Guías claras de config. rápida | 📉 Datos clínicos no públicos | ⭐⭐⭐⭐ **Alta (guía)** |
| 11 | 🌍 **U-Limb (GigaScience)** | 91 sanos + 65 post-stroke | ADLs + brazo | EMG (SENIAM) | NR | Multicentro | 2021 | CC BY 4.0 | Multimodal (GB–TB) | EEG, ECG, kinemática, fMRI | Neurociencia, interfaces multimodales | 🌐 Masivo, multimodal | 📊 Muy complejo, no gestual | ⭐⭐⭐ **Media** |

# 🏆 ¿Por qué **Ninapro DB1** es el mejor dataset para nuestro proyecto?

El dataset **Ninapro DB1 (Non-Invasive Adaptive Prosthetics Database – Collection 1)** es considerado un **estándar de referencia internacional** en el ámbito del reconocimiento de gestos mioeléctricos y el control de prótesis. Su relevancia y calidad lo posicionan como la opción más adecuada para nuestro proyecto por las siguientes razones:

---

## 👥 Población representativa  
- Incluye **27 sujetos sanos** (20 hombres y 7 mujeres), con edades entre 22 y 40 años.  
- Muestra suficientemente grande para el entrenamiento de modelos supervisados y para garantizar **variabilidad intersujeto**.  

---

## ✋ Variedad y riqueza de gestos  
- Registra **52 movimientos de la mano** más la posición de reposo.  
- Los gestos están organizados en tres grupos:  
  1. **Movimientos básicos de los dedos**  
  2. **Configuraciones isométricas e isotónicas del puño y muñeca**  
  3. **Agarres funcionales**  
- Cada gesto se repite **10 veces**, lo que genera una base sólida y equilibrada para entrenar clasificadores.  
- Esta diversidad permite **seleccionar un subconjunto de 3–5 gestos simples** para nuestro caso, sin perder robustez.

---

## 🎚️ Instrumentación y calidad de las señales  
- Señales EMG adquiridas con **10 electrodos de superficie Otto Bock MyoBock 13E200**:  
  - 8 colocados alrededor del antebrazo  
  - 2 adicionales en los músculos *flexor* y *extensor digitorum superficialis*  
- **Dispositivo complementario:** CyberGlove II con 22 sensores de ángulo → captura cinemática para correlacionar EMG con movimiento real.  
- Sincronización precisa entre EMG y cinemática → permite estudios más avanzados de control motor.

---

## ⏱️ Frecuencia de muestreo y consistencia  
- La frecuencia de muestreo es de **~100 Hz**, suficiente para capturar patrones musculares relevantes en gestos.  
- Cada sesión fue realizada en condiciones controladas y guiadas por video, lo que asegura **consistencia experimental**.  

---

## 📑 Formato y accesibilidad  
- Archivos disponibles en formato **.mat (MATLAB)**, ampliamente compatible con entornos de análisis como **Python, SciPy y scikit-learn**.  
- Base de datos **pública y gratuita**, con licencia académica abierta (CC BY 4.0).  
- Documentación clara y scripts de apoyo disponibles en la web oficial de Ninapro.  

---

## 📊 Ventajas científicas  
- Es el dataset más citado y utilizado en estudios de **machine learning aplicado a EMG**.  
- Permite explorar desde **clasificación básica de gestos** hasta modelos avanzados de **aprendizaje profundo**.  
- La gran cantidad de gestos y repeticiones lo convierten en un **benchmark confiable** para comparar algoritmos.  
- Ha sido validado en múltiples publicaciones científicas, lo que lo hace **confiable y reconocido en la comunidad internacional**.  

---

## ⚖️ Conclusión  
Aunque existen otros datasets con ventajas específicas (ej. GRABMyo por su frecuencia de muestreo de 2048 Hz, o UCI por su simplicidad), **Ninapro DB1 ofrece el mejor equilibrio entre tamaño de la muestra, diversidad de gestos, calidad de adquisición y accesibilidad de datos**.  

Esto lo convierte en la opción **más sólida y estratégica** para nuestro proyecto de **reconocimiento de gestos con EMG**, ya que nos permitirá entrenar modelos confiables, robustos y comparables con el estado del arte internacional.
