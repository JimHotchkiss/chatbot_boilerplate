# 🤖 Streamlit AI ChatBot Boilerplate

A quick‐start template for building a chat interface with [Streamlit](https://streamlit.io) and the OpenAI API.

---

## 🚀 Features

- **Instant Chat UI** — powered by Streamlit’s `st.chat_*` components  
- **OpenAI Integration** — drop in your `OPENAI_API_KEY` to talk to GPT-4/GPT-4o/etc.  
- **Session State** — keeps message history across reruns  
- **Configurable** — extend prompts, tools, or function-calling as needed  

---

## 🛠️ Prerequisites

- **Python** 3.8+  
- **OpenAI API Key** ([create one here](https://platform.openai.com/account/api-keys))  
- **Git** & **pip**  

---

## 🏁 Quick Start

1. **Clone repository**  
   ```bash
   git clone https://github.com/JimHotchkiss/chatbot_boilerplate.git
   cd your-repo
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**  
   Create a file named `.env` in the project root containing:
   ```dotenv
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   *(Add any other environment variables your app needs.)*

5. **Launch the app**  
   ```bash
   streamlit run main.py
   ```

6. **Chat away!**  
   Open your browser at `http://localhost:8501` to start the conversation.

---

## 📂 Project Layout

```
.
├── .venv/               # Virtual environment (gitignored)
├── assets/              # Screenshots, demo images
│   └── chatbot-demo.png
├── main.py              # Streamlit entrypoint
├── requirements.txt     # Pinned Python dependencies
├── README.md            # This guide
└── .env                 # Your API keys & settings (gitignored)
```

---

## 📝 Key Snippets

```python
# main.py (excerpt)

from dotenv import load_dotenv
import os, streamlit as st
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🤖 AI ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
if prompt := st.chat_input("Type your message..."):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *st.session_state.messages
        ],
    )
    answer = response.choices[0].message.content

    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
```

---

## 🛡️ Best Practices

- **Keep `.env` out of git** — your API keys should stay secret.  
- **Pin versions** in `requirements.txt` (e.g. `streamlit==1.24.1`) for reproducibility.  
- **Use `.gitignore`** to exclude `.venv/`, `.env`, and any local data files.

---

## 🔧 Customization

- Swap out or extend the LLM model and temperature via additional ENV vars (e.g. `MODEL_NAME`).  
- Add function-calling or custom tool integrations to route user intents.  
- Break UI into multipage views with Streamlit’s [multipage apps](https://docs.streamlit.io/library/app-structure/multipage-apps).

---

## 📄 License

MIT © [Your Name or Org]

---

> **Next steps:**  
> 1. Enhance error handling & retries  
> 2. Integrate richer prompts or retrieval tools  
> 3. Deploy to Streamlit Cloud, Heroku, or your own server  

---

**Questions or feedback?**  
Feel free to open an issue or reach out!  
