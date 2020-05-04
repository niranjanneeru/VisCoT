# VisCoT Telegram Chat Bot 

Symptom Checker and Global data Provider
---
___
The Python based telegram bot for using as a symptom checker and to get global data

Works along with __[Covid-19 project](https://github.com/Niranjanprof/Covid-19-Tracker)__


The project should be deployed on some server's and collects data through an API .

---

## Set-Up

```bash
$ pip install -r requirements.txt
```
---
---

## API

The **[API](https://coronavirus-tracker-api.herokuapp.com/v2/locations)** we used

The **[Repo](https://github.com/ExpDev07/coronavirus-tracker-api)** api provider

---


| Result | File | command|
|--------|------|--------|
|To get latest Global updates |      [latest.py](Covidbot/latest.py)|``` python3 latest.py ```|
|Message Manager |      [msgmanage.py](Covidbot/msgmanager.py)|``` python3 msgmanager.py ```|
|set-up file which runs in server integrates every other file | [setup.py](Covidbot/setup.py)|``` python3 setup..py ```|
|Symptom Checker | [tracker.py](Covidbot/tracker.py)|``` python3 tracker.py ```|
|Bot Class |      [bot.py](Covidbot/bot.py)|``` python3 bot.py ```|
|Configuration file give your bot token here |      [config.cfg](Covidbot/config.cfg)||


---


## Task

<ul>
  <li>'travis.yml' build status development.</li> 
  <li>Country wise data</li>
  <li>Button url's</li> 
  <li>More Options</li>
</ul>

---

## Contributors


<table>
  <tr>
    <td align="center"><a href="https://github.com/Niranjanprof"><img src="https://avatars1.githubusercontent.com/u/48713926?s=400&u=a473cb9bbbc98506ae6b55ccd2b45cfdc941d517&v=4" width="200px;" alt=""/><br /><sub><b>Niranjan B(Prof Moriarty)</b></sub></a><br /><a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=Niranjanprof" title="Code">💻</a> <a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=Niranjanprof" title="Documentation">📖</a> <a href="#maintenance-Niranjanprof" title="Maintenance">🚧</a></td>
  </tr>

</table>

---

## License & copyright

© Niranjan B 

Licensed under the [GNU GPL](LICENSE)

---

Mention This [Repo](https://github.com/Niranjanprof/VisCoT) while you use this in your projects :)
