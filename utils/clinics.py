import requests


def get_clinics():
    api_url = "https://tight-similarly-chigger.ngrok-free.app/api/getClinics"

    try:
        # Make the POST request with an empty JSON body
        response = requests.post(api_url, json={})

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

# not implemented yet in the API

# def get_clinic_schedule(clinic_id):
#     api_url = f"https://tight-similarly-chigger.ngrok-free.app/api/getClinicSchedule/{clinic_id}"

#     try:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             data = response.json()
#             schedule = data.get("schedule", [])
#             return schedule
#         else:
#             print(f"Error: {response.status_code} - {response.text}")
#             return []
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []


def add_appointment(clinic, time, mobile, date):
    api_url = "https://tight-similarly-chigger.ngrok-free.app/api/addAppointment"
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


def get_user_info_and_status(mobile):
    api_url = f"https://tight-similarly-chigger.ngrok-free.app/api/getUser"
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
    api_url = f"https://tight-similarly-chigger.ngrok-free.app/api/addUser"
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


def get_messages(mobile):
    api_url = f"https://tight-similarly-chigger.ngrok-free.app/api/getMessages"
    payload = {
        "mobile": mobile
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            messages = response.json().get("messages", [])
            return messages
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def add_message(mobile, message):
    api_url = "https://tight-similarly-chigger.ngrok-free.app/api/addMessage"
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


if __name__ == "__main__":
    clinics = add_appointment(
        "clinic1", "10:00", "1234567890", "2024-02-20T06:49:35Z")
    print(clinics)
