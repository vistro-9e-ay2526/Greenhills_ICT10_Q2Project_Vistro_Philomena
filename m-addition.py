# Memeber Addition System
from pyscript import display, document


members = {'Sam Temple', 'Lana Lazar', 'Caine Soren', 'Astrid Ellison', 'Quin Gaither', 'Edilio Escobar'}

member_list = "<br>".join(sorted(members))

document.getElementById("output").innerHTML = f'Member Names:<br>{member_list}<br><br>' f'Number of Members: {len(members)}'


def add_member(e):
    first_name = document.getElementById('firstname').value
    last_name = document.getElementById('lastname').value
    full_name = first_name + (" ") + last_name

    members.add(full_name)

    updated_list = "<br>".join(sorted(members))

    document.getElementById("output").innerHTML = (f'Member Names:<br><br>{updated_list.title()}<br><br>Number of Members: {len(members)}')
