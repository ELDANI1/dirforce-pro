#!/usr/bin/env python3
"""
Script de instalación para DirForcer Pro
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_banner():
    print("=" * 60)
    print("🚀 DIRFORCER PRO - INSTALADOR")
    print("=" * 60)
    print("Herramienta profesional de enumeración de directorios")
    print("Versión mejorada con funcionalidades avanzadas")
    print("Desarrollado por: NEZUKO - Versión 2.0 Pro")
    print("=" * 60)

def check_python_version():
    """Verificar versión de Python"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Error: Se requiere Python 3.7 o superior")
        print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
    return True

def install_dependencies():
    """Instalar dependencias"""
    print("\n📦 Instalando dependencias...")
    
    try:
        # Instalar desde requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar dependencias: {e}")
        return False

def setup_configuration():
    """Configurar herramienta"""
    print("\n⚙️ Configurando herramienta...")
    
    try:
        # Ejecutar script de configuración
        subprocess.check_call([sys.executable, "config.py", "--setup"])
        subprocess.check_call([sys.executable, "config.py", "--create-wordlists"])
        print("✅ Configuración completada")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en configuración: {e}")
        return False

def create_launcher_scripts():
    """Crear scripts de lanzamiento"""
    print("\n🔧 Creando scripts de lanzamiento...")
    
    # Script para Windows
    if platform.system() == "Windows":
        with open("dirforcer.bat", "w") as f:
            f.write("@echo off\n")
            f.write("python dirforcer_improved.py %*\n")
            f.write("pause\n")
        print("✅ Script de lanzamiento creado: dirforcer.bat")
    
    # Script para Unix/Linux/Mac
    with open("dirforcer.sh", "w") as f:
        f.write("#!/bin/bash\n")
        f.write("python3 dirforcer_improved.py \"$@\"\n")
    
    # Hacer ejecutable en Unix
    if platform.system() != "Windows":
        os.chmod("dirforcer.sh", 0o755)
        print("✅ Script de lanzamiento creado: dirforcer.sh")

def run_test():
    """Ejecutar prueba básica"""
    print("\n🧪 Ejecutando prueba básica...")
    
    try:
        # Probar importación de módulos
        import requests
        import pyfiglet
        import colorama
        print("✅ Módulos importados correctamente")
        
        # Probar configuración
        subprocess.check_call([sys.executable, "config.py", "--show"])
        print("✅ Configuración verificada")
        
        return True
    except ImportError as e:
        print(f"❌ Error en importación: {e}")
        return False

def show_usage_examples():
    """Mostrar ejemplos de uso"""
    print("\n📚 EJEMPLOS DE USO:")
    print("=" * 40)
    print("Uso básico:")
    print("  python dirforcer_improved.py -d example.com -w directorios.txt")
    print()
    print("Uso avanzado:")
    print("  python dirforcer_improved.py -d https://example.com -w wordlist.txt -t 20 --delay 0.1")
    print()
    print("Escaneo específico:")
    print("  python dirforcer_improved.py -d example.com -w admin.txt --status-codes 200 403")
    print()
    print("Con salida JSON:")
    print("  python dirforcer_improved.py -d example.com -w common.txt -o results.json")
    print()
    print("Modo verbose:")
    print("  python dirforcer_improved.py -d example.com -w wordlist.txt --verbose")

def main():
    print_banner()
    
    # Verificar Python
    if not check_python_version():
        sys.exit(1)
    
    # Instalar dependencias
    if not install_dependencies():
        print("❌ Instalación fallida. Revisa los errores anteriores.")
        sys.exit(1)
    
    # Configurar herramienta
    if not setup_configuration():
        print("❌ Configuración fallida. Revisa los errores anteriores.")
        sys.exit(1)
    
    # Crear scripts de lanzamiento
    create_launcher_scripts()
    
    # Ejecutar prueba
    if not run_test():
        print("❌ Prueba fallida. Revisa los errores anteriores.")
        sys.exit(1)
    
    # Mostrar ejemplos
    show_usage_examples()
    
    print("\n" + "=" * 60)
    print("🎉 ¡INSTALACIÓN COMPLETADA!")
    print("=" * 60)
    print("DirForcer Pro está listo para usar.")
    print("Revisa el README_IMPROVED.md para más información.")
    print("=" * 60)

if __name__ == "__main__":
    main()
