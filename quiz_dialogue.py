from aiogram import Router
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Row

from aiogram_dialog import (
    Dialog, DialogManager, StartMode, Window,
)

from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import CommandStart
from aiogram import types
from aiogram.types import CallbackQuery

import random

router_basic = Router()

class QuizStates(StatesGroup):
    Question1 = State()
    Question2 = State()
    Question3 = State()
    Question4 = State()
    Question5 = State()
    Question6 = State()


async def go_back(callback: CallbackQuery, button: Button,
                  manager: DialogManager):
    await manager.back()


async def go_next(callback: CallbackQuery, button: Button,
                  manager: DialogManager):
    await manager.next()

caption_list =[
    "Perhaps you got luckier than everyone - you got the best girl for the crypto chad  - Candice 💚",
    "I see you're a big fan of Pepe, I hope you're not a zoophile. Your girlfriend is Pepita.🐸",
    "Are you Sam Bankman-Fried? Have you decided to check if Caroline suits you? GIVE ME MY MONEY BACK🤬",
    "You love Vitalik Buterin, but you're not gay. Okay... Your girlfriend... um... Vitalina?",
    "Mr. President (no), glad to see you in our community! Make memes great again!🇺🇸💪",
    "You lucky duck! You'll be where Elon Musk has been. Enjoy!⭐️",
    "You're the default guy who got lucky with his girl. Cool... Don't die from depression.💀"
]

async def end_quiz(callback: CallbackQuery, button: Button,
                    manager: DialogManager):
    await manager.done()
    await callback.message.edit_text("Here is your result:")
    random_choice_number = random.randint(1, 7)
    caption = caption_list[random_choice_number-1]
    photo_link = f"https://raw.githubusercontent.com/orseniy99/test_data/" \
                 f"main/pictures_final/picture_{random_choice_number}.jpg"
    await callback.message.answer_photo(
        photo=photo_link,
        caption=caption
    )


dialog = Dialog(
    Window(
        Const("If you were suddenly attacked by a homeless person, what would you do?"),

        Row(Button(Const('Say "Homeless person, go home."'), id="q1_opt1", on_click=go_next)),
        Row(Button(Const("Run away."), id="q1_opt2", on_click=go_next)),
        Row(Button(Const("Give them all my money, because I have plenty."), id="q1_opt3", on_click=go_next)),

        state=QuizStates.Question1,
        getter={"question_number": lambda data, w, m: 1},
    ),
    Window(
        Const("You see an elderly woman trying to cross the road. What do you do?"),

        Row(Button(Const('Give her a nudge.'), id="q2_opt1", on_click=go_next)),
        Row(Button(Const("Buy a caramel syrup latte."), id="q2_opt2", on_click=go_next)),
        Row(Button(Const("You have a Hummer."), id="q2_opt3", on_click=go_next)),

        state=QuizStates.Question2,
        getter={"question_number": lambda data, w, m: 2},
    ),
    Window(
        Const("Tomorrow are the elections in the USA, who would you vote for?"),

        Row(Button(Const('Munning Trump.'), id="q3_opt1", on_click=go_next)),
        Row(Button(Const("Elon Tusk."), id="q3_opt2", on_click=go_next)),
        Row(Button(Const("I have hemorrhoids - I don't vote."), id="q3_opt3", on_click=go_next)),

        state=QuizStates.Question3,
        getter={"question_number": lambda data, w, m: 3},
    ),
    Window(
        Const("What is your penis size?"),

        Row(Button(Const('5 to 8 cm.'), id="q4_opt1", on_click=go_next)),
        Row(Button(Const("8 to 9 cm."), id="q4_opt2", on_click=go_next)),
        Row(Button(Const("25 to 35 cm."), id="q4_opt3", on_click=go_next)),

        state=QuizStates.Question4,
        getter={"question_number": lambda data, w, m: 4},
    ),
    Window(
        Const("Which car would you choose?"),

        Row(Button(Const('BMW X3.'), id="q5_opt1", on_click=go_next)),
        Row(Button(Const("DAF."), id="q5_opt2", on_click=go_next)),
        Row(Button(Const("Citroen C4."), id="q5_opt3", on_click=go_next)),

        state=QuizStates.Question5,
        getter={"question_number": lambda data, w, m: 5},
    ),
    Window(
        Const("Are you gay?"),

        Row(Button(Const('Possibly.'), id="q6_opt1", on_click=end_quiz)),
        Row(Button(Const("Had a kiss with a friend (we're not gay)"), id="q6_opt2", on_click=end_quiz)),
        Row(Button(Const("I'm a super homophobic gay."), id="q6_opt3", on_click=end_quiz)),

        state=QuizStates.Question6,
        getter={"question_number": lambda data, w, m: 6},
    ),

)

router_basic.include_routers(dialog)

@router_basic.message(CommandStart())
async def start_quiz(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(QuizStates.Question1, mode=StartMode.RESET_STACK)
