from jarvis.IO.io import InputInterface, OutputInterface
from jarvis.IO.voice.stt import SpeechToText
from jarvis.IO.voice.tts import TextToSpeech

class VoiceIO(InputInterface, OutputInterface):
    def __init__(self):
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

    def get_text(self) -> str:
        return self.stt.listen()

    def output_text(self, text: str):
        self.tts.speak(text)