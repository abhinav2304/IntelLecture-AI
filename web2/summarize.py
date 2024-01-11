import openai

# Directly assign your actual API key here
api_key = 'sk-'

client = openai.OpenAI(api_key=api_key)

def summarize_questions(file_path='data/questions.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    prompt_text = "The following are questions from students from a lecture,correct the sentence formation if needed,translate to english if there are any questions from other languages:\n\n" + file_content

    # Correcting the API call by using 'model' instead of 'engine'
    response = client.completions.create(model="gpt-3.5-turbo-instruct", prompt=prompt_text,
                                         max_tokens=100,  # Reduced for conciseness
                                         n=1,
                                         stop=None,
                                         temperature=0.0,
                                         frequency_penalty=1)

    return response.choices[0].text.strip()

# Call the function and print the summary
summary = summarize_questions()
print(summary)
# ... existing summarize.py code ...

# Save the output to a file
with open('output.txt', 'w') as file:
    file.write(summary)
