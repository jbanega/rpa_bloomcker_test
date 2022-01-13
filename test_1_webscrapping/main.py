from utils import (generate_list_of_identity_document,
                  retrieve_cne_information_from_web,
                  generate_csv_report)


def main():
    program_title = "REPORT GENERATOR OF CNE INFORMATION BASED ON IDENTITY DOCUMENT NUMBER"
    cne_url = "http://www.cne.gob.ve/"
    print(program_title.center(75, "*"))
    print("Source: ", cne_url, "\n")

    list_of_identity_document = generate_list_of_identity_document()
    cne_information_by_identity_document = retrieve_cne_information_from_web(list_of_identity_document, cne_url)
    generate_csv_report(cne_information_by_identity_document)


if __name__ == "__main__":
    main()