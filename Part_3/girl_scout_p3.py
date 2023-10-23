from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

# create client to connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# get project3 db from MongoDB server
db = client["project3"]

# get collections from db
adults = db['adults']
troops = db['troops']
cookietypes = db['cookietypes']

def fetchTroopSummaryByTroopNumber():
    try: 
        troop_number = int(input("Enter troop number: "))

        troop = troops.find_one({"_id": troop_number})
        if troop == None:
            print("No troops associated with troop number", troop_number, "was found.")
            return
        
        troop_summary = f"\nTroop Number: {troop['_id']}\n" +\
                f"Founding Date: {troop['founding_date']}\n" +\
                f"Community: {troop['community']}\n" +\
                f"Scouts: "
        
        # get scouts names
        scout_name_list = set()
        for scout in troop['scouts']:
            scout_name_list.add(f"{scout['firstname']} {scout['lastname']}")

        troop_summary += ", ".join(scout_name_list)

        # get volunteers names
        troop_summary += "\nVolunteers: "
        volunteer_name_list = set()
        for volunteer in troop['volunteers']:
            volunteer_name_list.add(f"{volunteer['firstname']} {volunteer['lastname']}")
        
        troop_summary += ", ".join(volunteer_name_list)
        troop_summary += "\n"
        print(troop_summary)
        
    except:
        print("There was an error. Please make sure to enter in a valid troop number.")

def fetchScoutSummaryByScoutNumber():
    try: 
        first_name = input("Enter scout's first name: ")
        last_name = input("Enter scout's last name: ")

        # unwind the scouts array & match scout documents w/ the given input name
        scout_pipeline = [
            {"$unwind" : "$scouts"},
            {"$match": {"scouts.firstname": first_name, "scouts.lastname": last_name}}
        ]

        # select troop object with matching scout
        troop_results = troops.aggregate(scout_pipeline)
        if troop_results == None:
            print(f"No scouts associated with the name {first_name} {last_name}")
            return
        
        # we can assume that each scout has a unique name, so there should only be 1 troop doc in the results
        scout = None
        for troop_doc in troop_results:
            s = troop_doc['scouts']
            if s['firstname'] == first_name and s['lastname'] == last_name:
                scout = s
                break
        
        if scout == None:
            print(f"No scouts associated with the name {first_name} {last_name}")
            return
        
        scout_summary = f"\nFull name: {scout['firstname']} {scout['lastname']}\n" +\
         f"Birthday: {scout['birthday'].strftime('%Y-%m-%d')}\n" +\
         f"Grade level: {scout['gradelevel']}\n" +\
         "Adults: "
        
        # get adult names
        adult_name_list = set()
        for adult in scout['adults']:
            adult_name_list.add(f"{adult['firstname']} {adult['lastname']}")

        scout_summary += ", ".join(adult_name_list)

        # get scout allotments
        scout_summary += "\nAllotments: \n"
        for allotment in scout['allotments']:
            scout_summary += f"\tDelivery Date: {allotment['deliverydate'].strftime('%Y-%m-%d')}\n"

            for cookie in allotment['cookies']:
                scout_summary += f"\t\t{cookie['cookietype']} - {cookie['boxes']} boxes\n"

        print(scout_summary)
    
    except:
        print("There was an error. Please make sure to enter in a valid first and last name.")

def fetchSaleReportByTroopNumber():
    try: 
        troop_number = int(input("Enter troop number: "))

        # just to make sure user enters in valid troop number
        troop = troops.find_one({"_id": troop_number})
        if troop == None:
            print("No troops associated with troop number", troop_number, "was found.")
            return
        
        sale_report_pipeline = [
            {
                '$match': {
                    '_id': troop_number
                }
            }, {
                '$unwind': {
                    'path': '$scouts'
                }
            }, {
                '$unwind': {
                    'path': '$scouts.allotments'
                }
            }, {
                '$unwind': {
                    'path': '$scouts.allotments.cookies'
                }
            }, {
                '$lookup': {
                    'from': 'cookietypes', 
                    'localField': 'scouts.allotments.cookies.cookieid', 
                    'foreignField': '_id', 
                    'as': 'cookie'
                }
            }, {
                '$unwind': {
                    'path': '$cookie'
                }
            }, {
                '$project': {
                    'firstname': '$scouts.firstname', 
                    'lastname': '$scouts.lastname', 
                    'totalvalue': {
                        '$multiply': [
                            '$scouts.allotments.cookies.boxes', '$cookie.price'
                        ]
                    }
                }
            }, {
                '$group': {
                    '_id': {
                        'firstname': '$firstname', 
                        'lastname': '$lastname'
                    }, 
                    'totalvalue': {
                        '$sum': '$totalvalue'
                    }
                }
            }
        ]

        sale_report_results = troops.aggregate(sale_report_pipeline)
        
        print(f"\nSale reports of Troop {troop_number}:")
        for sale_report in sale_report_results:
            print(f"\t{sale_report['_id']['firstname']} {sale_report['_id']['lastname']} - ${sale_report['totalvalue']}")
        
    except:
        print("There was an error. Please make sure to enter in a valid troop number.")    

# Print out main menu - 
# Option 1 - Fetch troop summary
# Option 2 - Fetch scout summary
# Option 3 - Fetch sales report

print("Main Menu:\n" + 
      "[1] Fetch troop summary by troop number\n" +
      "[2] Fetch scout summary by scout's first and last name\n" +
      "[3] Fetch sale reports by troop number\n" +
      "[4] Exit\n\n")

while True: 
    try:
        input_int = int(input("\nEnter in the option number: "))
        if input_int == 1: 
            fetchTroopSummaryByTroopNumber()
        elif input_int == 2:
            fetchScoutSummaryByScoutNumber()
        elif input_int == 3:
            fetchSaleReportByTroopNumber()
        
        # break out of the while loop & reach sys.exit()
        elif input_int == 4:
            print("Exiting\n")
            break
        else:
            print("Invalid option. Please enter a number 1 through 4.\n\n")
    except:
        print("Invalid option. Please enter a number 1 through 4.\n\n")

sys.exit()

