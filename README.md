# AI Text Cleaner & Enhancer

AI Text Cleaner & Enhancer is an AI-powered web application that improves grammar, clarity, sentence structure, and readability of user-provided text. It is built using a pretrained Natural Language Processing (NLP) model and deployed as an interactive web app using Gradio on Hugging Face Spaces.

The application is designed to help users quickly clean informal, grammatically incorrect, or poorly structured text and convert it into clearer and more readable language.

---

## Project Overview

This project demonstrates the practical deployment of an AI-based NLP model as a real-world web application. Instead of training a model from scratch, a pretrained transformer-based text-to-text model is used to rewrite and enhance text.

The system combines:
- AI-based text rewriting
- Deterministic post-processing for formatting
- A simple and accessible web interface

This makes the project suitable for beginners while still reflecting real-world AI deployment practices.

---

## Features

- Improves grammar and sentence clarity
- Enhances readability of informal or broken text
- Rewrites sentences using better structure
- Automatically fixes missing spaces after punctuation
- Ensures proper capitalization at sentence boundaries
- Clean and minimal user interface
- Runs entirely on CPU (no GPU required)

---

## How the Application Works

1. The user enters raw or grammatically incorrect text.
2. The input text is passed to a pretrained NLP model.
3. The model generates an improved version of the text.
4. Post-processing logic ensures proper spacing and capitalization.
5. The final enhanced text is displayed to the user in the browser.

---

## Model Used

The application uses a pretrained text-to-text transformer model from Hugging Face.  
This model is capable of understanding input text and generating an improved version with corrected grammar and clearer sentence structure.

Pretrained models are chosen because:
- They reduce training complexity
- They work well for general language tasks
- They are suitable for quick deployment in production-like environments

---

## Technology Stack

- Python  
- Hugging Face Transformers  
- Gradio  
- Hugging Face Spaces  

---

## Project Structure

```
ai-text-cleaner-enhancer/
├── app.py
├── requirements.txt
└── README.md
```

---

## Run Locally

  ```bash
  python -m venv venv
  source venv/bin/activate || venv\Scripts\activate
  pip install -r requirements.txt
  python app.py
  ```

The application will be available at http://127.0.0.1:7860

---

## Deployment

The application is deployed on Hugging Face Spaces using the Gradio SDK.

During deployment:
- Hugging Face automatically installs dependencies from requirements.txt
- The app is launched using app.py
- The project is hosted publicly with a shareable link

No additional server configuration is required.

---

## Sample Run

![Sample Run Image](image-path-or-url)

---

## Use Cases

- Cleaning informal or poorly written text
- Improving clarity in project descriptions and reports
- Helping non-native English speakers improve writing
- Demonstrating AI-powered NLP deployment
- Learning how to deploy transformer models as web apps

---

## Limitations

- The model may not always fully rewrite very short inputs
- Outputs depend on the behavior of the pretrained model
- The application focuses on grammar and clarity, not advanced style rewriting

---

## Future Improvements

- Add multiple rewriting modes (formal, simple, professional)
- Support longer documents
- Add confidence scoring for corrections
- Improve UI with examples and usage tips


---

## License

This project is created for educational and demonstration purposes.

---

By Jairaj R.
