# 🚀 DirForcer Pro - Herramienta de Enumeración Avanzada

**Herramienta profesional de enumeración de directorios** - Versión mejorada con funcionalidades avanzadas y mejores prácticas de seguridad.

**Desarrollado por: NEZUKO**  
**Versión: 2.0 Pro**

---

## ✨ **Características Destacadas**

### 🎨 **Banner Especial de NEZUKO**
- **Detección automática** de Kali Linux
- **Banner personalizado** con "NEZUKO" en letras grandes
- **Interfaz adaptativa** según la plataforma
- **Colores dinámicos** para mejor experiencia visual

### 🔧 **Mejoras Técnicas**
- **Manejo robusto de errores** con try-catch y logging
- **Validación de entrada** para URLs y archivos
- **Configuración de User-Agent** personalizable
- **Soporte para múltiples códigos de estado HTTP** (200, 301, 302, 403, 401)
- **Sistema de logging** completo con archivos de registro
- **Interrupción elegante** con Ctrl+C
- **Compatibilidad cross-platform** con colorama

### ⚡ **Funcionalidades Avanzadas**
- **Escaneo multi-thread** configurable
- **Control de velocidad** con delays personalizables
- **Barra de progreso** en tiempo real
- **Exportación de resultados** en formato JSON
- **Headers HTTP realistas** para evitar detección
- **Verificación SSL** opcional
- **Modo verbose** para debugging

### 🛡️ **Mejoras de Seguridad**
- **Rate limiting** para evitar sobrecarga del servidor
- **User-Agent realista** por defecto
- **Headers HTTP completos** que simulan navegador real
- **Timeout configurable** para requests
- **Manejo de certificados SSL** opcional

---

## 🚀 **Instalación Rápida**

### **Requisitos Previos**
- Python 3.7+
- pip

### **Instalación General**
```bash
# Clonar el repositorio
git clone https://github.com/ELDANI1/dirforcer-pro.git
cd dirforcer-pro

# Instalar dependencias
pip install -r requirements.txt

# Configurar herramienta
python config.py --setup
python config.py --create-wordlists
```

### **Instalación en Kali Linux (Recomendado)**
```bash
# Clonar y instalar automáticamente
git clone https://github.com/ELDANI1/dirforcer-pro.git
cd dirforcer-pro
chmod +x install_kali.sh
./install_kali.sh
```

### **Uso Básico**
```bash
# Uso básico
python dirforcer_improved.py -d example.com -w directorios.txt

# Uso avanzado
python dirforcer_improved.py -d https://example.com -w wordlist.txt -t 20 --delay 0.1

# Con salida JSON
python dirforcer_improved.py -d example.com -w common.txt -o results.json --verbose
```

---

## 🐍 **Banner Especial en Kali Linux**

Cuando ejecutes DirForcer Pro en Kali Linux, verás un banner especial con "NEZUKO" en letras grandes:

```
 _   _  _____ ____ _   _ _  __ ____  
| \ | |/ ____|  _ \ \ | | |/ /|  _ \ 
|  \| | |  __| |_) | \| | ' / | |_) |
| . ` | | |_ |  _ <| . ` |  < |  __/ 
|_|\_\_|\_____|_| \_\_|\_\_|\_\_|     
                                      
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🐍 DIRFORCER PRO v2.0 🐍                               ║
║              ⚡ Herramienta de Enumeración Avanzada ⚡                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
🐍 Optimizado para Kali Linux - Entorno de Pentesting
⚡ Desarrollado con mejores prácticas de seguridad
🔥 Desarrollado por: NEZUKO - Versión 2.0 Pro
🎯 Listo para descubrir directorios ocultos
💀 Uso ético y responsable requerido
─────────────────────────────────────────────────────────────────────────────
¡Bienvenido al entorno de pentesting de NEZUKO!
```

---

## 📊 **Parámetros Disponibles**

