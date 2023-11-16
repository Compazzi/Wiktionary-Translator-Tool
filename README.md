# Wiktionary Translator Tool
 This tool uses Wiktionary to translate English words into a variety of languages.
 
## Functionality
 The program uses the `requests` package in Python to access the Wiktionary website and the `Beautiful Soup` package to parse the HTML content. The standardized structure of Wiktionary in English facilitates this process, making the extraction of translations an easily automated task that requires minimal data manipulation.

## Installation

 To run the program, it is necessary to have the `requests` and `Beautiful Soup` packages installed.  
 After cloning this repository, navigate to the program's directory and install the packages listed in the `requirements.txt` file. Like this:

    pip install -r requirements.txt

 ## Basic Usage
 The input should be in lowercase, except for proper nouns, name of countries, etc. For example:  
  
    python main.py beer

 ## Output
 The result of the request includes translations of the input into your preferred languages, accounting for potential multiple meanings that yield different translations in various contexts. It showcases a title along with a concise contextual meaning of the word, followed by a list of translations into predefined languages.

 Example for the input "beer":
 
    [1] ALCOHOLIC DRINK MADE OF MALT

    Arabic: بِيرَة‎ f (bīra), جِعَة‎ f (jiʕa), مِزْر‎ m (mizr)
    Egyptian Arabic: بيرة‎ f (bīra)
    Juba Arabic: [Term?] (merisa), [Term?] (bira)
    Mandarin: 啤酒 (zh) (píjiǔ), 麥酒／麦酒 (zh) (màijiǔ) (rare or regional)
    Greek: Μπίρα (el) f (bíra), ζύθος (el) m (zýthos)
    Hebrew: בִּירָה‎ (he) f (bíra)
    Italian: Birra (it) f
    Japanese: ビール (ja) (bīru), 麦酒 (ja) (ば​くしゅ, bakushu) (dated or rare)
    Korean: 맥주(麥酒) (ko) (maekju), 비어 (ko) (bieo) (rare or in compounds)
    Portuguese: Cerveja (pt) f
    Spanish: Cerveza (es) f, birra (es) f
    
    [2] DRINK MADE FROM ROOTS

    Portuguese: Cerveja (pt) f
    Spanish: Cerveza (es) f
 

 ## Command Line Arguments
 By default, the program prints the translation for some languages that are defined in the code itself. However, you can change this list of languages in two ways:
  1. **Modifying the code:** You can edit the code directly to add or remove languages from the default list. Open the `languages.py` file and locate the section where the languages are defined.
  2. **Via the program:** Use the `-l` or `--language` flag.

 ### Print All Available Translations
 * Use the `-a` or `--all` flag to print all translations without language filtering.

 ### Print Translations for Only One Language
 * Use the `-o` or `--one` flag to print translations only for the specified language.
