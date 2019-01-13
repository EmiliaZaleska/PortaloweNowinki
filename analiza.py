from datetime import date, timedelta
import csv
import matplotlib.pyplot as plt

# sample = {
#     "Robert Lewandowski":
#         {
#             date.fromisoformat('2019-01-12'):
#                 {
#                     "pudelek": 1
#                 },
#             date.fromisoformat('2019-01-05'):
#                 {
#                     "plotek": 2
#                 },
#         }
# }


def parse_csv(filename):
    """
    Read CSV file and return dict with more useful data format
    """
    data_dict = {}
    with open(filename) as csv_file:
        datareader = csv.reader(csv_file)
        for row in datareader:
            if datareader.line_num != 1:
                current_date, name, portal = row
                current_date = date.fromisoformat(current_date)
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
    data_dict = parse_csv('example_data.csv')
    new_tags = []
    for name in data_dict:
        dates = data_dict[name]
        dates_appeared = [date_ for date_ in dates.keys() if dates[date_].get(portal)]
        if dates_appeared == [today]:
            new_tags.append(name)
    return new_tags


def get_popular_tags():
    # TODO do not parse every time
    data_dict = parse_csv('example_data.csv')
    popular_tags = []
    for name in data_dict:
        appeared_in_portals = set()
        dates = data_dict[name]
        for date_ in dates:
            portals = dates[date_]
            for portal in portals:
                if dates[date_][portal] > 0:
                    appeared_in_portals.add(portal)
        if len(appeared_in_portals) >= 3:
            popular_tags.append(name)
    return popular_tags


def plot_tags(tag_list):
    # TODO do not parse every time
    data_dict = parse_csv('example_data.csv')
    dates = []
    for tag in tag_list:
        dates.extend(data_dict[tag].keys())
    first_date = min(dates)
    last_date = max(dates)
    days = (last_date - first_date).days
    x = [first_date + timedelta(days=days_to_add) for days_to_add in range(days + 1)]
    fig, ax = plt.subplots()
    for tag in tag_list:
        y = []
        for date_ in x:
            appearances = data_dict[tag].get(date_)
            if appearances is None:
                y.append(0)
            else:
                y.append(sum(appearances.values()))

        ax.plot(x, y, label=tag)
        ax.set(xlabel='data', ylabel='popularność')

    ax.legend()
    plt.show()


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_popular_tags())
    pprint(get_new_tags('pudelek'))
    plot_tags(['Dżoana Krupa', 'Anna Lewandowska', 'Robert Lewandowski'])
