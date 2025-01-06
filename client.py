from openai import OpenAI
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

client = OpenAI(
  api_key="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"
)
def ai(message: str):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis(Just like marvel's Iron Man's AI), give brief answers to anything that is asked and give utmost respect to the user and address them as sir (not madam)"},
        {"role": "user", "content": message}
    ]
    )

    speak(completion.choices[0].message.content);
