import csv


input = {
  "0": {
    "desired_bed_cleanup": True,
    "has_dry_leaves": True,
    "has_wet_leaves": True,
    "has_fallen_limbs": False,
    "has_cut_limbs": False,
    "has_rocks": True,
    "has_mulch": True,
    "has_pine": False,
    "has_pet_waste": False,
    "has_other": True,
    "has_cement": False,
    "has_acorns": True,
    "has_pine_cones": False,
    "other_debris": "this is a description of the other types of debris I have",
    "last_service": "8_to_12_weeks",
    "desired_haulaway": True,
    "details": "these are some details"
  },
  "1": {
    "desired_bed_cleanup": False,
    "has_dry_leaves": True,
    "has_wet_leaves": True,
    "has_fallen_limbs": False,
    "has_cut_limbs": False,
    "has_rocks": False,
    "has_mulch": True,
    "has_pine": False,
    "has_pet_waste": False,
    "has_other": True,
    "has_cement": True,
    "has_acorns": True,
    "has_pine_cones": False,
    "other_debris": "this is a description of the other types of debris I have",
    "last_service": "1_to_2_weeks",
    "desired_haulaway": False,
    "details": "details"
  }
}

def printCSV():
    csv_list = []

    for key in input:
        csv_list.append(input[key]) 

    # print(csv_list)
    
    #mycsv = open('mycsvfile.csv', 'w')
    #f = csv.writer(mycsv)
    #for i in csv_list:
      #  f.writerow(i)
    #mycsv.close();    


    with open('mycsvfile.csv', 'w', newline='') as csvfile:
        fieldnames = csv_list[0].keys()
        #values = csv_list[0].values()
        #print(fieldnames)
        #print(values)
        writer = csv.DictWriter(csvfile, quoting= csv.QUOTE_ALL, fieldnames=fieldnames)
        writer.writeheader()
        csv_dict = csv_list[0]
        for csv_dict in csv_list:
            print(csv_dict)
            print('___"," '.join(csv_dict))
            #writer.writerow(csv_dict)
            writer.writerow(csv_dict)
printCSV()