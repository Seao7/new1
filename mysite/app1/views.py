from django.shortcuts import render
import os
import pickle
from django.conf import settings

base_dir = settings.BASE_DIR
model_file_path = os.path.join(base_dir, 'app1/feature_selected_model.pkl')
model = pickle.load(open(model_file_path, 'rb'))

def predictor(request):
    if request.method == 'POST':
        #['cp', 'oldpeak', 'thalach', 'thal', 'exang', 'ca', 'sex', 'fbs']
        cp = request.POST['cp']
        oldpeak = request.POST['oldpeak']
        thalach = request.POST['thalach']
        thal = request.POST['thal']
        exang = request.POST['exang']
        ca = request.POST['ca']
        fbs = request.POST['fbs']
        sex = request.POST['sex']
        if sex == 'Male':
            sex = 1
        else:
            sex = 0
        y_pred = model.predict([[cp, oldpeak, thalach, thal, exang, ca, sex, fbs]])
        if y_pred[0] == 0:
            return render(request, 'main.html', {'result' : 'You do not have heart disease'})
        elif y_pred[0] == 1:
            return render(request, 'main.html', {'result' : 'You have heart disease, visit the nearest hospital'})

    return render(request, 'main.html')