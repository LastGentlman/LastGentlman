import os
import re

EXACT_REPLACEMENTS = [
    (
        "[![English](https://img.shields.io/badge/Language-English-blue?style=for-the-badge&logo=readme)](README.md)",
        "[![English](https://img.shields.io/badge/Language-English-lightgrey?style=for-the-badge&logo=readme)](README.md)"
    ),
    (
        "[![Español](https://img.shields.io/badge/Idioma-Español-lightgrey?style=for-the-badge&logo=readme)](README.es.md)",
        "[![Español](https://img.shields.io/badge/Idioma-Español-green?style=for-the-badge&logo=readme)](README.es.md)"
    ),
    (
        "# Hi, I'm Rodrigo - a.k.a. <a target=\"_blank\" href=\"https://ingroy.com\">Ing Roy</a> 👋",
        "# Hola, soy Rodrigo - a.k.a. <a target=\"_blank\" href=\"https://ingroy.com\">Ing Roy</a> 👋"
    ),
    (
        "### Software Engineer & Full-Stack Developer · *Coding a Better Tomorrow*",
        "### Ingeniero de Software & Desarrollador Full-Stack · *Codificando un mejor mañana*"
    ),
    (
        "&label=Follow%20%401ngRoy",
        "&label=Seguir%20%401ngRoy"
    ),
    (
        "> 💬 *Always eager to build, solve complex problems, and share knowledge. Feel free to reach out or connect!*  \n> 📍 **International Citizen** · 👨‍💻 **Pronouns:** he/him · 📬 **DM:** [@1ngRoy](https://twitter.com/1ngRoy)",
        "> 💬 *Siempre entusiasmado por construir, resolver problemas complejos y compartir conocimiento. ¡No dudes en escribirme o conectar!*  \n> 📍 **Ciudadano Internacional** · 👨‍💻 **Pronombres:** él/he · 📬 **DM:** [@1ngRoy](https://twitter.com/1ngRoy)"
    ),
    (
        "## 🚀 Featured Projects Portfolio",
        "## 🚀 Portfolio de Proyectos Destacados"
    ),
    (
        "A curated collection of full-stack platforms, production SaaS solutions, computer vision tools, and multimedia experiments.",
        "Una colección de plataformas full-stack, soluciones SaaS en producción, herramientas de visión por computadora y proyectos multimedia."
    ),
    (
        "### 💼 Enterprise Systems & SaaS Solutions",
        "### 💼 Sistemas Empresariales y Soluciones SaaS"
    ),
    (
        "### 🛠️ AI, Computer Vision & Multimedia Engineering",
        "### 🛠️ IA, Visión por Computadora e Ingeniería Multimedia"
    ),
    (
        "### 🎮 Gaming & Desktop Applications",
        "### 🎮 Videojuegos y Aplicaciones de Escritorio"
    ),
    (
        "## ⚡ Recently Updated Open Source Repositories",
        "## ⚡ Repositorios Open Source Actualizados Recientemente"
    ),
    (
        "> *Automatically synced daily via GitHub Actions*",
        "> *Sincronizados automáticamente todos los días mediante GitHub Actions*"
    ),
    (
        "## 🛠️ Tech Stack & Core Competencies",
        "## 🛠️ Stack Tecnológico y Competencias Clave"
    ),
    (
        "| Area | Technologies |",
        "| Área | Tecnologías |"
    ),
    (
        "| **Databases & Cloud** |",
        "| **Bases de Datos & Cloud** |"
    ),
    (
        "| **Tools & DevOps** |",
        "| **Herramientas & DevOps** |"
    ),
    (
        "## 📺 Latest YouTube Videos",
        "## 📺 Últimos Videos en YouTube"
    ),
    (
        "➡️ [More videos on YouTube...]",
        "➡️ [Más videos en YouTube...]"
    ),
    (
        "## 📕 Latest Blog Posts",
        "## 📕 Últimas Publicaciones del Blog"
    ),
    (
        "➡️ [More blog posts at ingroy.com...]",
        "➡️ [Más artículos en ingroy.com...]"
    ),
    (
        "<summary>⚡ <b>Recent GitHub Activity</b></summary>",
        "<summary>⚡ <b>Actividad Reciente en GitHub</b></summary>"
    ),
    (
        "Designed & engineered with ❤️ by",
        "Diseñado y desarrollado con ❤️ por"
    ),
    ("Live Application", "Aplicación en Vivo"),
    ("Live Demo", "Demo en Vivo"),
    ("Live System", "Sistema en Vivo"),
    ("Live Platform", "Plataforma en Vivo"),
    ("Live Tool", "Herramienta en Vivo"),
    ("Live Web App", "Aplicación Web en Vivo"),
    ("Production / Enterprise Code", "Código en Producción / Empresarial"),
    ("Private Enterprise", "Solución Empresarial"),
    ("Enterprise Solution", "Solución Corporativa"),
    ("Proprietary Engine", "Motor Propietario"),
    ("Surveillance R&D Project", "Proyecto de I+D en Vigilancia"),
    ("Security Suite", "Suite de Seguridad"),
    ("Marketing AI Engine", "Motor de IA para Marketing"),
    ("Archival Utility", "Utilidad de Respaldo"),
    ("Interactive Gaming Lab", "Laboratorio Interactivo de Juegos"),
    ("Cross-Platform Utility", "Utilidad Multiplataforma"),
]

def auto_translate_readme():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    en_path = os.path.join(base_dir, "README.md")
    es_path = os.path.join(base_dir, "README.es.md")

    if not os.path.exists(en_path):
        print("README.md not found.")
        return

    with open(en_path, "r", encoding="utf-8") as f:
        content = f.read()

    for src, dst in EXACT_REPLACEMENTS:
        content = content.replace(src, dst)

    with open(es_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("README.es.md successfully synchronized with README.md.")

if __name__ == "__main__":
    auto_translate_readme()
