import os
import re
from pypdf import PdfReader

# --- ԿԱՐԳԱՎՈՐՈՒՄՆԵՐ ---
BOOKS_FOLDER = "other/books"  # Թղթապանակի անունը, որտեղ դուք կտեղադրեք ձեր գրքերը
OUTPUT_FILE = "output.txt"  # Ելքային ֆայլի անունը՝ յուրահատուկ բառերի համար
PROCESSED_FILES_TRACKER = (
    "processed_files.txt"  # Ֆայլ, որտեղ կպահվեն արդեն մշակված ֆայլերի անունները
)


def get_processed_files():
    """Կարդում է արդեն մշակված ֆայլերի ցանկը։"""
    if not os.path.exists(PROCESSED_FILES_TRACKER):
        return set()
    with open(PROCESSED_FILES_TRACKER, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f)


def mark_file_as_processed(filename):
    """Նշում է ֆայլը որպես մշակված՝ ավելացնելով այն մեր ցուցակին։"""
    with open(PROCESSED_FILES_TRACKER, "a", encoding="utf-8") as f:
        f.write(filename + "\n")


def get_existing_words():
    """
    Կարդում է բոլոր բառերը output.txt ֆայլից և վերադարձնում է դրանք որպես set
    (հավաքածու), ինչը երաշխավորում է, որ կրկնություններ չեն լինի։
    """
    if not os.path.exists(OUTPUT_FILE):
        return set()
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        words = set(line.strip().lower() for line in f)
    return words


def extract_text_from_pdf(file_path):
    """Կորզում է տեքստը PDF ֆայլից։"""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        print(f"ERROR: Չհաջողվեց կարդալ PDF ֆայլը '{file_path}': {e}")
        return None


def extract_text_from_txt(file_path):
    """Կորզում է տեքստը TXT ֆայլից։"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"ERROR: Չհաջողվեց կարդալ TXT ֆայլը '{file_path}': {e}")
        return None


def main():
    """Հիմնական ֆունկցիան, որը կատարում է ամբողջ գործընթացը։"""

    # Ստուգում ենք՝ արդյոք "books" թղթապանակը գոյություն ունի
    if not os.path.exists(BOOKS_FOLDER):
        os.makedirs(BOOKS_FOLDER)
        print(
            f"'{BOOKS_FOLDER}' թղթապանակը ստեղծված է։ Խնդրում ենք տեղադրել ձեր ֆայլերն այնտեղ և կրկին գործարկել սկրիպտը։"
        )
        return

    # Ստանում ենք արդեն գոյություն ունեցող բառերի և մշակված ֆայլերի ցանկը
    existing_words = get_existing_words()
    processed_files = get_processed_files()

    new_words_count = 0

    print("Սկսվում է նոր ֆայլերի որոնումը...")

    # Ցիկլով անցնում ենք "books" թղթապանակի բոլոր ֆայլերի վրայով
    for filename in os.listdir(BOOKS_FOLDER):
        if filename in processed_files:
            continue  # Եթե ֆայլն արդեն մշակվել է, անցնում ենք առաջ

        file_path = os.path.join(BOOKS_FOLDER, filename)
        text = None

        # Կորզում ենք տեքստը՝ կախված ֆայլի տիպից
        if filename.lower().endswith(".pdf"):
            print(f"Մշակվում է PDF ֆայլը՝ {filename}")
            text = extract_text_from_pdf(file_path)
        elif filename.lower().endswith(".txt"):
            print(f"Մշակվում է TXT ֆայլը՝ {filename}")
            text = extract_text_from_txt(file_path)
        # Այստեղ կարող եք ավելացնել այլ ֆորմատների մշակում (օրինակ՝ .docx, .epub)

        if text:
            # Տեքստը դարձնում ենք փոքրատառ և բաժանում բառերի
            # re.findall-ը գտնում է միայն տառերից կազմված բառերը
            words = re.findall(r"\b[a-z]+\b", text.lower())

            # Բացում ենք ելքային ֆայլը 'append' ռեժիմով՝ նոր բառեր ավելացնելու համար
            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                for word in words:
                    # Ստուգում ենք՝ արդյոք բառը նոր է
                    if word not in existing_words:
                        existing_words.add(word)  # Ավելացնում ենք մեր ընթացիկ ցուցակին
                        f.write(word + "\n")  # Ավելացնում ենք ֆայլի մեջ
                        new_words_count += 1

            # Ֆայլի մշակումից հետո այն նշում ենք որպես մշակված
            mark_file_as_processed(filename)
            print(f"'{filename}' ֆայլի մշակումն ավարտվեց։")

    if new_words_count > 0:
        print(
            f"\nԳործընթացն ավարտված է։ Ավելացվել է {new_words_count} նոր յուրահատուկ բառ։"
        )
    else:
        print("\nՆոր ֆայլեր կամ նոր բառեր չեն գտնվել։")


if __name__ == "__main__":
    main()
