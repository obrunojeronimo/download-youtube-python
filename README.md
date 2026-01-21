# download-youtube-python

Script em Python para fazer download de vídeos do YouTube de forma simples e rápida, utilizando a biblioteca `pytubefix`.

## Requisitos

- Python 3.6+
- pytubefix

## Instalação

### 1. Instalar a biblioteca

```bash
pip install pytubefix
```

### 2. Usar o script

Clone ou baixe este repositório e execute o script com sua URL do YouTube.

## Recursos

- Download de vídeos em alta resolução
- Exibição de progresso durante o download
- Criação automática de pasta de destino
- Acesso a informações do vídeo (título, duração)
- Suporte a múltiplas resoluções

## Customização

Você pode modificar o script para:

- **Alterar a resolução**: Substitua `get_highest_resolution()` por `get_lowest_resolution()` ou use `streams.first()`
- **Adicionar múltiplas URLs**: Use um loop com uma lista de URLs
- **Selecionar apenas áudio**: Use `.get_audio_only()`

## Licença

MIT

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
Contato: https://www.instagram.com/obrunojeronimo/