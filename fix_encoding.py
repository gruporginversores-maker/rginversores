import os
import glob

# Mapping for common UTF-8 Mojibake in Spanish
replacements = {
    'Ã¡': 'á',
    'Ã©': 'é',
    'Ã­': 'í', 
    'Ã³': 'ó',
    'Ãº': 'ú',
    'Ã\x81': 'Á',
    'Ã\x89': 'É',
    'Ã\x8d': 'Í',
    'Ã\x93': 'Ó',
    'Ã\x9a': 'Ú',
    'Ã±': 'ñ',
    'Ã\x91': 'Ñ',
    'Â¿': '¿',
    'Â¡': '¡',
    'â‚¬': '€',
    'Ã¼': 'ü',
    'Ã\x9c': 'Ü',
    'â€œ': '"',
    'â€\x9d': '"',
    'â€˜': "'",
    'â€™': "'",
    'â€“': '-',
    'â€”': '-',
    'Âº': 'º',
    'Âª': 'ª',
    'â€¢': '•',
    'Ã\xad': 'í',
    'Â´': '´',
    'Ã\x8f': 'Ï',
    'Â': ''
}

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for k, v in replacements.items():
        content = content.replace(k, v)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Replacement complete.")
