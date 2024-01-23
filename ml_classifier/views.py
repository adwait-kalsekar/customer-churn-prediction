from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

import pandas as pd

from .data_preprocessing import preprocessing
from .models import Slide, Prediction

# Create your views here.

def index(request):
    return render(request, "ml_classifier/home.html")

@csrf_exempt
def predict(request):
    # Load model data
    model_1, model_2, score_1, score_2, col_names = preprocessing.load_model_data()
    model_1_name = "Logistic Regression"
    model_2_name = "Random Forest Classification"

    hosted_url = "https://3193-2601-84-8800-6ac0-9df2-33da-dad8-570d.ngrok-free.app"
    context = { "hosted_url": hosted_url, "model_1": model_1_name, "model_2": model_2_name, "score_1": score_1, "score_2": score_2 }
    if request.method == 'POST':
        try:
            pred_obj = Prediction()

            # Get JSON request
            data = request.POST.dict()

            #pred_obj.name = data['name']

            del data['csrfmiddlewaretoken']
            pred_obj.name = data['Name']
            del data['Name']

            # Convert JSON to Pandas DF
            df = pd.DataFrame(data, index=[0])
            print(df.info())

            # Clean and encode data according to the model
            encoded_df = preprocessing.encode_data(df, col_names)
            

            # Predict Results
            prediction_1 = list(model_1.predict(encoded_df))
            probability_1 = list(model_1.predict_proba(encoded_df))

            prediction_2 = list(model_2.predict(encoded_df))
            probability_2 = list(model_2.predict_proba(encoded_df))
            
            final_prediction_1 = '{0:.2f}'.format(probability_1[0][prediction_1[0]] * 100)
            final_prediction_2 = '{0:.2f}'.format(probability_2[0][prediction_2[0]] * 100)

            pred_obj.age = data['Age']
            pred_obj.gender = data['Gender']
            pred_obj.credit_score = data['CreditScore']
            pred_obj.geography = data['Geography']
            pred_obj.tenure = data['Tenure']
            pred_obj.balance = data['Balance']
            pred_obj.num_of_prod = data['NumOfProducts']
            pred_obj.has_cr_card = data['HasCrCard']
            pred_obj.is_active = data['IsActiveMember']
            pred_obj.estimated_salary = data['EstimatedSalary']
            pred_obj.prediction_1 = "Will not Churn" if prediction_1[0] == 0 else "Will Churn"
            pred_obj.probability_1 = final_prediction_1
            pred_obj.prediction_2 = "Will not Churn" if prediction_2[0] == 0 else "Will Churn"
            pred_obj.probability_2 = final_prediction_2

            pred_obj.save()
            

            context["prediction_1"] = f"has a {final_prediction_1}% probability of not Churning (Exiting)" if prediction_1[0] == 0 else f"has a {final_prediction_1}% probability of Churning (Exiting)"
            context["prediction_2"] = f"has a {final_prediction_2}% probability of not Churning (Exiting)" if prediction_2[0] == 0 else f"has a {final_prediction_2}% probability of Churning (Exiting)"
            context["data"] = data
        
        except Exception as err:
            print("Error", err)
            return redirect(error_page, "error")

    return render(request, "ml_classifier/predict.html", context)

def view_project(request, page):
    context = {}
    try:
        if page == "intro" or page == "eda" or page == "clf" or page == "clus":
            slides = Slide.objects.filter(category=page).order_by('slide_num').values()
            print(slides)
            context = { "slides": slides , "slide_count": len(slides)}
        else:
            return redirect(error_page, "404")
    except Exception as err:
        print("Error", err)
        return redirect(error_page, "error")
    return render(request, "ml_classifier/project.html", context)

def view_table(request):
    context = {}
    try:
        predictions = Prediction.objects.all()
        context = { "predictions": predictions }
    except Exception as err:
        print("Error", err)
        return redirect(error_page, "error")
    return render(request, "ml_classifier/table.html", context)

def error_page(request, all_paths):
    context = {"message": "Something Went Wrong!"}
    if all_paths == "404":
        context = {"message": "Oops! Page Not Found!"}
    return render(request, "ml_classifier/error.html", context)