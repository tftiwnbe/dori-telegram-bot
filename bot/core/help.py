from random import choice

help_text = ["Помоги себе сам", "У меня лапки\!", "Обратись к психиатру"]

selected = []


async def help_say():
    text = choice(help_text)
    while text in selected:
        text = choice(help_text)
    selected.append(text)
    if len(selected) == 3:
        del selected[0]
    return text
