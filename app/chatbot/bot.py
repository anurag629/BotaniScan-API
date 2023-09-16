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
        self.model = 'models/text-bison-001'

    def plant_chat(self, prompt, message):
        '''
        prompt: str - the prompt to be used for the bot
        message: str - the message to be used for the bot

        returns: str - the response from the bot
        '''
        prompt = f"{prompt} {message}\nBot:"
        completion = palm.generate_text(
            model=self.model, 
            prompt=prompt, 
            temperature=1,
            max_output_tokens=10000
            )
        
        return completion.result


def _test_bot():
    bot = Bot()
    print(bot.get_plant_details('Neem'))


if __name__ == '__main__':
    _test_bot()