| Parámetro | Descripción | Valor por Defecto |
|-----------|-------------|-------------------|
| `-d, --domain` | Dominio objetivo | **Requerido** |
| `-w, --wordlist` | Archivo de wordlist | **Requerido** |
| `-t, --threads` | Número de threads | 10 |
| `--delay` | Delay entre requests (segundos) | 0 |
| `--timeout` | Timeout para requests (segundos) | 10 |
| `--user-agent` | User-Agent personalizado | Navegador Chrome |
| `--no-ssl-verify` | No verificar certificados SSL | False |
| `--status-codes` | Códigos de estado de interés | 200 301 302 403 401 |
| `-o, --output` | Archivo de salida JSON | None |
| `-v, --verbose` | Modo verbose | False |

---

## 📊 **Wordlists Recomendadas**

### **Incluidas en el Proyecto**
- `admin.txt` - Directorios administrativos
- `common.txt` - Directorios comunes  
- `sensitive.txt` - Directorios sensibles

### **SecLists (Kali Linux)**
```bash
# Instalar SecLists
sudo apt install seclists

# Usar wordlists de SecLists
dirforcer -d example.com -w /usr/share/seclists/Discovery/Web-Content/common.txt
dirforcer -d example.com -w /usr/share/seclists/Discovery/Web-Content/big.txt
```

---

## 🔧 **Configuración de Seguridad**

### **Headers Personalizados**
```bash
# User-Agent personalizado
dirforcer -d example.com -w wordlist.txt --user-agent "Kali-Pentest/1.0"

# Sin verificación SSL
dirforcer -d example.com -w wordlist.txt --no-ssl-verify
```

### **Rate Limiting**
```bash
# Escaneo discreto
dirforcer -d example.com -w wordlist.txt --delay 0.5

# Escaneo agresivo
dirforcer -d example.com -w wordlist.txt -t 50 --delay 0.1
```

### **Con Proxychains (Kali Linux)**
```bash
# Usar con proxychains
proxychains dirforcer -d target.com -w wordlist.txt
```

---

## 🔗 **Integración con Otras Herramientas**

### **Con Nmap**
```bash
# Escaneo de puertos + enumeración de directorios
nmap -p 80,443 target.com && dirforcer -d target.com -w wordlist.txt
```

### **Con Nikto**
```bash
# Escaneo de vulnerabilidades + enumeración
nikto -h target.com && dirforcer -d target.com -w wordlist.txt
```

### **Con Gobuster (comparación)**
```bash
# Comparar resultados
gobuster dir -u https://target.com -w wordlist.txt
dirforcer -d target.com -w wordlist.txt
```

---

## 🐛 **Troubleshooting**

### **Problemas Comunes**
```bash
# Permisos
chmod +x dirforcer_improved.py

# Dependencias
pip3 install --upgrade -r requirements.txt

# Performance
dirforcer -d example.com -w wordlist.txt -t 50 --delay 0.05

# Timeout
dirforcer -d example.com -w wordlist.txt --timeout 30
```

---

## 🔒 **Consideraciones de Seguridad**

### **Uso Ético**
- **Solo usa esta herramienta en sitios que poseas o tengas autorización explícita**
- **Respeta los términos de servicio de los sitios web**
- **No sobrecargues servidores con requests excesivos**

### **Mejores Prácticas**
- Usa delays apropiados para evitar ser bloqueado
- Configura User-Agents realistas
- Monitorea los logs para detectar problemas
- Guarda resultados para análisis posterior

---

## 📈 **Comparación con la Versión Original**

| Característica | Original | Mejorada |
|----------------|----------|----------|
| Manejo de errores | ❌ | ✅ |
| Multi-threading | ❌ | ✅ |
| Validación de entrada | ❌ | ✅ |
| Logging | ❌ | ✅ |
| Barra de progreso | ❌ | ✅ |
| Exportación JSON | ❌ | ✅ |
| Headers realistas | ❌ | ✅ |
| Control de velocidad | ❌ | ✅ |
| Interrupción elegante | ❌ | ✅ |
| Documentación | Básica | Completa |
| Banner personalizado | ❌ | ✅ |

---

## 🤝 **Contribuciones**

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 **Licencia**

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## ⚠️ **Descargo de Responsabilidad**

Esta herramienta está diseñada únicamente para propósitos educativos y de testing en sistemas propios o con autorización explícita. Los desarrolladores no son responsables del uso indebido de esta herramienta.

---

<div align="center">

**Desarrollado con ❤️ por NEZUKO**  
**Versión 2.0 Pro - Herramienta profesional de enumeración de directorios**

</div>
