# Features, traits, and descriptions of all races


def race_(race_choice):
    if race_choice == 0:
        description = "Dwarves are a hardy folk, shout and stout, strong and loyal, they live deep in mountains and " \
                      "caves, they come in all shorts of shades and hues, are a people of lawful nature, and stick to " \
                      "their own, but if need be they will come to the aid of any oppressed people and help fight " \
                      "their oppressors. Dwarves tend to be lawful good, and you gain +2 on con, and +1 on wisdom if " \
                      "you choose hill, and a +2 to strength if you choose Mountain, if you'd like to read more about " \
                      "them go to page 20 in the PHB. "

    if race_choice == 1:
        description = "Dragonborn are a people created by the magic of dragons, born into this world to serve their masters, both" \
            "good and evil. Dragonborn tend to extremes and are rarely neutral in anyways, even if the dragon they serve" \
            "is. Dragonborns are a tall and strong scaly humanoid race you gain +2 on strength and +1 on charisma, and if" \
            "like to learn more about them go to page 34 of the PHB." \

    if race_choice == 2:
        description = "Elves are a very slender race of people, they are agile in quick in both physical and mental tasks, they " \
            "hone to perfection any task they want to learn, and are typically chaotic good, flowing through life doing" \
            "whatever makes them happy. Elves gain a +2 on dexterity and a +1 on intelligence if you choose High, and " \
            "a +1 to wisdom if you choose wood. If you'd like to learn more go to page 24 of the PHB." \

    if race_choice == 3:
        description = "Humans are anything they want to be, they live short lives compared to the other people of aridon, and " \
            "because of that they strive to learn as much as quickly as possible, most humans spend their lives " \
            "dedicating themselves to one task or job, learning how to do it the best they can. Humans can be anything" \
            "good, bad, lawful, evil, neutral, and come in all shorts of shades and hues, they gain a +1 to all stats, " \
            "unless you choose the variant options which then they get 2 +1s of your choosing, a feat, and a proficiency." \
            "If you want to learn more about humans, go to page 31 of the PHB." \

    if race_choice == 4:
        description = "The loxodon of Aridon are an ancient race, in fact some believe they are the oldest race, but they are rare" \
            "long ago there was a war that nearly wiped out all loxodon and finding one is an exceptional site to behold" \
            "for most people. Loxodon tend to be smart, but simple folk, they are all almost always good, except for" \
            "extremely rare cases, are typically light shades of gray, walk on 2 massive feet, have huge limbs, are very " \
            "tall, and you gain +2 on constitution and a +1 on wisdom, and if you'd like to learn more about them, please" \
            "read page 18 of 'Guildmasters' Guide to Ravnica'" \

    if race_choice == 5:
        description = "Orcs are a chaotic race, but unlike in most other settings, in Aridion Orcs, while still very aggressive," \
            "and warrior like, they are not evil. Orcs in Aridon are a strange people to most, most would look at them" \
            "and assume they are beings of hatred and war, and while partially true, Orcs have sworn their hatred and " \
            "war culture to the downfall of any people who would harm the meek, Orcs are strong allies of Halflings, and" \
            "while you would rarely see a random Halfling or Orc strolling about through the others city or town, they" \
            "both harbor friendship for one another. However, as a half-Orc you may or may not be apart of Orc culture," \
            " you may grow up in another territory away from your orc relatives. Half-Orcs gain a +2 to strength and" \
            "+1 to constitution, and if you'd like to learn more read page 41 of the PHB" \

    if race_choice == 6:
        description = "Tieflings aren't actually their own full on race, they are more like a strong blooded ethnicity among humans" \
            ". Long ago a group of vile humans sought to ruin their own kingdom in an act of hatred and made a deal with" \
            "an evil devious god, and in doing so became cursed. Tieflings typically have a long thick tails and horns." \
            "They come in all shades and colors humans do, but then also red/purple, and rarely shades of blue. Tieflings" \
            ", nowadays, however are so far removed from their once evil ancestors, and so much mixing of other humans" \
            "and themselves have made it so that culture of evil in the original group has long since been lost, and" \
            "while most still know of the tieflings ancestry, very few care, and tieflings walk among most humans like" \
            "anyone else would in Aridon. As a Tiefling you gain +2 to Charisma and a +1 to Intelligence. If you would" \
            "like to read more about them please read page 43 or the PHB." \

    return description