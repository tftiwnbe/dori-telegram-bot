from random import choice

self_text = [
    "Я бот, созданный Конатуром Кустом",
    "Unkcat помогал меня делать \(:",
    "Мне нравится бумага",
    "Мой любимый цвет \- прозрачный\!",
]

selected = []


async def about_self():
    text = choice(self_text)
    while text in selected:
        text = choice(self_text)
    selected.append(text)
    if len(selected) == 3:
        del selected[0]
    return text
