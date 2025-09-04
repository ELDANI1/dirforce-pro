#!/usr/bin/env python3
"""
Script de configuración y utilidades para DirForcer Pro
Desarrollado por: NEZUKO
Versión: 2.0 Pro
"""

import os
import sys
import json
import argparse
from pathlib import Path

class DirForcerConfig:
    def __init__(self):
        self.config_dir = Path.home() / '.dirforcer'
        self.config_file = self.config_dir / 'config.json'
        self.default_config = {
            'default_threads': 10,
            'default_delay': 0,
            'default_timeout': 10,
            'default_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'default_status_codes': [200, 301, 302, 403, 401],
            'output_directory': str(Path.cwd()),
            'wordlists_directory': str(Path.cwd()),
            'log_level': 'INFO'
        }
    
    def setup_config(self):
        """Configurar directorio y archivo de configuración"""
        self.config_dir.mkdir(exist_ok=True)
        
        if not self.config_file.exists():
            self.save_config(self.default_config)
            print(f"✅ Configuración inicial creada en: {self.config_file}")
        else:
            print(f"📁 Configuración existente encontrada en: {self.config_file}")
    
    def load_config(self):
        """Cargar configuración desde archivo"""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self.default_config
        except json.JSONDecodeError:
            print("⚠️ Error en archivo de configuración. Usando configuración por defecto.")
            return self.default_config
    
    def save_config(self, config):
        """Guardar configuración en archivo"""
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def update_config(self, key, value):
        """Actualizar un valor específico en la configuración"""
        config = self.load_config()
        config[key] = value
        self.save_config(config)
        print(f"✅ Configuración actualizada: {key} = {value}")
    
    def show_config(self):
        """Mostrar configuración actual"""
        config = self.load_config()
        print("📋 Configuración actual de DirForcer Pro:")
        print("=" * 50)
        for key, value in config.items():
            print(f"{key}: {value}")
    
    def create_wordlist(self, name, content):
        """Crear una wordlist personalizada"""
        wordlist_dir = Path(self.load_config().get('wordlists_directory', Path.cwd()))
        wordlist_dir.mkdir(exist_ok=True)
        
        wordlist_file = wordlist_dir / f"{name}.txt"
        
        with open(wordlist_file, 'w', encoding='utf-8') as f:
            for item in content:
                f.write(f"{item}\n")
        
        print(f"✅ Wordlist creada: {wordlist_file}")
        return wordlist_file
    
    def create_common_wordlists(self):
        """Crear wordlists comunes predefinidas"""
        admin_words = [
            'admin', 'administrator', 'admin1', 'admin2', 'admin-panel',
            'admin_area', 'admin_area_new', 'admin_area_old', 'admin_area2',
            'admin_login', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5',
            'administrator', 'administrator_accounts', 'administrators',
            'admins', 'adm', 'ad', 'login', 'logon', 'signin', 'sign-in',
            'auth', 'authentication', 'secure', 'security', 'panel',
            'cpanel', 'webadmin', 'webmaster', 'webadmin_area', 'webadmin1',
            'webadmin2', 'webadmin3', 'webadmin4', 'webadmin5', 'webadmin6',
            'webadmin7', 'webadmin8', 'webadmin9', 'webadmin10', 'webadmin11',
            'webadmin12', 'webadmin13', 'webadmin14', 'webadmin15', 'webadmin16',
            'webadmin17', 'webadmin18', 'webadmin19', 'webadmin20', 'webadmin21',
            'webadmin22', 'webadmin23', 'webadmin24', 'webadmin25', 'webadmin26',
            'webadmin27', 'webadmin28', 'webadmin29', 'webadmin30', 'webadmin31',
            'webadmin32', 'webadmin33', 'webadmin34', 'webadmin35', 'webadmin36',
            'webadmin37', 'webadmin38', 'webadmin39', 'webadmin40', 'webadmin41',
            'webadmin42', 'webadmin43', 'webadmin44', 'webadmin45', 'webadmin46',
            'webadmin47', 'webadmin48', 'webadmin49', 'webadmin50', 'webadmin51',
            'webadmin52', 'webadmin53', 'webadmin54', 'webadmin55', 'webadmin56',
            'webadmin57', 'webadmin58', 'webadmin59', 'webadmin60', 'webadmin61',
            'webadmin62', 'webadmin63', 'webadmin64', 'webadmin65', 'webadmin66',
            'webadmin67', 'webadmin68', 'webadmin69', 'webadmin70', 'webadmin71',
            'webadmin72', 'webadmin73', 'webadmin74', 'webadmin75', 'webadmin76',
            'webadmin77', 'webadmin78', 'webadmin79', 'webadmin80', 'webadmin81',
            'webadmin82', 'webadmin83', 'webadmin84', 'webadmin85', 'webadmin86',
            'webadmin87', 'webadmin88', 'webadmin89', 'webadmin90', 'webadmin91',
            'webadmin92', 'webadmin93', 'webadmin94', 'webadmin95', 'webadmin96',
            'webadmin97', 'webadmin98', 'webadmin99', 'webadmin100'
        ]
        
        common_dirs = [
            'images', 'img', 'css', 'js', 'javascript', 'scripts', 'assets',
            'static', 'media', 'uploads', 'downloads', 'files', 'docs',
            'documents', 'pdf', 'images', 'pics', 'photos', 'gallery',
            'blog', 'news', 'articles', 'posts', 'forum', 'forums',
            'shop', 'store', 'cart', 'checkout', 'payment', 'pay',
            'account', 'accounts', 'user', 'users', 'member', 'members',
            'profile', 'profiles', 'settings', 'config', 'configuration',
            'api', 'rest', 'xml', 'json', 'rss', 'feed', 'atom',
            'search', 'find', 'query', 'results', 'sitemap', 'robots',
            'backup', 'backups', 'old', 'archive', 'archives', 'temp',
            'tmp', 'cache', 'cached', 'logs', 'log', 'error', 'errors',
            '404', '500', 'maintenance', 'maintenance-mode', 'offline',
            'test', 'testing', 'dev', 'development', 'staging', 'beta',
            'alpha', 'demo', 'demos', 'example', 'examples', 'sample',
            'samples', 'help', 'support', 'contact', 'about', 'info',
            'information', 'privacy', 'terms', 'legal', 'sitemap',
            'robots.txt', 'favicon.ico', 'apple-touch-icon.png'
        ]
        
        sensitive_dirs = [
            'admin', 'administrator', 'admin1', 'admin2', 'admin-panel',
            'admin_area', 'admin_area_new', 'admin_area_old', 'admin_area2',
            'admin_login', 'administrator', 'administrator_accounts',
            'administrators', 'admins', 'adm', 'ad', 'login', 'logon',
            'signin', 'sign-in', 'auth', 'authentication', 'secure',
            'security', 'panel', 'cpanel', 'webadmin', 'webmaster',
            'phpmyadmin', 'mysql', 'database', 'db', 'sql', 'oracle',
            'postgres', 'mssql', 'backup', 'backups', 'bak', 'old',
            'archive', 'archives', 'temp', 'tmp', 'cache', 'logs',
            'log', 'error', 'errors', 'config', 'configuration',
            'conf', 'settings', 'setup', 'install', 'installation',
            'update', 'upgrade', 'maintenance', 'maintenance-mode',
            'debug', 'debugging', 'test', 'testing', 'dev', 'development',
            'staging', 'beta', 'alpha', 'demo', 'demos', 'example',
            'examples', 'sample', 'samples', 'private', 'secret',
            'hidden', 'internal', 'intranet', 'vpn', 'remote', 'ssh',
            'ftp', 'sftp', 'telnet', 'shell', 'bash', 'root', 'sudo',
            'su', 'passwd', 'password', 'pwd', 'shadow', 'htpasswd',
            '.htaccess', '.htpasswd', '.env', 'config.php', 'config.ini',
            'wp-config.php', 'config.json', 'secrets', 'credentials',
            'keys', 'certificates', 'certs', 'ssl', 'tls', 'ssh_keys',
            'private_keys', 'public_keys', 'id_rsa', 'id_dsa', 'id_ecdsa',
            'id_ed25519', 'authorized_keys', 'known_hosts', 'hosts',
            'hosts.allow', 'hosts.deny', 'passwd', 'group', 'shadow',
            'gshadow', 'sudoers', 'fstab', 'mtab', 'crontab', 'cron',
            'anacrontab', 'at.allow', 'at.deny', 'cron.allow', 'cron.deny'
        ]
        
        # Crear wordlists
        self.create_wordlist('admin', admin_words)
        self.create_wordlist('common', common_dirs)
        self.create_wordlist('sensitive', sensitive_dirs)
        
        print("✅ Wordlists comunes creadas:")
        print("   - admin.txt (directorios administrativos)")
        print("   - common.txt (directorios comunes)")
        print("   - sensitive.txt (directorios sensibles)")

