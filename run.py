# run.py
import os
import sys

# Adiciona a raiz do projeto ao sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from scripts.populate_db import main

if __name__ == "__main__":
    print("🔄 Executando script populate_db.py...")
    main()
    print("✅ Script concluído com sucesso.")
