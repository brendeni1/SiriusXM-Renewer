import requests
import uuid
import os
import json
import time
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
    
    def renew(self):
        renewID(self.id)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def appconfig():
    # appConfig
    # POST https://mcare.siriusxm.ca/authService/100000002/appconfig

    try:
        response = requests.post(
            url="https://mcare.siriusxm.ca/authService/100000002/appconfig",
            headers={
                "X-Kony-Integrity":
                "GWSUSEVMJK;FEC9AA232EC59BE8A39F0FAE1B71300216E906B85F40CA2B1C5C7A59F85B17A4",
                "X-HTTP-Method-Override": "GET",
                "X-Kony-App-Key": "85ee60a3c8f011baaeba01ff3a5ae2c9",
                "Accept": "*/*",
                "X-Kony-App-Secret": "e3048b73f2f7a6c069f7d8abf5864115",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def login():
    # login
    # POST https://mcare.siriusxm.ca/authService/100000002/login

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
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-SDK-Version": "8.4.134",
                "X-Kony-App-Key": "85ee60a3c8f011baaeba01ff3a5ae2c9",
            },
        )
        return response.json().get('claims_token').get('value')
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def versionControl():
    # VersionControl
    # POST https://mcare.siriusxm.ca/services/DealerAppService7/VersionControl

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DealerAppService7/VersionControl",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
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
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def getProperties():
    # getProperties
    # POST https://mcare.siriusxm.ca/services/DealerAppService7/getProperties

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DealerAppService7/getProperties",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        #print('Response HTTP Response Body: {content}'.format(
        #    content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def update_1():
    # 1-updateDeviceSATRefreshWithPriority
    # POST https://mcare.siriusxm.ca/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/USUpdateDeviceSATRefresh/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
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
        return response.json().get('seqValue')
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def getCRM():
    # GetCRMAccountPlanInformation
    # POST https://mcare.siriusxm.ca/services/DemoConsumptionRules/GetCRMAccountPlanInformation

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DemoConsumptionRules/GetCRMAccountPlanInformation",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def dbUpdate():
    # DBUpdateForGoogle
    # POST https://mcare.siriusxm.ca/services/DBSuccessUpdate/DBUpdateForGoogle

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DBSuccessUpdate/DBUpdateForGoogle",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
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
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def blocklist():
    # BlockListDevice
    # POST https://mcare.siriusxm.ca/services/USBlockListDevice/BlockListDevice

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/USBlockListDevice/BlockListDevice",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "deviceId": uuid4,
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


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
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def createAccount():
    # CreateAccount
    # POST https://mcare.siriusxm.ca/services/DealerAppService3/CreateAccount

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/DealerAppService3/CreateAccount",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
                "X-Kony-Authorization": auth_token,
            },
            data={
                "seqVal": seq,
                "deviceId": radio_id_input,
                "oracleCXFailed": "1",
                "appVersion": "2.7.0",
            },
        )
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def update_2():
    # 2-updateDeviceSATRefreshWithPriority
    # POST https://mcare.siriusxm.ca/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority

    try:
        response = requests.post(
            url=
            "https://mcare.siriusxm.ca/services/USUpdateDeviceRefreshForCC/updateDeviceSATRefreshWithPriority",
            headers={
                "Accept": "*/*",
                "X-Kony-API-Version": "1.0",
                "X-Kony-DeviceId": uuid4,
                "Accept-Language": "en-us",
                "Accept-Encoding": "br, gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent":
                "SXM%20Dealer/2.7.0 CFNetwork/978.0.7 Darwin/18.7.0",
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
        #print('Response HTTP Status Code: {status_code}'.format(
        #    status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

def renewID(radioID: str):
    requests = requests.Session()
    radio_id_input = radioID
    uuid4 = str(uuid.uuid4())
    auth_token = ""
    seq = ""

    print("Configuring...")
    appconfig()
    print("Successfully Configured\n")

    print("Logging In...")
    auth_token = login()
    print("Logged In\n")

    print("Controlling Version...")
    versionControl()
    print("Version Controlled\n")

    print("Getting Properties...")
    getProperties()
    print("Properties Retrieved\n")

    print("First Update...")
    seq = update_1()
    print("First Update Complete\n")

    print("Getting CRM...")
    getCRM()
    print("CRM Retrieved\n")

    print("Updating Database...")
    dbUpdate()
    print("Database Updated\n")

    print("Checking Blocklist...")
    blocklist()
    print("Blocklist Checked\n")

    # Probably not neccessary.
    print("Calling Oracle Address...")
    oracle()
    print("Oracle Address Called\n")

    print("Creating Account...")
    createAccount()
    print("Account Created\n")

    print("Second Update...")
    update_2()
    print("Second Update Complete\n")

def readCars() -> list:
    with open("cars.json") as carList:
        cars = json.load(carList)

        parsedCars = []

        for car in cars:
            carClass = Car(car["owner"], car["make"], car["model"], car["id"], car["lastRenewed"], car["note"], )
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

def chooseCar(cars: list[Car]) -> list[Car]:
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

            if choice < 0 or choice > (len(cars) - 1):
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

    car.renew()

    (list(filter(lambda x: x.id == car.id, cars))[0]).lastRenewed = datetime.now().isoformat()

writeCars(cars)

print("\nRenewal Finished.")