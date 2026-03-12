import glob
import re

for filename in glob.glob("*.html"):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace email mentions
    content = content.replace("info@riogarona.com", "info@rginversores.com")

    # 2. In jumbotron/footer, append the email
    # Let's find the footer paragraph and replace it to add the email
    footer_pattern = r'(<p class="text-gray-400 leading-relaxed mb-)8( max-w-sm mx-auto">\s*Líderes en el mercado inmobiliario nacional con una red de oficinas propias dedicadas a la\s*excelencia en el servicio al cliente con Rio Garona\.\s*</p>)'
    
    replacement = r'\g<1>4\g<2>\n                    <p class="text-gold font-bold mb-8">\n                        <a href="mailto:info@rginversores.com" class="hover:text-white transition-colors"><i class="fas fa-envelope mr-2"></i> info@rginversores.com</a>\n                    </p>'
    
    new_content = re.sub(footer_pattern, replacement, content)

    if content != new_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        # If it didn't change, just write the basic email replacements anyway
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print("Email update complete.")
