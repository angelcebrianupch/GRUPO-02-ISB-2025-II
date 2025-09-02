# 📘 Guía Interactiva: Git y GitHub desde Cero  

Si eres **desarrollador, investigador o estudiante**, seguramente has escuchado sobre **Git** y **GitHub**.  
Son herramientas poderosas para el **control de versiones** y la **colaboración en proyectos**.  
¡Lo mejor es que son **gratuitas**! 🚀  

---

## 🔹 Git vs GitHub
- **Git** → Sistema de control de versiones que corre en tu computadora.  
- **GitHub** → Plataforma en la nube para alojar repositorios y colaborar.  

💡 Piensa en **Git** como tu *máquina del tiempo* y en **GitHub** como *Dropbox para código con superpoderes*.  

---

## ⚙️ Cómo funciona Git
1. **Working Directory** → donde editas y creas archivos. (`git add`)  
2. **Staging Area** → preparación antes de guardar.  
3. **Local Repository** → historial en tu PC (`git commit`).  
4. **Remote Repository** → el repositorio compartido (ej. GitHub).  

---

## 🛠️ Paso 1: Instalar Git
- **Windows** → [Descargar aquí](https://git-scm.com)  
- **Linux**  
  ```markdown
  sudo apt-get install git
  ```
- **macOS**
  ```markdown
  brew install git
  ```
  Verificar instalación:
  ```markdown
  git --version
  ```
## 🧑‍💻 Paso 2: Configurar Git
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

## 📂 Paso 3: Crear un Repositorio Local

```markdown
mkdir mi-primer-repo
cd mi-primer-repo
git init
```

## 📝 Paso 4: Primer Commit
Crear archivo `README.md`:

```markdown
echo "# Mi Primer Proyecto" > README.md
```

Agregar y confirmar:

```markdown
git add README.md
git commit -m "Primer commit"
```

## 🔍 Paso 5: Comandos Clave
* Estado actual
```markdown
git status
git status -s   # versión corta
```

* Historial
```markdown
git log
git log --oneline --graph --decorate --all
```
## 🌱 Ramas (Branches)
* Crear y cambiar:
```markdown
git checkout -b nueva_rama
```

* Listar ramas:
```markdown
git branch -a
```

* Eliminar:
```markdown
git branch -d nueva_rama
```

## 🔀 Fusionar (Merge)
* Fast-forward:
```markdown
git switch main
git merge nueva_rama
```

## 💻 Usando VS Code + GitHub
1. Inicializar y hacer commit en pestaña Source Control.

2. Publicar en GitHub → Publish Branch.

3. Crear ramas desde la barra inferior.

4. Resolver conflictos con botones: Accept Current / Accept Incoming / Accept Both.

5. Activar auto-push en Configuración → Git › Post Commit Command → push.

## ✅ Conclusión

* Git = control local de versiones.

* GitHub = colaboración en la nube.

* Juntos = 🚀 trabajo en equipo eficiente.

## 📌 Créditos
<p align="center">
  <img src="https://media.licdn.com/dms/image/v2/D4E03AQG4pHJE7KF8Yw/profile-displayphoto-shrink_200_200/B4EZVtbchRHgAg-/0/1741297666662?e=2147483647&v=beta&t=LHt2LlOd5SBCGbXGEVcbFw2C41RFQaZgg27hLsD550o" alt="moises_meza">
</p>

Resumen basado en el artículo original de [Moises Stevend Meza Rodriguez](https://www.linkedin.com/in/moises-meza-rodriguez/):

👉 [Git y GitHub desde Cero](https://medium.com/@moises.meza/vscode-and-markdown-a-perfect-combination-e236e07065e9)

*¡Síganlo y denle like para más publicaciones!*

