#!/bin/bash

clear
echo "Verificando Python3..."
sleep 2

sudo apt update
sudo apt install python3

clear

echo "Verificando Permisão..."
sleep 2

clear

chmod 744 Calculadora.sh
chmod 744 Atividade.py

python3 Atividade.py
