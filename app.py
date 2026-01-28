import queue
import sounddevice as sd
import vosk
import json
import pyttsx3
import pyautogui
from actions import *
from llm import ask_llm

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Load VOSK Model
model = vosk.Model("vosk-model-small-en-us-0.15")
recognizer = vosk.KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    audio_queue.put(bytes(indata))

def listen_real_time():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        print("🎧 Listening... Speak now!")
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text = json.loads(result)["text"]
                if text:
                    handle_command(text.lower())

def handle_command(text):
    print("You said:", text)

    if "open chrome" in text:
        speak("Opening Chrome")
        open_chrome()

    elif "search file" in text:
        keyword = text.replace("search file", "").strip()
        results = search_files(keyword)
        speak(f"Found {len(results)} files")
        print(results)

    elif "read clipboard" in text:
        content = read_clipboard()
        speak("Clipboard contains:")
        speak(content)

    elif "explain screenshot" in text:
        image = pyautogui.screenshot()
        image.save("screen.png")
        text = ask_llm("Explain this image in simple words:")
        speak(text)

    else:
        # Send unknown commands to the LLM
        answer = ask_llm(text)
        speak(answer)

if __name__ == "__main__":
    listen_real_time()
