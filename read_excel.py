import json
import sys

try:
    import pandas as pd
except ImportError:
    print("pandas no está instalado. Instalando...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "openpyxl"])
    import pandas as pd

def process_excel(file_path):
    try:
        xl = pd.ExcelFile(file_path)
        data = {}
        for sheet_name in xl.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            data[sheet_name] = df.to_dict(orient='records')

        with open('data_dump.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("EXITO")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    process_excel("Calculos.xlsx")
