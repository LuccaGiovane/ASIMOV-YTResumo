import yt_dlp
import whisper
import openai
import ffmpeg
import os

# Colocar aqui a Key do chatGPT
openai.api_key = 'API_KEY'


def baixar_audio(url):
    """
    Baixa o áudio de um vídeo do YouTube usando yt-dlp.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': 'audio.wav'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return 'audio.wav'


def transcrever_audio(audio_path):
    """
    Transcreve o áudio usando Whisper.
    """
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]


def resumir_texto(texto):
    """
    Resume o texto transcrito usando a API de linguagem da OpenAI.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Resuma o seguinte texto:\n\n{texto}",
        max_tokens=150,
        temperature=0.5
    )
    resumo = response.choices[0].text.strip()
    return resumo


def analisar_video(url):
    """
    Função principal para analisar um vídeo do YouTube.
    """
    print("Baixando o áudio do vídeo...")
    audio_path = baixar_audio(url)

    print("Transcrevendo o áudio...")
    texto_transcrito = transcrever_audio(audio_path)

    print("Resumindo o conteúdo transcrito...")
    resumo = resumir_texto(texto_transcrito)

    # Limpa o arquivo de áudio
    os.remove(audio_path)

    return resumo


# Colocar a URL do video aqui
url_video = "www.seu.video.do.Youtube.com"
resumo_video = analisar_video(url_video)
print("Resumo do vídeo:", resumo_video)
