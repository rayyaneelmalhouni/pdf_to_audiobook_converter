
from gtts import gTTS
import PyPDF2


def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


# Specify the path to your PDF file
pdf_file_path = ""

# Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_file_path)

# Convert text to speech
tts = gTTS(text=extracted_text, lang='en')

# Save speech as an MP3 file
tts.save('output.mp3')


