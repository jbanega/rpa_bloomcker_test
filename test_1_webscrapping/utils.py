import csv
import datetime
import os
import requests

from bs4 import BeautifulSoup
from pathlib import Path


def generate_list_of_identity_document():
    # Setting default values to inialize the program
    identity_document_number = None
    nationality = "V"
    list_of_identity_document = []
    message_to_user = "[Type 'done' to finish or 'exit' to close the program]: "

    while (identity_document_number != "done") or (identity_document_number == None) or (nationality != "done"):
        nationality = input("Write the nationality ['V' or 'E'] " + message_to_user)

        if nationality == "done":
            print("Starting to retrieve the information...", "\n")
            break
        elif (nationality == "exit"):
            print("Closing the program...", "\n")
            exit()
        elif (nationality == "V") or (nationality == "E"):
            pass
        else:
            print("The nationality must be 'V' or 'E'.")
            continue

        identity_document_number = input("Write the identity document number " + message_to_user)
        
        if identity_document_number == "done":
            print("Starting to retrieve the information...", "\n")
            break
        elif identity_document_number == "exit":
            print("Closing the program...", "\n")
            exit()
        elif identity_document_number.isdigit():
            list_of_identity_document.append((nationality, identity_document_number))
        else:
            print("The identity document number must contains only digits.", "\n")
    
    return list_of_identity_document


def retrieve_cne_information_from_web(list_of_identity_document, url):
    # Initialize variable to save the retrieving information
    cne_information_by_identity_document = {}

    # Send and retrieve information by identity document number 
    for nationality, identity_document in list_of_identity_document:

        # Update url with nationality and identity document number
        reference_point = "web/registro_electoral/ce.php?" + "nacionalidad=" + nationality + \
            "&cedula=" + identity_document
        identity_document_url = url + reference_point

        # Request identity document information
        print(f"Retrieving information for identity document number: {nationality}-{identity_document}", "\n")
        r = requests.get(identity_document_url)
        html_page = r.content
        soup = BeautifulSoup(html_page, "html.parser")
        information = soup.find_all(text=True)

        # Filtering information
        filtered_information = [i for i in information if (i != "\n")]

        # Validate identity document information
        if "ADVERTENCIA" in filtered_information or "ESTATUS" in filtered_information:
            print(f"{nationality}-{identity_document} is not valid.", "\n")
            continue

        # Extracting the data
        data = []
        for key in ["Cédula:", "Nombre:", "Estado:", "Municipio:", "Parroquia:"]:
                index = filtered_information.index(key)
                value = filtered_information[index + 1]
                data.append(value)

        # Saving the final result
        cne_information_by_identity_document[data[0]] = {
            "name":data[1],
            "state":data[2],
            "municipality":data[3],
            "parish":data[4],
        }

    return cne_information_by_identity_document

     
def generate_csv_report(cne_information_by_identity_document):
    print("Generating CVS Report...", "\n")
    
    # Setting csv file name
    date = str(datetime.datetime.now()).split()[0]
    BASE_DIR = Path(__file__).resolve().parent
    csv_file = os.path.join(BASE_DIR, "reports", "cne_information_" + date +".csv")
    
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Cedula", "Nombre", "Estado", "Municipio", "Parroquia"])
    
        for identity_document, data in cne_information_by_identity_document.items():
            writer.writerow([
                identity_document,
                data["name"],
                data["state"],
                data["municipality"],
                data["parish"]
            ])
    f.close()

    print(f"CSV report has been generated.\nSee the file {csv_file}")
    exit()