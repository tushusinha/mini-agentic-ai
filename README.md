# **🤖 Mini Agentic AI Assistant**
*(Now live on GitHub!)*

This is a **mini agentic AI project** built with:
- **LangChain** + **OpenAI** (for LLM reasoning)
- **Tools**: Calculator, File Reader, Web Search (DuckDuckGo), Weather (OpenWeatherMap API)
- **Streamlit** frontend
- **CI/CD with GitHub Actions**

The agent demonstrates how to orchestrate multiple tools under an LLM to answer real-world queries.
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
    # Optional: uncomment if you want weather functionality
    # WEATHER_API_KEY=your_openweathermap_key_here

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

### 🧪 Testing

#### Hand-Written Tests

All hand-written unit and integration tests live in the tests/ folder.
Run them with:

    pytest tests/

#### Auto-Generated Tests (Pynguin)

We use Pynguin to automatically generate tests for safe functions (simple_calculator, read_file) in safe_utils.py.

	• These generated tests are created during CI/CD runs only.
	• They are written into generated-tests/ but this folder is excluded from Git (see .gitignore).
	• This ensures that only hand-written tests live in the repo, while Pynguin contributes extra coverage in the pipeline.

To manually generate them locally:

    export PYNGUIN_DANGER_AWARE=1
    pynguin --project-path . --output-path generated-tests --module-name safe_utils
    pytest generated-tests/

### ✅ CI/CD Pipeline

	• Linting with flake8
	• Run hand-written tests with pytest
	• Run Pynguin to auto-generate safe tests
	• Execute Pynguin tests to improve coverage

This pipeline ensures that every push is validated by both manual + generated tests.