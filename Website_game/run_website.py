import webbrowser
import os

# Path to the HTML file
file_path = os.path.abspath("./Website_game/start.html")

# Open the HTML file in the default web browser
webbrowser.open(f"file://{file_path}")