from phonenumbers import parse, timezone, carrier, geocoder

def get_phone_info():
    # Get phone number input from user
    number = input("Enter your phone number: ")

    try:
        # Parse the phone number
        phone = parse(number)

        # Get timezone, carrier, and region
        phone_timezone = timezone.time_zones_for_number(phone)
        phone_carrier = carrier.name_for_number(phone, "en")
        phone_region = geocoder.description_for_number(phone, "en")

        # Display the results
        print(f"Phone: {phone}")
        print(f"Timezone(s): {phone_timezone}")
        print(f"Carrier: {phone_carrier}")
        print(f"Region: {phone_region}")

    except Exception as e:
        print(f"Error: {e}. Please enter a valid phone number.")

# Call the function
get_phone_info()
