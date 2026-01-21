# Instale a biblioteca: pip install pytubefix
# Importe as bibliotecas
from pytubefix import YouTube  # Manipular os videos do YouTube
from pytubefix.cli import (
    on_progress,
)  # Mostrar o progresso do download (não obrigatório)
from pathlib import Path  # Criar e manipular caminhos de arquivos e pastas

url = "https://www.youtube.com/watch?v=_hHzhijt-Jk"  # URL do vídeo do YouTube que será baixado

destino = Path("pasta_video")  # Pasta onde o vídeo será salvo
destino.mkdir(exist_ok=True)  # Cria a pasta se ela não existir

yt = YouTube(
    url, on_progress_callback=on_progress
)  # Cria um objeto YouTube com a URL fornecida e a função de callback para progresso

print(
    f"Título: {yt.title}\nDuração: {yt.length}s"
)  # Exibe no console o título do vídeo e a duração (em segundos)

yt.streams.get_highest_resolution().download(
    output_path=destino
)  # Faz o download do vídeo na maior resolução disponível

print(
    f"Download concluído! Vídeo salvo em: {destino}"
)  # Mensagem de conclusão do download
