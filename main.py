from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key (from Replit Secrets or hardcoded for testing)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return "✅ Roast API is running!"

@app.route('/roast', methods=['POST'])
def roast():
    data = request.get_json()
    image_url = data.get("image_url")

    # This is a temporary response for testing purposes
    roast_text = f"Nice try. That face belongs on a caution sign."

    # Uncomment this block later when you're ready to use the actual API
    """
    prompt = "Roast this person in a funny but not mean way."
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "You are a clever roast comic."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ],
        max_tokens=200
    )
    roast_text = response.choices[0].message.content
    """

    return jsonify({"roast": roast_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
