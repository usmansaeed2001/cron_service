# Handle the tasks in the Kajabi table and process accordingly
from services.google_sheets import google_sheets

def process_kajabi():
    print("Hello World")
    google_sheets.append_new_row("1cF7Zdx1uwCe8yC_0i336b096l9iGXup96wUga1KOvhg", "Sheet1", ["Hello", "this is a  test"])