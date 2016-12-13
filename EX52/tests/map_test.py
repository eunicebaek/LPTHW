from nose.tools import *
from map import Scene

def test_room():
    paint = Scene("PaintScene", "paintroom", """
    This room has a painting.
    """)
    assert_equal(paint.title, "PaintScene")
    assert_equal(paint.urlname, "paintroom")
    assert_equal(paint.paths, {})

def test_room_paths():
    center = Scene("Center", "center", "Test room in the center.")
    north = Scene("North", "north", "Test room in the north.")
    south = Scene("South", "south", "Test room in the south.")

    center.add_paths({'north':north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Scene("Start", "start", "You can go west to see the painting.")
    west = Scene("Sofa", "sofa", "There is a sofa here, you can seat.")
    down = Scene("Alarm", "alarm", "There is an alarm down there. You should be careful..")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_museum_game_map():
    assert_equal(START.go('cry'), generic_death)
    assert_equal(START.go('give her a hankercheif'), generic_death)
    room = START.go('ignore')
    assert_equal(room, munch_room)
