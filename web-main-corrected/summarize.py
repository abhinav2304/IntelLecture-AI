import openai

def summarize_questions(api_key, file_path='data/questions.txt'):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    prompt_text = "The following are questions from a lecture. Summarize them into bullet points:\n\n" + file_content

    openai.api_key = api_key

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-1106",
        prompt=prompt_text,
        max_tokens=100,  # Reduced for conciseness
        n=1,
        stop=None,
        temperature=0.0,
        frequency_penalty=0.5  # Added to reduce repetition
    )

    return response.choices[0].text.strip()

api_key = ''  # Replace with your actual API key
summary = summarize_questions(api_key)
print(summary)
