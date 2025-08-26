## Título del Proyecto: 📶 _BioGesto: Rehabilitación Motora Inteligente con EMG_ 📶

### Problemática a Abordar

La recuperación motora de pacientes post-ictus se ve obstaculizada por la falta de **sistemas de rehabilitación accesibles y asequibles**. Los dispositivos clínicos para el monitoreo de la recuperación motora suelen ser costosos, lo que limita su uso fuera de los centros médicos. El reconocimiento de gestos a través de **señales electromiográficas (EMG)** tiene el potencial de ser una solución, pero su implementación aún no es masivamente accesible, lo que impide un seguimiento constante y personalizado del progreso del paciente en su propio hogar.

<div align="center">
  <img src="https://cdn.hackaday.io/images/original/9534081685454426715.gif" alt="Un GIF animado de ejemplo" width="600"/>
</div>

### Objetivos a Alcanzar

* **Objetivo General:** Desarrollar un sistema de bajo costo y fácil uso, llamado **BioGesto**, que reconozca gestos de la mano mediante señales EMG para facilitar la rehabilitación motora de pacientes.
* **Objetivos Específicos:**
    1.  Crear una base de datos de **señales EMG** de gestos sencillos (3-5 gestos), utilizando un hardware accesible.
    2.  Implementar técnicas de **procesamiento de señales** para filtrar el ruido y extraer características relevantes de los datos EMG.
    3.  Entrenar y comparar el rendimiento de **modelos de machine learning** (como **KNN, SVM y Random Forest**) para determinar el clasificador más óptimo para el reconocimiento de gestos en tiempo real.
    4.  Diseñar y desarrollar una **interfaz de usuario intuitiva** que ofrezca retroalimentación visual en tiempo real del gesto reconocido.

---

### Herramientas a Utilizar

* **Hardware:**
    * **Placa de Desarrollo:** Arduino Nano o ESP32.
    * **Sensores EMG:** MyoWare 2.0.
* **Software:**
    * **Lenguaje de Programación:** Python.
    * **Librerías:**
        * `Numpy` y `Pandas` para el manejo de datos.
        * `Scikit-learn` para la implementación de los modelos de machine learning.
        * `PyQt` o `Kivy` para el desarrollo de la interfaz gráfica.
        * `Pyserial` para la comunicación entre el hardware y la computadora.

---

### Plus Adicional: Módulo de Gamificación y Seguimiento

Para hacer el proceso de rehabilitación más atractivo y efectivo, **BioGesto** incluirá las siguientes características adicionales:

* **Gamificación:** El sistema se convertirá en un videojuego interactivo. Los gestos del paciente controlarán un personaje o una acción dentro del juego, convirtiendo la rehabilitación en una actividad divertida. Por ejemplo, un gesto de "pinza" podría servir para recoger objetos virtuales.
* **Seguimiento del Progreso:** Se integrará un módulo de registro que guardará datos sobre la cantidad de repeticiones de cada gesto, la precisión y la velocidad. El paciente y el terapeuta podrán visualizar estos datos a través de gráficos de progreso, lo que permitirá ajustar la rutina de ejercicios de forma más precisa y motivar al paciente al ver su mejora.
