import csv

def  transform_user_details(csv_file_name):
    new_user_data = []
    with open("user_details.csv") as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")
        for user in user_details_csv:
            transfomation = []
            transfomation.append(user[1].replace("\n", ""))
            transfomation.append(user[2].replace("\n", ""))
            transfomation.append(user[-1].replace("\n", ""))

            new_user_data.append(transfomation)
    return new_user_data                                ## This is a list


def create_new_user_data_csv(old_user_data_file = "user_details.csv", new_filename="new_user_data.csv"):
    new_user_data = transform_user_details(old_user_data_file)

    with open(new_filename, "w") as newfile:                    # New file opened in write mode
        csvwriter = csv.writer(newfile)
        csvwriter.writerows(new_user_data)


create_new_user_data_csv()


# with open("new_user_data.csv") as file:
#     csvreader = csv.reader(file)
#
#     for row in csvreader:
#         print(row)


    # names=[]
    # for row in csvreader:
    #     names.append(row[2])
    # print(names)
    #OR
    #print(list(csvreader)[1:])
