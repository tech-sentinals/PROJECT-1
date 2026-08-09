from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import SymptomSession

COMMON_GUIDANCE = {
    "fever": "Monitor temperature, rest, and maintain hydration.",
    "cough": "Consider rest and fluids; seek care if breathing becomes difficult.",
    "headache": "Rest, hydrate, and seek professional advice if severe or persistent.",
    "chest pain": "Chest pain can be serious. Seek urgent medical evaluation.",
}

@require_http_methods(["POST"])
def check_symptoms(request):
    import json
    try:
        data = json.loads(request.body or "{}")
        name = str(data.get("name", "Guest")).strip() or "Guest"
        age = int(data.get("age", 0))
        sex = str(data.get("sex", "unspecified"))
        symptoms = str(data.get("symptoms", "")).strip().lower()
    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({"error": "Invalid request data."}, status=400)

    if not symptoms:
        return JsonResponse({"error": "Please enter at least one symptom."}, status=400)

    matched = [msg for key, msg in COMMON_GUIDANCE.items() if key in symptoms]
    response = " ".join(matched) or "Your symptoms need professional assessment. This tool provides general information only."
    record = SymptomSession.objects.create(patient_name=name, age=age, sex=sex, symptoms=symptoms, response=response)
    return JsonResponse({"id": record.id, "response": response, "created_at": record.created_at})

@require_http_methods(["GET"])
def history(request):
    records = SymptomSession.objects.order_by("-created_at")[:20]
    return JsonResponse({"history": [
        {"id": r.id, "name": r.patient_name, "symptoms": r.symptoms, "response": r.response, "created_at": r.created_at}
        for r in records
    ]})
