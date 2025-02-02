# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create the Flask app instance
app = Flask(__name__)

# Route for the Home Page (home.html)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here (you will likely check the username/password)
        username = request.form['username']
        password = request.form['password']
        
        # Example check (you'll need a more secure method in a real application)
        if username == "user" and password == "pass":
            return redirect(url_for('dashboard'))  # Redirect to the dashboard after successful login
        else:
            return "Invalid credentials, please try again"  # In production, handle errors properly
        
    return render_template('login.html')  # Render the login page if it's a GET request


# Route for the dashboard page (after login)
@app.route('/dashboard')
def dashboard():
    return render_template('dash.html')  # Show the dashboard page after login

if __name__ == '__main__':
    app.run(debug=True)

# Route for the Activity Page (activity.html)
@app.route('/activity')
def activity():
    return render_template('activity.html')

# Route for the Age Page (age.html)
@app.route('/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        return redirect(url_for('describe'))  # Redirect to the describe page after form submission
    return render_template('age.html')

# Route for the Describe Page (describe.html)
@app.route('/describe', methods=['GET', 'POST'])
def describe():
    if request.method == 'POST':
        return redirect(url_for('genderpref'))  # Redirect to gender preference page
    return render_template('describe.html')

# Route for the Gender Preference Page (genderpref.html)
@app.route('/genderpref', methods=['GET', 'POST'])
def genderpref():
    if request.method == 'POST':
        return redirect(url_for('health'))  # Redirect to the health page
    return render_template('genderpref.html')

# Route for the Health Page (health.html)
@app.route('/health', methods=['GET', 'POST'])
def health():
    if request.method == 'POST':
        return redirect(url_for('info'))  # Redirect to the info page
    return render_template('health.html')

# Route for the Info Page (info.html)
@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        return redirect(url_for('login'))  # Redirect to the login page
    return render_template('info.html')

# Route for the Login Page (login.html)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('lookinfor'))  # Redirect to the lookinfor page
    return render_template('login.html')

# Route for the Lookinfor Page (lookinfor.html)
@app.route('/lookinfor', methods=['GET', 'POST'])
def lookinfor():
    if request.method == 'POST':
        return redirect(url_for('signup'))  # Redirect to the signup page
    return render_template('lookinfor.html')

# Route for the Signup Page (signup.html)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('signupcomplete'))  # Redirect to the signup complete page
    return render_template('signup.html')

# Route for the Signup Complete Page (signupcomplete.html)
@app.route('/signupcomplete')
def signupcomplete():
    return render_template('signupcomplete.html')

# Route for the Upload Pet Photos Page (upload_pet_photos.html)
@app.route('/upload_pet_photos', methods=['GET', 'POST'])
def upload_pet_photos():
    if request.method == 'POST':
        return redirect(url_for('home'))  # Redirect to the home page after uploading photos
    return render_template('upload_pet_photos.html')

# New Route for the Cat or Dog Selection Page (catordog.html)
@app.route('/catordog', methods=['GET', 'POST'])
def catordog():
    if request.method == 'POST':
        pet_type = request.form.get('pet_type')  # Get the selected pet type (cat or dog)
        # Process the pet type if needed, and redirect to the next page
        return redirect(url_for('dash'))  # Redirect to the dashboard after selection
    return render_template('catordog.html')

# New Route for the Dashboard Page (dash.html)
@app.route('/dash')
def dash():
    return render_template('dash.html')

# Finally, run the app
if __name__ == '__main__':
    app.run(debug=True)
