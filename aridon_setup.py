# ? C:\Users\Bobasarous\Documents\Random Windows Stuff\Programming\PythonStuffs\aridon\aridon_setup.py

# Aridon is a text based adventure based on DnD rules, classes, etc...
# TODO Add user input that allows them to choose to see explanations for all races, classes, backgrounds, and alignments
# TODO Finish making all the class option set ups for all the classes in game, and everything

import race_descriptions


# Setup for the player's race, size, most of the languages they will know, and their gender
def race_setup():
    while True:  # Loop for user to choose their gender
        genders = ["male", "female", "neutral/NB", "Choose your own"]

        print(f"Do you want to be {genders[0]}(1), {genders[1]}(2), or {genders[2]}(3), {genders[3]}(4)?")

        gender_choice = input().lower()  # User input for which gender they want

        try:  # Making sure the user input a number and converting it to a list usable set
            gender_choice = int(gender_choice) - 1  # Turning the numbers into usable numbers for the list

            if gender_choice < 0 or gender_choice > 3:  # Making sure the numbers are in the right range
                print("Please only choose numbers 1-4")
                gender_choice = "yes"

            if 0 <= gender_choice <= 3:
                while True:
                    yes_ = "yes y ye"  # variations of yes
                    no_ = "no n o on"  # Variations of no
                    if 0 <= gender_choice <= 2:
                        print(f"You have chosen {genders[gender_choice]}, do you wish to continue? (yes or no)")

                        gender_correct = input().lower()  # User input for making sure they didn't change their mind

                        if gender_correct in yes_:
                            print(f"You have chosen {genders[gender_choice]} as your gender, good luck!")
                            gender_choice = genders[gender_choice]  # Generates the users gender so we can return it
                            gender_correct = "yes"
                            break
                        if gender_correct in no_:
                            print("Alright, please try again.")
                            break
                        else:  # Making sure they only type yes or no
                            print("Please only type yes or no!")

                    if gender_choice == 3:
                        yes_ = "yes y ye"  # variations of yes
                        no_ = "no n o on"  # Variations of no
                        print("Please type your own gender")
                        gender_choice = input()  # Allowing the player to choose and type their own gender
                        print(f"You have chosen {gender_choice} as your gender are you sure you wish to continue?")
                        # Showing the user what they typed and making sure they want it

                        gender_correct = input().lower()  # Input for users to tell if they are sure they choose right

                        if gender_correct in yes_:
                            print(f"You have chosen {gender_choice}, good luck!")
                            gender_correct = "yes"
                            break
                        if gender_correct in no_:
                            print("Alright, please try again.")
                            break
                        else:  # Making sure they only type yes or no
                            print("Please only type yes or no!")

        except ValueError:  # In case they did not type a number
            print("Please type only numbers")

        try:  # Making sure that gender_correct doesn't get used if it is not defined (Happens if the user chooses no)
            if gender_correct in yes_:
                break
        except UnboundLocalError:
            pass

    while True:  # Loop for choosing their race

        # Used to access the races_dict variable, and makes it easier to assign race here, only making the user type -
        # numbers, instead of typing a whole word, which they could misspell, and then I'd have to make if statements -
        # for each race, instead of just assigning it based off of numbers and such, much easier to have both variables
        races = ["Dwarf", "Elf", "Human", "Half-Orc", "Tiefling"]

        # All the races in the game, make sure they line up with their racial counterpart, will make it easier to -
        # grab which lang you want based on the race the user choose
        languages = ["Dwarvish", "Elvish", "Common", "Orcish", "Infernal"]
        # All the sizes in the game
        sizes = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]

        print("Please choose a race for your character.")
        print(f"Type 1 for {races[0]}")
        print(f"Type 2 for {races[1]}")
        print(f"Type 3 for {races[2]}")
        print(f"Type 4 for {races[3]}")
        print(f"Type 5 for {races[4]}")

        race_choice = input()  # User input for which race they want

        try:  # Making sure the user input a number and converting it to a list usable set
            race_choice = int(race_choice) - 1

            if race_choice < 0 or race_choice > 4:  # Making sure they only used number in proper range
                print("Please only type numbers between and including 1 through 5!")

            if 0 <= race_choice <= 4:
                print(f"You have chosen {races[race_choice]} here is a little bit about them")
                print(race_descriptions.race_(race_choice))
                print("Do you wish to continue (yes or no)")
                yes_ = "yes y ye"  # variations of yes
                no_ = "no n o on"  # Variations of no

                if 0 <= race_choice <= 4:  # Making sure they choose the correct numbers, and then generates users size
                    size_choice = sizes[2]

                while True:
                    race_correct = input().lower()  # User input for making sure they didn't change their minds

                    if race_correct in yes_:
                        print(f"You have chosen {races[race_choice]} as your race, good luck!")
                        lang_choice = [languages[race_choice], languages[3]]  # Generates users lang based on their race
                        print(f"You know the languages {lang_choice}")
                        race_choice = races[race_choice]  # Generates the race they chose
                        race_correct = "yes"
                        break
                    if race_correct in no_:
                        print("Please choose again then.")
                        race_correct = "no"
                        break
                    else:  # Making sure they only type yes or no
                        print("Please only type yes or no.")

        except ValueError:  # In case they did not type a number
            print("Please only type numbers!")
            race_correct = "no"

        try:  # In case the user does change their mind, and the race_correct variable doesn't get defined
            if race_correct == "yes":
                break
        except UnboundLocalError:
            pass

    # Returning all the variables that make up their racial info
    return gender_choice, lang_choice, race_choice, size_choice


