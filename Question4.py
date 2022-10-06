"""
Q4. Provide a program to read the file from URL and display the content in terminal.
 Provide a program to read the file from URL and display the content
in terminal.
• The file URL has to be input by the user.
• The program has to work from the terminal. The input and output have been taken/displayed
on the terminal
"""

import requests # importing the url library
url = input("Enter the URL with https:// \n")
data = requests.get(url)
print(data.text)