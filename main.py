# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 09:02:30 2022

@author: 10
"""

import torch
from flask import Flask, request, jsonify
import cv2
#https://www.youtube.com/watch?v=vieoHqt7pxo&ab_channel=PythonEngineer

model = torch.hub.load('ultralytics/yolov5','custom', path = 'best.pt')
def predict(img,a,b): #
    #model = torch.hub.load('ultralytics/yolov5','custom', path = 'best.pt')
    xpos = 0
    ypos = 0
    img_ = cv2.imread(img,0)
    result = model(img_)
    rl = result.xyxy[0].tolist()
    
    if len(rl) > 0:
        if rl[0][4] > 0.05:
            if rl[0][5] == 0: #enemy

                x = int(rl[0][2])
                y = int(rl[0][3])
                width = int(rl[0][2] - rl[0][0])
                height = int(rl[0][3]-rl[0][1])
                    
                xpos = int(1.0 * ((x-(width/2))-a))
                ypos = int(1.0 * ((y-(height/2))-b))
                
    #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, xpos, ypos, 1920,1080)
    return xpos,ypos

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def index():
    if request.method == "POST":
        
        file = request.files.get('file')
        request_data = request.form.to_dict()
        a = request_data["a"]
        b = request_data["b"]
        
        if file is None:
            return jsonify({"error": "no file"})
        
        #try:
        return {"prediction": predict(file,float(a),float(b))}
        #except Exception as e:
        #    return jsonify({"error": str(e)})  
                    
    return "Ok"

if __name__ == "__main__":
    app.run(debug = True)





    