from random import choice

help_text = [
    "Я не могу помочь, у меня лапки\(",
    "Напиши своё обращение",
    "Бесплатно работаем",
    "Помоги себе сам, хаха",
    "Будь окуратен в своих желаниях\!",
    "Дай\-ка угадаю, кто\-то украл твой сладкий рулет\?",
    "КАМЕНЬ Я НЕ ДАМ\!",
]

selected = []


async def help_say():
    text = choice(help_text)
    while text in selected:
        text = choice(help_text)
    selected.append(text)
    if len(selected) == 3:
        del selected[0]
    return text
