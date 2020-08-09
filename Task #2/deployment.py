# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 22:59:37 2020

@author: Abdelfattah Mohamed

BOUNS PART
"""
# Importing packages
import numpy as np 
from flask import Flask,request,Response
import simplejson as json
import matplotlib.pyplot as plt 
import pickle 
# Deployment

def fun1(mTest):
    filename = 'E:\Internship\widebot\Task #2\classifier.sav'
    model = loaded_model = pickle.load(open(filename, 'rb'))
    abdelfattah = loaded_model.predict(mTest)
    print(abdelfattah)   
    #print(model)
    return json.dumps(abdelfattah)
# API
app = Flask(__name__)
#route http post to this method 
@app.route('/api/upload',methods=['POST'])
def upload():
    #img = cv2.imdecode(np.fromstring(request.files['image'].read(),np.uint8),cv2.IMREAD_UNCHANGED)
    #img_proc = poster_film(img)
    input_feature = [[-0.8546415  ,-0.93879347 ,-0.29343897 ,-0.60896388 ,-0.23475788 ,-0.26514357,
  -0.23475788  ,0.28317281 ,-0.72669368  ,0.72669368 ,-0.08520286  ,0.43174581,
  -0.4199356   ,0.43174581 ,-0.08520286 ,-0.4199356  ,-0.34029718 ,-0.24899338,
   1.84519969 ,-0.32084447 ,-0.15487169 ,-0.19928685 ,-0.18097038 ,-0.23565743,
  -0.10628912 ,-0.21718612 ,-0.2216965  ,-0.44692348 ,-0.09725217 ,-0.31947634,
  -0.31465839 ,-0.07120833 ,-0.19534424 ,1.67997442 ,-0.1097042  ,-0.09340289,
  -0.06013848 ,-1.15070439 ,-0.11302089  ,2.45103565 ,-2.45103565  ,1.2414543,
  -1.2414543  ,-1.02592144  ,1.02592144  ,0.28093933 ,-0.14481472 ,-0.23565743,
  -0.40135753 ,-0.62193778 ,-0.28317281  ,0.28317281],
 [-1.11476359  ,0.69452648 ,-0.77917563 ,-0.60896388 ,-0.41584027 ,-0.26514357,
  -0.41584027  ,0.28317281  ,1.37609564 ,-1.37609564 ,-0.08520286  ,0.43174581,
  -0.4199356   ,0.43174581 ,-0.08520286 ,-0.4199356  ,-0.34029718  ,4.01617102,
  -0.54194676 ,-0.32084447 ,-0.15487169 ,-0.19928685 ,-0.18097038 ,-0.23565743,
  -0.10628912 ,-0.21718612 ,-0.2216965  ,-0.44692348 ,-0.09725217 ,-0.31947634,
  -0.31465839 ,-0.07120833 ,-0.19534424 ,-0.59524716 ,-0.1097042  ,-0.09340289,
  -0.06013848  ,0.86903292 ,-0.11302089 ,-0.4079908   ,0.4079908   ,1.2414543,
  -1.2414543   ,0.97473351 ,-0.97473351  ,0.28093933,-0.14481472 ,-0.23565743,
  -0.40135753 ,-0.62193778 ,-0.28317281  ,0.28317281]]
    input_feature = np.asarray(input_feature)
    fun1(input_feature[:2])
    return Response(response=input_feature,status=200,mimetype='application/json')
app.run(host='0.0.0.0',port=5000)