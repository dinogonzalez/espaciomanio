import os
from PIL import Image, ImageDraw, ImageFont

# Set up paths
base_dir = r"C:\Users\dinog\OneDrive\Desktop\Proyectos de Trabajo\Proyecto Parcela\05-Flyers"
logo_path = os.path.join(base_dir, "logo_espacio_manio_oficial.png")
pool_path = os.path.join(base_dir, "fotos_reales", "piscina_15x7.jpg")
green_path = os.path.join(base_dir, "fotos_reales", "pradera_flores_oficial.jpg")
qr_path = os.path.join(base_dir, "qr_whatsapp_oficial.png")
output_post = os.path.join(base_dir, "..", "04-Instagram", "post_lanzamiento_instagram.png")
desktop_post = r"C:\Users\dinog\OneDrive\Desktop\POST_INSTAGRAM_LANZAMIENTO_NUEVA_MARCA.png"

# Canvas 1080x1080
width, height = 1080, 1080
canvas = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(canvas)

# Fonts
try:
    font_bold = ImageFont.truetype("arialbd.ttf", 28)
    font_sub = ImageFont.truetype("arialbd.ttf", 22)
    font_small = ImageFont.truetype("arial.ttf", 20)
    font_phone = ImageFont.truetype("arialbd.ttf", 36)
except Exception:
    font_bold = ImageFont.load_default()
    font_sub = font_bold
    font_small = font_bold
    font_phone = font_bold

# 1. Header Bar (Top 150px)
header_bg = Image.new("RGB", (width, 150), "white")
canvas.paste(header_bg, (0, 0))

if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")
    logo.thumbnail((500, 130), Image.Resampling.LANCZOS)
    lx = (width - logo.width) // 2
    ly = (150 - logo.height) // 2
    canvas.paste(logo, (lx, ly), logo)

draw.line([(0, 150), (width, 150)], fill="#e2e8f0", width=3)

# 2. Hero Pool Photo (150px to 520px -> height 370px)
if os.path.exists(pool_path):
    pool_img = Image.open(pool_path).convert("RGB")
    # Resize & Crop to 1080x370
    p_ratio = pool_img.width / pool_img.height
    t_ratio = 1080 / 370
    if p_ratio > t_ratio:
        new_w = int(370 * p_ratio)
        pool_img = pool_img.resize((new_w, 370), Image.Resampling.LANCZOS)
        crop_x = (new_w - 1080) // 2
        pool_img = pool_img.crop((crop_x, 0, crop_x + 1080, 370))
    else:
        new_h = int(1080 / p_ratio)
        pool_img = pool_img.resize((1080, new_h), Image.Resampling.LANCZOS)
        crop_y = (new_h - 370) // 2
        pool_img = pool_img.crop((0, crop_y, 1080, crop_y + 370))
    canvas.paste(pool_img, (0, 150))

# 3. Teal Badge over Pool Bottom
badge_w, badge_h = 620, 48
bx = (width - badge_w) // 2
by = 496
draw.rounded_rectangle([bx, by, bx + badge_w, by + badge_h], radius=24, fill="#0284c7")
badge_text = "ESPECTACULAR PISCINA DE 15 X 7 METROS"
bbox = font_bold.getbbox(badge_text)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text((bx + (badge_w - tw)//2, by + (badge_h - th)//2 - 2), badge_text, fill="white", font=font_bold)

# 4. Green Area Photo (560px to 740px -> height 180px)
if os.path.exists(green_path):
    green_img = Image.open(green_path).convert("RGB")
    g_w, g_h = 1000, 170
    gx = (width - g_w) // 2
    gy = 560
    # resize green
    g_ratio = green_img.width / green_img.height
    t_g_ratio = g_w / g_h
    if g_ratio > t_g_ratio:
        nw = int(g_h * g_ratio)
        green_img = green_img.resize((nw, g_h), Image.Resampling.LANCZOS)
        cx = (nw - g_w) // 2
        green_img = green_img.crop((cx, 0, cx + g_w, g_h))
    else:
        nh = int(g_w / g_ratio)
        green_img = green_img.resize((g_w, nh), Image.Resampling.LANCZOS)
        cy = (nh - g_h) // 2
        green_img = green_img.crop((0, cy, g_w, cy + g_h))
    canvas.paste(green_img, (gx, gy))

# 5. Services Line Text (750px to 790px)
serv_text = "Piscina 15x7m  ·  Quincho  ·  Áreas Verdes  ·  Baños  ·  Estacionamiento"
sbox = font_bold.getbbox(serv_text)
stw = sbox[2] - sbox[0]
draw.text(((width - stw)//2, 755), serv_text, fill="#0f172a", font=font_bold)

# 6. CTA Button (805px to 865px)
cta_w, cta_h = 820, 60
cx_btn = (width - cta_w) // 2
cy_btn = 800
draw.rounded_rectangle([cx_btn, cy_btn, cx_btn + cta_w, cy_btn + cta_h], radius=16, fill="#16a34a")
cta_txt = "CONSULTA POR VALORES Y FECHAS DISPONIBLES"
cbox = font_bold.getbbox(cta_txt)
ctw, cth = cbox[2] - cbox[0], cbox[3] - cbox[1]
draw.text((cx_btn + (cta_w - ctw)//2, cy_btn + (cta_h - cth)//2 - 2), cta_txt, fill="white", font=font_bold)

# 7. Address (875px to 905px)
addr_txt = "Lonquén Sur. 38 1/2. Talagante."
abox = font_bold.getbbox(addr_txt)
atw = abox[2] - abox[0]
draw.text(((width - atw)//2, 872), addr_txt, fill="#0f172a", font=font_bold)

# 8. Dark Footer Bar (920px to 1080px -> height 160px)
draw.rectangle([0, 920, width, height], fill="#071426")

# Real QR Code Paste (Size 130x130 px on the left footer)
if os.path.exists(qr_path):
    qr_img = Image.open(qr_path).convert("RGBA")
    qr_img = qr_img.resize((130, 130), Image.Resampling.LANCZOS)
    canvas.paste(qr_img, (40, 935), qr_img)
    draw.text((185, 975), "Escanea y\nescríbenos", fill="white", font=font_bold)

# Phone & Instagram on right footer
draw.text((520, 950), "WhatsApp: +56 9 8888 6174", fill="#25D366", font=font_phone)
draw.text((520, 1005), "Instagram: @espaciomanio", fill="#38bdf8", font=font_sub)

# Save result
canvas.save(output_post)
canvas.save(desktop_post)
print(f"Final scannable post generated and saved at:\n  - {output_post}\n  - {desktop_post}")
