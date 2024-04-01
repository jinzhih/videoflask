from flask import Flask, request,jsonify
import json
from datetime import datetime
from video import video_gen

app = Flask(__name__)

@app.route("/")
def index():
  return "hello world"

@app.route("/video",methods=["POST"])
def video():
  data = request.get_json()
  id = data["id"]
  summary = data["summary"]
  dialogue = data["Dialogue"]

  video_name = video_gen(id,summary,dialogue)
  return video_name

if __name__ == "__main__":
  app.run()