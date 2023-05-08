import openai

openai.api_key = "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"

def ask_gpt(prompt: str) -> str:
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 4000,
        temperature = 0.5,
        frequency_penalty = 0,
        presence_penalty = 0,
    )
    return response.choices[0].text.strip()


def main() -> None:
    topic = input("Enter a podcast topic you'd like to create a script about: ")
    prompt = f"Write a detailed script for podcast about '{topic}'."

    response = ask_gpt(prompt)
    print(response)
    
    with open("summary.txt", "w", encoding="utf-8") as file:
        file.write(response)


if __name__ == "__main__":
    main()