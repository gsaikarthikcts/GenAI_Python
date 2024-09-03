import whisper
import openai
 
# Replace with your actual API key
openai.api_key = "API_KEY"
 
# Load the Whisper model
model = whisper.load_model("base")
 
# Path to your audio file
audio_file = "/content/song.mp3"
 
# Transcribe the audio
result = model.transcribe(audio_file)

# Extract the transcribed text
text = result["text"]
print("Transcribed Text:\n", text)
 
# Function to ask questions and get answers
def ask_question(question):
  prompt = text + "\n\nQuestion: " + question + "\nAnswer:"
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
  )
  answer = response.choices[0].text.strip()
  return answer
 
# Get user question
user_question = input("Ask Question : ")
 
# Get answer using OpenAI
answer = ask_question(user_question)
print("Answer:\n", answer)