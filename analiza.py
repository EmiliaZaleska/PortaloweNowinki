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
    """
    Read CSV file and return dict with more useful data format
    """
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


def get_new_tags(portal):
    # TODO do not parse every time
    today = date.today()
    data_dict = parse_csv()
    new_tags = []
    for name in data_dict:
        dates = data_dict[name]
        dates_appeared = [date_ for date_ in dates if dates[date_].get(portal) > 0]
        if dates_appeared == [today.isoformat()]:
            new_tags.append(name)
    return new_tags


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_new_tags('pudelek'))
