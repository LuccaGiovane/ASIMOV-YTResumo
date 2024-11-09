# YTResumo
YTResumo é um projeto em Python que permite baixar o áudio de vídeos do YouTube, transcrevê-los usando a API Whisper da OpenAI e gerar um resumo utilizando o modelo GPT-4. Ideal para aqueles que desejam obter resumos de conteúdos em vídeo de forma rápida e prática.

## Funcionalidades
- Download de áudio de vídeos do YouTube: Baixa apenas o áudio do vídeo especificado.
- Conversão de áudio para texto: Utiliza a API Whisper da OpenAI para transcrever o áudio em texto.
- Geração de resumo: Resume o conteúdo transcrito usando a API GPT-4 da OpenAI.

## Requisitos
- Python 3.7+
- ffmpeg

## Bibliotecas Python:
- pytubefix (para download de áudio do YouTube)
- ffmpeg-python (para conversão de áudio)
- openai (para integração com a API Whisper e GPT-4)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/LuccaGiovane/ASIMOV-YTResumo.git
cd ASIMOV-YTResumo
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Instale o ffmpeg e adicione-o ao PATH do sistema.

## Configuração
1. Crie uma conta na OpenAI e obtenha sua chave de API.
2. No arquivo YoutubeResumeVideos.py, substitua "Sua key do chatGPT" pela sua chave da API OpenAI.
Uso
3. No arquivo YoutubeResumeVideos.py, substitua o valor da variável url_video pela URL do vídeo do YouTube que você deseja resumir:
```bash
url_video = "https://www.youtube.com/SEUVIDEO"
```
Para executar o script e gerar o resumo do vídeo:

```bash
python YoutubeResumeVideos.py
```
O resumo do vídeo será exibido no console.

## Estrutura do Código
- baixar_audio(url): Baixa o áudio do vídeo e o converte para formato WAV.
- transcrever_audio(audio_path): Transcreve o áudio usando a API Whisper.
- analisar_video(url): Função principal que baixa o áudio, o transcreve e gera o resumo.
- resumir_texto(texto): Usa a API GPT-4 para resumir o texto transcrito.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

