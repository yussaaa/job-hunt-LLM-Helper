import pdftotext

def extract_text_from_PDF(pdf_path:str) -> str:
    """This is a helper function to raed the text out of a PDF file.

    Args:
        pdf_path (str): Local path to the PDF file
    Returns:
        str: text inside the PDF file
    """
    
    # Load your PDF
    with open(pdf_path, "rb") as f:

        pdf = pdftotext.PDF(f)

    # Read all the text into one string
    pdftotext_text = "\n\n".join(pdf)
    
    return pdftotext_text

if __name__ == "__main__":
    print(extract_text_from_PDF("data/Resume_Yusa Li_MLEngineer.pdf"))
