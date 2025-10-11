# Պոլիմորֆիզմ (Polymorphism)

class PdfDocument():
    def save(self):
        print("Saving PDF document...")

class WordDocument():
    def save(self):
        print("Saving Word document...")

class ExcelDocument():
    def save(self):
        print("Saving Excel document...")

documents = [PdfDocument(), WordDocument(), ExcelDocument()]

for doc in documents:
    doc.save()