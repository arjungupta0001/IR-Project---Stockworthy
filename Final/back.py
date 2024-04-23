import requests

# Define the form data
form_data = {
    'email': 'ankush21232@iiitd.ac.in',
    'password': 'qoXX4HVF',
    # Include any other form fields needed for authentication or submission
}

# URL of the form submission endpoint
url = 'https://formoid.net/?call=forms_entries&param=528179'

# Send a POST request to simulate form submission
response = requests.post(url, data=form_data)

# Check if the request was successful
if response.status_code == 200:
    # Save the CSV file from the response content
    with open('form_data.csv', 'wb') as f:
        f.write(response.content)
    print('CSV file downloaded successfully.')
else:
    print('Failed to download CSV file.')
