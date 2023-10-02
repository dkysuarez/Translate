# Introduction
In the translator project, several tools and technologies were used, including Python, various natural language processing (NLP) libraries such as Transformers and Tokenizers, and the Helsinki NLP model from Hugging Face. Additionally, Streamlit was used to create an interactive and user-friendly interface for end users. Together, these tools allowed for the creation of an efficient and accurate translation application that can handle multiple languages and types of text.

### Text Translator
This is a simple program that uses Hugging Face's transformers library to translate text from English to multiple languages. It uses the pre-trained MarianMTModel and the MarianTokenizer tokenizer to perform the translation.


### Requirements

    Python 3.7 o superior
    Bibliotecas: streamlit, transformers

### Installation

    Clone the repository or download the program files.
    Create a virtual environment (optional, but recommended):

(bash)

    python3 -m venv myenv
    source myenv/bin/activate

Instala las bibliotecas requeridas:

(bash)

    pip install -r requirements.txt

Use

   Ejecute el programa:

bash

streamlit run main.py
 
1-A window will open in your browser with the application interface.
2-Enter the English text you want to translate in the text entry field.
3-Select the target language from the drop-down menu.
4-Click the "Translate" button to perform the translation.
5-The translated text will be displayed on the screen.

