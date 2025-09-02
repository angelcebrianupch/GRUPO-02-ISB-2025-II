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
