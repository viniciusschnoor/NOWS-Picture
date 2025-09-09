from PIL import Image
import pillow_heif
import os
import glob
import numpy as np
from moviepy import VideoFileClip, ImageClip, CompositeVideoClip

# Dados do evento
nome_do_evento = input("Digite o Nome do Evento: ")
ano_do_evento = input("Digite o Ano do Evento: ")
mes_do_evento = input("Digite o Mês do Evento: ")
dia_do_evento = input("Digite o Dia do Evento: ")

# Extensões suportadas
extensoes_imagem = (".jpg", ".jpeg", ".png", ".heic", ".webp", ".bmp", ".tiff", ".gif")
extensoes_video = (".mp4", ".mov", ".avi", ".mkv", ".webm")

# Arquivos ordenados por data
arquivos = sorted(glob.glob('fotos/*'), key=os.path.getmtime)

# Marca d'água obrigatória
watermark = Image.open('watermark/watermark.png')

# Pasta de saída
caminho = f"resultado/{ano_do_evento}_{mes_do_evento}_{dia_do_evento}_{nome_do_evento}"
os.makedirs(caminho, exist_ok=True)

for i, arquivo in enumerate(arquivos, start=1):
    ext = os.path.splitext(arquivo)[1].lower()

    # Converter HEIC para JPG
    if ext == ".heic":
        heif_file = pillow_heif.read_heif(arquivo)
        image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw")
        arquivo_jpg = arquivo.replace(".heic", ".jpg")
        image.save(arquivo_jpg)
        os.remove(arquivo)
        arquivo = arquivo_jpg
        ext = ".jpg"

    # Processar imagens
    if ext in extensoes_imagem:
        with Image.open(arquivo) as img:
            img.thumbnail((1000, 1000))
            min_dim = min(img.size)

            wm = watermark.copy()
            wm.thumbnail((min_dim * 0.42, min_dim * 0.42))
            pos_img = (img.width - wm.width - 15, img.height - wm.height - 15)
            img.paste(wm, pos_img, wm)

            img.save(f"{caminho}/{nome_do_evento}_{i:03}.jpg")
        os.remove(arquivo)

    # Processar vídeos
    elif ext in extensoes_video:
        clip = VideoFileClip(arquivo)
        w, h = clip.size
        min_dim = min(w, h)

        wm_resized = watermark.copy()
        wm_resized.thumbnail((min_dim * 0.42, min_dim * 0.42))

        # Convert PIL image to numpy array for ImageClip
        wm_array = np.array(wm_resized.convert("RGBA"))
        wm_clip = ImageClip(wm_array).with_duration(clip.duration).with_position((w - wm_resized.width - 15, h - wm_resized.height - 15))

        final = CompositeVideoClip([clip, wm_clip])
        output_path = f"{caminho}/{nome_do_evento}_{i:03}.mp4"
        final.write_videofile(output_path, codec="libx264", audio_codec="aac")

        clip.close()
        final.close()

        try:
            os.remove(arquivo)
        except PermissionError:
            print(f"Aviso: não foi possível remover o arquivo '{arquivo}' porque ainda está em uso.")
