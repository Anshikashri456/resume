import openai

client = openai.OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def ask_llm(prompt, user_content, temperature=0.7):
    response = client.chat.completions.create(
        model="C://Users//admin//.lmstudio//models//lmstudio-community//gemma-3-12b-it-GGUF",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_content}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content
