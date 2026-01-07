# Working with Dictionaries
from pyscript import display, when
from js import document

clubs = {
    'Art_club': {
        'Name': 'Art Club',
        'President': 'Ms. Macabago',
        'Location': 'Room 607',
        'Members': 45
    },
    'Chess_club': {
        'Name': 'Chess Club',
        'President': 'Mr. Mergal',
        'Location': 'Room 407',
        'Members': 20
    },
    'Ict_club': {
        'Name': 'ICT Club',
        'President': 'Ms. Ko',
        'Location': 'Room 508',
        'Members': 25
    }
}

@when("click", "#showBtn")
def generate():
    document.getElementById("output").innerHTML = ""
    selected = document.getElementById("clubDropdown").value
    club = clubs[selected]

    display(club, target="output")
    display(club["Name"], target="output")
    display(club["Location"], target="output")
    display(club["President"], target="output")
    display(club["Members"], target="output")




