SmartCourseBot : 
SmartCourseBot is an AI-powered chatbot built with Streamlit and OpenAI that helps students explore and understand course details interactively.

Features :
- ChatGPT-powered responses
- Dynamic course search from a JSON file
- Simple UI using Streamlit
- Secure OpenAI key via `.env`

Live Demo : 
[Click here to try SmartCourseBot](https://smartcoursebot-kgcojexq6gjqmxr75edgw8.streamlit.app/)

Tech Stack : 
- Python
- Streamlit
- OpenAI GPT (API)
- JSON (course data)
- dotenv

How to Run Locally : 
Open your terminal and follow these steps:
```bash
# 1. Clone the repository
git clone https://github.com/anaazmi/SmartCourseBot.git

# 2. Navigate to the project folder
cd SmartCourseBot

# 3. (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows

# 4. Install the required packages
pip install -r requirements.txt

# 5. Set your OpenAI API Key
# Create a `.env` file and add your key:
echo "OPENAI_API_KEY=your-key-here" > .env

# 6. Run the Streamlit app
streamlit run app.py
```

Project Structure : 
```bash
SmartCourseBot/
│
├── app.py             # Main Streamlit app
├── chatbot.py         # GPT-based chatbot logic
├── courses.json       # Course data
├── utils.py           # Utility functions
├── .env               # API key (not tracked by Git)
├── .gitignore         # Files to exclude from Git
├── requirements.txt   # Dependencies
└── README.md          # This file
```

License :
This project is licensed under the MIT License. See the LICENSE file for details.
