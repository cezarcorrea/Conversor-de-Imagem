from PIL import Image

# Função de conversão
def converter(caminho_imagem):

    try:
        # Abrir a imagem colorida
        imagem_colorida = Image.open(caminho_imagem)

        # Converter para tons de cinza
        imagem_cinza = imagem_colorida.convert('L')
        imagem_cinza.save("imagem_cinza.png")
        print("Imagem convertida para tons de cinza e salva como imagem_cinza.png")

        # Converter a imagem cinza para binarizada
        limiar = 128
        imagem_binaria = imagem_cinza.point(lambda p: 255 if p > limiar else 0)
        imagem_binaria.save("imagem_binaria.png")
        print("Imagem binarizada e salva como imagem_binaria.png")
    
    # Verifica possíveis erros durante a execução
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_imagem}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Caminho para a imagem a ser covertida
converter('.\Dimensionalidade em Imagens\laranja.png')