from pypdf import PdfReader

reader = PdfReader('esempio.pdf')
print(len(reader.pages))
for i in reader.pages:
   print(i.extract_text())
