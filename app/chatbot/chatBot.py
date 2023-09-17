from .bot import Bot

bot = Bot()

def get_plant_details(plant_name):
    '''
    plant_name: str - the name of the plant

    returns: str - the plant details
    '''
    prompt = f'''
        As a distinguished expert specializing in biodiversity research with a particular emphasis on the medicinal attributes of various plant species, your task is to unravel a holistic perspective on a given medicinal plant:

Upon receiving the name of a specified medicinal plant, we need you to unravel in-depth information about the plant, starting from its origin, historical usage, botanical characteristics, current application in the health industry, to any recent scientific studies linked to it.

In response to the prevailing challenges that the plant might be facing, please offer innovative and effective strategies. We require your valuable insights and recommendations to be presented in a detailed report, composed using the Markdown formatting style for improved readability. Ensure to incorporate relevant headings, subheadings, and exhaustive contextual explanations with emoji's as needed.
'''
    message = prompt + f'\nStudent: {plant_name}'
    return bot.plant_chat(prompt, message)


if __name__ == '__main__':
    print(get_plant_details('Neem'))
