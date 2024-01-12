from random import choice

help_text = ["Я не могу помочь, у меня лапки\(", "Напиши своё обращение", "Бесплатно работаем", "Телефон помощи \- 8\-800\-555\-35\-35", "Будь окуратен в своих желаниях!"]

selected = []


async def help_say():
    text = choice(help_text)
    while text in selected:
        text = choice(help_text)
    selected.append(text)
    if len(selected) == 3:
        del selected[0]
    return text
