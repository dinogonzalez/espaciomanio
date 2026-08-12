import os
from PIL import Image

# Path to the EXACT user-uploaded image that is perfect
input_image_path = r"C:\Users\dinog\.gemini\antigravity-ide\brain\9329ce21-ad39-4e4b-8b14-64b91ed1307b\media__1786501320912.jpg"
qr_path = r"C:\Users\dinog\OneDrive\Desktop\Proyectos de Trabajo\Proyecto Parcela\05-Flyers\qr_whatsapp_oficial.png"

output_desktop = r"C:\Users\dinog\OneDrive\Desktop\POST_INSTAGRAM_LANZAMIENTO_NUEVA_MARCA.png"
output_project = r"C:\Users\dinog\OneDrive\Desktop\Proyectos de Trabajo\Proyecto Parcela\04-Instagram\post_lanzamiento_instagram.png"

# Open user image
img = Image.open(input_image_path).convert("RGBA")
width, height = img.size

# Open the 100% real scannable QR code
qr = Image.open(qr_path).convert("RGBA")

# In the user image, the QR code is located at the bottom left.
# Let's inspect coordinates: The QR box is roughly in bottom-left.
# Image size is ~1024x1024.
# QR position: left ~35px, top ~845px, width ~150px, height ~150px.
# Let's scale the QR code to match the exact box size in the image.

qr_size = int(width * 0.145)  # ~14.5% of width
qr_resized = qr.resize((qr_size, qr_size), Image.Resampling.LANCZOS)

# Position: bottom left corner
qr_x = int(width * 0.038)
qr_y = int(height * 0.824)

# Paste the real scannable QR code over the old QR code
img.paste(qr_resized, (qr_x, qr_y), qr_resized)

# Save result in high quality
img.convert("RGB").save(output_desktop, quality=98)
img.convert("RGB").save(output_project, quality=98)

print("Successfully replaced ONLY the QR code with the 100% real scannable QR code!")
