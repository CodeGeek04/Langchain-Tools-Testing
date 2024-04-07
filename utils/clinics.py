import requests


def get_clinics(latitude, longitude):
    api_url = " http://localhost:3000/api/getClinics"
    payload = {
        "latitude": latitude,
        "longitude": longitude
    }

    try:
        # Make the POST request with an empty JSON body
        response = requests.post(api_url, json=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract clinic information from the response
            clinics = data.get("message", [])
            return clinics
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_Appointment(clinic_id):
    api_url = " http://localhost:3000/api/getAppointment"
    payload = {
        "clinicUserId": clinic_id
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return response.json()

        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def add_appointment(clinic, time, mobile, date):
    api_url = " http://localhost:3000/api/addAppointment"
    payload = {
        "clinic": clinic,
        "time": time,
        "mobile": mobile,
        "date": date
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return response.json().get("message", "Appointment added successfully")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return "Failed to add appointment"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while adding the appointment"


def update_appointment(id, mobile, clinic, date, time, status):
    api_url = " http://localhost:3000/api/updateAppointment"
    payload = {
        "id": id,
        "mobile": mobile,
        "clinic": clinic,
        "date": date,
        "time": time,
        "status": status
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return response.json().get("message", "Appointment updated successfully")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return "Failed to update appointment"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while adding the appointment"


def get_user_info_and_status(mobile):
    api_url = f" http://localhost:3000/api/getUser"
    payload = {
        "mobile": mobile
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


def addUser(mobile):
    api_url = f" http://localhost:3000/api/addUser"
    payload = {
        "mobile": mobile
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


def getUser(mobile):
    api_url = f" http://localhost:3000/api/getUser"
    payload = {
        "mobile": mobile
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


def updateUser(mobile, name, address):
    api_url = f" http://localhost:3000/api/updateUser"
    payload = {
        "mobile": mobile,
        "name": name,
        "address": address
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return response.json().get("user", "User updated successfully")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


def get_messages(mobile):
    api_url = f" http://localhost:3000/api/getMessages"
    payload = {
        "mobile": mobile
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            messages = response.json()
            return messages
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def add_message(mobile, message):
    api_url = " http://localhost:3000/api/addMessage"
    payload = {
        "mobile": mobile,
        "message": message
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return response.json().get("message", "Message sent successfully")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return "Failed to send message"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while sending the message"


# if __name__ == "__main__":
#     clinics = get_clinics(0, 0)
#     print(clinics)
