from pypdf import PdfReader
import tkinter as tk
from tkinter import filedialog
import os
from google import genai


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
pdf_text = ""
if selected_pdf:
   print(f"Successfully selected: {selected_pdf}")

   # 3. Feed the file path directly into pypdf
   reader = PdfReader(selected_pdf)

   total_pages = len(reader.pages)
   print(f"Total Pages: {total_pages}")



   # Text extracting


   for i in range(total_pages):
      page = reader.pages[i]
      pdf_text += page.extract_text()

   print(pdf_text)

else:
    print("No file was selected.")

#OpenAI integration
# client = OpenAI()

# prompt_text = f"Summarize the following document concisely, highlighting key insights: {text}"
# response = client.responses.create(
#     model="gpt-5.6-luna",      # Or use "gpt-4o", "gpt-5.5", etc.
#     input=prompt_text
# )
# print(response.output_text)

#Gemini Integration

client = genai.Client()
def summarize_text(document_text: str) -> str:
   prompt_text = f"Summarize the following document concisely, highlighting key insights: \n\n{document_text}"

   response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt_text
    )
   text = response.text
   if text is None:
      raise RuntimeError("No text returned from model")
   return text

print(f"PDF SUMMARIZED \n\n\n\n{summarize_text(pdf_text)}")
