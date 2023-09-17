import google.generativeai as palm
import os

# API Key
try:
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv('GOOGLE_PALM_API_KEY')
except:
    print('dotenv not installed')


palm.configure(api_key=API_KEY)

class Bot:
    def __init__(self):
        self.text_model = 'models/text-bison-001'
        self.chat_model = 'models/chat-bison-001'

    def plant_chat(self, prompt, message):
        '''
        prompt: str - the prompt to be used for the bot
        message: str - the message to be used for the bot

        returns: str - the response from the bot
        '''
        prompt = f"{prompt} {message}\nBot:"
        completion = palm.generate_text(
            model=self.text_model, 
            prompt=prompt, 
            temperature=1,
            max_output_tokens=10000
            )
        
        return completion.result


    def general_chat(self, message, context=None, examples=None):
        '''
        context: str - the context to be used for the bot
        message: str - the message to be used for the bot

        returns: str - the response from the bot
        '''
        response = palm.chat(
            model=self.chat_model, 
            context=context,
            examples=examples,
            temperature=1,
            messages=message
            )
        
        msg = {
            'messages': response.messages
        }
        return msg


# Test the bot
def _test_bot():
    bot = Bot()
    print(bot.plant_chat('You are an expert in plants', 'Neem'))
    print(bot.general_chat("Be an alien that lives on one of Jupiter's moons", "How's it going?"))

if __name__ == '__main__':
    _test_bot()