def build_setup():  # The setup for the PC's alignment, background, build (class), health, and level

    while True:
        # All the classes in the game
        classes_ = ["Bard", "Cleric", "Druid", "Paladin", "Warlock"]
        # The health values for each class MAKE SURE THIS IS ALIGNED with ^
        health_values = [8, 8, 8, 10, 8]

        print("Please choose a class.")
        print(f"Type 1 for {classes_[0]}")
        print(f"Type 2 for {classes_[1]}")
        print(f"Type 3 for {classes_[2]}")
        print(f"Type 4 for {classes_[3]}")
        print(f"Type 5 for {classes_[4]}")

        build_choice = input()  # User input to choose which class they want

        try:  # Making sure the user input a number and converting it to a list usable set
            build_choice = int(build_choice) - 1

            if build_choice < 0 or build_choice > 4:  # Making sure they choose the right numbers
                print("Please only type numbers 1 through 5")

            if 0 <= build_choice <= 4:
                while True:
                    print(f"You have chosen {classes_[build_choice]} as your class, do you wish to continue?(yes or no)"
                          f"")
                    yes_ = "yes y ye"  # variations of yes
                    no_ = "no n o on"  # Variations of no

                    build_correct = input().lower()  # Making sure the user didn't change their mind

                    if build_correct in yes_:
                        health_choice = health_values[build_choice]
                        build_choice = classes_[build_choice]
                        print("Good luck!")
                        build_correct = "yes"
                        break
                    if build_correct in no_:
                        print("Then please choose again.")
                        break
                    else:
                        print("Please just type yes or no.")

        except ValueError:  # In case they don't type a number
            print("Please only type numbers!")

        try:
            if build_correct == "yes":
                break
        except UnboundLocalError:
            pass

    while True:  # Allowing the user to choose their alignment

        # All the alignments in the game
        alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral",
                      "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]

        print("Please choose an alignment")
        print(f"1 for {alignments[0]}")
        print(f"2 for {alignments[1]}")
        print(f"3 for {alignments[2]}")
        print(f"4 for {alignments[3]}")
        print(f"5 for {alignments[4]}")
        print(f"6 for {alignments[5]}")
        print(f"7 for {alignments[6]}")
        print(f"8 for {alignments[7]}")
        print(f"9 for {alignments[8]}")

        alignment_choice = input()  # User input to choose the alignments

        try:  # Making sure the user input a number and converting it to a list usable set
            alignment_choice = int(alignment_choice) - 1

            if alignment_choice < 0 or alignment_choice > 8:  # Making sure the user used numbers 1 through 9
                print("Only numbers 1 through 9 please!")

            if 0 <= alignment_choice <= 8:
                print(f"You have chosen {alignments[alignment_choice]} as your alignment do you wish to continue? ("
                      f"yes or no)")

                while True:  # Giving the player a chance to change their minds
                    yes_ = "yes y ye"  # variations of yes
                    no_ = "no n o on"  # Variations of no

                    alignment_correct = input().lower()

                    if alignment_correct in yes_:
                        print("Good luck!")
                        alignment_choice = alignments[alignment_choice]  # Setting the variable to the value we want -
                        alignment_correct = "yes"  # so we can return it
                        break
                    if alignment_correct in no_:
                        print("Then please choose again.")
                        break
                    else:
                        print("Please only type yes or no!")
        except ValueError:  # In case the user did not input a number
            print("Please only type a number")

        try:
            if alignment_correct == "yes":
                break
        except UnboundLocalError:
            pass

    while True:

        # All backgrounds in DnD 5e PHB, look in there if you want more *background* info on them... I'll see myself out
        backgrounds = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermit",
                       "Noble", "Outlander", "Sage", "Sailor", "Soldier", "Urchin"]

        print("Please choose a background, if you want further explanation on backgrounds 'The Players Handbook' is a "
              "great place to look")
        print(f"1 for {backgrounds[0]}")
        print(f"2 for {backgrounds[1]}")
        print(f"3 for {backgrounds[2]}")
        print(f"4 for {backgrounds[3]}")
        print(f"5 for {backgrounds[4]}")
        print(f"6 for {backgrounds[5]}")
        print(f"7 for {backgrounds[6]}")
        print(f"8 for {backgrounds[7]}")
        print(f"9 for {backgrounds[8]}")
        print(f"10 for {backgrounds[9]}")
        print(f"11 for {backgrounds[10]}")
        print(f"12 for {backgrounds[11]}")
        print(f"13 for {backgrounds[12]}")

        background_choice = input().lower()  # Users input for what background they want to choose

        try:
            background_choice = int(background_choice) - 1

            if background_choice < 0 or background_choice > 12:
                print("Please only type 1 through 13")

            if 0 <= background_choice <= 12:
                print(f"You chose {backgrounds[background_choice]}, do you wish to continue? (yes or no)")

                while True:
                    yes_ = "yes y ye"  # variations of yes
                    no_ = "no n o on"  # Variations of no

                    bg_correct = input().lower()

                    if bg_correct in yes_:
                        print("Good luck!")
                        background_choice = backgrounds[background_choice]
                        bg_correct = "yes"
                        break
                    if bg_correct in no_:
                        print("Please choose again then.")
                        break
                    else:
                        print("Please only yes or no")

        except ValueError:
            print("Please only type numbers")

        try:
            if bg_correct == "yes":
                break
        except UnboundLocalError:
            pass

    return alignment_choice, background_choice, build_choice, health_choice


def build_options():
    print(f"You have chosen {build} as your class.")
    print("You are now going to choose your classes options")
    print(f"For a full list of all available options for both your class and the level you chose, look inside the 5th"
          f"edition PHB")


# p_alignment, p_background, p_bonds, p_flaws, p_gender, p_height, p_ideals, p_lang, p_lvl, p_race, p_size, p_weight
# p_c_features, p_r_traits, p_attacks, p_bg_options, p_build, p_health, p_proficiencies
gender, lang_choices, race, size = race_setup()
alignment, bg, build, health = build_setup()

lang_str = ""
lang_len = len(lang_choices)
for x in range(lang_len):
    lang_len = lang_len - 1
    lang_str = lang_str.__add__(f"{lang_choices[lang_len]}")


with open("class_options.txt", "w") as f:
    f.write(f"alignment={alignment}" + "\n"
            f"background={bg}" + "\n"
            f"class={build}" + "\n"
            f"gender={gender}" + "\n"
            f"health={health}" + "\n"
            f"languages={lang_str}" + "\n"
            f"race={race}" + "\n"
            f"size={size}" + "\n")
