import openai
import json

def split_text(text, max_chunk_size):
    paragraphs = text.split('\n')
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) + 1 <= max_chunk_size:
            current_chunk += paragraph + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + "\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

openai.api_key = 'your_api_key'

filename = './file.txt'
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

max_chunk_size = 2000
text_chunks = split_text(text, max_chunk_size)

responses = []

for chunk in text_chunks:
    prompt = "One multiple choice question from the text below with 4 options and one of them to be true.\nText: " + chunk

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.8
    )
    responses.append({
        #'prompt': prompt,
        'response': response.choices[0].text.strip()
    })

# Save responses to a JSON file
with open('responses.json', 'w', encoding='utf-8') as file:
    json.dump(responses, file, indent=4, ensure_ascii=False)

print('Responses saved to responses.json')
