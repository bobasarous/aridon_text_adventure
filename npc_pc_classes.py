# ? C:\Users\Bobasarous\Documents\Random Windows Stuff\Programming\PythonStuffs\Aridon\npc_pc_classes.py


class PlayerClass:  # The players class options and such
    def __init__(self, p_alignment, p_background, p_bonds, p_flaws, p_gender, p_height, p_ideals, p_lang, p_lvl,
                 p_race, p_size, p_weight):
        self.p_alignment = p_alignment  # Player's alignment
        self.p_background = p_background  # Player's background, only backgrounds found in PHB will be found in here so-
        # far, but I plan to add more
        self.p_bonds = p_bonds  # Character's bonds, used to give inspiration
        self.p_flaws = p_flaws  # Flaws of the character, used to give inspiration
        self.p_gender = p_gender  # Player's gender
        self.p_height = p_height  # PC's height
        self.p_ideals = p_ideals  # PC's ideals, used to give inspiration
        self.p_lang = p_lang  # The languages the player knows
        self.p_lvl = p_lvl  # The players level
        self.p_race = p_race  # The players race
        self.p_size = p_size  # The player's character's size, can be any size in DnD
        self.p_weight = p_weight  # PC's weight


class PlayerAbilities:  # The abilities and options the player can have, from the classes, races, backgrounds: such
    # as attacks, feats, etc...
    def __init__(self, p_c_abilities, p_r_abilities, p_attack, p_bg_options, p_build, p_cha, p_con, p_dex, p_health,
                 p_int, p_proficiencies, p_str, p_wis):
        self.p_c_abilities = p_c_abilities  # All the characters abilities granted by their class, race, etc...
        self.p_r_abilities = p_r_abilities  # All the characters abilities granted by their class, race, etc...
        self.p_attack = p_attack  # The characters ability to attack
        self.p_bg_options = p_bg_options  # Background options and such for the character
        self.p_build = p_build  # Build is the players class, but cant use the word class, so build is in its place
        self.p_cha = p_cha  # PC's charisma modifier
        self.p_con = p_con  # PC's constitution modifier
        self.p_dex = p_dex  # PC's dexterity modifier
        self.p_health = p_health  # Players health
        self.p_int = p_int  # PC's intelligence modifier
        self.p_proficiencies = p_proficiencies  # Proficiencies the player has when doing ability checks, saving-
        # throws, etc...
        self.p_str = p_str  # PC's strength modifier
        self.p_wis = p_wis  # PC's wisdom modifier


class Goblin:  # Class for all fights against goblins
    def __init__(self, p_abilities, p_alignment, p_attack, p_gender, p_health, p_lang, p_lvl, p_race, p_size):
        self.p_abilities = p_abilities  # All the goblin's abilities granted by their class, race, etc...
        self.p_alignment = p_alignment  # Goblin's alignment
        self.p_attack = p_attack  # The goblins to attack
        self.p_gender = p_gender  # Goblin's gender
        self.p_health = p_health  # goblin's health
        self.p_lang = p_lang  # The languages the goblin knows
        self.p_lvl = p_lvl  # The goblin's level
        self.p_race = p_race  # The goblin's race
        self.p_size = p_size  # The goblin's size, can be any size in DnD
