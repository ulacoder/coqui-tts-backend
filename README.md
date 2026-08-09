# Coqui TTS Backend

Flask API для генерации речи с клонированием голоса используя Coqui TTS (XTTS-v2).

## Возможности

- Клонирование голоса из аудио-сэмпла
- Поддержка русского языка
- REST API для интеграции

## Установка

```bash
pip install -r requirements.txt
```

## Использование

1. Положи свой аудио-сэмпл (30 сек - 1 мин) как `voice_sample.wav`
2. Запусти сервер:

```bash
python app.py
```

3. API эндпоинт:

```bash
POST /tts
Content-Type: application/json

{
  "text": "Текст для озвучки"
}
```

## Деплой

Railway/Render/Heroku:

```bash
git push railway main
```

## Переменные окружения

- `PORT` - порт сервера (default: 5000)
- `VOICE_SAMPLE_PATH` - путь к аудио-сэмплу (default: voice_sample.wav)
