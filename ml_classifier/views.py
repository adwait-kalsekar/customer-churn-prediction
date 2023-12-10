from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import pandas as pd

from .data_preprocessing import preprocessing

# Create your views here.

def index(request):
    return render(request, "ml_classifier/home.html")

@csrf_exempt
def predict(request):
    # Load model data
    model_1, model_2, score_1, score_2, col_names = preprocessing.load_model_data()
    model_1_name = "Logistic Regression"
    model_2_name = "Random Forest Classification"

    hosted_url = "https://5325-128-6-37-144.ngrok-free.app/predict"
    context = { "hosted_url": hosted_url, "model_1": model_1_name, "model_2": model_2_name, "score_1": score_1, "score_2": score_2 }
    if request.method == 'POST':
        try:
            #pred_obj = Prediction()

            # Get JSON request
            data = request.POST.dict()

            #pred_obj.name = data['name']

            del data['csrfmiddlewaretoken']
            del data['name']

            # Convert JSON to Pandas DF
            df = pd.DataFrame(data, index=[0])
            print(df.info())
            #df.reindex(columns=col_names)

            # Clean and encode data according to the model
            encoded_df = preprocessing.encode_data(df, col_names)
            

            # Predict Results
            prediction_1 = list(model_1.predict(encoded_df))
            probability_1 = list(model_1.predict_proba(encoded_df))

            prediction_2 = list(model_2.predict(encoded_df))
            probability_2 = list(model_2.predict_proba(encoded_df))
            
            final_prediction_1 = '{0:.2f}'.format(probability_1[0][prediction_1[0]] * 100)
            final_prediction_2 = '{0:.2f}'.format(probability_2[0][prediction_2[0]] * 100)

            # pred_obj.age = data["age"]
            # pred_obj.gender = "Female" if data["sex"] == "0" else "Male"
            # pred_obj.prediction = "No" if prediction[0] == 0 else "Yes"
            # pred_obj.probability = final_prediction

            # pred_obj.save()
            

            context["prediction_1"] = f"has a {final_prediction_1}% probability of not Churning (Exiting)" if prediction_1[0] == 0 else f"has a {final_prediction_1}% probability of Churning (Exiting)"
            context["prediction_2"] = f"has a {final_prediction_2}% probability of not Churning (Exiting)" if prediction_2[0] == 0 else f"has a {final_prediction_2}% probability of Churning (Exiting)"
            context["data"] = data
        
        except Exception as err:
            print("Error", err)

    return render(request, "ml_classifier/predict.html", context)

def view_project(request):
    return render(request, "ml_classifier/project.html")

def view_eda(request):
    context = {}
    context = {"slide_num": 2}
    return render(request, "ml_classifier/eda.html", context)

def view_results(request):
    context = {}
    try:
        info = Info.objects.filter(category="ml")
        context = {"info": info}
    except Exception as err:
        print("Error", err)
    return render(request, "ml_classifier/results.html", context)

def view_eval(request):
    context = {}
    try:
        info = Info.objects.filter(category="eval")
        context = {"info": info}
    except Exception as err:
        print("Error", err)
    return render(request, "ml_classifier/eval.html", context)

def view_table(request):
    context = {}
    try:
        predictions = Prediction.objects.all()
        context = { "predictions": predictions }
    except Exception as err:
        print(err)
    return render(request, "ml_classifier/table.html", context)

def view_data_dictionary(request):
    return render(request, "ml_classifier/data_dictionary.html")

def view_team(request):
    return render(request, "ml_classifier/team.html")