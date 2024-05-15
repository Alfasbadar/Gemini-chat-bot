
import requests
import json
import time
import threading

# ANSI color codes
BLUE = "\033[94m"
WHITE = "\033[0m"

# Function to print a loading animation
def loading_animation():
    animation = "|/-\\"
    for _ in range(10):
        for char in animation:
            print(f"\r{BLUE}Ask {char}{WHITE}", end="", flush=True)
            time.sleep(0.1)

# Function to send the request to the AI model
def send_request(input_text, response_callback):
    API_KEY = "your-api-key-here"  # Replace with your actual API key
    API_ENDPOINT = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"
    
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": input_text
                    }
                ]
            }
        ]
    }
    
    payload_json = json.dumps(payload)
    headers = {
        "Content-Type": "application/json"
    }
    url = f"{API_ENDPOINT}?key={API_KEY}"
    
    try:
        response = requests.post(url, data=payload_json, headers=headers)
        response_data = response.json()
        generated_text = response_data["candidates"][0]["content"]["parts"][0]["text"]
        response_callback(generated_text)
    except Exception as e:
        print(f"Error occurred during request: {e}")

# Main function
def main():
    print(f"{BLUE}Enter a prompt or Type 'Exit'{WHITE}")

    while True:
        user_input = input(f"{BLUE}> {WHITE}")

        if user_input.lower() == 'exit':
            print("See yah!")
            break

        loading_thread = threading.Thread(target=loading_animation)
        loading_thread.start()

        # Send the user input for processing
        send_request(user_input, response_callback)

# Function to handle the response from the AI model
def response_callback(response):
    # Stop the loading animation thread
    print("\r", end="", flush=True)
    
    if response:
        print(response)

if __name__ == "__main__":
    main()
