class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
picasso_room = Scene("Picasso Room", "picasso_room",
"""
You wake up after a while. Darkness around. Silent.
You can see nothing and hear nothing.
Where is everybody? Where is Mrs. Lee and my classmates?

You remember today was a school trip day to museum.
Everyone was follwing Mrs. Lee, their teacher, listeing to her explanation of artworks.
You, however, thought everything about the museum was boring shit so you sneaked out to have fun.
While wandering around alone, you feel tired and fall asleep.

Suddenly the light turns on.
You are in a red room. There is a weeping woman in the middle of the red room.
Thick drops of tear fall from her sad eyes.
Her face is weird, you thought.
It's distorted, divided into irregular pieces.
You are confused, and scared.

What is happening?
You look at the weeping woman.
What will you do?

-cry
-give her a hankercheif
-ignore

""")

munch_room = Scene("Munch Room", "munch_room",
"""
Wise of you to help a sad woman.
She is pleased by your kindness and leads you to a distorted door.
You enter the next room.
As soon as you enter there, you hear a screeching sound.
Somebody is screaming like a mad person.
You see a screaming man on the black bridge.
He is screaming everybody's ears off. Two hands on his ears, his mouth as big as his face.
You are so annoyed by the scream.
What do you do?

-punch him in the face
-start screaming back
-ask why he is screaming

""")

klimt_room = Scene("Klimt Room", "klimt_room",
"""
The man stops screaming as you punched him in his face.
He looks startled, and looks at you.

"What happened?", he asked.
"Sir, you were screamig like a mad guy."
"Oh, I must have lost my mind after dropping my cellphone into the lake."
"Maybe you should go back home and take some rest."

The man is still upset from losing his cellphone but decides to go back.
After he goes back home you cross the bridge.
A couple is kissing. They are kissing so hard that they don't even realize you are there.
Will you take photo, run away, or cheer?

""")

gogh_room = Scene("Gogh Room", "gogh_room",
"""

You give the photo to the couple. They love it and thank you.
The couple gives you a vase.
Vase full of beautiful sunflowers.
They are yellow, big, and beautiful.
There are total seven sunflowers.
They tell you that only one has roots under and other six with roots cut off.
You need to pick the only one.
Which one do you pick?

""")

you_made_it = Scene("You Made It!", "you_made_it",
"""
You picked the right sunflower!
You sniff it gently and holds it high.
Sunflower starts to move. It slowly turns its head to a certain way.
You see a dim light coming from the way sunflower is facing.
You start to walk towards where the light is coming.
You walk and walk and walk. You walk into the full light.

You wake up.
Angry Mrs. Lee is looking down at you. Your classmates are giggling behind her looking at you.
You were sleeping in front of the ticket office.

"Do you find the museum boring?" Mrs. Lee asks, her face frowning as if to shout him at any time.
"No Mrs. Lee, I find them fascinating! I was in the paintings in my dream!"
Classmates burst into laughter. Mrs. Lee's face is getting redder and redder.
"You should be punished for sleeping during school trip. You should join the art history class." Mrs. Lee said.
"Cool! I'd really love too."
Mrs. Lee looks puzzled because you didn't sound sarcastic.

""")

you_failed = Scene("...", "you_failed",
"""
You gets eaten by the paint because you have no respect for them.
You fall into limbo and will never wake up again.

""")

generic_death = Scene("Dead...", "death", "You died in your dream.")

# Define the action commands available in each scene
gogh_room.add_paths({
    'third': you_made_it,
    '*': you_failed
})

klimt_room.add_paths({
    'cheer': generic_death,
    'run away': generic_death,
    'take photo': gogh_room
})

munch_room.add_paths({
    'punch him in the face': klimt_room,
    'ask why he is screaming': generic_death,
    'start screaming back': generic_death
})

picasso_room.add_paths({
    'cry':generic_death,
    'give her a hankercheif': munch_room,
    'ignore': generic_death
})

# Make some useful variables to be used in the web application
SCENES = {
    picasso_room.urlname : picasso_room,
    munch_room.urlname : munch_room,
    klimt_room.urlname : klimt_room,
    gogh_room.urlname : gogh_room,
    you_made_it.urlname : you_made_it,
    you_failed.urlname : you_failed,
    generic_death.urlname : generic_death
}
START = picasso_room
