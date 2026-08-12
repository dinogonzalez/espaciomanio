import qrcode
from PIL import Image

# WhatsApp URL encoding phone +56 9 8888 6174
target_url = "https://wa.me/56988886174?text=Hola%20Espacio%20Ma%C3%B1io,%20quisiera%20consultar%20por%20valores%20y%20fechas%20disponibles"

# Configure QR Code parameters for maximum scannability
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=2,
)
qr.add_data(target_url)
qr.make(fit=True)

# Create crisp black & white QR code
img = qr.make_image(fill_color="#071426", back_color="white")

# Save as PNG
output_path = r"C:\Users\dinog\OneDrive\Desktop\Proyectos de Trabajo\Proyecto Parcela\05-Flyers\qr_whatsapp_oficial.png"
img.save(output_path)
print(f"QR code successfully generated and saved at: {output_path}")
