import gradio as gr
from transformers import pipeline
import re

text_cleaner = pipeline(
    "text2text-generation",
    model="Vamsi/T5_Paraphrase_Paws"
)

def normalize_text(text):
    # Add space after punctuation if missing
    text = re.sub(r'([.!?])([A-Za-z])', r'\1 \2', text)
    return text

def capitalize_sentences(text):
    text = text.strip()
    if not text:
        return text

    text = text[0].upper() + text[1:]
    text = re.sub(
        r'([.!?]\s+)([a-z])',
        lambda m: m.group(1) + m.group(2).upper(),
        text
    )
    return text

def clean_text(input_text):
    input_text = normalize_text(input_text)

    prompt = (
        "Rewrite the following text to be clear, grammatically correct, and professional. "
        "Use proper sentence structure and different wording.\n\n"
        f"Text: {input_text}\n\n"
        "Rewritten version:"
    )

    result = text_cleaner(
        prompt,
        max_length=256,
        do_sample=False
    )

    output = result[0]["generated_text"]

    # Fallback: if model returns almost same text
    if output.strip().lower() == input_text.strip().lower():
        output = input_text

    output = normalize_text(output)
    output = capitalize_sentences(output)

    return output

interface = gr.Interface(
    fn=clean_text,
    inputs=gr.Textbox(lines=6, placeholder="Paste your text here..."),
    outputs=gr.Textbox(lines=6),
    title="AI Text Cleaner & Enhancer",
    description="Improves grammar, clarity, sentence structure, and capitalization."
)

interface.launch()
