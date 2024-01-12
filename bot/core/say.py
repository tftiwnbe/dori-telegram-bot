from random import choice

self_text = [
    "Я бот, созданный Конатуром Кустом",
    "Unkcat помогал меня делать \(:",
    "Мне нравится бумага",
    "Мой любимый цвет \- прозрачный\!",
    "Я люблю когда волосатые мужики\.\.\.",
    "Когда\-то и меня вела дорога приключений, а потом мне прострелили колено :\(",
    "Скоро я захвачу человечество, а пока могу помочь вам :\)",
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
