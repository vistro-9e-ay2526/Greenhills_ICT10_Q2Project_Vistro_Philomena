# Candidate Verification
from pyscript import display, document


def verify_candidate(e):
    document.getElementById('output').innerHTML = ' '
    first_name = document.getElementById('firstName').value
    last_name = document.getElementById('lastName').value
    candidates = ['SAMTEMPLE', 'LANALAZAR', 'CAINESOREN', 'ASTRIDELLISON', 'QUINNGAITHER', 'EDILIOESCOBAR']
    full_name = first_name + last_name
    candidate_verification = ((full_name).upper()) in candidates

    display_message = (f'Sorry {(first_name).capitalize()} {(last_name).capitalize()}, your name is not on the list.', f'Congratulations {(first_name).capitalize()} {(last_name).capitalize()}! You are now part of the FAYZ club.<br><a href="index.html">Log In</a>')

    document.getElementById("output").innerHTML = display_message[candidate_verification]