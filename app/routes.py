from app import app

@app.route('/')
def home():
    return 'welcome to FarmSmart!'
