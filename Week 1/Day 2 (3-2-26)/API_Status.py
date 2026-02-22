status_code = int(input("Enter API status code: "))

if 200 <= status_code < 300:
    print(" Success response")
elif 300 <= status_code < 400:
    print(" Redirection message")
elif 400 <= status_code < 500:
    print(" Client side error (check request)")
elif 500 <= status_code < 600:
    print(" Server side error (try again later)")
else:
    print(" Invalid status code")
