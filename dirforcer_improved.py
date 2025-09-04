#!/usr/bin/env python3
"""
DirForcer Pro - Herramienta profesional de enumeración de directorios
Versión mejorada con funcionalidades avanzadas y mejores prácticas de seguridad

Desarrollado por: NEZUKO
Versión: 2.0 Pro
"""

import requests
import time
import argparse
import random
import sys
import os
import json
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlparse
from datetime import datetime
import logging
from pyfiglet import Figlet
from colorama import init, Fore, Style
import signal

# Inicializar colorama para compatibilidad cross-platform
init(autoreset=True)

class DirForcerPro:
    def __init__(self):
        self.session = requests.Session()
        self.found_dirs = []
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.start_time = None
        self.stop_scanning = False
        
        # Configurar logging
        self.setup_logging()
        
        # Configurar signal handlers para interrupción elegante
        signal.signal(signal.SIGINT, self.signal_handler)
        
    def setup_logging(self):
        """Configurar sistema de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('dirforcer.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def signal_handler(self, signum, frame):
        """Manejar interrupción del usuario (Ctrl+C)"""
        print(f"\n{Fore.YELLOW}[!] Interrupción detectada. Finalizando escaneo...{Style.RESET_ALL}")
        self.stop_scanning = True
    
    def validate_url(self, url):
        """Validar y normalizar URL"""
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        try:
            parsed = urlparse(url)
            if not parsed.netloc:
                raise ValueError("URL inválida")
            return url.rstrip('/')
        except Exception as e:
            self.logger.error(f"URL inválida: {url}")
            return None
    
    def setup_session(self, user_agent=None, timeout=10, verify_ssl=True):
        """Configurar sesión de requests con headers personalizados"""
        if user_agent:
            self.session.headers.update({'User-Agent': user_agent})
        else:
            # User-Agent por defecto que simula un navegador real
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            })
        
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        self.session.timeout = timeout
        self.session.verify = verify_ssl
    
    def check_directory(self, base_url, directory, status_codes=None, delay=0):
        """Verificar si un directorio existe"""
        if self.stop_scanning:
            return None
            
        url = urljoin(base_url + '/', directory)
        
        try:
            # Aplicar delay si se especifica
            if delay > 0:
                time.sleep(delay)
            
            response = self.session.get(url, allow_redirects=False)
            self.total_requests += 1
            
            # Verificar códigos de estado de interés
            if status_codes is None:
                status_codes = [200, 301, 302, 403, 401]
            
            if response.status_code in status_codes:
                self.successful_requests += 1
                result = {
                    'url': url,
                    'status_code': response.status_code,
                    'content_length': len(response.content),
                    'directory': directory
                }
                self.found_dirs.append(result)
                return result
            else:
                self.failed_requests += 1
                return None
                
        except requests.exceptions.RequestException as e:
            self.failed_requests += 1
            self.logger.debug(f"Error al verificar {url}: {e}")
            return None
    
    def load_wordlist(self, wordlist_path):
        """Cargar wordlist desde archivo"""
        try:
            with open(wordlist_path, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip() and not line.startswith('#')]
        except FileNotFoundError:
            self.logger.error(f"Archivo de wordlist no encontrado: {wordlist_path}")
            return []
        except Exception as e:
            self.logger.error(f"Error al cargar wordlist: {e}")
            return []
    
    def print_banner(self):
        """Mostrar banner de la herramienta"""
        # Detectar si estamos en Kali Linux
        is_kali = False
        try:
            with open('/etc/os-release', 'r') as f:
                content = f.read()
                if 'kali' in content.lower():
                    is_kali = True
        except:
            pass
        
        colors = [Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.RED]
        
        if is_kali:
            # Banner especial para Kali Linux con NEZUKO en grande
            f_large = Figlet(font='big')
            f_medium = Figlet(font='digital')
            
            # Limpiar pantalla (opcional)
            os.system('clear' if os.name == 'posix' else 'cls')
            
            # Banner principal con NEZUKO
            print(random.choice(colors) + f_large.renderText('NEZUKO') + Style.RESET_ALL)
            
            # Marco decorativo con estilo hacker
            print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}║                    🐍 DIRFORCER PRO v2.0 🐍                               ║{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}║              ⚡ Herramienta de Enumeración Avanzada ⚡                    ║{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
            
            # Información adicional con emojis
            print(f"{Fore.CYAN}🐍 Optimizado para Kali Linux - Entorno de Pentesting{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}⚡ Desarrollado con mejores prácticas de seguridad{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}🔥 Desarrollado por: NEZUKO - Versión 2.0 Pro{Style.RESET_ALL}")
            print(f"{Fore.GREEN}🎯 Listo para descubrir directorios ocultos{Style.RESET_ALL}")
            print(f"{Fore.RED}💀 Uso ético y responsable requerido{Style.RESET_ALL}")
            
            # Separador con estilo
            print(f"{Fore.MAGENTA}─" * 70 + Style.RESET_ALL)
            
            # Mensaje de bienvenida
            print(f"{Fore.CYAN}¡Bienvenido al entorno de pentesting de NEZUKO!{Style.RESET_ALL}")
            print("")
        else:
            # Banner estándar para otros sistemas
            f = Figlet(font='digital')
            print(random.choice(colors) + f.renderText('DirForcer Pro') + Style.RESET_ALL)
            print(f"{Fore.CYAN}Versión mejorada - Herramienta profesional de enumeración de directorios{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Desarrollado con mejores prácticas de seguridad{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}Desarrollado por: NEZUKO - Versión 2.0 Pro{Style.RESET_ALL}")
        
        print("")
    
    def print_progress(self, current, total):
        """Mostrar barra de progreso"""
        percentage = (current / total) * 100
        bar_length = 50
        filled_length = int(bar_length * current // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        
        print(f"\r{Fore.CYAN}Progreso: [{bar}] {percentage:.1f}% ({current}/{total}){Style.RESET_ALL}", end='')
        sys.stdout.flush()
    
    def print_results(self, results, output_file=None):
        """Mostrar resultados del escaneo"""
        print(f"\n\n{Fore.GREEN}=== RESULTADOS DEL ESCANEO ==={Style.RESET_ALL}")
        print(f"{Fore.CYAN}Total de directorios encontrados: {len(results)}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Total de requests: {self.total_requests}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Requests exitosos: {self.successful_requests}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Requests fallidos: {self.failed_requests}{Style.RESET_ALL}")
        
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            print(f"{Fore.CYAN}Tiempo total: {elapsed_time:.2f} segundos{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}Directorios encontrados:{Style.RESET_ALL}")
        
        # Agrupar por código de estado
        status_groups = {}
        for result in results:
            status = result['status_code']
            if status not in status_groups:
                status_groups[status] = []
            status_groups[status].append(result)
        
        for status_code in sorted(status_groups.keys()):
            color = Fore.GREEN if status_code == 200 else Fore.YELLOW if status_code in [301, 302] else Fore.RED
            print(f"\n{color}[{status_code}] - {len(status_groups[status_code])} directorios:{Style.RESET_ALL}")
            
            for result in status_groups[status_code]:
                print(f"  {result['url']} ({result['content_length']} bytes)")
        
        # Guardar resultados en archivo si se especifica
        if output_file:
            self.save_results(results, output_file)
    
    def save_results(self, results, output_file):
        """Guardar resultados en archivo"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'scan_time': datetime.now().isoformat(),
                    'total_found': len(results),
                    'total_requests': self.total_requests,
                    'successful_requests': self.successful_requests,
                    'failed_requests': self.failed_requests,
                    'results': results
                }, f, indent=2)
            print(f"\n{Fore.GREEN}Resultados guardados en: {output_file}{Style.RESET_ALL}")
        except Exception as e:
            self.logger.error(f"Error al guardar resultados: {e}")
    
    def scan(self, target_url, wordlist_path, **kwargs):
        """Realizar escaneo de directorios"""
        # Validar URL
        target_url = self.validate_url(target_url)
        if not target_url:
            return False
        
        # Cargar wordlist
        directories = self.load_wordlist(wordlist_path)
        if not directories:
            return False
        
        # Configurar sesión
        self.setup_session(
            user_agent=kwargs.get('user_agent'),
            timeout=kwargs.get('timeout', 10),
            verify_ssl=kwargs.get('verify_ssl', True)
        )
        
        # Configurar parámetros
        max_workers = kwargs.get('threads', 10)
        delay = kwargs.get('delay', 0)
        status_codes = kwargs.get('status_codes', [200, 301, 302, 403, 401])
        
        print(f"{Fore.BLUE}Objetivo: {target_url}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Wordlist: {wordlist_path} ({len(directories)} entradas){Style.RESET_ALL}")
        print(f"{Fore.BLUE}Threads: {max_workers}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Delay: {delay} segundos{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Códigos de estado de interés: {status_codes}{Style.RESET_ALL}\n")
        
        self.start_time = time.time()
        
        # Realizar escaneo con threads
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            
            for i, directory in enumerate(directories):
                if self.stop_scanning:
                    break
                    
                future = executor.submit(
                    self.check_directory, 
                    target_url, 
                    directory, 
                    status_codes, 
                    delay
                )
                futures.append(future)
                
                # Mostrar progreso cada 10 requests
                if (i + 1) % 10 == 0:
                    self.print_progress(i + 1, len(directories))
            
            # Esperar resultados
            for future in as_completed(futures):
                if self.stop_scanning:
                    break
                result = future.result()
                if result:
                    print(f"\n{Fore.GREEN}[+] Encontrado: {result['url']} ({result['status_code']}){Style.RESET_ALL}")
        
        return True