def main():
    parser = argparse.ArgumentParser(
        description="Herramienta de configuración para DirForcer Pro",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python config.py --setup
  python config.py --show
  python config.py --update default_threads 20
  python config.py --create-wordlists
        """
    )
    
    parser.add_argument('--setup', action='store_true',
                       help='Configurar directorio y archivo de configuración inicial')
    parser.add_argument('--show', action='store_true',
                       help='Mostrar configuración actual')
    parser.add_argument('--update', nargs=2, metavar=('KEY', 'VALUE'),
                       help='Actualizar un valor específico en la configuración')
    parser.add_argument('--create-wordlists', action='store_true',
                       help='Crear wordlists comunes predefinidas')
    
    args = parser.parse_args()
    
    config = DirForcerConfig()
    
    if args.setup:
        config.setup_config()
    elif args.show:
        config.show_config()
    elif args.update:
        key, value = args.update
        # Intentar convertir el valor a tipo apropiado
        try:
            if value.lower() in ['true', 'false']:
                value = value.lower() == 'true'
            elif value.isdigit():
                value = int(value)
            elif value.startswith('[') and value.endswith(']'):
                value = [int(x.strip()) for x in value[1:-1].split(',')]
        except:
            pass
        config.update_config(key, value)
    elif args.create_wordlists:
        config.create_common_wordlists()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
