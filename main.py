from tkinter import *
from tkinter import messagebox
from PIL import Image
from rembg import remove
FONT_STYLE = ("Arial", 10, "bold")

def remove_back():
    input_path = url_entry.get()
    output_path = "Updated_picture.png"
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)
    messagebox.showinfo(title="Task completed", message="Removed background successfully")

window =Tk()
window.title("Remove Background")
window.config(padx=20, pady=20)
url_label = Label(text="Enter the path and name of the image: ", font=FONT_STYLE)
url_label.grid(row=0, column=0)

url_entry = Entry(width=30)
url_entry.grid(row=0, column=1)

remove_button = Button(text="Remove Background", command=remove_back)
remove_button.grid(row=1, column=0, columnspan=2, pady=20)



window.mainloop()