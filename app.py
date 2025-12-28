from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/membership')
def membership():
    plans = [
        {"name": "Basic Plan", "price": "Rs 3000/month", "features": ["Gym Access", "Locker Access"]},
        {"name": "Standard Plan", "price": "Rs 5000/month", "features": ["Gym Access", "2 PT Sessions", "Diet Plan"]},
        {"name": "Premium Plan", "price": "Rs 8000/month", "features": ["Unlimited Classes", "Sauna", "Diet + PT"]},
    ]
    return render_template('membership.html', plans=plans)

if __name__ == "__main__":
    app.run(debug=True)
