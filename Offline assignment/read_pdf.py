import fitz
import sys

pdf_path = sys.argv[1] if len(sys.argv) > 1 else '00724205101098_Offline1.pdf'
doc = fitz.open(pdf_path)
for i in range(len(doc)):
    print(f"=== PAGE {i+1} ===")
    text = doc[i].get_text()
    # Remove zero-width spaces and other problematic chars
    text = text.encode('ascii', errors='replace').decode('ascii')
    print(text)
    print()
