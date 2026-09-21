import os
from PIL import Image, ImageDraw, ImageFont

base_dir = r"C:\Users\dinog\OneDrive\Desktop\Proyectos de Trabajo\Proyecto Parcela"
logo_path = os.path.join(base_dir, "logo_oficial_espacio_manio.png")
pool_path = os.path.join(base_dir, "05-Flyers", "piscina_15x7.jpg")
lawn_path = os.path.join(base_dir, "Fotos Parcela", "Fotos", "foto_parcela_18.jpeg")
qr_path = os.path.join(base_dir, "05-Flyers", "qr_whatsapp_oficial.png")

out_feed = os.path.join(base_dir, "04-Instagram", "post_feed_temporada_fin_de_ano.png")
out_story = os.path.join(base_dir, "04-Instagram", "story_temporada_fin_de_ano.png")
desktop_feed = r"C:\Users\dinog\OneDrive\Desktop\POST_FEED_FIN_DE_ANO_ESPACIO_MANIO.png"
desktop_story = r"C:\Users\dinog\OneDrive\Desktop\STORY_FIN_DE_ANO_ESPACIO_MANIO.png"

# Fonts
font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 36)
font_badge = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 26)
font_btn = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 30)
font_body = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 22)
font_bold = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 24)
font_phone = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 38)
font_web = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 17)
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 20)
font_sub_bold = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 22)

# ==========================================================
# 1. POST FEED INSTAGRAM (1080 x 1080)
# ==========================================================
w, h = 1080, 1080
canvas = Image.new("RGB", (w, h), "#061019")
draw = ImageDraw.Draw(canvas)

# Header (0 to 140)
header = Image.new("RGB", (w, 140), "#ffffff")
canvas.paste(header, (0, 0))

