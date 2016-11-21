import remind
from random import randint

class Scene(object):

    def enter(self):
        print "Hang on! Don't give up too early you idiot!"
        exit(1)

class Engine(object):

    def __init__(self, scene_dream):
        self.scene_dream = scene_dream

    def play(self):
        current_scene = self.scene_dream.opening_scene()
        last_scene = self.scene_dream.next_scene('hospital')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_dream.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You died."
        "This is what you have wanted at the first time."
        "\n Or is it?"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class TigerCage(Scene):

    def enter(self):
        print "You fall into the room with a cage in the middle."
        print "What is going on?"
        print "Maybe you are dreaming."
        print "Or maybe you are really in front of the tiger cage."
        print "You have entered the tiger cage."
        print "There is a huge orange hungry tiger sleeping in the corner."
        print "What do you do? scream / run away / fart"

        action = raw_input("> ")

        if action == "scream":
            print "You idiot! You have awaken the hungry tiger."
            print "The tiger eats you alive."
            return 'death'

        elif action == "run away":
            print "The tiger wakes up as he hears your footsteps."
            print "He jumps at you and tears your body apart."
            return 'death'

        elif action == "fart":
            print "The tiger wakes up."
            print "He is disgusted by smell of your fart"
            print "He walks out of the cage."
            print "You see a door on the floor where the tiger was sleeping on."
            return 'underground_aquarium'


        else:
            print "What do you mean?"
            print "You are too stupid. You were before and you are now."
            return 'death'

class UndergroundAquarium(Scene):

    def enter(self):
        print "You go inside the door in the tiger cage."
        print "After going down for a while you find a large aquarium."
        print "There are class of fish and sharks."
        print "\n"
        print "How many sharks do you see?"
        print "They are under 10"

        shark = raw_input("> ")

        if shark == "4":
            print "Glad that you graduated elementary school at least."
            print "Sharks are now satisfied. They might have gone outrageous if you were too dumb."
            print "Sharks like smart people."
            print "One of the sharks presses a red button in the middle of the aquarium with his nose."
            print "Suddenly the floor you are stepping on cracks apart and you fall down into the dark hole."
            return 'dark_hole'

        else :
            print "Don't you even know how to count?!"
            print "Sharks are getting angry."
            print "Sharks are disappointed by human being's stupidity."
            print "They start to devour the class of fish."
            print "The aquarium tank is filled with red blood."
            print "\n"
            print "They are looking at you now."
            print "\n"
            print "They swim together to the glass at once and breaks it."
            print "You are hit by massive amount of water and broken glasses."
            return 'death'


class DarkHole(Scene):

    def enter(self):
        print "You fall on the soft ground."
        print "You can see nothing because it's too dark."

        remind.background()

        print "You can feel two buttons on the ground with your hand."
        print "Which one do you push? First, or the Second?"

        action = raw_input("> ")

        if action == "First":
            print "As you press the first button,"
            print "the bomb explodes."
            return 'death'

        elif action == "Second":
            print "As you press the second button,"
            print "the room lights up."
            return 'giant_bell'
        else:
            print "You cannot even choose between two?!"
            return 'death'

class GiantBell(Scene):

    def enter(self):
        print "You confront a giant gold bell."

        remind.background()

        print "You want to find out."
        print "It's gonna be super loud if you ring that bell."
        print "Will you ring the bell?"

        bell = raw_input("> ")

        if bell == "Yes":
            print " You ring the bell."
            print "It is hella loud."
            print "Your ears cannot take it and they burst into parts."
            return 'death'

        elif bell == "No":
            print "You coward. You can do nothing."
            print "You see a bell, and you don't ring it?"
            print "You should be ashamed of yourself."
            print "You are given another chance."
            print "Life is tough and second chance is rare."
            print "You should be thankful."
            return 'giant_bell'
        else:
            print "You don't ring a bell but you decided to do something else."
            print "I like that creativity! World needs more creative people."
            print "So a creative person like you must go back to real world."
            print "You can go back to where you came from."
            print "Good luck!"

            return 'hospital'

class Hospital(Scene):

    def enter(self):
        print "You wake up and open your eyes."
        print "You are lying in the hospital."
        print "You see many people staring down at you."
        print "They are your family."
        print "and they are crying."
        print "\n"
        print "Now you remember."
        print "\n"
        print "You were so depressed that you don't want to live anymore."
        print "You attempt suicide by hanging yourself."
        print "As you are choking and losing breath, the world is getting dimmer."
        print "Everything is getting dimmer and dimmer..."
        print "...and it felt like you are falling into sleep."
        print "\n"
        print "The doctor said it is a true miracle that I came back alive."
        print "I think about my weird mysterious dream."
        print "I am proud of my choices and bravery. I am proud of myself."
        print "Life is tough, but it's worth to live."
        print "And I have my family who loves me more than anybody does."
        print "-The End-"
        return 'hospital'

class Dream(object):

    scenes = {
        'tiger_cage': TigerCage(),
        'underground_aquarium': UndergroundAquarium(),
        'dark_hole': DarkHole(),
        'giant_bell': GiantBell(),
        'death': Death(),
        'hospital': Hospital(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Dream.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_dream = Dream('tiger_cage')
a_game = Engine(a_dream)
a_game.play()
