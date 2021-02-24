# ? C:\Users\Bobasarous\Documents\Random Windows Stuff\Programming\PythonStuffs\aridon\aridon_setup.py

# Aridon is a text based adventure based on DnD rules, classes, etc...
# TODO Add explanations for all races, classes/subclasses, backgrounds, alignments, class items, ec
# TODO Add remaining character creation tools, class options, give players their background items, class items, pro.
# TODO Add remaining character creation stuffs, bonds, flaws, height, weight, skin/eye color, etc...
# TODO Separate everything into smaller, more manageable functions, gender, race, class, etc... all in own functions

import game_descriptions


# Setup function for the player's race, size, languages, and their gender
def race_setup():
    while True:  # Loop for user to choose their gender
        genders = ["male", "female", "neutral/NB", "Choose your own"]  # Genders you can choose to be

        print(f"Do you want to be {genders[0]}(1), {genders[1]}(2), or {genders[2]}(3), {genders[3]}(4)?")

        gender_choice = input().lower()  # User input for which gender they want

        try:  # Making sure the user input a number and converting it to a list usable set
            gender_choice = int(gender_choice) - 1

            if not 1 <= gender_choice <= 3:
                print("Please only choose numbers 1-4")

            if 0 <= gender_choice <= 3:
                while True:
                    yes_ = "yes y ye"
                    no_ = "no n o on"
                    if 0 <= gender_choice <= 2:
                        print(f"You have chosen {genders[gender_choice]}, do you wish to continue? (yes or no)")

                        gender_correct = input().lower()

                        if gender_correct in yes_:
                            print(f"You have chosen {genders[gender_choice]} as your gender, good luck!")
                            gender_choice = genders[gender_choice]  # Generates the users gender so we can return it
                            gender_correct = "yes"
                            break
                        if gender_correct in no_:
                            print("Alright, please try again.")
                            break
                        else:
                            print("Please only type yes or no!")

                    if gender_choice == 3:
                        yes_ = "yes y ye"
                        no_ = "no n o on"
                        print("Please type your own gender")
                        gender_choice = input()
                        while True:
                            print(f"You have chosen {gender_choice} as your gender are you sure you wish to continue?")

                            gender_correct = input().lower()

                            if gender_correct in yes_:
                                print(f"You have chosen {gender_choice}, good luck!")
                                gender_correct = "yes"
                                break
                            if gender_correct in no_:
                                print("Alright, please try again.")
                                break
                            else:
                                print("Please only type yes or no!")

                        if gender_correct in yes_:
                            break
                        if gender_correct in no_:
                            break

        except ValueError:  # In case they did not type a number
            print("Please type only numbers")

        try:  # Making sure that gender_correct doesn't get used if it is not defined (Happens if the user chooses no)
            if gender_correct in yes_:
                break
        except UnboundLocalError:
            pass

    while True:  # Loop for choosing their race

        races = ["Dwarf", "Elf", "Human", "Half-Orc", "Tiefling"]  # Races in game
        languages = ["Dwarvish", "Elvish", "Common", "Orcish", "Infernal"]  # Langs the races can know
        sizes = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]  # Sizes in game

        while True:

            print("Please choose a race for your character, or a description of the races")
            for amount, _ in enumerate(races):
                print(f"{amount + 1} for {races[amount]}")
            # print(f"Type 1 for {races[0]}")
            # print(f"Type 2 for {races[1]}")
            # print(f"Type 3 for {races[2]}")
            # print(f"Type 4 for {races[3]}")
            # print(f"Type 5 for {races[4]}")
            print(f"Type 6 for descriptions.")

            race_choice = input()

            try:  # Making sure the user input a number and converting it to a list usable set
                race_choice = int(race_choice) - 1

                if 0 <= race_choice <= 4:
                    break
                if not 0 <= race_choice <= 5:
                    break

                for amount, _ in enumerate(races):
                    print(f"{amount + 1} for a {races[amount]} description.")
                # print(f"Type 1 for a {races[0]} description.")
                # print(f"Type 2 for a {races[1]} description.")
                # print(f"Type 3 for a {races[2]} description.")
                # print(f"Type 4 for a {races[3]} description.")
                # print(f"Type 5 for a {races[4]} description.")
                print(f"Type 6 to go back to choose a race.")

                race_description_choice = input()

                try:  # Making sure the user input a number and converting it to a list usable set
                    race_description_choice = int(race_description_choice) - 1

                    if not 0 <= race_description_choice <= 5:
                        print("Only type 1 through 6 please.")
                    if 0 <= race_description_choice <= 4:
                        print(game_descriptions.race_(race_description_choice))
                    if race_description_choice == 5:
                        pass

                except ValueError:  # In case they did not type a number
                    print("Please only type numbers!")

            except ValueError:  # In case they did not type a number
                print("Please only type numbers!")

        if not 0 <= race_choice <= 4:
            print("Please only type numbers between and including 1 through 5!")

        if 0 <= race_choice <= 4:
            print(f"You have chosen {races[race_choice]}")
            print("Do you wish to continue (yes or no)")
            yes_ = "yes y ye"
            no_ = "no n o on"

            while True:
                race_correct = input().lower()  # User input for making sure they didn't change their minds

                if race_correct in yes_:
                    size_choice = sizes[2]
                    print(f"You have chosen {races[race_choice]} as your race, good luck!")
                    if races[race_choice] == races[2]:
                        # Generates your language if you choose human (humans as a species only gain common
                        # But then they also gain one of your choice, so they still get to know 2 just you choose
                        lang_choice = [languages[2]]
                        print(f"Your race knows the languages {lang_choice}")
                        race_choice = races[race_choice]  # Generates chosen race if they choose human
                        race_correct = "yes"
                        break
                    lang_choice = [languages[race_choice], languages[2]]  # Generates users lang based on their race
                    print(f"Your race knows the languages {lang_choice}")
                    race_choice = races[race_choice]  # Generates the race they chose
                    race_correct = "yes"
                    break
                if race_correct in no_:
                    print("Please choose again then.")
                    race_correct = "no"
                    break
                else:
                    print("Please only type yes or no.")

        try:  # In case the user does change their mind, and the race_correct variable doesn't get defined
            if race_correct == "yes":
                break
        except UnboundLocalError:
            pass

    # Returning all the variables that make up their racial info
    return gender_choice, lang_choice, race_choice, size_choice


