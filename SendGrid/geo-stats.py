import os
import json
import sendgrid

API_KEY = os.environ['SENDGRID_API_KEY']
sg = sendgrid.SendGridAPIClient(apikey=API_KEY)


def best_country(str_date):
    params = {'aggregated_by': 'day', 'limit': 1000,'start_date': str_date}
    response = sg.client.geo.stats.get(query_params=params)
    data = json.loads(response.body.decode('ascii'))
    max_data = max(data[0]['stats'], key=lambda a: a['metrics']['unique_clicks'])
    return max_data['name']

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
    print('Check your results')


