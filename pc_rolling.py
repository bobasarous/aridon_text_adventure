# ? C:\Users\Bobasarous\Documents\Random Windows Stuff\Programming\PythonStuffs\aridon\pc_rolling.py

import aridon_setup


def pc_appearance():  # Letting the user choose what their character looks like or letting them roll for it
    print("Now we will figure out exactly how your character may look")

    while True:  # Loop for height and weight
        print("Do you wish to choose your characters height and weight, or roll for it?")
        print("1 for choosing yourself.")
        print("2 for rolling for it.")

        app_choice = ["choose yourself", "roll"]

        one_or_two = input()

        try:
            one_or_two = int(one_or_two) - 1

            print(f"You have chosen to {app_choice[one_or_two]}, is this correct? (yes or no)")
            yes_ = "yes y ye"  # variations of yes
            no_ = "no n o on"  # Variations of no

            app_correct = input().lower()

            if app_correct in yes_:
                print("Choose wisely!")

                if one_or_two == 0:
                    print(f"You have chosen to choose yourself, so your choices will be based on your race, "
                          f"{aridon_setup.race}.")

                    races_height_weight = {
                        {aridon_setup.race_list[0]: {
                            "Hill Dwarf": {"Height": "3'10\" - 4'4\"", "Weight": "119lbs - 211lbs"},
                            "Mountain Dwarf": {"Height": "4' - 4'4\"", "Weight": "234lbs - 226lbs"}}}}

                if one_or_two == 1:
                    print(f"You have chosen to roll, the roll will be based on your race, {aridon_setup.race}.")

            if app_correct in no_:
                print("Please choose again then!")
                break

            else:
                print("Please only type yes or no")
        except ValueError:
            print("Only type 1 or 2 please!")


appearance = pc_appearance()
