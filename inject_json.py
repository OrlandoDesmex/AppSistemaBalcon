import json

with open('data_dump.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix key names (remove encoding artifacts)
clean_data = {}
for potencia, rows in data.items():
    clean_rows = []
    for row in rows:
        clean_row = {}
        for key, value in row.items():
            clean_key = key.replace('OrientaciÃ³n', 'Orientación').replace('Ã³', 'ó')
            clean_row[clean_key] = value
        clean_rows.append(clean_row)
    clean_data[potencia] = clean_rows

data_json = json.dumps(clean_data, ensure_ascii=False, indent=2)

js_code = f"""
const calculosData = {data_json};

document.addEventListener('DOMContentLoaded', () => {{
    const slider = document.getElementById('rotation-slider');
    const degreeValue = document.getElementById('degree-value');
    const buildingWrapper = document.getElementById('building-wrapper');
    const potenciaSelect = document.getElementById('potencia');
    const tarifaSelect = document.getElementById('tarifa');
    const ahorroValue = document.getElementById('ahorro-value');

    function updateAhorro(degrees) {{
        const potencia = potenciaSelect.value + ' W';
        const tarifa = tarifaSelect.value;
        const tarifaKey = tarifa === '01' ? ' Ahorro tarifa 01' : 'Ahorro tarifa DAC';

        const dataForPotencia = calculosData[potencia];
        if (dataForPotencia) {{
            const dataRow = dataForPotencia.find(row => row['Orientación'] === parseInt(degrees, 10));
            if (dataRow && dataRow[tarifaKey] !== undefined) {{
                const formatter = new Intl.NumberFormat('es-MX', {{
                    style: 'currency',
                    currency: 'MXN'
                }});
                ahorroValue.textContent = formatter.format(dataRow[tarifaKey]);
            }} else {{
                ahorroValue.textContent = '$0.00';
            }}
        }}
    }}

    function updateRotation(degrees) {{
        degreeValue.textContent = degrees;
        buildingWrapper.style.transform = `rotate(${{degrees}}deg)`;
        updateAhorro(degrees);
    }}

    slider.addEventListener('input', (e) => {{
        updateRotation(e.target.value);
    }});

    potenciaSelect.addEventListener('change', () => {{
        updateAhorro(slider.value);
    }});

    tarifaSelect.addEventListener('change', () => {{
        updateAhorro(slider.value);
    }});

    const compassContainer = document.querySelector('.compass-container');
    compassContainer.addEventListener('wheel', (e) => {{
        e.preventDefault();

        let currentValue = parseInt(slider.value, 10);
        const step = parseInt(slider.step, 10);

        if (e.deltaY > 0) {{
            currentValue = Math.min(parseInt(slider.max, 10), currentValue + step);
        }} else {{
            currentValue = Math.max(parseInt(slider.min, 10), currentValue - step);
        }}

        slider.value = currentValue;
        updateRotation(currentValue);
    }});

    updateRotation(slider.value);
}});
"""

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("JS actualizado exitosamente")
