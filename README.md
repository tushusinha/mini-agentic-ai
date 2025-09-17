# **🤖 Mini Agentic AI Assistant**
*(Now live on GitHub!)*

A mini sample project to explore how Agentic AI works.
This assistant can:

	• 🔍 Search the web for current news.
	• ➗ Solve math expressions with a calculator.
	• 📂 Read and summarize local text files.

It’s stateless, lightweight, and cost-efficient — perfect for hands-on experimentation.

### **🗂️ Project Structure**

    mini_agentic_ai/
    │── app.py              # Streamlit web app
    │── agent.py            # Agent logic + tools
    │── requirements.txt    # Dependencies
    │── sample.txt          # Example file for testing
    │── .env                # API key (not in git!)
    │── README.md           # Project overview

### **⚙️ Setup Instructions**

#### **1. Clone this project**

    git clone https://github.com/your-username/mini_agentic_ai.git
    cd mini_agentic_ai

#### **2. Create a virtual environment (recommended)**

    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows

#### **3. Install dependencies**

    pip install -r requirements.txt

#### **4. Add your OpenAI API key**

    OPENAI_API_KEY=your_openai_api_key_here

### 🔒 Security Notes

#### • Never commit .env to GitHub

Your .env file contains sensitive API keys. Make sure .env is listed in .gitignore.

#### • Check if .env is already tracked

If you accidentally committed it before, remove it from Git history:

    git rm --cached .env
    git commit -m "Remove sensitive .env file from repo"

#### • Everyone creates their own .env

Each developer or user should create their own .env file locally with their personal API keys, e.g.:

    OPENAI_API_KEY=sk-xxxx

#### • Good practice

    • Don’t share your API key publicly.

    • Use OpenAI billing limits to prevent accidental overspending.

    • Rotate your key if you suspect it was exposed.

### **🚀 Run the App**

streamlit run app.py

Open http://localhost:8501 in your browser.

### **🧪 Example Queries**
	
##### •	Math:

"What is 25*42?" → Uses Calculator

##### •	News:

"Summarize today’s top 2 AI news stories." → Uses Web Search

##### •	File Reading:

"Read ./sample.txt and summarize it in 3 points." → Uses File Reader