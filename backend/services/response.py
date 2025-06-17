from services.gemini import generate_response

def get_bot_reply(message):
    prompt = f"The customer said: {message}. Give a helpful support response."
    return generate_response(prompt)
