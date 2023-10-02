import streamlit as st
from transformers import MarianMTModel, MarianTokenizer





def translate(text, target_language):
    model_name = f'Helsinki-NLP/opus-mt-en-{target_language}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs, num_beams=4, max_length=50, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text

def main():
    st.title("Text Translator")
    
    input_text = st.text_input("Enter the English text to be translated")
    target_language = st.selectbox("Select your destination language", ['es', 'fr', 'de', 'it'])
    st.markdown("---")
    if st.button("Translate", key="translate-button"):
     translated_text = translate(input_text, target_language)
     
     st.success(f"Translated text: {translated_text}")
     
    

st.markdown("---")




if __name__ == "__main__":
    main()