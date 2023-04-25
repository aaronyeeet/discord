import random
import pyautogui
import time
# List of phrases
phrases = [
    "Hello!",
    "This is awesome!",
    "i like kalepa!",
    "Chatgpt is good!",
    ":Joseph: joseph",
    "rank up!",
    "@everyone ?!?!,
    "'no' - Emby",
    "Join the server!",
    "Join the hub (student hub)!",
    "'idk' - kalepa",
    "'same' - kalepa",
    "'when's my bedtime' - coffee jelly",
    "'Cna you buy me spotify premisum' - kalepa",
    "'Why is he dressed up like a guy that diverts people into dark alleyways and drugs them unconscious to use as slaves to create computer parts for an incredibly obscure phone brand from Liechtenstein that had been sued multiple times' - kalepa",
    "'bro just pulled at least 3 women' - Emby",
    "'what about those girls at handball' - Emby",
    "https://tenor.com/view/omg-what-no-way-emoji-shock-gif-2439067' - emby",
    "カレパはどのようにして良いランクを獲得しましたか.",
    "カレパ 는 좋은 순위를 가지고 있습니다",
    "ඞඞඞඞඞ",
    "https://tinyurl.com/ungamia",
    "spamming!",
    "# big text",
    "__***underline bold italics***__",
    "`look at this code`",
    "get ugmania on steam",
    "rank up script",
    "kalepa is online 24 hours of the day",
    "this role is not whitelisted!"
]
# Loop indefinitely
while True:
    time.sleep(30)
    # Select a random phrase from the list
    random_phrase = random.choice(phrases)
    # Type out the phrase and press enter
    pyautogui.typewrite(random_phrase)
    pyautogui.press('enter')
    # Wait for 59 seconds before typing the next phrase
    time.sleep(31)

