from flask import Flask, render_template, request, redirect, url_for
import os
import openai
import google.generativeai as genai
import requests
from dotenv import load_dotenv
from datetime import datetime
import random
# Load .env variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
FB_PAGE_ID = os.getenv("FB_PAGE_ID")
FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
AI_API_KEY = os.getenv("AI_API_KEY")


app = Flask(__name__)
genai.configure(api_key=AI_API_KEY)
def generate_sqa_post():
    

# subject list
    subjects = ['Software Quality Assurance (SQA)', 'Software Development Life Cycle (SDLC)', 'Software Testing Life Cycle (STLC)', 'Manual Testing vs Automation Testing', 'Test Case ', 'Functional Testing', 'Black Box Testing','Regression Testing', 'Security Testing']
    random_subject = random.choice(subjects)
#     prompt = f"""
#     Generate a short Facebook post about {random_subject} in Bangla.

# ⚠️ Only return the post content.

# Do not include any explanation, headings, or formatting — just the one versions of the post.
#     """

    prompt = """আমি একজন experienced SQA expert। দয়া করে ১০০ থেকে ২০০ শব্দের মধ্যে একটি নতুন, সহজবোধ্য এবং ইউনিক পোস্ট লিখুন software testing নিয়ে, যেখানে বাংলা এবং ইংরেজির মিক্স থাকবে। পোস্টে থাকতে হবে:

- software testing এর কোনো একটা specific টপিক (যেমন test case, bug reporting, automation, regression testing ইত্যাদি)  
- practical example বা simple tips  
- friendly এবং professional tone  
- পোস্টের শেষে একটি question রাখবেন যা reader কে comment করতে encourage করবে  
- অন্তত দুইটা hashtag ব্যবহার করবেন: #SoftwareTesting #SQA
Post should be fresh and useful for both beginners and intermediate learners.
⚠️ Only return the post content.
"""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

def post_to_facebook(message):
    url = f"https://graph.facebook.com/{FB_PAGE_ID}/feed"
    payload = {
        "message": message,
        "access_token": FB_ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    post = generate_sqa_post()
    return render_template('index.html', generated_post=post)

@app.route('/post', methods=['POST'])
def post():
    content = request.form.get('content')
    if content:
        response = post_to_facebook(content)
        if response.status_code == 200:
            status = "✅ Post Successful"
        else:
            status = f"❌ Failed: {response.text}"
    else:
        status = "⚠️ No content to post"
    return render_template('index.html', post_status=status, generated_post=content)

if __name__ == '__main__':
    app.run(debug=True)
