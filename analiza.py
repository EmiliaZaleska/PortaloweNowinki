from datetime import date
import csv

sample = {
    "Robert Lewandowski":
        {
            date.fromisoformat('2019-01-12'):
                {
                    "pudelek": 1
                },
            date.fromisoformat('2019-01-05'):
                {
                    "plotek": 2
                },
        }
}


def parse_csv():
    data_dict = {}
    with open('example_data.csv') as csv_file:
        datareader = csv.reader(csv_file)
        for row in datareader:
            if datareader.line_num != 1:
                current_date, name, portal = row
                if data_dict.get(name) is None:
                    data_dict[name] = {}
                if data_dict[name].get(current_date) is None:
                    data_dict[name][current_date] = {}
                if data_dict[name][current_date].get(portal) is None:
                    data_dict[name][current_date][portal] = 1
                else:
                    data_dict[name][current_date][portal] += 1
    return data_dict

