#!/bin/bash
"""
Script de instalación específico para Kali Linux
Optimizado para el entorno de pentesting
"""

echo "🐍 DIRFORCER PRO - INSTALACIÓN KALI LINUX"
echo "=========================================="
echo "Configuración optimizada para Kali Linux"
echo "Desarrollado por: NEZUKO - Versión 2.0 Pro"
echo ""

# Verificar si estamos en Kali Linux
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    if [[ "$ID" == "kali" ]]; then
        echo "✅ Kali Linux detectado: $VERSION"
    else
        echo "⚠️ Sistema detectado: $ID"
        echo "Este script está optimizado para Kali Linux"
    fi
else
    echo "⚠️ No se pudo detectar el sistema operativo"
fi

echo ""

# Verificar Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "✅ Python3 detectado: $PYTHON_VERSION"
else
    echo "❌ Python3 no encontrado. Instalando..."
    sudo apt update
    sudo apt install -y python3 python3-pip
fi

# Verificar pip
if command -v pip3 &> /dev/null; then
    echo "✅ pip3 detectado"
else
    echo "❌ pip3 no encontrado. Instalando..."
    sudo apt install -y python3-pip
fi

echo ""

# Instalar dependencias del sistema
echo "📦 Instalando dependencias del sistema..."
sudo apt update
sudo apt install -y python3-requests python3-colorama

# Instalar dependencias de Python
echo "📦 Instalando dependencias de Python..."
pip3 install -r requirements.txt

# Configurar la herramienta
echo "⚙️ Configurando DirForcer Pro..."
python3 config.py --setup
python3 config.py --create-wordlists

# Crear scripts ejecutables
echo "🔧 Creando scripts ejecutables..."

# Script principal
cat > dirforcer << 'EOF'
#!/bin/bash
python3 dirforcer_improved.py "$@"
EOF

# Script de configuración
cat > dirforcer-config << 'EOF'
#!/bin/bash
python3 config.py "$@"
EOF

# Hacer ejecutables
chmod +x dirforcer
chmod +x dirforcer-config
chmod +x dirforcer_improved.py

echo "✅ Scripts ejecutables creados:"
echo "   - dirforcer (herramienta principal)"
echo "   - dirforcer-config (configuración)"

# Crear directorio en PATH del usuario
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo "📁 Configurando PATH..."
    mkdir -p ~/.local/bin
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
fi

# Mover scripts a PATH
cp dirforcer ~/.local/bin/
cp dirforcer-config ~/.local/bin/

echo ""
echo "🎯 EJEMPLOS DE USO EN KALI:"
echo "============================"
echo "Uso básico:"
echo "  dirforcer -d example.com -w directorios.txt"
echo ""
echo "Uso avanzado:"
echo "  dirforcer -d https://example.com -w wordlist.txt -t 20 --delay 0.1"
echo ""
echo "Configuración:"
echo "  dirforcer-config --show"
echo "  dirforcer-config --update default_threads 20"
echo ""
echo "Escaneo agresivo:"
echo "  dirforcer -d example.com -w sensitive.txt -t 50 --status-codes 200 403"
echo ""

echo "🎉 ¡INSTALACIÓN COMPLETADA EN KALI LINUX!"
echo "=========================================="
echo "DirForcer Pro está listo para usar."
echo "Reinicia tu terminal o ejecuta: source ~/.bashrc"
echo ""

# Mostrar información adicional para Kali
echo "💡 CONSEJOS PARA KALI LINUX:"
echo "============================"
echo "• Usa wordlists de SecLists: apt install seclists"
echo "• Integra con otras herramientas de Kali"
echo "• Usa proxychains para anonimato: dirforcer -d target.com -w wordlist.txt"
echo "• Monitorea logs: tail -f dirforcer.log"
echo ""
