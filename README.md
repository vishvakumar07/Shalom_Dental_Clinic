# Shalom Multispecialist Clinic Website

A highly polished, premium, and fully responsive static website designed for **Shalom Multispecialist Clinic**. The project features custom vector branding, multiple design variants, interactive GSAP scroll animations, and a seamless callback lead form integrated directly with WhatsApp.

---

## 🌟 Key Features

*   **Premium Modern Aesthetic**: Curated color palettes, sleek dark modes, drop-shadow card layouts, and premium Google Fonts (Sora) typography.
*   **Dual Theme Variants**:
    *   **Teal/Green Theme (Default)**: Located in the root folder, using clinical teal and dark forest elements (`#24a3b1` to `#011f23`).
    *   **Blue Theme Variant**: Located in the [variant-blue/](file:///E:/Shalom_Dental_Clinic/variant-blue) directory, styled with premium healthcare blues (`#2f80ff` to `#0b2a55`).
*   **Mobile-First Responsive Layout**: Stacked navigation headers, collapsing menus, and centered mobile footer cards with responsive layouts.
*   **GSAP-Powered Animations**: Interactive scroll-reveals and fluid section entry effects via customized GSAP timelines.
*   **Self-Contained Brand Assets**: All hospital emblem files (`.svg`) and tab icons (`favicon.svg`) use self-contained Base64 data strings to bypass external browser loading issues and ensure instant, crisp rendering.
*   **WhatsApp Lead Form Integration**: Booking forms collect patient details and automatically format and forward the callback request to the clinic's WhatsApp number (`+91 98842 25017`).
*   **Clean Static Architecture**: Light, fast-loading pages requiring zero compile times or complex node dependencies.

---

## 📂 Project Structure

```text
├── assets/
│   ├── css/
│   │   └── shalom.css         # Main stylesheet for Teal/Green theme
│   ├── img/
│   │   ├── shalom-logo.svg    # Light theme brand logo
│   │   ├── shalom-logo-dark.svg # Dark theme footer logo
│   │   ├── shalom-logo-icon.jpg # Source image file of hospital emblem
│   │   ├── favicon.svg        # Browser tab icon
│   │   └── webclip.png        # Mobile bookmark touch icon
│   └── js/
│       └── gsap.min.js        # Scroll animation scripts
│
├── variant-blue/              # Full variant of the site with Blue styling
│   ├── assets/
│   │   ├── css/
│   │   │   └── shalom.css     # Main stylesheet for Blue theme
│   │   └── img/               # Blue-themed brand images
│   ├── index.html
│   ├── about.html
│   ├── service.html
│   └── blog.html
│
├── scratch/                   # Developer helper utility scripts
│   ├── embed_logo.py          # Script to encode logo JPG as base64 into SVGs
│   ├── generate_webclip.py    # Script to resize source JPG to webclip PNG
│   └── add_cache_buster.py    # Script to append cache query parameters
│
├── index.html                 # Homepage (Default Teal)
├── about.html                 # Doctor Details Page
├── service.html               # Service Details Page
├── blog.html                  # Blog/News Page
├── privacy.html               # Privacy Policy
├── cookies.html               # Cookie Policy
└── terms.html                 # Terms of Service
```

---

## 🚀 How to Run the Website Locally

Since the site consists of standard static HTML, CSS, and JS files, it requires no build steps. 

### 1. Launch with VS Code Live Server (Recommended)
1. Open the project folder in VS Code.
2. Click **Go Live** in the bottom status bar, or right-click `index.html` and select **Open with Live Server**.
3. It will host the site on `http://127.0.0.1:5500/`.

### 2. Launch with Python
If you have Python installed, you can launch a local HTTP server by running this command in your terminal inside the project root:
```bash
python -m http.server 5500
```
Then open `http://localhost:5500/` in your web browser.

---

## 🛠 Developer Utilities (in `scratch/`)

We have included helper scripts in the `scratch/` directory to simplify rebranding and asset management:

### 1. Recompile SVGs with a New Logo Image (`embed_logo.py`)
If you ever change or update the hospital logo image:
1. Save your new logo JPG at `assets/img/shalom-logo-icon.jpg`.
2. Run:
   ```bash
   python scratch/embed_logo.py
   ```
   This script will read your new image, encode it as Base64, and compile all light theme logos, dark theme logos, and favicons inside both the root and blue variant folders.

### 2. Generate New Touch Webclips (`generate_webclip.py`)
To generate standard high-resolution bookmark touch icons (`webclip.png`) from your updated logo image, run:
```bash
python scratch/generate_webclip.py
```

### 3. Clear Browser Caches (`add_cache_buster.py`)
Browsers cache assets like favicons and SVG logos very aggressively. To force user browsers to immediately load your updated logo and webclip files, run:
```bash
python scratch/add_cache_buster.py
```
This appends a version parameter (e.g. `?v=2`) to the asset links in all HTML files, prompting browsers to reload them immediately.
