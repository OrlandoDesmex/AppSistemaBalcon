import re

def update_styles():
    with open('styles.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # Root variables
    css = re.sub(
        r':root \{.*?\n\}',
        """:root {
    --bg-gradient: linear-gradient(135deg, #e5e7eb 0%, #cbd5e1 100%);
    --glass-bg: rgba(255, 255, 255, 0.65);
    --glass-border: rgba(255, 255, 255, 0.4);
    --primary: #d16b7a; /* Institucional Rosa/Coral */
    --balcony: #5c5e60; /* Institucional Gris Oscuro */
    --text-main: #1e293b;
    --text-muted: #64748b;
    --accent: #d16b7a;
    --border-color: #334155;
}""",
        css, flags=re.DOTALL
    )

    css = css.replace(
        'background: linear-gradient(to right, #f8fafc, #94a3b8);',
        'background: linear-gradient(to right, #1e293b, #475569);'
    )
    css = css.replace(
        'background: rgba(0, 0, 0, 0.2);',
        'background: rgba(255, 255, 255, 0.3);'
    )
    css = css.replace(
        'box-shadow: inset 0 4px 20px rgba(0,0,0,0.5);',
        'box-shadow: inset 0 4px 20px rgba(0,0,0,0.05);'
    )
    css = css.replace(
        'border: 2px dashed rgba(255, 255, 255, 0.15);',
        'border: 2px dashed rgba(0, 0, 0, 0.15);'
    )
    css = css.replace('rgba(255, 255, 255, 0.1)', 'rgba(0, 0, 0, 0.1)')
    css = css.replace('rgba(56, 189, 248, 0.4)', 'rgba(209, 107, 122, 0.4)')
    css = css.replace('rgba(56, 189, 248, 0.3)', 'rgba(209, 107, 122, 0.3)')
    css = css.replace('rgba(56, 189, 248, 0.6)', 'rgba(209, 107, 122, 0.6)')
    css = css.replace('rgba(56, 189, 248, 0.8)', 'rgba(209, 107, 122, 0.8)')
    css = css.replace('rgba(249, 115, 22, 0.3)', 'rgba(209, 107, 122, 0.3)')
    css = css.replace(
        'background: rgba(255, 255, 255, 0.15);',
        'background: rgba(0, 0, 0, 0.15);'
    )
    css = css.replace(
        'box-shadow: inset 0 1px 3px rgba(0,0,0,0.3);',
        'box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);'
    )
    css = css.replace(
        'background: rgba(0, 0, 0, 0.3);',
        'background: rgba(255, 255, 255, 0.5);'
    )
    css = css.replace('color: white;', 'color: var(--text-main);')
    css = css.replace(
        'border-color: rgba(255, 255, 255, 0.3);',
        'border-color: rgba(0, 0, 0, 0.2);'
    )
    css = css.replace('background-color: #1e293b;', 'background-color: #ffffff;')
    css = css.replace(
        'background: rgba(15, 23, 42, 0.5);',
        'background: rgba(255, 255, 255, 0.6);'
    )
    css = css.replace(
        'box-shadow: inset 0 2px 10px rgba(0,0,0,0.3);',
        'box-shadow: inset 0 2px 10px rgba(0,0,0,0.05);'
    )
    css = css.replace('color: #4ade80;', 'color: #16a34a;')
    css = css.replace('rgba(74, 222, 128, 0.3)', 'rgba(22, 163, 74, 0.2)')

    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(css)

    print("CSS actualizado a modo claro institucional")

update_styles()
