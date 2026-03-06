import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def ask_chatgpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-5.1",          # choose model: gpt-4o, gpt-4.1, gpt-5.1 etc.
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message["content"]

    except Exception as e:
        return f"Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    question = "You are an expert in searching vessel details using an IMO number. \
        Your task is to search and return the following information exactly as found \
        from verified ship-building sources (no hallucination): \
            Name of yard (without including the country name): , \
            Country: ,\
            Hull number:  Search these details exclusively using the provided IMO number. \
            IMO number: 1074644 Return the results in clean JSON format:"
    answer = ask_chatgpt(question)
    print("ChatGPT Response:", answer)
