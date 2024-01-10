from datetime import *
import time
import sys

import json
import requests
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    
    url1 = "http://172.31.32.241/myflix/videos"
    resp1 = requests.get(url1)
    if resp1.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(resp1.reason, resp1.status, jresp1['Exception']['Message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(resp1.reason, resp1.status, jresp1['Exception']['Message'])
    jresp1 = resp1.json()
                
    url2 = "http://172.31.32.241/myflix/categories"
    resp2 = requests.get(url2)
    if resp2.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(resp2.reason, resp2.status, jresp2['Exception']['Message']))
      return "Unexpected response: {0}. Status: {1}. Message: {2}".format(resp2.reason, resp2.status, jresp2['Exception']['Message'])
    jresp2 = resp2.json()

    return render_template("home.html", user = current_user, catalogue = jresp1, category = jresp2)

@views.route('/<video>')
@login_required
def video_page(video):
  
  url = 'http://172.31.32.241/myflix/videos?filter={"video.uuid":"'+video+'"}'
  response = requests.get(url)
  if response.status_code != 200:
    print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
    return "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message'])
  jResp = response.json()
  for index in jResp:
    for key in index:
      if (key != "_id"):
        for key2 in index[key]:
          if (key2 == "category"):
            category = index[key][key2]
  url2= 'http://172.31.32.241/myflix/videos?filter={"video.category":"'+category+'"}'
  response2 = requests.get(url2)
  jResp2 = response2.json()
  return render_template("video.html", user = current_user, video = jResp,cat = jResp2)
  
