# 📘 Guía Interactiva: Anaconda & Entornos Virtuales (conda)
---
## 🎯 Objetivos
- Instalar **conda**  
- Crear y usar entornos virtuales aislados  
- Instalar paquetes  
- Conectar con **Jupyter** / **VS Code**  
- Compartir entornos de forma reproducible  

---

## 🐍 1. ¿Qué es Anaconda / Miniconda / conda-forge?
- **Anaconda** → distribución completa (muchos paquetes preinstalados).  
- **Miniconda** → instalador ligero con conda (recomendado).  
- **conda** → gestor de paquetes y entornos.  
- **conda-forge** → canal comunitario con los paquetes más actualizados.  

🔗 [Descargar Miniconda](https://docs.conda.io/en/latest/miniconda.html)  
🔗 [Descargar Anaconda](https://www.anaconda.com/download)  

---

## ⚙️ 2. Instalación e Inicialización
```bash
# Inicializar conda (una sola vez)
conda init
# Cerrar y reabrir terminal

# Extra: Actualizar conda (seguro):

conda update -n base -c defaults conda
```

## 📦 3. Crear, Activar y Manejar Entornos
```bash
# Crear entorno Python 3.11
conda create -n ds-env python=3.11

# Activar / desactivar
conda activate ds-env
conda deactivate

# Listar entornos
conda env list
conda info --envs

# Eliminar
conda remove -n ds-env --all

# Clonar (útil antes de actualizar)
conda create -n ds-env-backup --clone ds-env
```

## 📚 4. Instalar y Administrar Paquetes

```bash
# Instalar stack de ciencia de datos
conda activate ds-env
conda install numpy pandas matplotlib scikit-learn jupyterlab

# Buscar y listar
conda search numpy
conda list

# Usar pip dentro del entorno
pip install package-not-on-conda
pip list
```
⚡ Tip: Preferir conda > pip. Si usas ambos, instala primero conda.

## 📓 5. Integración con Jupyter y VS Code
Registrar el kernel en Jupyter:
```bash
conda activate ds-env
python -m ipykernel install --user --name ds-env --display-name "Python (ds-env)"
jupyter lab

```
En VS Code:

Instala extensiones Python y Jupyter.

``Ctrl+Shift+P`` → Python: Select Interpreter → selecciona ``ds-env``.

Para notebooks: Kernel → Python (ds-env).

## 🔁 6. Reproducibilidad: Exportar y Compartir Entornos

Exportar (historial limpio):
```bash
conda env export --from-history > environment.yml
```

Exportar (completo):

```bash
conda env export > environment-full.yml
```

Crear desde YAML:
```bash
conda env create -f environment.yml
# o actualizar existente
conda env update -n ds-env -f environment.yml --prune
```

Ejemplo environment.yml:

```yml
name: ds-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pandas
  - matplotlib
  - scikit-learn
  - jupyterlab
  - pip
  - pip:
    - python-dotenv
```

## 🚀 7. Workflows Comunes

Data Science Starter

```bash
conda create -n ds-env python=3.11 numpy pandas matplotlib scikit-learn jupyterlab
conda activate ds-env
python -m ipykernel install --user --name ds-env --display-name "Python (ds-env)"
jupyter lab
```

Computer Vision (CPU)
``` bash
conda create -n cv-env python=3.11 opencv numpy matplotlib
conda activate cv-env
```

PyTorch (GPU)
```bash
conda create -n torch-env python=3.11 pytorch pytorch-cuda=12.1 -c pytorch -c nvidia
conda activate torch-env
``` 
## 🧪 8. Mini-Lab Interactivo (15–20 min)

Crear un entorno:
```bash
conda create -n lab-311 python=3.11
conda activate lab-311
```

Instalar paquetes:
```bash
conda install numpy pandas jupyterlab
```

Registrar kernel y abrir Jupyter:
```bash
python -m ipykernel install --user --name lab-311 --display-name "Python (lab-311)"
jupyter lab
```

En un notebook, ejecutar:
```bash
import sys, numpy as np, pandas as pd
print(sys.executable)
print(np.__version__, pd.__version__)
```

Exportar entorno:
```bash
conda env export --from-history > environment.yml
```

(Opcional) Crear un segundo entorno desde ese YAML y comprobar que funciona.

## 📌 Créditos
<p align="center">
  <img src="https://media.licdn.com/dms/image/v2/D4E03AQG4pHJE7KF8Yw/profile-displayphoto-shrink_200_200/B4EZVtbchRHgAg-/0/1741297666662?e=2147483647&v=beta&t=LHt2LlOd5SBCGbXGEVcbFw2C41RFQaZgg27hLsD550o" alt="moises_meza">
</p>

Resumen basado en el artículo original de [Moises Stevend Meza Rodriguez](https://www.linkedin.com/in/moises-meza-rodriguez/):

👉 [Anaconda & Entornos Virtuales (conda)](https://medium.com/@moises.meza/vscode-and-markdown-a-perfect-combination-e236e07065e9)
