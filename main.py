import requests
import uuid
import os
import json
from datetime import datetime

class Car:
    def __init__(self, owner, make, model, id, lastRenewed, note) -> None:
        self.owner = owner
        self.make = make
        self.model = model
        self.id = id
        self.lastRenewed = lastRenewed
        self.note = note
    
    def prettyName(self):
        date = "Never"
        if self.lastRenewed:
            date = datetime.fromisoformat(self.lastRenewed)
            date = date.strftime("%c")
        return f"{self.owner}'s {self.make} {self.model} (ID: {self.id}) (Last Renewed: {date})"
    
    def prettyNameShort(self):
        return f"{self.owner}'s {self.make} {self.model}"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def appconfig():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/authService/100000002/appconfig",
            headers={
                "X-Kony-Integrity": "GWSUSEVMJK;FEC9AA232EC59BE8A39F0FAE1B71300216E906B85F40CA2B1C5C7A59F85B17A4",
                "X-HTTP-Method-Override": "GET",
                "X-Kony-App-Key": "85ee60a3c8f011baaeba01ff3a5ae2c9",
                "Accept": "*/*",
                "X-Kony-App-Secret": "e3048b73f2f7a6c069f7d8abf5864115",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
            },
        )
        return ["OK", response.status_code]
    except requests.exceptions.RequestException as e:
        return [str(e), None]

def login():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/authService/100000002/login",
            headers={
                "X-Kony-Platform-Type": "ios",
                "Accept": "application/json",
                "X-Kony-App-Secret": "e3048b73f2f7a6c069f7d8abf5864115",
                "Accept-Language": "en-us",
                "X-Kony-SDK-Type": "js",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-SDK-Version": "8.4.134",
                "X-Kony-App-Key": "85ee60a3c8f011baaeba01ff3a5ae2c9",
            },
        )
        return [response.json().get('claims_token').get('value'), response.status_code]
    except requests.exceptions.RequestException as e:
        return [str(e), None]

def versionControl():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/services/DealerAppService7/VersionControl",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "deviceCategory": "iPhone",
                "appver": "2.7.0",
                "deviceLocale": "en_US",
                "deviceModel": "iPhone%206%20Plus",
                "deviceVersion": "12.5.7",
                "deviceType": "",
            },
        )
        return ["OK", response.status_code]
    except requests.exceptions.RequestException as e:
        return [str(e), None]

def getProperties():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/services/DealerAppService7/getProperties",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
        )
        return ["OK", response.status_code]
    except requests.exceptions.RequestException as e:
        return [str(e), None]

def update_1():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "deviceId": radio_id_input,
                "appVersion": "2.7.0",
                "lng": "-86.210313195",
                "deviceID": uuid4,
                "provisionPriority": "2",
                "provisionType": "activate",
                "lat": "32.37436705",
            },
        )
        return [response.json().get('seqValue'), response.status_code, response.content]
    except requests.exceptions.RequestException as e:
        return [str(e), None, None]

def getCRM():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/services/DemoConsumptionRules/GetCRMAccountPlanInformation",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
            },
        )
        return ["OK", response.status_code, response.content]
    except requests.exceptions.RequestException as e:
        return [str(e), None, None]

def dbUpdate():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/services/DBSuccessUpdate/DBUpdateForGoogle",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "OM_ELIGIBILITY_STATUS": "Eligible",
                "appVersion": "2.7.0",
                "flag": "failure",
                "Radio_ID": radio_id_input,
                "deviceID": uuid4,
                "G_PLACES_REQUEST": "",
                "OS_Version": "iPhone 12.5.7",
                "G_PLACES_RESPONSE": "",
                "Confirmation_Status": "SUCCESS",
                "seqVal": seq,
            },
        )
        return ["OK", response.status_code, response.content]
    except requests.exceptions.RequestException as e:
        return [str(e), None, None]

def blocklist():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/services/USBlockListDevice/BlockListDevice",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "deviceId": uuid4,
            },
        )
        return ["OK", response.status_code, response.content]
    except requests.exceptions.RequestException as e:
        return [str(e), None, None]

def oracle():
    try:
        response = requests.post(
            url="https://oemremarketing.custhelp.com/cgi-bin/oemremarketing.cfg/php/custom/src/oracle/program_status.php",
            params={
                "google_addr": "395 EASTERN BLVD, MONTGOMERY, AL 36117, USA",
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "*/*",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
            },
        )
        parsed_content = json.loads(response.content.decode('utf8').replace("'", '"'))
        return ["OK", response.status_code, parsed_content]
    except requests.exceptions.RequestException as e:
        return [str(e), None, None]

def createAccount():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/services/DealerAppService3/CreateAccount",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SXM Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
                "oracleCXFailed": "1",
                "appVersion": "2.7.0",
            },
        )
        parsed_content = response.content.decode('utf8')
        return ["OK", response.status_code, parsed_content]
    except requests.exceptions.RequestException as e:
        return [str(e), None, None]

