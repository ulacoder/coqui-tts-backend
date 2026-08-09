from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from TTS.api import TTS
import io
import os

app = Flask(__name__)
CORS(app)

# Path to voice sample for cloning
VOICE_SAMPLE_PATH = os.getenv("VOICE_SAMPLE_PATH", "voice_sample.wav")

# Lazy load TTS model to avoid startup timeout
tts = None

def get_tts():
    global tts
    if tts is None:
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    return tts

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "model": "xtts_v2"})

@app.route('/tts', methods=['POST'])
def generate_speech():
    try:
        data = request.json
        text = data.get('text', '')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Check if voice sample exists
        if not os.path.exists(VOICE_SAMPLE_PATH):
            return jsonify({"error": "Voice sample not found. Upload voice_sample.wav"}), 500

        # Generate speech with voice cloning
        tts_instance = get_tts()
        wav = tts_instance.tts(
            text=text,
            speaker_wav=VOICE_SAMPLE_PATH,
            language="ru"  # Russian language
        )

        # Convert to bytes
        audio_buffer = io.BytesIO()
        tts_instance.synthesizer.save_wav(wav, audio_buffer)
        audio_buffer.seek(0)

        return send_file(
            audio_buffer,
            mimetype='audio/wav',
            as_attachment=False
        )

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
