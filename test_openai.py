import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env if you’re using one
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Say the word 'working' if you received this message"
            }
        ],
        max_tokens=10  # keep it tiny
    )

    print("✅ API Key is working!")
    print("Response:", response.choices[0].message.content.strip())

except Exception as e:
    print("❌ Something went wrong:", str(e))
