from tkinter import *

interface = Tk()
interface.title("A3AJAGBE QUOTE GUI")
interface.config(padx=50, pady=50)

# Add quote background image
canvas = Canvas(width=300, height=414)
bg_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=bg_img)
quote_text = canvas.create_text(150, 207, text="Priyanka Quote Goes HERE", width=250, font=("Tahoma", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

# Add PCJ image to button
pc_img = PhotoImage(file="pc.png")
pc_button = Button(image=pc_img, highlightthickness=0)
pc_button.grid(row=1, column=0)

# Keep the interface open until exited
interface.mainloop()
