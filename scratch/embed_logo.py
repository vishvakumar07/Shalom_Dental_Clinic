import base64
import os

def main():
    img_path = r"e:\lumora-dental\assets\img\shalom-logo-icon.jpg"
    if not os.path.exists(img_path):
        print(f"Error: image not found at {img_path}")
        return

    with open(img_path, "rb") as f:
        img_data = f.read()
    
    b64_str = base64.b64encode(img_data).decode("utf-8")
    data_url = f"data:image/jpeg;base64,{b64_str}"

    # 1. shalom-logo.svg (Light theme)
    logo_light = f"""<svg xmlns="http://www.w3.org/2000/svg" width="260" height="40" viewBox="0 0 260 40" fill="none" role="img" aria-label="Shalom Multispecialist Clinic">
  <defs>
    <clipPath id="circleView">
      <circle cx="20" cy="20" r="18" />
    </clipPath>
  </defs>
  <!-- White background circle for the logo -->
  <circle cx="20" cy="20" r="19" fill="#ffffff" stroke="#e0e5e4" stroke-width="1"/>
  <!-- Image -->
  <image href="{data_url}" x="1" y="1" width="38" height="38" clip-path="url(#circleView)" />
  <!-- Clinic Name Text -->
  <text x="48" y="19" font-family="Sora, 'Helvetica Neue', Arial, sans-serif" font-size="15" font-weight="700" letter-spacing="-0.2" fill="#011f23">SHALOM</text>
  <text x="48" y="32" font-family="Sora, 'Helvetica Neue', Arial, sans-serif" font-size="8" font-weight="600" letter-spacing="0.5" fill="#5d6c7b" opacity="0.8">MULTISPECIALIST CLINIC</text>
</svg>"""

    # 2. shalom-logo-dark.svg (Dark theme / Footer)
    logo_dark = f"""<svg xmlns="http://www.w3.org/2000/svg" width="260" height="40" viewBox="0 0 260 40" fill="none" role="img" aria-label="Shalom Multispecialist Clinic">
  <defs>
    <clipPath id="circleView">
      <circle cx="20" cy="20" r="18" />
    </clipPath>
  </defs>
  <!-- White background circle for the logo -->
  <circle cx="20" cy="20" r="19" fill="#ffffff" stroke="#e0e5e4" stroke-width="1"/>
  <!-- Image -->
  <image href="{data_url}" x="1" y="1" width="38" height="38" clip-path="url(#circleView)" />
  <!-- Clinic Name Text (White) -->
  <text x="48" y="19" font-family="Sora, 'Helvetica Neue', Arial, sans-serif" font-size="15" font-weight="700" letter-spacing="-0.2" fill="#ffffff">SHALOM</text>
  <text x="48" y="32" font-family="Sora, 'Helvetica Neue', Arial, sans-serif" font-size="8" font-weight="600" letter-spacing="0.5" fill="#ffffff" opacity="0.8">MULTISPECIALIST CLINIC</text>
</svg>"""

    # 3. variant-blue shalom-logo.svg (Blue Variant Light theme)
    logo_light_blue = f"""<svg xmlns="http://www.w3.org/2000/svg" width="260" height="40" viewBox="0 0 260 40" fill="none" role="img" aria-label="Shalom Multispecialist Clinic">
  <defs>
    <clipPath id="circleView">
      <circle cx="20" cy="20" r="18" />
    </clipPath>
  </defs>
  <!-- White background circle for the logo -->
  <circle cx="20" cy="20" r="19" fill="#ffffff" stroke="#e0e5e4" stroke-width="1"/>
  <!-- Image -->
  <image href="{data_url}" x="1" y="1" width="38" height="38" clip-path="url(#circleView)" />
  <!-- Clinic Name Text -->
  <text x="48" y="19" font-family="Sora, 'Helvetica Neue', Arial, sans-serif" font-size="15" font-weight="700" letter-spacing="-0.2" fill="#06182e">SHALOM</text>
  <text x="48" y="32" font-family="Sora, 'Helvetica Neue', Arial, sans-serif" font-size="8" font-weight="600" letter-spacing="0.5" fill="#5d6c7b" opacity="0.8">MULTISPECIALIST CLINIC</text>
</svg>"""

    # 4. variant-blue shalom-logo-dark.svg (Blue Variant Dark theme / Footer)
    logo_dark_blue = logo_dark  # Same white text fits variant-blue dark background perfectly

    # 5. favicon.svg (Circle cropped logo favicon)
    favicon = f"""<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" fill="none">
  <defs>
    <clipPath id="circleView">
      <circle cx="32" cy="32" r="30" />
    </clipPath>
  </defs>
  <!-- Background Circle border -->
  <circle cx="32" cy="32" r="32" fill="#ffffff"/>
  <!-- Image -->
  <image href="{data_url}" x="2" y="2" width="60" height="60" clip-path="url(#circleView)" />
</svg>"""

    # Save files
    files = {
        r"e:\lumora-dental\assets\img\shalom-logo.svg": logo_light,
        r"e:\lumora-dental\assets\img\shalom-logo-dark.svg": logo_dark,
        r"e:\lumora-dental\variant-blue\assets\img\shalom-logo.svg": logo_light_blue,
        r"e:\lumora-dental\variant-blue\assets\img\shalom-logo-dark.svg": logo_dark_blue,
        r"e:\lumora-dental\assets\img\favicon.svg": favicon,
        r"e:\lumora-dental\variant-blue\assets\img\favicon.svg": favicon,
    }

    for path, content in files.items():
        # Ensure directories exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {path}")

if __name__ == "__main__":
    main()
