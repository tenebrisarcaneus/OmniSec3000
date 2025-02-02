import os
import sys
import subprocess
import argparse
import platform

class OmniSec3000:
    def __init__(self):
        self.modules = {
            "AutoSploit X": self.auto_sploit,
            "OmniPhish Hunter": self.omni_phish,
            "DarkInject": self.dark_inject,
            "VitaWeb Pentest": self.vitaweb_pentest,
            "BlackRAT 3000": self.black_rat,
            "PassBreaker AI": self.pass_breaker,
            "HybridCrack": self.hybrid_crack,
            "EtherHack": self.ether_hack,
            "TorXploit": self.tor_xploit,
            "AI Malware Analyzer": self.ai_malware_analyzer,
        }

    def install_dependencies(self):
        print("[+] Verificando e instalando dependências...")
        packages = ["python3", "python3-pip", "git", "tor", "nmap", "hydra"]
        os_system = platform.system()
        
        if os_system == "Linux":
            pkg_manager = "apt" if os.path.exists("/etc/debian_version") else "pacman"
            install_cmd = "install -y" if pkg_manager == "apt" else "-S --noconfirm"
            
            for package in packages:
                try:
                    subprocess.run(["sudo", pkg_manager, install_cmd, package], check=True)
                except subprocess.CalledProcessError:
                    print(f"[!] Falha ao instalar {package}, tentando força bruta...")
                    subprocess.run(["sudo", pkg_manager, install_cmd, package, "--force-reinstall", "--break-system-packages"], check=True)
        
        print("[+] Todas as dependências foram instaladas!")

    def auto_sploit(self):
        print("[+] Executando AutoSploit X...")
        subprocess.run(["python3", "modules/autosploit.py"])

    def omni_phish(self):
        print("[+] Iniciando OmniPhish Hunter...")
        subprocess.run(["python3", "modules/omniphish.py"])

    def dark_inject(self):
        print("[+] Iniciando DarkInject...")
        subprocess.run(["python3", "modules/darkinject.py"])

    def vitaweb_pentest(self):
        print("[+] Executando VitaWeb Pentest...")
        subprocess.run(["python3", "modules/vitaweb.py"])

    def black_rat(self):
        print("[+] Iniciando BlackRAT 3000...")
        subprocess.run(["python3", "modules/blackrat.py"])

    def pass_breaker(self):
        print("[+] Iniciando PassBreaker AI...")
        subprocess.run(["python3", "modules/passbreaker.py"])

    def hybrid_crack(self):
        print("[+] Iniciando HybridCrack...")
        subprocess.run(["python3", "modules/hybridcrack.py"])

    def ether_hack(self):
        print("[+] Iniciando EtherHack...")
        subprocess.run(["python3", "modules/etherhack.py"])

    def tor_xploit(self):
        print("[+] Executando TorXploit...")
        subprocess.run(["python3", "modules/torxploit.py"])

    def ai_malware_analyzer(self):
        print("[+] Iniciando AI Malware Analyzer...")
        subprocess.run(["python3", "modules/aimalware.py"])

    def run(self):
        while True:
            print("\n[OmniSec 3000] Escolha uma ferramenta:")
            for index, tool in enumerate(self.modules.keys(), start=1):
                print(f"{index}. {tool}")
            print("0. Sair")

            choice = input("Selecione uma opção: ")
            if choice == "0":
                print("[+] Saindo...")
                break
            
            try:
                selected_tool = list(self.modules.keys())[int(choice) - 1]
                self.modules[selected_tool]()
            except (IndexError, ValueError):
                print("[!] Escolha inválida, tente novamente.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cli", action="store_true", help="Modo terminal")
    parser.add_argument("--gui", action="store_true", help="Modo gráfico")
    args = parser.parse_args()
    
    omni_sec = OmniSec3000()
    omni_sec.install_dependencies()
    omni_sec.run()
