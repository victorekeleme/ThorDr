from app import handler

def bot_responses(input_text):
    user_message = str(input_text)

    if user_message.lower() in ("hello", "hi"):
        return "Hey, How are you?"
    
    elif str(user_message)[:15] == "magnet:?xt=urn:":        
        return handler(user_message)


    return "I don't understand you"
