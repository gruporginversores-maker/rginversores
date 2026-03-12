import glob
import os

files_to_check = glob.glob("*.html") + ['sitemap.xml', 'robots.txt']

for filename in files_to_check:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Reemplazar dominio en urls, etiquetas canonical, og:url, og:image, schema markup, etc.
        new_content = content.replace("riogarona.com", "rginversores.com")

        if content != new_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Updated {filename}")

print("Domain update complete.")
