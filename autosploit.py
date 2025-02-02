import os
import subprocess
import sys

def check_dependencies():
    print("[+] Verificando dependências...")
    required_tools = ["nmap", "msfconsole"]
    for tool in required_tools:
        if not shutil.which(tool):
            print(f"[!] {tool} não encontrado. Instalando...")
            install_dependency(tool)

def install_dependency(tool):
    try:
        if shutil.which("apt"):  # Debian-based
            subprocess.run(["sudo", "apt", "install", "-y", tool], check=True)
        elif shutil.which("pacman"):  # Arch-based
            subprocess.run(["sudo", "pacman", "-S", "--noconfirm", tool], check=True)
        elif shutil.which("pkg"):  # Termux
            subprocess.run(["pkg", "install", "-y", tool], check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Erro ao instalar {tool}. Tente instalar manualmente.")

def scan_target(target):
    print(f"[+] Escaneando {target} em busca de vulnerabilidades...")
    scan_results = subprocess.run(["nmap", "-sV", "-O", "--script=vuln", target], capture_output=True, text=True)
    print(scan_results.stdout)
    return scan_results.stdout

def exploit_target(target):
    print(f"[+] Tentando exploração automática no alvo {target}...")
    exploit_script = f"""
    use auxiliary/scanner/http/dir_scanner
    set RHOSTS {target}
    run
    exit
    """
    with open("autosploit.rc", "w") as f:
        f.write(exploit_script)
    subprocess.run(["msfconsole", "-q", "-r", "autosploit.rc"])
    os.remove("autosploit.rc")

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 autosploit.py <IP/Host>")
        sys.exit(1)
    target = sys.argv[1]
    check_dependencies()
    scan_results = scan_target(target)
    exploit_target(target)

if __name__ == "__main__":
    main()
