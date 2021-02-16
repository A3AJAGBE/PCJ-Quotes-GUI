from tkinter import *
import requests


def get_quote():
    """This function gets the quote from the api"""
    response = requests.get("https://pc-quotes-api.herokuapp.com/quotes/v1.0/")
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
    canvas.itemconfig(quote_text, text=quote)


interface = Tk()
interface.title("A3AJAGBE QUOTE GUI")
interface.config(padx=50, pady=50)

pc_label = Label(text="Priyanka Chopra Says", font=("Tahoma", 20, "bold"), padx=10, pady=10)
pc_label.grid(row=0, column=0)

# Add quote background image
canvas = Canvas(width=300, height=414)
bg_img = PhotoImage(file="images/background.png")
canvas.create_image(150, 207, image=bg_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Tahoma", 30, "bold"),
                                fill="#0066ff")
canvas.grid(row=1, column=0)

# Add PCJ image to button
pc_img = PhotoImage(file="images/pc.png")
pc_button = Button(image=pc_img, highlightthickness=0, command=get_quote)
pc_button.grid(row=2, column=0)

get_quote()

# Keep the interface open until exited
interface.mainloop()
