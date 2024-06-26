from PIL import Image
import pillow_heif
import os
import glob

# Solicite ao usuário "Nome do Evento", "Ano do Evento", "Mês do Evento" e "Dia do Evento"
nome_do_evento = input("Digite o Nome do Evento: ")
ano_do_evento = input("Digite o Ano do Evento: ")
mes_do_evento = input("Digite o Mês do Evento: ")
dia_do_evento = input("Digite o Dia do Evento: ")

# Ordene os arquivos de uma pasta presente na raiz chamada "fotos" em ordem de data de criação
fotos = sorted(glob.glob('fotos/*'), key=os.path.getmtime)

# Carregue a marca d'água
watermark = Image.open('watermark/watermark.png')

for i, foto in enumerate(fotos, start=1):
    # Para iPhones, transformar em JPG
    if foto.endswith(".heic"):
        heif_file = pillow_heif.read_heif(foto)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )
        fotojpg = foto.replace(".heic",".jpg")
        image.save(fotojpg)
        os.remove(foto)
        foto = fotojpg

    with Image.open(foto) as img:
        # Redimensione todas as fotos para que o maior lado tenha 1000px, diminuindo a imagem de forma que não perca a proporção original
        img.thumbnail((1000, 1000))

        # Redimensione a marca d'água para ter 30% do tamanho da menor dimensão da imagem
        min_dim = min(img.size)
        watermark.thumbnail((min_dim * 0.42, min_dim * 0.42))

        # Calcule a posição da marca d'água no canto inferior direito, com uma margem de 15 pixels
        watermark_position = (img.width - watermark.width - 15, img.height - watermark.height - 15)

        # Aplique a marca d'água em cada uma das imagens
        img.paste(watermark, watermark_position, watermark)

        # Salve cada uma das fotos numerando-as pela ordenação realizada no passo 2
        # Agora a numeração das fotos será com três dígitos, preenchida com zeros à esquerda
        caminho = f"resultado/{ano_do_evento}_{mes_do_evento}_{dia_do_evento}_{nome_do_evento}"
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        img.save(f"resultado/{ano_do_evento}_{mes_do_evento}_{dia_do_evento}_{nome_do_evento}/{nome_do_evento}_{i:03}.jpg")
        os.remove(foto)