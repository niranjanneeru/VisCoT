import requests

def latest():
    try:
        # Collects Data from the api
        response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations?timelines=true')
    except:
        return '''Bad Connection'''
# Converts to python dictionary
    data = response.json()

    confirmed = data['latest']['confirmed']
    deaths = data['latest']['deaths']
    last_updated = data['locations'][0]['last_updated'][:10]

    msg = f"Global Covid Data as last updated on {last_updated}\n\nConfirmed Cases:  {confirmed:,}\nDeath Toll: {deaths:,}"
    print(msg)
    return msg
latest()