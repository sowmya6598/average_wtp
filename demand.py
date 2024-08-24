import csv

with open('data.csv', mode ='r') as file:
    csv_file = list(csv.DictReader(file))
    
def get_average_wtp(category, segment_one, segment_two):

    segment_one_total = 0
    segment_one_count = 0

    segment_two_total = 0
    segment_two_count = 0

    for line in csv_file:
        if line[category] == segment_one:
            segment_one_total += int(line['WTP'])
            segment_one_count += 1
        else: 
            segment_two_total += int(line['WTP'])
            segment_two_count += 1

    print(f"Category: {category} || {segment_one}: {round(segment_one_total / segment_one_count, 2)} || {segment_two}: {round(segment_two_total / segment_two_count, 2)}")


# get_average_wtp('If_rafted_before', 'Yes', 'No')
# get_average_wtp('If_camped_before', 'Yes', 'No')
# get_average_wtp('If_rode_horse_before', 'Yes', 'No')
# get_average_wtp('Gender', 'F', 'M')
# get_average_wtp('Marital_status', 'Single', 'Married')


def get_average_wtp_age():

    young_total = 0
    young_count = 0

    old_total = 0
    old_count = 0

    for line in csv_file:
        if int(line['Age']) <= 25:
            young_total += int(line['WTP'])
            young_count += 1
        else: 
            old_total += int(line['WTP'])
            old_count += 1

    print(f"Category: Age || <=25 : {round(young_total / young_count, 2)} || >25: {round(old_total / old_count, 2)}")

get_average_wtp_age()
