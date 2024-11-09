import pytube
import os
import ffmpeg
import whisper
import openai

# Colocar aqui a Key do chatGPT
openai.api_key = 'Sua key do chatGPT'


def baixar_audio(url):
    """
    Baixa o áudio de um vídeo do YouTube usando pytube e converte para WAV.
    """
    yt = pytube.YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first().url

    # Define o nome do arquivo de saída
    filename = "audio.wav"

    # Usa ffmpeg para baixar e converter para o formato WAV diretamente
    ffmpeg.input(audio_stream).output(filename, format='wav', loglevel="error").run()

    return filename

def transcrever_audio(audio_path):
    """
    Transcreve o áudio usando a API Whisper da OpenAI.
    """
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript["text"]

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

def resumir_texto(texto):
    """
    Resume o texto transcrito usando a API de linguagem da OpenAI.
    """
    completion = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que resume vídeos detalhadamente. Responda com formatação Markdown."},
            {"role": "user", "content": f"Descreva o seguinte vídeo: {texto}"}
        ]
    )
    resumo = completion.choices[0].message.content.strip()
    return resumo

# Colocar a URL do vídeo aqui
url_video = "https://www.youtube.com/SEUVIDEO"
resumo_video = analisar_video(url_video)
print("Resumo do vídeo:", resumo_video)
