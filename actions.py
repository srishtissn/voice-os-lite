import os
import webbrowser
import pyperclip

def open_chrome():
    webbrowser.open("https://google.com")

def search_files(keyword):
    results = []
    for root, dirs, files in os.walk("C:\\"):
        for file in files:
            if keyword.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results[:5]

def read_clipboard():
    return pyperclip.paste()
