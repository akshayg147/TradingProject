from django.http import HttpResponseRedirect,JsonResponse,FileResponse
from django.shortcuts import render,redirect,HttpResponse
from .models import Document
import os
from django.contrib import messages
from django.core.files.base import ContentFile, File
import json
import pandas as pd
def upload(request):
    if request.method == 'POST':
        #Fetching the user response
        user = request.POST['name']
        docfile = request.FILES.get('file')
        timee = int(request.POST['timeframe'])
        data = pd.read_csv(docfile, engine="pyarrow")
        #length of data so to get the range of for 'for' loop
        x = len(data.HIGH)
        d = data.columns
        header = data.columns
        n = timee      #no of data to be skipped each time
        fl = []        #would be list of list so that could be converted into pd dataframe later on.
        for i in range(0,x,int(timee)):
            l = [data.BANKNIFTY[i],data.DATE[i],data.TIME[i],data.OPEN[i],max(data.HIGH[i:i+timee]),min(data.LOW[i:i+timee]),data.CLOSE[i+timee-1],data.VOLUME[i+timee-1]]
            fl.append(l)
        p = pd.DataFrame(fl, columns=header)
        result = p.to_json(orient="values") #converting the file to json
        parsed = json.loads(result) #having the data in dictonary formate
        with open("ew.json", 'w') as file:
            json.dump(parsed,file, indent=4) #writting the dictionary formatted data into json
        file.close()
        #########################################################
        # getting error to be solved
        # with open('C:/Users/Win/PycharmProjects/django/webD/ew.json') as f:
        #     Document.docfile.save('output.json', File(f))
        # Document.docfile.save('output.json', ContentFile(result))
        ############################################################



        return render(request, 'upload.html',{'final':"/webD/ew.json"})
    return render(request, 'upload.html')
