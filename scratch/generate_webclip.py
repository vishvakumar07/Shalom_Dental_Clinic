from PIL import Image

def main():
    img_path = r"e:\lumora-dental\assets\img\shalom-logo-icon.jpg"
    try:
        img = Image.open(img_path)
        # Resize to standard high-resolution webclip size (256x256)
        img_resized = img.resize((256, 256), Image.Resampling.LANCZOS)
        
        # Save PNG to both directories
        img_resized.save(r"e:\lumora-dental\assets\img\webclip.png", "PNG")
        img_resized.save(r"e:\lumora-dental\variant-blue\assets\img\webclip.png", "PNG")
        
        print("Generated: assets/img/webclip.png")
        print("Generated: variant-blue/assets/img/webclip.png")
    except Exception as e:
        print(f"Error generating webclip: {e}")

if __name__ == "__main__":
    main()
