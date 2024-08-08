import socket

def port_scanner(target, ports):
    clcoding = socket.gethostbyname(target)
    print(f"Scanning {target} ({clcoding})")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((clcoding, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

# Example usage
target = "clcoding.com"
ports = [22, 80, 443, 8080]
port_scanner(target, ports)


'''
Explicación del Código:
Importación de la Biblioteca socket:

import socket: Importa la biblioteca socket, que proporciona acceso a la API de red de bajo nivel.
Función port_scanner:

Parámetros:
target: El dominio o dirección IP del objetivo.
ports: Una lista de puertos a escanear en el objetivo.
Resolución de Nombre de Host:
clcoding = socket.gethostbyname(target): Convierte el nombre de dominio del objetivo en una dirección IP.
Bucle para Escaneo de Puertos:
Itera sobre cada puerto en la lista ports y crea un socket para intentar conectarse a ese puerto.
sock.connect_ex((clcoding, port)): Intenta conectar al puerto en la dirección IP del objetivo.
Si la conexión tiene éxito (result == 0), el puerto se reporta como "Open".
Uso Ejemplo:

Se escanean los puertos 22, 80, 443, y 8080 en el dominio clcoding.com.
Pasos para Usar este Código:
Guardar el Código:

Copia el código en un archivo Python, por ejemplo, port_scanner.py.
Ejecutar el Código:

Ejecuta el archivo desde la terminal: python port_scanner.py.

'''
# ---------------------------------------
# ---------------------------------------
# ---------------------------------------
'''
Puertos Comunes para Escanear
Algunos puertos que son interesantes para escanear incluyen:

80 (HTTP): Usado para tráfico web sin cifrar.
443 (HTTPS): Usado para tráfico web cifrado.
22 (SSH): Usado para conexiones seguras a servidores.
21 (FTP): Usado para transferencias de archivos.
25 (SMTP): Usado para enviar correos electrónicos.
53 (DNS): Usado para resolver nombres de dominio.
3389 (RDP): Usado para acceso remoto a escritorios.
Escanear Peticiones de un Navegador
Si quieres ver las peticiones que hace el navegador Chrome, en lugar de escanear puertos, lo que realmente quieres hacer es capturar el tráfico de red que genera el navegador. Aquí hay algunos métodos que puedes utilizar:

1. Herramientas de Desarrollador en Chrome:
Chrome tiene una excelente herramienta incorporada para inspeccionar las solicitudes de red:

Abre Chrome y navega a cualquier sitio web.
Haz clic derecho en la página y selecciona Inspeccionar o presiona Ctrl+Shift+I.
Ve a la pestaña Network (Red).
Aquí verás todas las peticiones que Chrome está realizando, incluyendo el tipo de archivo, método HTTP, tiempo de carga, etc.
2. Wireshark:
Wireshark es una herramienta de análisis de red que te permite capturar y analizar paquetes de red en tiempo real.

Instalación:

Descárgalo desde wireshark.org.
Captura de Tráfico:

Abre Wireshark y selecciona la interfaz de red desde la cual quieres capturar tráfico (por ejemplo, la conexión Wi-Fi).
Filtra por "http" o "tcp.port == 443" para ver solo las peticiones HTTP/HTTPS.
Inicia la captura y luego abre Chrome y navega como lo harías normalmente.
Análisis:

Wireshark te permitirá ver todas las conexiones que el navegador hace, incluidos los puertos utilizados y los datos intercambiados.
Consideraciones Éticas y Legales
Es importante recordar que escanear puertos o capturar tráfico de red sin permiso puede ser ilegal o una violación de términos de servicio. Asegúrate de que tienes el permiso adecuado para realizar estas acciones, especialmente si no estás analizando tu propio tráfico o infraestructura.
'''