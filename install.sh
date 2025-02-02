#!/bin/bash

# Verificando permissões de root
if [[ $EUID -ne 0 ]]; then
    echo "[!] Este script deve ser executado como root!"
    exit 1
fi

echo "[+] Atualizando pacotes e instalando dependências..."
if command -v apt > /dev/null; then
    sudo apt update && sudo apt install -y python3 python3-pip git tor nmap hydra
elif command -v pacman > /dev/null; then
    sudo pacman -Syu --noconfirm python python-pip git tor nmap hydra
elif command -v pkg > /dev/null; then
    pkg update && pkg install -y python python-pip git tor nmap hydra
else
    echo "[!] Gerenciador de pacotes não suportado! Instale as dependências manualmente."
    exit 1
fi

echo "[+] Instalando bibliotecas Python..."
pip3 install -r requirements.txt

echo "[+] Configuração concluída! Execute 'python3 OmniSec3000.py' para iniciar."