def update_2():
    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "deviceId": radio_id_input,
                "provisionPriority": "2",
                "appVersion": "2.7.0",
                "device_Type": "iPhone iPhone 6 Plus",
                "deviceID": uuid4,
                "os_Version": "iPhone 12.5.7",
                "provisionType": "activate",
            },
        )
        return ["OK", response.status_code, response.content]
    except requests.exceptions.RequestException as e:
        return [str(e), None, None]

def readCars() -> list:
    with open("cars.json") as carList:
        cars = json.load(carList)
        parsedCars = []
        for car in cars:
            carClass = Car(car["owner"], car["make"], car["model"], car["id"], car["lastRenewed"], car["note"])
            parsedCars.append(carClass)
        return parsedCars

def writeCars(carList) -> list:
    jsonCars = []
    for car in carList:
        obj = {
            "owner": car.owner,
            "make": car.make,
            "model": car.model,
            "id": car.id,
            "lastRenewed": car.lastRenewed,
            "note": car.note
        }
        jsonCars.append(obj)
    with open("cars.json", "w") as existingList:
        json.dump(jsonCars, existingList)

def chooseCar(cars: list) -> list:
    while True:
        clear()
        print("Choose a car to renew by number or use 'a' to renew all cars.\n\n")
        for num, car in enumerate(cars, 1):
            print(f"{num}. {car.prettyName()}")
        choice = input("\n> ")
        if choice == "a":
            return cars
        try:
            choice = int(choice)
            choice -= 1
            if choice < 0 or choice >= len(cars):
                raise ValueError
            return [cars[choice]]
        except ValueError:
            clear()
            input("Invalid input. Try again.\n\nPress [ENTER] to continue.")
            continue

clear()
cars = readCars()
carChoices = chooseCar(cars)

for num, car in enumerate(carChoices, 1):
    clear()
    print(f"[{num}/{len(carChoices)}] Renewing {car.prettyNameShort()}")
    radio_id_input = car.id
    uuid4 = str(uuid.uuid4())
    auth_token = ""
    seq = ""
    alreadyActive = False

    print("Configuring...")
    result = appconfig()
    if result[1] == 200:
        print("Successfully Configured\n")
    else:
        print(f"!!Unsuccessfully Configured!! Status Code: {result[1]}\n")
        exit()

    print("Logging In...")
    result = login()
    if result[1] == 200 or not result[1]:
        print("Logged In\n")
        auth_token = result[0]
    else:
        print(f"!!Unsuccessfully Logged In!! Status Code: {result[1]}\n")
        exit()

    print("Controlling Version...")
    result = versionControl()
    if result[1] == 200:
        print("Version Controlled\n")
    else:
        print(f"!!Unsuccessfully Version Controlled!! Status Code: {result[1]}\n")
        exit()

    print("Getting Properties...")
    result = getProperties()
    if result[1] == 200:
        print("Properties Retrieved\n")
    else:
        print(f"!!Properties Retrieved Unsuccessfully!! Status Code: {result[1]}\n")
        exit()
    
    print("First Update...")
    result = update_1()
    if result[1] == 200 or not result[1]:
        print("First Update Success\n")
        seq = result[0]
    else:
        print(f"!!First Update Unsuccessful!! Status Code: {result[1]}\n")
        exit()

    print("Getting CRM...")
    result = getCRM()
    if result[1] == 200:
        print("CRM Retrieved\n")
    else:
        print(f"!!CRM Retrieved Unsuccessfully!! Status Code: {result[1]}\n")
        exit()

    print("Updating Database...")
    result = dbUpdate()
    if result[1] == 200:
        print("Database Updated\n")
    else:
        print(f"!!Database Updated Unsuccessfully!! Status Code: {result[1]}\n")
        exit()

    print("Checking Blocklist...")
    result = blocklist()
    if result[1] == 200:
        print("Blocklist Checked\n")
    else:
        print(f"!!Blocklist Checked Unsuccessfully!! Status Code: {result[1]}\n")
        exit()

    print("Calling Oracle Address...")
    result = oracle()
    if result[1] == 200:
        print("Oracle Address Called")
        print(f"Dealer Code: {result[2]['dealerCode']}, Dealer ID: {result[2]['dealerId']}\n")
    else:
        print(f"!!Oracle Address Called Unsuccessfully!! Status Code: {result[1]}\n")
        exit()

    print("Creating Account...")
    result = createAccount()
    if result[1] == 200:
        print("Account Created\n")
    else:
        print(f"!!Account Created Unsuccessfully!! Status Code: {result[1]}\n")
        exit()

    print("Second Update...")
    result = update_2()
    if result[1] == 200:
        print("Second Update Complete\n")
    else:
        print(f"!!Second Update Unsuccessful!! Status Code: {result[1]}\n")
        exit()

    if not alreadyActive:
        (list(filter(lambda x: x.id == car.id, cars))[0]).lastRenewed = datetime.now().isoformat()
    
    if num != len(carChoices):
        input("Press [ENTER] to continue.")

writeCars(cars)
print("\nRenewal Finished.")