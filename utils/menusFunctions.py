import utils.languagePack
### views functions and variables###
# app_buttons list is used to change language in every button at once
app_buttons = []
# list of languages, very easy to add a new one - add to this list + translations in languagePack file
languageList = ["English", "Polski"]
currentLanguage = 0
language = languageList[currentLanguage]
# sound
soundState = True
soundText = utils.languagePack.soundOnText[currentLanguage]
# difficulty
difficultyList = [0, 1, 2, 3]
currentDifficulty = 0
difficultyText = utils.languagePack.difficultyEasy[currentLanguage]
# turn sound on/off + change text


def toggleSound():
    global soundState
    global soundText
    global language

    soundState = not soundState

    if(soundText == utils.languagePack.soundOnText[currentLanguage]):
        soundText = utils.languagePack.soundOffText[currentLanguage]
    else:
        soundText = utils.languagePack.soundOnText[currentLanguage]

# this fun is simply a fix to situation where we switch lang but sound button displays old lang text(it worked only when switching on/off)


def soundLang():
    global soundText
    if(soundState == True):
        soundText = utils.languagePack.soundOnText[currentLanguage]
    else:
        soundText = utils.languagePack.soundOffText[currentLanguage]

# change language of every button, header, etc


def changeLanguage():
    global language
    global currentLanguage

    # this is important in other lists, iterate over lang list
    currentLanguage += 1

    if(currentLanguage == len(languageList)):
        currentLanguage = 0

    # this sets text on button in language options
    language = languageList[currentLanguage]

    [button.update() for button in app_buttons]


def changeDifficulty():
    global difficultyList
    global currentDifficulty
    global difficultyText

    currentDifficulty += 1

    if(currentDifficulty == len(difficultyList)):
        currentDifficulty = 0

    if(currentDifficulty == 0):
        difficultyText = utils.languagePack.difficultyEasy[currentLanguage]
    elif(currentDifficulty == 1):
        difficultyText = utils.languagePack.difficultyNormal[currentLanguage]
    elif(currentDifficulty == 2):
        difficultyText = utils.languagePack.difficultyHard[currentLanguage]
    elif(currentDifficulty == 3):
        difficultyText = utils.languagePack.difficultyHell[currentLanguage]


def difficultyLang():
    global difficultyText

    if(currentDifficulty == 0):
        difficultyText = utils.languagePack.difficultyEasy[currentLanguage]
    elif(currentDifficulty == 1):
        difficultyText = utils.languagePack.difficultyNormal[currentLanguage]
    elif(currentDifficulty == 2):
        difficultyText = utils.languagePack.difficultyHard[currentLanguage]
    elif(currentDifficulty == 3):
        difficultyText = utils.languagePack.difficultyHell[currentLanguage]
