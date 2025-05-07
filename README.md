![Screenshot 2025-05-08 000030](https://github.com/user-attachments/assets/9b163275-06b4-48b6-88f6-660bc06d8582)# 🏏 IPL Match Prediction System

This project is a comprehensive AI-based prediction platform for Indian Premier League (IPL) cricket matches. It leverages both machine learning models and local Large Language Models (LLMs) to offer two key features:

- 🎯 **Match Winner Prediction** – using historical match data and 1st innings score  
- 📊 **First Innings Score Prediction** – based on toss, teams, and venue data  
- 🤖 **LLM-based Reasoning** – generates a short, logic-based explanation for the outcome using **LLaMA3** running via **Ollama**

It is built using **FastAPI** for the backend and **Django** with **Bootstrap 5** for the frontend.

ScreenShot of Project

![Screenshot 2025-05-07 235957](https://github.com/user-attachments/assets/8eabb953-2a4b-4b6f-8b51-bde98bd3bc74)

![Screenshot 2025-05-08 000030](https://github.com/user-attachments/assets/5259d7bb-b69c-47a8-a7b6-83a3e35f4a73)

---

## 📁 Project Structure

```plaintext
ipl-cricket-predictor/
│
├── data/
│   ├── raw/                # Raw CSV dataset (must be created)
│   └── processed/          # Optional cleaned or feature-engineered files
│
├── models/                 # Trained models and saved encoders
│
├── src/
│   ├── api/                # FastAPI application
│   └── frontend/           # Django frontend application
│       └── dashboard/
│
├── notebooks/              # Jupyter notebooks for EDA and training
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Features

* 🏏 Match winner prediction based on team names and 1st innings performance  
* 🔢 Predicts likely first innings scores using game context  
* 🤖 Generates reasoning with local LLM (LLaMA3) through natural language  
* 📋 Fully documented APIs via Swagger UI  
* 🎨 Beautiful web interface with Bootstrap 5 integration

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/PriyanshuKanyal37/Ipl-prediction-model.git
cd ipl-cricket-predictor
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗃️ Dataset Setup

You **must create** the following folder structure and add your dataset file accordingly:

```bash
mkdir -p data/raw data/processed models
```

Place your CSV dataset here:

```bash
data/raw/match_data.csv
```

This file should contain columns such as `team1`, `team2`, `team1_score`, `team2_score`, `winner`, and `venue_name`.

---

## 🧠 Model Training

You can train your models using the Jupyter notebook provided in the `notebooks/` directory. This will:

* Preprocess the data  
* Train an XGBoost classifier and regressor  
* Save the models in the `models/` folder:

  * `match_winner_xgb_model.pkl`  
  * `score_predictor_model.pkl`  
  * Label encoders as `.pkl` files  

---

## 🧠 Local LLM Setup (LLaMA via Ollama)

Install [Ollama](https://ollama.com/) for running the LLaMA3 model locally:

```bash
# Install ollama if not already
brew install ollama  # for macOS
# OR follow installation guide from https://ollama.com

# Run the model
ollama run llama3
```

## 💻 Running the Project

### Start the FastAPI Backend

```bash
cd src/api
uvicorn main:app --reload
```

* You can access API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Start the Django Frontend

```bash
cd ../frontend
python manage.py runserver
```

* Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the user interface

---

If error accour because of link overlap than you can use
http://127.0.0.1:8001

## 📦 API Endpoints

| Endpoint         | Method | Description                              |
| ---------------- | ------ | ---------------------------------------- |
| `/`              | GET    | Root health check                        |
| `/predict`       | POST   | Predicts match winner                    |
| `/predict-score` | POST   | Predicts first innings score             |
| `/reason`        | POST   | Provides LLM-generated logical reasoning |
| `/health`        | GET    | Backend status check                     |

---

## 🧪 Testing (Optional Enhancements)

* Add unit tests for form validation and API logic  
* Measure inference latency for `/predict` and `/predict-score`  
* Track LLaMA response times for `/reason`

---


## 📄 License

T
* Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the user interface

---

## 📦 API Endpoints

| Endpoint         | Method | Description                              |
| ---------------- | ------ | ---------------------------------------- |
| `/`              | GET    | Root health check                        |
| `/predict`       | POST   | Predicts match winner                    |
| `/predict-score` | POST   | Predicts first innings score             |
| `/reason`        | POST   | Provides LLM-generated logical reasoning |
| `/health`        | GET    | Backend status check                     |

---

## 🧪 Testing (Optional Enhancements)

* Add unit tests for form validation and API logic  
* Measure inference latency for `/predict` and `/predict-score`  
* Track LLaMA response times for `/reason`

---

## Priyanshu Kanyal
