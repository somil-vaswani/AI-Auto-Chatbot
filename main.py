import pyautogui
import time
import pyperclip
import google.generativeai as genai


googleapi = "<your key>"  # Your Google Generative AI API key


def is_last_message_from_sender(chat_log, sender_name="Bank"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1].lower()
    if  messages.lower().startswith(sender_name.lower()):
        return True 
    
    return False
    
    

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(1210, 1049)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(688,220)
    pyautogui.dragTo(1846, 890, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(684, 632)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        genai.configure(api_key=googleapi)  # Configure the API with your specific key

        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
        description = (
            "You are Somil, chatting with your bank on WhatsApp. "
            "Your responses should be super casual, warm, and natural, like you're talking to corporate. "
            "Use common WhatsApp language, emojis if appropriate, and keep it friendly and concise. "
            "The last message in the provided chat history was sent by bank. "
            "Generate a human-like response from Somil. Don't include your name or anything about the timestamp."
        )
        chat_history = description +"\n"+ chat_history
        responsei = model.generate_content(chat_history) # Use the model to generate content based on the chat history
        response = responsei.text
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1021, 958)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')
