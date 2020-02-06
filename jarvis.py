import speech_recognition as sr

def _get_audio():
    # TODO limit the size/length/duration/whatever of the sound
	r = sr.Recognizer()
	with sr.AudioFile('file_13.wav') as source:
		audio = r.listen(source)
		said = ""
		try:
		    said = r.recognize_google(audio)
		    # print(said.lower())
		except Exception as e:
		    print("Exception: " + str(e))
	return said.lower()

class JarvisCommands:
    def __init__(self, *args, **kwargs):
        self.commands = []
        self.trigger_token = kwargs.get("trigger_token", None)
        if type(self.trigger_token) is str:
            self.trigger_token = self.trigger_token.strip()

    def __call__(self, cmd):
        def wrapper(func):
            self.commands.append((cmd, func))
        return wrapper
    
    def execute(self, text):
        for j in self.commands:
            if j[0] in text:
                j[1]()
                return
    
    def listen(self):
        text = _get_audio()
        print(text)
        if type(self.trigger_token) is str:
            if not text.startswith(self.trigger_token):
                return
            text = text[len(self.trigger_token):]
        self.execute(text)
