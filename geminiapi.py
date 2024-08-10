import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyC2tHTRzveUziwdv2xyPnvxvZFrhj4ZD6o")

# Example function call (replace with actual functions based on what you want to do)
response = genai.generate_text(prompt="who is the inventer of sattelite")
print(response)
