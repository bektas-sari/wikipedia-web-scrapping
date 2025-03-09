# Wikipedia Article Explorer

A **Flask-based web application** that allows users to explore random Wikipedia articles with a click of a button. The application fetches a random article using **web scraping (Requests & BeautifulSoup)** and displays it in a modern, user-friendly interface.

## 🚀 Features
- **Fetch Random Wikipedia Articles** with a single click
- **Modern UI with CSS Animations & Hover Effects**
- **Responsive Design** (Works on Desktop & Mobile)
- **Asynchronous Fetching** (No page refresh required)
- **Flask Backend with JSON API Support**

## 📸 Screenshot
![App Screenshot](screenshot.png)

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/wikipedia-article-explorer.git
   cd wikipedia-article-explorer
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

5. **Open in Browser:**
   ```
   http://127.0.0.1:5000/
   ```

## 🛠 Technologies Used
- **Flask** (Python Web Framework)
- **BeautifulSoup & Requests** (Web Scraping)
- **HTML, CSS, JavaScript** (Frontend)
- **JSON API** (Flask Routes)

## 📂 Project Structure
```
📦 wikipedia-article-explorer
├── 📂 static
│   ├── style.css (Styling for UI)
├── 📂 templates
│   ├── index.html (Frontend UI)
├── app.py (Flask Backend)
├── requirements.txt (Dependencies)
└── README.md (Project Documentation)
```

## 📝 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! If you find any issues, feel free to open an issue or contribute with improvements.

## 🌟 Show Your Support
If you like this project, give it a ⭐ on GitHub!

---

📩 **Contact:** [Your Name] - your.email@example.com  
🔗 **GitHub:** [yourusername](https://github.com/yourusername)

description:
Wikipedia Article Explorer is a Flask-based web app that fetches random Wikipedia articles using web scraping. Users can explore articles with a single click in a modern, responsive UI. Built with Flask, BeautifulSoup, and JavaScript, it supports asynchronous fetching without page refresh. Fast, user-friendly, and mobile-compatible!