# GPT Multiple Question Generator

The GPT Multiple Question Generator is a Python script that takes a large piece of text, breaks it into smaller chunks, and utilizes OpenAI's GPT to generate multiple-choice questions. These questions are subsequently stored in a JSON file. This script is highly beneficial for creating educational resources, enhancing learning platforms, and for general language processing tasks.

## How it Works

1. The script begins by taking a large piece of text, which is then split into manageable chunks of up to 2000 characters each.
2. Each chunk is passed to the OpenAI's GPT API with a prompt asking to generate a multiple-choice question based on the text.
3. The GPT API returns a multiple-choice question which is then stored in a Python dictionary.
4. The process repeats for each chunk of text until all chunks have been processed.
5. Finally, all generated questions are saved to a JSON file.

## Prerequisites

- Python 3.x
- OpenAI Python package
- An OpenAI API key

## How to Run

1. Ensure that your text data is placed inside a file named `file.txt` in the same directory as the Python script. A sample text from Wikipedia is currently provided for your reference.
   
2. If you haven't installed the OpenAI package yet, you can install it by running the following command in your terminal:
```bash
pip install openai
```
3. Run the following command in your terminal after making sure you're in the correct directory:
```bash
python3 GPT_Question_Generator.py
```
4. Once the script finishes running, it should print 'Responses saved to responses.json'. This message indicates that the multiple-choice questions have been successfully generated and stored in the responses.json file.

## Caution

Please ensure your OpenAI API key is kept secure and confidential. Do not expose it publicly as it may lead to misuse.
