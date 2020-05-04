import requests


def convert(number):
    accum = 0
    numbers = number.split(',')
    for i in numbers:
        accum = accum * 1000 + int(i)
    return accum


def latest():
    try:
        info = requests.get('https://www.worldometers.info/coronavirus/').text
    except:
        return "BAD Connection"

    lines = info.split('\n')
    flag = 0
    comfirmed = ''
    recovered = ''
    death = ''
    for line in lines:
        if flag == 1:
            flag = 0
            words = line.split('>')
            recovered = words[1].split('<')[0]
        if line.startswith('<title>'):
            words = line.split()
            confirmed = words[words.index('Cases') - 1]
            death = words[words.index('Deaths') - 1]

        if line.startswith('<div class="maincounter-number" style="color:#8ACA2B ">'):
            flag = 1

    active = (convert(confirmed) - convert(death) - convert(recovered))
    msg = f"Global Covid Data\n\nConfirmed Cases:  {confirmed}\nDeath Toll: {death}\nRecovered Cases:  {recovered}\nActive:     {(convert(confirmed) - convert(death) - convert(recovered)):,}"
    return msg