import csv
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/', methods=['POST']) 

def process_form():
    name = request.form.get("name-contact-form-3-uaz4g7GXVt")
    email = request.form.get('email')
    input_text = request.form.get('textarea')
    print(name)

    # Store form data in a CSV file
    with open('form_data.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([name, email, input_text])

    # Redirect back to a thank you page or wherever you want
    return redirect('https://your-website.com/thank-you-page')

if __name__ == '__main__':
    app.run(debug=True)
