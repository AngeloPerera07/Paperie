from pypdf import PdfReader
import tkinter as tk
from tkinter import filedialog

def select_pdf():
   root = tk.Tk()
   root.withdraw()

   file_path = filedialog.askopenfilename(
      title = "Select a PDF or TXT file",
      filetypes=[("PDF Files", "*.pdf"), ("txt Files", "*.txt"), ("All Files", "*")]
   )

   return file_path

selected_pdf = select_pdf()
total_pages = 0

# Check if the user selected a file or cancelled the prompt
if selected_pdf:
   print(f"Successfully selected: {selected_pdf}")

    # 3. Feed the file path directly into pypdf
   reader = PdfReader(selected_pdf)

   total_pages = len(reader.pages)
   print(f"Total Pages: {total_pages}")



   # Text extracting
   text = ""

   for i in range(total_pages):
      page = reader.pages[i]
      text += page.extract_text()

   print(text)

else:
    print("No file was selected.")

