# 🚀 DroidAgent: The Autonomous AI Social Media Intern

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![DroidRun](https://img.shields.io/badge/Powered%20By-DroidRun-orange?style=for-the-badge)
![AI Model](https://img.shields.io/badge/Brain-Gemini%20%2F%20DeepSeek-purple?style=for-the-badge)


> **"Stop writing brittle scripts. Start hiring AI agents."**

## 📢 The Vision
Social media management is repetitive, time-consuming, and manual. Existing automation tools (like Appium or Selenium) are **brittle**, they break if a button moves by 10 pixels.

We built **DroidAgent**: a next-generation **AI Agent** that sees your screen, understands social media apps, and executes complex workflows just like a human social media manager.

**The best part?** It's not hard-coded. You can change its entire job description just by changing a **single text prompt.**

## ✨ Key Capabilities

### 1. 🧠 Universal Flexibility (The "Prompt-Driven" Engine)
Unlike traditional bots that only do one thing, DroidManager is a generalist. By simply changing the `goal` string in Python, the agent adapts instantly:

* **Scenario A (Content Creator):** *"Upload the last video from Gallery to Reels with a generated caption with respect to the content."*
* **Scenario B (Comment Farming Bot):** *"Opens Instagram, sees the next potential viral reel and comments on it which can acquire new profile views and maybe followers if some comment hits."*
* **Scenario C (Community Manager):** *"Check my DMs. If anyone asks for 'Price', reply with '$50' and archive the chat."*

### 2. 👁️ Computer Vision UI Navigation
We use **DroidRun's Vision capabilities** (powered by Gemini) to "see" the app.
* It doesn't need hidden XML IDs.
* It recognizes buttons by their icon (e.g., "The + button", "The blue Share button").
* It handles pop-ups, keyboard obstructions, and UI changes dynamically.

### 3. 📝 "App Cards" Knowledge Base
We created a custom **Intelligence Layer** (`instagram.md`) that teaches the agent the specific layout of Instagram. This means the AI doesn't have to guess; it knows exactly where the "Reels" tab and "Share" buttons are, reducing hallucinations to near zero.

### 4. 🎨 Generative Creativity
The agent doesn't just click buttons; it **creates content**.
* It analyzes your video context.
* It uses an LLM (Large Language Model) to generate viral, context-aware captions and hashtags on the fly.
* It types the caption naturally, just like a human user.

---

## 🛠️ The Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Orchestration** | **DroidRun SDK** | The core framework controlling the Android device via ADB. |
| **The Brain** | **Gemini 2.0 Flash**  | Provides reasoning, vision, and decision-making capabilities. |
| **The Hands** | **Python & ADB** | Executes physical taps, swipes, and text input. |
| **Knowledge** | **Markdown App Cards** | A cheat-sheet system (RAG-lite) for app-specific navigation rules. |
| **Platform** | **Android** | Works on any real Android phone or Emulator. |

---

## 📸 Showcase: The "Auto-Uploader" Mode

In this repository, we demonstrate the **Auto-Uploader** configuration. Here is the workflow the Agent executes autonomously:

1.  **Wake Up:** Connects to the device and loads the `instagram.md` App Card.
2.  **Navigation:** Launches Instagram and navigates to the "Create" (+) tab.
3.  **Selection:** Intelligently switches to "Reel" mode and selects the most recent video from the gallery.
4.  **Creation:**
    * Navigates through the editing screens.
    * **Generates a caption** (e.g., *"Check out this futuristic AI! #Tech"*) using the LLM.
    * Types the caption into the text field.
5.  **Execution:** Identifies the "Share" button (even if hidden by the keyboard) and posts the content.

---

##  How to Run It

### Prerequisites
1.  **Android Phone:** Developer Mode ON, USB Debugging ON.
2.  **DroidRun Portal:** Installed on the phone (for accessibility access).
3.  **Python 3.10+**

### Installation
```bash
# Clone the repository
git clone [https://github.com/satyam22i/Droidrun-Android-Automation.git]
cd Automation

# Install dependencies
pip install droidrun llama-index-llms-gemini llama-index-llms-openai-like python-dotenv

#Create a .env file with your AI provider key:
# For Gemini Users
GOOGLE_API_KEY=your_key_here

#Run the main agent script:
python upload_bot.py


```
### Grasp the new execution ! This agent will take control and performs the action that drives growth for you.

## Future Roadmap
AI Automation Workflows:- Curate a workflow on platforms like n8n/zapier which helps making it more easy to operate.

Multi-App Workflows: "Take a screenshot of a Tweet, crop it, and post it to Instagram Stories."

Schedule Listener: An agent that runs when you want, waits for your command on specific times.

Analytics Reporter: Opens "Insights," reads the required metrics via OCR, saves them to a Google Sheet and make further classification on command.

<br />
<br />

<br />

<br />

##  Meet the Team

<div align="center">

| **Satyam Srivastav** | **Anurag Kumar** | **Shivam Rawat** |
| :---: | :---: | :---: |



</div>

<br />

---

<div align="center">

Made with ❤️, ☕, and 🤖 by the **DroidAgent Team**

</div>