def main():
    parser = argparse.ArgumentParser(
        description="DirForcer Pro - Herramienta profesional de enumeración de directorios (Desarrollado por NEZUKO)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python dirforcer_improved.py -d example.com -w directorios.txt
  python dirforcer_improved.py -d https://example.com -w wordlist.txt -t 20 -o results.json
  python dirforcer_improved.py -d example.com -w common.txt --delay 0.1 --status-codes 200 403

Desarrollado por: NEZUKO
Versión: 2.0 Pro
        """
    )
    
    parser.add_argument("-d", "--domain", dest="domain", required=True,
                       help="Dominio objetivo para escanear")
    parser.add_argument("-w", "--wordlist", dest="wordlist", required=True,
                       help="Archivo de wordlist con directorios a probar")
    parser.add_argument("-t", "--threads", dest="threads", type=int, default=10,
                       help="Número de threads concurrentes (default: 10)")
    parser.add_argument("--delay", dest="delay", type=float, default=0,
                       help="Delay entre requests en segundos (default: 0)")
    parser.add_argument("--timeout", dest="timeout", type=int, default=10,
                       help="Timeout para requests en segundos (default: 10)")
    parser.add_argument("--user-agent", dest="user_agent",
                       help="User-Agent personalizado")
    parser.add_argument("--no-ssl-verify", dest="verify_ssl", action="store_false",
                       help="No verificar certificados SSL")
    parser.add_argument("--status-codes", dest="status_codes", nargs="+", type=int,
                       default=[200, 301, 302, 403, 401],
                       help="Códigos de estado HTTP de interés (default: 200 301 302 403 401)")
    parser.add_argument("-o", "--output", dest="output_file",
                       help="Archivo de salida para guardar resultados (JSON)")
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true",
                       help="Modo verbose para más información")
    
    args = parser.parse_args()
    
    # Configurar logging según verbosidad
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Crear instancia y mostrar banner
    dirforcer = DirForcerPro()
    dirforcer.print_banner()
    
    # Realizar escaneo
    success = dirforcer.scan(
        target_url=args.domain,
        wordlist_path=args.wordlist,
        threads=args.threads,
        delay=args.delay,
        timeout=args.timeout,
        user_agent=args.user_agent,
        verify_ssl=args.verify_ssl,
        status_codes=args.status_codes
    )
    
    if success:
        dirforcer.print_results(dirforcer.found_dirs, args.output_file)
    else:
        print(f"{Fore.RED}Error durante el escaneo. Revisa los logs para más detalles.{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
