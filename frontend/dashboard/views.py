from django.shortcuts import render
from .forms import MatchForm, ScoreInputForm
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

def match_form(request):
    prediction = None
    reasoning = None

    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Send to FastAPI /predict
            try:
                predict_res = requests.post(f"{FASTAPI_URL}/predict", json=data)
                reasoning_res = requests.post(f"{FASTAPI_URL}/reason", json=data)

                if predict_res.status_code == 200:
                    prediction = predict_res.json().get("predicted_winner")
                if reasoning_res.status_code == 200:
                    reasoning = reasoning_res.json().get("llm_reasoning")

            except Exception as e:
                prediction = "Error contacting prediction service."
                reasoning = str(e)

    else:
        form = MatchForm()

    return render(request, 'dashboard/dashboard.html', {
        'form': form,
        'prediction': prediction,
        'reasoning': reasoning,
    })
def score_form(request):
    prediction = None
    if request.method == 'POST':
        form = ScoreInputForm(request.POST)
        if form.is_valid():
            payload = form.cleaned_data
            try:
                response = requests.post("http://127.0.0.1:8000/predict-score", json=payload)
                prediction = response.json().get("predicted_score")
            except Exception as e:
                prediction = f"Error: {e}"
    else:
        form = ScoreInputForm()

    return render(request, "dashboard/score.html", {
        "form": form,
        "prediction": prediction
    })

