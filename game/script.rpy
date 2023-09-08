define n = Character("Nigel")
define d = Character("Digby")
define y = Character("[name]")
define z = Character("???")
define N = Character(what_italic=True)
define slowdissolve = Dissolve(1.0)

label start:

    python:
        name = renpy.input("What's your name?")

        name = name.strip() or "Guy Shy"

    N "Stupes and Dan find themselves working another late night on their videos."
    N "Stupes ends up neck deep into animating a new music video while Dan edits his latest project."
    N "Stupes yawns as they stretch their back, a loud pop resonates throughout the room. They groan as they rub their eyes."
    N "Dan drinks from his neglected cup of coffee as his eyes began to feel more and more heavy."
    N "The both of them, overworked and exhausted, close their respective projects."
    N "Stupes crosses their arms as they begin to sigh."
    N "Dan gets up and groggily makes his way to bed."
    N "They both begin to speak simultaneously, \"I wish this video would just finish itself.\""
    N "Both leave their respective rooms as their computers whir to life."
    N "A bright red light emits from both their monitors."
    N "Pixels begin to hum and scream as multiple hands reach through the LCD displays."

scene black
show bg park table:
    xzoom .60 yzoom .60 xalign 0.5
with slowdissolve
N "It was a beautiful day, you decide to get out of the house to take advantage of the gorgeous weather."
N "You find yourself walking in the park as you see someone playing battleship by themselves."
N "They appear to be losing."
N "You approach the stranger as you realize that they're too engrossed in their task to even notice you."

menu:
    "Say Hi":
        jump choice1_yes

    "Tap them on the shoulder":
        jump choice1_no

label choice1_yes:

    $ menu_flag = True

    y "...Hello?"

    N "The stranger jumps as they knock over a peg."

    jump choice1_done

label choice1_no:

    $ menu_flag = False

    N "You tap the stranger on the shoulder. The stranger jumps and lets out a yelp."

    jump choice1_done

label choice1_done:

z "Oh, my apologies, I didn't see you there"

menu:
    "Tell them it's okay":
        jump choice2_yes1

    "Ask them where the other player is":
        jump choice2_no1

label choice2_yes1:

    $ menu_flag = True

    y "Don't worry, it's alright."
    y "What are you doing if you don't mind me asking?"
    z "I'm honing my craft."
    z "You see, I'm a bit of a board game enthusiast."
    y "Wouldn't it be better if you played with someone else, to give yourself a bit of a challenge?"
    z "I've tried."
    z "But none of my friends really want to go against me anymore."

jump choice2_done

label choice2_no1:

    $ menu_flag = False

    y "Who are you playing against?"
    z "I'm playing against myself."
    z "I'm trying to hone my skills."

jump choice2_done

label choice2_done:

    z "Excuse me, where are my manners?"
    n "The name's Nigel."
    n "And you are?..."
    y "The name's [name]"
    y "Would it be okay if I joined you?"
    n "Does using all 7 tiles in Scrabble give you a 50 point bonus?"
    N "..."
    N "Huh?"
    n "Yes."
    n "The answer's yes."
    N "You sit down at the bench and look down at the board, pieces scattered from a game unfinished."
    N "You assemble your fleet and get to work."
    N ". . ."
    N "A few minutes pass and you slowly begin to realize that you're losing horribly."
    N "A smug grin spreads against Nigel's face."
    N "At this point, there's a strong likelyhood that any hit will result in you losing."
    N "Nigel swiftly lands on your last peg as they laugh triumphantly and fold their arms."
    N "Nigel reaches out their hand, as if extending their hand to friendship."
    n "Well played."
    n "You really had me there."
    N "You know they're just trying to butter you up but they're being nice so you accept their compliment."
    n "Say..."
    n "Would you like to accompany me to my place to  play a bit of Scrabble?"
    n "You see, I've been looking for someone to test my wits and well..."
    n "You're the only person in a long time to offer to play with me."
    N "You're unsure if you should go with them."
    N "I mean, you just met them."

    menu:
        "Agree to go with them":
            jump choice3_yes2

        "Ask what's in it for you":
            jump choice3_no2

label choice3_yes2:

    $ menu_flag = True

    scene bg city

    N "You decide to go with them, they usher you in their direction as you both make it back to their place."
    N "The sun begins to set as you make it to an apartment complex."
    N "You make your way up the elevator as you make it to apartment number 302."

jump choice3_done

label choice3_no2:

    $ menu_flag = False

    y "What's in it for me if I do go with you?"
    n "I can get you free tickets to the Scrabble tournement I'm going to be competing in."
    y "Deal."

    scene bg city

    N "You decide to go with them, they usher you in their direction as you both make it back to their place."
    N "The sun begins to set as you make it to an apartment complex."
    N "You make your way up the elevator as you make it to apartment number 302."

jump choice3_done

label choice3_done:

    scene black

    n "Welcome to my They Cave!"
    n "Be wary of the boards, I'd hate to lose weeks of progress."
    N "Scattered around are several games of Monopoly, seemingly in different stages of progression, all meticulously arranged."
    N "It looks as if they're part of one larger game."
    n "5th-Dimensional Monopoly, it's all the rage these days!"
    n "At least, within the confines of this room that is."
    N "Your eyes scan the room for the Scrabble board, quickly spotting it set up at a table sitting in the corner."
    n "Come— Sit, sit."
    N "They gesture towards a small stool adjacent to the table."
    N "The tiles are already set up; catching a glimpse of their side, you see mainly consonants and few vowels, with yours being quite the opposite."
    N "It appears that you have the advantage."
    N "As you sit down you feel your surroundings begin to shift."
    N "Papers flutter about, game tiles begin to scatter, the ground rumbles beneath your feet."
    n "Oh, don't worry about that, this just happens sometimes."
    N "They crack their neck and look you dead in the eye."
    n "I told you, I haven't had anyone to challenge in a while."
    n "You should go first."
    n "Please, I insist."

return