def player_class_setup():  # The setup for the PC's alignment, background, build (class), health, and level

    while True:
        game_classes = ["Bard", "Cleric", "Druid", "Paladin", "Warlock"]  # Classes in the game
        health_values = [8, 8, 8, 10, 8]  # HP for each class (aligned with class on list index)

        while True:

            print("Please choose a class.")
            for amount, _ in enumerate(game_classes):
                print(f"{amount + 1} for {game_classes[amount]}")
            # print(f"Type 1 for {game_classes[0]}")
            # print(f"Type 2 for {game_classes[1]}")
            # print(f"Type 3 for {game_classes[2]}")
            # print(f"Type 4 for {game_classes[3]}")
            # print(f"Type 5 for {game_classes[4]}")
            print(f"Type 6 for descriptions of each class")

            player_class_choice = input()

            try:  # Making sure the user input a number and converting it to a list usable set
                player_class_choice = int(player_class_choice) - 1

                if 0 <= player_class_choice >= 4:
                    break
                if not 0 <= player_class_choice >= 5:
                    print("Only numbers 1 through 6")
                    break

                for amount, _ in enumerate(game_classes):
                    print(f"{amount + 1} for a {game_classes[amount]} description.")
                # print(f"Type 1 for a {game_classes[0]} description.")
                # print(f"Type 2 for a {game_classes[1]} description.")
                # print(f"Type 3 for a {game_classes[2]} description.")
                # print(f"Type 4 for a {game_classes[3]} description.")
                # print(f"Type 5 for a {game_classes[4]} description.")
                print(f"Type 6 to go back to choose a class.")

                class_description_choice = input()

                try:
                    class_description_choice = int(class_description_choice) - 1

                    if not 0 <= player_class_choice >= 5:
                        print("please only numbers 1 through 6")
                    if class_description_choice == 5:
                        pass
                    if 0 <= class_description_choice <= 4:
                        print(game_descriptions.classes_(class_description_choice))

                except ValueError:
                    print("Please only type numbers!")

            except ValueError:  # In case they don't type a number
                print("Please only type numbers!")

        if 0 <= player_class_choice <= 4:
            while True:
                print(
                    f"You have chosen {game_classes[player_class_choice]} as your class, do you wish to continue?(yes or no)")
                yes_ = "yes y ye"
                no_ = "no n o on"

                class_correct = input().lower()

                if class_correct in yes_:
                    health_choice = health_values[player_class_choice]
                    player_class_choice = game_classes[player_class_choice]
                    print("Good luck!")
                    class_correct = "yes"
                    break
                if class_correct in no_:
                    print("Then please choose again.")
                    break
                else:
                    print("Please just type yes or no.")

        try:
            if class_correct == "yes":
                break
        except UnboundLocalError:
            pass

    # while True:  # Allowing the user to choose their alignment
    #
    #     alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral",
    #                   "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]  # DnD alignments
    #
    #     print("Please choose an alignment")
    #     print(f"1 for {alignments[0]}")
    #     print(f"2 for {alignments[1]}")
    #     print(f"3 for {alignments[2]}")
    #     print(f"4 for {alignments[3]}")
    #     print(f"5 for {alignments[4]}")
    #     print(f"6 for {alignments[5]}")
    #     print(f"7 for {alignments[6]}")
    #     print(f"8 for {alignments[7]}")
    #     print(f"9 for {alignments[8]}")
    #
    #     alignment_choice = input()
    #
    #     try:  # Making sure the user input a number and converting it to a list usable set
    #         alignment_choice = int(alignment_choice) - 1
    #
    #         if alignment_choice < 0 or alignment_choice > 8:
    #             print("Only numbers 1 through 9 please!")
    #
    #         if 0 <= alignment_choice <= 8:
    #             print(
    #                 f"You have chosen {alignments[alignment_choice]} as your alignment do you wish to continue? (yes or no)")
    #
    #             while True:
    #                 yes_ = "yes y ye"
    #                 no_ = "no n o on"
    #
    #                 alignment_correct = input().lower()
    #
    #                 if alignment_correct in yes_:
    #                     print("Good luck!")
    #                     alignment_choice = alignments[alignment_choice]  # Generating players alignment
    #                     alignment_correct = "yes"
    #                     break
    #                 if alignment_correct in no_:
    #                     print("Then please choose again.")
    #                     break
    #                 else:
    #                     print("Please only type yes or no!")
    #     except ValueError:  # In case the user did not input a number
    #         print("Please only type a number")
    #
    #     try:
    #         if alignment_correct == "yes":
    #             break
    #     except UnboundLocalError:
    #         pass

    while True:

        # All backgrounds in DnD 5e PHB, look in there if you want more *background* info on them... I'll see myself out
        backgrounds = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermit",
                       "Noble", "Outlander", "Sage", "Sailor", "Soldier", "Urchin"]

        while True:

            print(
                "Please choose a background, if you want further explanation on backgrounds 'The Players Handbook' is a great place to look")
            for amount, y in enumerate(backgrounds):
                print(f"{amount + 1} for {backgrounds[amount]}")

            print(f"14 for a description of each background.")

            # print(f"1 for {backgrounds[0]}")
            # print(f"2 for {backgrounds[1]}")
            # print(f"3 for {backgrounds[2]}")
            # print(f"4 for {backgrounds[3]}")
            # print(f"5 for {backgrounds[4]}")
            # print(f"6 for {backgrounds[5]}")
            # print(f"7 for {backgrounds[6]}")
            # print(f"8 for {backgrounds[7]}")
            # print(f"9 for {backgrounds[8]}")
            # print(f"10 for {backgrounds[9]}")
            # print(f"11 for {backgrounds[10]}")
            # print(f"12 for {backgrounds[11]}")
            # print(f"13 for {backgrounds[12]}")
            # print(f"14 for a description of each background.")

            background_choice = input().lower()

            try:
                background_choice = int(background_choice) - 1

                if background_choice == 13:
                    for amount, y in enumerate(backgrounds):
                        print(f"{amount + 1} for a {backgrounds[amount]} description.")

                    print(f"14 to go back to choose a background.")

                    background_description_choice = input()

                    try:
                        background_description_choice = int(background_description_choice) - 1

                        if 0 <= background_description_choice <= 12:
                            print(game_descriptions.backgrounds_(background_description_choice))

                        if not 0 <= background_description_choice <= 13:
                            print("Only 1 through 14")

                    except ValueError:
                        print("Numbers only dumb dumb")

                # if background_choice < 0 or background_choice > 12:
                #     print(f"1 for a {backgrounds[0]} description")
                #     print(f"2 for a {backgrounds[1]} description")
                #     print(f"3 for a {backgrounds[2]} description")
                #     print(f"4 for a {backgrounds[3]} description")
                #     print(f"5 for a {backgrounds[4]} description")
                #     print(f"6 for a {backgrounds[5]} description")
                #     print(f"7 for a {backgrounds[6]} description")
                #     print(f"8 for a {backgrounds[7]} description")
                #     print(f"9 for a {backgrounds[8]} description")
                #     print(f"10 for a {backgrounds[9]} description")
                #     print(f"11 for a {backgrounds[10]} description")
                #     print(f"12 for a {backgrounds[11]} description")
                #     print(f"13 for a {backgrounds[12]} description")

                if 0 <= background_choice <= 12:
                    print(f"You chose {backgrounds[background_choice]}, do you wish to continue? (yes or no)")

                    while True:
                        yes_ = "yes y ye"
                        no_ = "no n o on"

                        bg_correct = input().lower()

                        if bg_correct in yes_:
                            print("Good luck!")
                            background_choice = backgrounds[background_choice]  # Generating players background
                            bg_correct = "yes"
                            break
                        if bg_correct in no_:
                            print("Please choose again then.")
                            break
                        else:
                            print("Please only yes or no")

                if not 0 <= background_choice <= 13:
                    print("Please only 1 through 14")

            except ValueError:  # Making sure player typed a number
                print("Please only type numbers")

            try:
                if bg_correct == "yes":
                    break
            except UnboundLocalError:
                pass

        break

    # Returning all info based on class and such
    # // return alignment_choice, taking this off for now might bring back
    return background_choice, player_class_choice, health_choice


def build_options():
    print(f"You have chosen {build} as your class.")
    print("You are now going to choose your classes options")
    print(f"For a full list of all available options for both your class and the level you chose, look inside the 5th"
          f"edition PHB")


# p_alignment, p_background, p_bonds, p_flaws, p_gender, p_height, p_ideals, p_lang, p_lvl, p_race, p_size, p_weight
# p_c_features, p_r_traits, p_attacks, p_bg_options, p_build, p_health, p_proficiencies
gender, lang_choices, race, size = race_setup()
bg, build, health = player_class_setup()

lang_str = ""  # making it so when PC's with more than two languages come in here they are properly handled
for x in lang_choices:
    lang_str = lang_str.__add__(f"{x} ")

with open("class_options.txt", "w") as f:
    f.write(f"""
background={bg}
class={build}
gender={gender}
health={health}
languages={lang_str}
race={race}
size={size}""")
