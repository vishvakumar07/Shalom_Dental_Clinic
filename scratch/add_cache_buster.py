import os

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Define replacements
    replacements = {
        'src="assets/img/shalom-logo.svg"': 'src="assets/img/shalom-logo.svg?v=2"',
        'src="assets/img/shalom-logo-dark.svg"': 'src="assets/img/shalom-logo-dark.svg?v=2"',
        'href="assets/img/favicon.svg"': 'href="assets/img/favicon.svg?v=2"',
        'href="assets/img/webclip.png"': 'href="assets/img/webclip.png?v=2"'
    }
    
    changed = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changed = True
            
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added cache-buster in: {file_path}")

def main():
    paths = [
        "e:\\lumora-dental",
        "e:\\lumora-dental\\variant-blue"
    ]
    
    for base_path in paths:
        for file in os.listdir(base_path):
            if file.endswith(".html"):
                full_path = os.path.join(base_path, file)
                process_file(full_path)

if __name__ == "__main__":
    main()
