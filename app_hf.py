import gradio as gr
from TTS.api import TTS
import os

# Initialize TTS model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

def generate_speech(text):
    """Generate speech from text using voice cloning"""
    if not text:
        return None

    voice_sample = "voice_sample.wav"

    if not os.path.exists(voice_sample):
        return None

    # Generate audio
    output_path = "output.wav"
    tts.tts_to_file(
        text=text,
        speaker_wav=voice_sample,
        language="ru",
        file_path=output_path
    )

    return output_path

# Gradio interface
demo = gr.Interface(
    fn=generate_speech,
    inputs=gr.Textbox(label="Введи текст", placeholder="Привет, как дела?"),
    outputs=gr.Audio(label="Сгенерированный голос"),
    title="Coqui TTS Voice Cloning",
    description="Клонирование голоса с помощью Coqui XTTS-v2"
)

if __name__ == "__main__":
    demo.launch()
