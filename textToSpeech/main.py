import PyPDF2
import pyttsx3

def pdf_to_speech(pdf_file):
    engine = pyttsx3.init()
    # Initialize the text-to-speech engine
    voices = engine.getProperty('voices')
    for idx, voice in enumerate(voices):
        print(f"{idx}: {voice.name} ({voice.id})")

    # Change voice (pick index you like, e.g., 0 or 1)
    engine.setProperty('voice', voices[1].id)


    engine.setProperty('rate', 200)  # Adjust speaking rate if you like

    # Open the PDF file in read-binary mode
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        print("No text found in the PDF!")

if __name__ == "__main__":
    file = input("Enter the path to your PDF file: ")
    pdf_to_speech(file)