if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")
    logo.thumbnail((650, 125), Image.Resampling.LANCZOS)
    canvas.paste(logo, ((w - logo.width)//2, (140 - logo.height)//2), logo)

draw.line([(0, 140), (w, 140)], fill="#00A896", width=4)

# Pool Image (144 to 555) - 411px height
if os.path.exists(pool_path):
    pool = Image.open(pool_path).convert("RGB")
    pr = pool.width / pool.height
    tr = w / 411
    if pr > tr:
        nw = int(411 * pr)
        pool = pool.resize((nw, 411), Image.Resampling.LANCZOS)
        cx = (nw - w) // 2
        pool = pool.crop((cx, 0, cx + w, 411))
    else:
        nh = int(w / pr)
        pool = pool.resize((w, nh), Image.Resampling.LANCZOS)
        cy = (nh - 411) // 2
        pool = pool.crop((0, cy, w, cy + 411))
    canvas.paste(pool, (0, 144))

# Badge over pool image
badge_w, badge_h = 680, 48
bx = (w - badge_w) // 2
by = 530
draw.rounded_rectangle([bx, by, bx + badge_w, by + badge_h], radius=24, fill="#00A896")
txt = "ESPECTACULAR PISCINA DE 15 X 7 METROS"
bbox = font_badge.getbbox(txt)
tw = bbox[2] - bbox[0]
draw.text((bx + (badge_w - tw)//2, by + 10), txt, fill="#ffffff", font=font_badge)

# Campaign Headline (600 to 670)
c_title = "PASEOS DE FIN DE AÑO & EVENTOS PRIVADOS"
tbox = font_title.getbbox(c_title)
draw.text(((w - (tbox[2]-tbox[0]))//2, 598), c_title, fill="#ffffff", font=font_title)

c_sub = "Paseos de Curso · Eventos de Empresa · Celebraciones Familiares"
sbox = font_bold.getbbox(c_sub)
draw.text(((w - (sbox[2]-sbox[0]))//2, 644), c_sub, fill="#00f5ab", font=font_bold)

# Feature Pill Boxes (685 to 740)
features = [
    "Quincho Equipado",
    "Áreas Verdes",
    "+30 Estacionamientos",
    "100% Exclusivo"
]
fw = 232
fh = 44
fx_start = (w - (4 * fw + 3 * 16)) // 2
for i, feat in enumerate(features):
    x = fx_start + i * (fw + 16)
    y = 690
    draw.rounded_rectangle([x, y, x + fw, y + fh], radius=12, fill="#0f2922", outline="#00A896", width=1)
    fbox = font_bold.getbbox(feat)
    draw.text((x + (fw - (fbox[2]-fbox[0]))//2, y + 8), feat, fill="#ffffff", font=font_bold)

# Call to Action button (750 to 818)
btn_w, btn_h = 860, 64
btn_x = (w - btn_w) // 2
btn_y = 750
draw.rounded_rectangle([btn_x, btn_y, btn_x + btn_w, btn_y + btn_h], radius=18, fill="#25D366")
cta_txt = "¡CONSULTA VALORES Y FECHAS DISPONIBLES!"
cbbox = font_btn.getbbox(cta_txt)
draw.text((btn_x + (btn_w - (cbbox[2]-cbbox[0]))//2, btn_y + 14), cta_txt, fill="#04121d", font=font_btn)

# Location line (826 to 855)
loc_txt = "Lonquén Sur, Paradero 38 1/2 · Talagante, Región Metropolitana"
lbox = font_body.getbbox(loc_txt)
draw.text(((w - (lbox[2]-lbox[0]))//2, 828), loc_txt, fill="#cbd5e1", font=font_body)

# Dark Footer Bar (865 to 1080)
draw.rectangle([0, 865, w, h], fill="#03080e")
draw.line([(0, 865), (w, 865)], fill="#00A896", width=2)

if os.path.exists(qr_path):
    qr = Image.open(qr_path).convert("RGBA")
    qr = qr.resize((175, 175), Image.Resampling.LANCZOS)
    canvas.paste(qr, (35, 885), qr)
    draw.text((230, 900), "Escanea con tu cámara", fill="#ffffff", font=font_title)
    draw.text((230, 946), "para chatear directo al WhatsApp oficial", fill="#94a3b8", font=font_body)
    draw.text((230, 988), "Web: dinogonzalez.github.io/Proyecto-Parcela", fill="#38bdf8", font=font_web)

# Phone & Instagram Right (x=680)
draw.text((680, 885), "WhatsApp Oficial:", fill="#94a3b8", font=font_sub)
draw.text((680, 915), "+56 9 8888 6174", fill="#25D366", font=font_phone)
draw.text((680, 980), "Instagram:", fill="#94a3b8", font=font_sub)
draw.text((775, 980), "@espaciomanio", fill="#00e5ff", font=font_sub_bold)
draw.text((680, 1015), "Lonquén Sur · Talagante", fill="#64748b", font=font_sub)

canvas.save(out_feed, "PNG")
canvas.save(desktop_feed, "PNG")
print("Feed post saved at:", out_feed)

# ==========================================================
# 2. STORY / REEL COVER (1080 x 1920)
# ==========================================================
sw, sh = 1080, 1920
scanvas = Image.new("RGB", (sw, sh), "#061019")
sdraw = ImageDraw.Draw(scanvas)

# Header with white card
sheader = Image.new("RGB", (sw, 210), "#ffffff")
scanvas.paste(sheader, (0, 0))

if os.path.exists(logo_path):
    slogo = Image.open(logo_path).convert("RGBA")
    slogo.thumbnail((700, 180), Image.Resampling.LANCZOS)
    scanvas.paste(slogo, ((sw - slogo.width)//2, (210 - slogo.height)//2), slogo)

sdraw.line([(0, 210), (sw, 210)], fill="#00A896", width=5)

# Pool photo in the story upper half (215 to 880 -> 665px)
if os.path.exists(pool_path):
    spool = Image.open(pool_path).convert("RGB")
    pr = spool.width / spool.height
    tr = sw / 665
    if pr > tr:
        nw = int(665 * pr)
        spool = spool.resize((nw, 665), Image.Resampling.LANCZOS)
        cx = (nw - sw) // 2
        spool = spool.crop((cx, 0, cx + sw, 665))
    else:
        nh = int(sw / pr)
        spool = spool.resize((sw, nh), Image.Resampling.LANCZOS)
        cy = (nh - 665) // 2
        spool = spool.crop((0, cy, sw, cy + 665))
    scanvas.paste(spool, (0, 215))

# Lawn / Pergola photo in the middle (890 to 1290 -> 400px)
if os.path.exists(lawn_path):
    sq = Image.open(lawn_path).convert("RGB")
    qr = sq.width / sq.height
    tr = sw / 400
    if qr > tr:
        nw = int(400 * qr)
        sq = sq.resize((nw, 400), Image.Resampling.LANCZOS)
        cx = (nw - sw) // 2
        sq = sq.crop((cx, 0, cx + sw, 400))
    else:
        nh = int(sw / qr)
        sq = sq.resize((sw, nh), Image.Resampling.LANCZOS)
        cy = (nh - 400) // 2
        sq = sq.crop((0, cy, sw, cy + 400))
    scanvas.paste(sq, (0, 890))

# Badge 1 over pool
sdraw.rounded_rectangle([120, 810, sw - 120, 868], radius=28, fill="#00A896")
txt_p = "PISCINA GIGANTE DE 15 X 7 METROS"
p_box = font_badge.getbbox(txt_p)
sdraw.text(((sw - (p_box[2]-p_box[0]))//2, 824), txt_p, fill="#ffffff", font=font_badge)

# Badge 2 over lawn
sdraw.rounded_rectangle([120, 1225, sw - 120, 1280], radius=25, fill="#1B4332")
txt_q = "QUINCHO TECHADO Y EXTENSAS ÁREAS VERDES"
q_box = font_badge.getbbox(txt_q)
sdraw.text(((sw - (q_box[2]-q_box[0]))//2, 1238), txt_q, fill="#ffffff", font=font_badge)

# Middle details (1310 to 1570)
font_st_h = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 40)
font_st_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 28)

st_title = "PASEOS DE FIN DE AÑO & PRIVADOS"
st_box = font_st_h.getbbox(st_title)
sdraw.text(((sw - (st_box[2]-st_box[0]))//2, 1315), st_title, fill="#ffffff", font=font_st_h)

st_sub = "¡Exclusividad total para tu grupo en Talagante!"
st_sub_box = font_st_sub.getbbox(st_sub)
sdraw.text(((sw - (st_sub_box[2]-st_sub_box[0]))//2, 1370), st_sub, fill="#00f5ab", font=font_st_sub)

# Check items
items = [
    "• Paseos de Curso y Colegios (Temporada Primavera-Verano)",
    "• Eventos de Fin de Año de Empresa & Integración",
    "• Cumpleaños y Celebraciones Familiares Privadas",
    "• Estacionamiento cerrado para más de 30 vehículos"
]
for i, item in enumerate(items):
    sdraw.text((120, 1425 + i * 42), item, fill="#f8fafc", font=font_bold)

# CTA button
sbtn_w, sbtn_h = 920, 78
sbtn_x = (sw - sbtn_w) // 2
sbtn_y = 1605
sdraw.rounded_rectangle([sbtn_x, sbtn_y, sbtn_x + sbtn_w, sbtn_y + sbtn_h], radius=22, fill="#25D366")
scta_txt = "¡CONSULTA TU FECHA POR WHATSAPP!"
scbox = font_title.getbbox(scta_txt)
sdraw.text((sbtn_x + (sbtn_w - (scbox[2]-scbox[0]))//2, sbtn_y + 18), scta_txt, fill="#04121d", font=font_title)

# Story Footer (1715 to 1920)
sdraw.rectangle([0, 1715, sw, sh], fill="#03080e")
sdraw.line([(0, 1715), (sw, 1715)], fill="#00A896", width=2)

if os.path.exists(qr_path):
    sqr = Image.open(qr_path).convert("RGBA")
    sqr = sqr.resize((170, 170), Image.Resampling.LANCZOS)
    scanvas.paste(sqr, (35, 1735), sqr)
    sdraw.text((225, 1740), "Escanea para chatear", fill="#ffffff", font=font_bold)
    sdraw.text((225, 1782), "Lonquén Sur, Par. 38 1/2 · Talagante", fill="#94a3b8", font=font_sub)
    sdraw.text((225, 1822), "Web: dinogonzalez.github.io/Proyecto-Parcela", fill="#38bdf8", font=font_web)

sdraw.text((660, 1735), "WhatsApp Oficial:", fill="#94a3b8", font=font_sub)
sdraw.text((660, 1765), "+56 9 8888 6174", fill="#25D366", font=font_phone)
sdraw.text((660, 1828), "Instagram:", fill="#94a3b8", font=font_sub)
sdraw.text((755, 1828), "@espaciomanio", fill="#00e5ff", font=font_sub_bold)

scanvas.save(out_story, "PNG")
scanvas.save(desktop_story, "PNG")
print("Story post saved at:", out_story)
