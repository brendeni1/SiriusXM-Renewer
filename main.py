import requests as requestss
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

# --- Updated API Functions from new.py ---
def appconfig():
    # appConfig
    # POST https://dealerapp.siriusxm.com/authService/100000002/appconfig

    try:
        response = requests.post(
            url="https://dealerapp.siriusxm.com/authService/100000002/appconfig",
            headers={
                "X-Kony-Integrity":
                "GWSUSEVMJK;FEC9AA232EC59BE8A39F0FAE1B71300216E906B85F40CA2B1C5C7A59F85B17A4",
                "X-HTTP-Method-Override": "GET",
                "X-Voltmx-App-Key": "67cfe0220c41a54cb4e768723ad56b41",
                "Accept": "*/*",
                "X-Voltmx-App-Secret": "c086fca8646a72cf391f8ae9f15e5331",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "User-Agent": "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
            },
        )
        return [None, 200]
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

def login():
    # login
    # POST https://dealerapp.siriusxm.com/authService/100000002/login

    try:
        response = requests.post(
            url="https://dealerapp.siriusxm.com/authService/100000002/login",
            headers={
                "X-Voltmx-Platform-Type": "ios",
                "Accept": "application/json",
                "X-Voltmx-App-Secret": "c086fca8646a72cf391f8ae9f15e5331",
                "Accept-Language": "en-us",
                "X-Voltmx-SDK-Type": "js",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-SDK-Version": "9.5.36",
                "X-Voltmx-App-Key": "67cfe0220c41a54cb4e768723ad56b41",
            },
        )
        return [response.json().get('claims_token').get('value'), response.status_code]
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

def versionControl():
    # VersionControl
    # POST https://dealerapp.siriusxm.com/services/DealerAppService7/VersionControl

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DealerAppService7/VersionControl",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "deviceCategory": "iPhone",
                "appver": "3.1.0",
                "deviceLocale": "en_US",
                "deviceModel": "iPhone%206%20Plus",
                "deviceVersion": "12.5.7",
                "deviceType": "",
            },
        )
        return [None, response.status_code]
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

def getProperties():
    # getProperties
    # POST https://dealerapp.siriusxm.com/services/DealerAppService7/getProperties

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DealerAppService7/getProperties",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
        )
        return [None, response.status_code]
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

def update_1():
    # 1-updateDeviceSATRefreshWithPriority
    # POST https://dealerapp.siriusxm.com/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "deviceId": radio_id_input,
                "appVersion": "3.1.0",
                "lng": "-86.210313195",
                "deviceID": uuid4,
                "provisionPriority": "2",
                "provisionType": "activate",
                "lat": "32.37436705",
            },
        )
        return [response.json().get('seqValue'), response.status_code]
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

def getCRM():
    # GetCRMAccountPlanInformation
    # POST https://dealerapp.siriusxm.com/services/DemoConsumptionRules/GetCRMAccountPlanInformation

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DemoConsumptionRules/GetCRMAccountPlanInformation",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
            },
        )
        return ["OK", response.status_code, response.content]
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

def dbUpdate():
    # DBUpdateForGoogle
    # POST https://dealerapp.siriusxm.com/services/DBSuccessUpdate/DBUpdateForGoogle

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DBSuccessUpdate/DBUpdateForGoogle",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "OM_ELIGIBILITY_STATUS": "Eligible",
                "appVersion": "3.1.0",
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
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

def blocklist():
    # BlockListDevice
    # POST https://dealerapp.siriusxm.com/services/USBlockListDevice/BlockListDevice

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/USBlockListDevice/BlockListDevice",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "deviceId": uuid4,
            },
        )
        return ["OK", response.status_code, response.content]
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

def oracle():
    # Request (9)
    # POST https://oemremarketing.custhelp.com/cgi-bin/oemremarketing.cfg/php/custom/src/oracle/program_status.php

    try:
        response = requests.post(
            url=
            "https://oemremarketing.custhelp.com/cgi-bin/oemremarketing.cfg/php/custom/src/oracle/program_status.php",
            params={
                "google_addr": "395 EASTERN BLVD, MONTGOMERY, AL 36117, USA",
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "*/*",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        parsed_content = json.loads(response.content.decode('utf8').replace("'", '"'))
        return ["OK", response.status_code, parsed_content]
    except requestss.exceptions.RequestException as e:
        return [str(e), e.response.status_code if e.response else "400", None]

def createAccount():
    # CreateAccount
    # POST https://dealerapp.siriusxm.com/services/DealerAppService3/CreateAccount

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/DealerAppService3/CreateAccount",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
                "oracleCXFailed": "1",
                "appVersion": "3.1.0",
            },
        )
        return ["OK", response.status_code, response.json()]
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

def update_2():
    # 2-updateDeviceSATRefreshWithPriority
    # POST https://dealerapp.siriusxm.com/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority

    try:
        response = requests.post(
            url=
            "https://dealerapp.siriusxm.com/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Voltmx-API-Version": "1.0",
                "X-Voltmx-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SiriusXM%20Dealer/3.1.0 CFNetwork/1568.200.51 Darwin/24.1.0",
                "X-Voltmx-Authorization": auth_token,
            },
            data={
                "deviceId": radio_id_input,
                "provisionPriority": "2",
                "appVersion": "3.1.0",
                "device_Type": "iPhone iPhone 6 Plus",
                "deviceID": uuid4,
                "os_Version": "iPhone 12.5.7",
                "provisionType": "activate",
            },
        )
        return ["OK", response.status_code, response.content]
    except requestss.exceptions.RequestException as e:
        return [None, e.response.status_code if e.response else "400"]

# --- End Updated Functions ---

def readCars() -> list:
    with open("cars.json") as carList:
        cars = json.load(carList)
        parsedCars = []
        for car in cars:
            carClass = Car(car["owner"], car["make"], car["model"], car["id"], car["lastRenewed"], car["note"])
            parsedCars.append(carClass)
        return parsedCars

def writeCars(carList) -> None:
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

# --- Main Execution ---
clear()
cars = readCars()
carChoices = chooseCar(cars)

requests = requestss.Session()

for num, car in enumerate(carChoices, 1):
    clear()
    print(f"[{num}/{len(carChoices)}] Renewing {car.prettyNameShort()}")
    radio_id_input = (car.id).upper()
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
        print(f"Dealer Code: {result[2].get('dealerCode')}, Dealer ID: {result[2].get('dealerId')}\n")
    else:
        print(f"!!Oracle Address Called Unsuccessfully!! Status Code: {result[1]}\n")
        exit()

    print("Creating Account...")
    result = createAccount()
    if result[1] == 200:
        if result[2]["resultData"][0]["resultCode"] == "FAILURE":
            if result[2]["resultData"][2]["message"]  == "Device ID is already active":
                print("\nThis car has already been registered and is still currently active. Please try again later.\n")
                alreadyActive = True
        else:
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