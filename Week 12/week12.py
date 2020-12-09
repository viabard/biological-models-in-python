import requests
import matplotlib.pyplot as plt
import time

"""
A program that uses covid19api and datausa api to make two graphs of covid19 information via the requests and matplotlib.pyplot modules respectively.
The first graph is total, accumulative numbers, while the second graph is changes in these numbers (single day changes).

Joshua Schaaf
"""

dayone_USA_covid19 = requests.get("https://api.covid19api.com/total/dayone/country/united-states") #documentation https://documenter.getpostman.com/view/10808728/SzS8rjbc 
dayone_USA_covid19_json = dayone_USA_covid19.json()

values = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population&year=latest")
values_json = values.json()
USA_population_year = values_json.get("data")[0].get("Year")
USA_population = values_json.get("data")[0].get("Population")


active = [] 
active_pop = []
confirmed = []
confirmed_pop = []
deaths = []
deaths_pop = []
recovered = []
recovered_pop = []
dates = []
i = 0

date = dayone_USA_covid19_json[0].get("Date")
print(type(date))

for data in dayone_USA_covid19_json: #getting data
    dates.append(data.get("Date").split('T')[0])
    active.append(data.get("Active"))
    confirmed.append(data.get("Confirmed"))
    deaths.append(data.get("Deaths"))
    recovered.append(data.get("Recovered"))
    active_pop.append(active[i]/(USA_population/100000))
    confirmed_pop.append(confirmed[i]/(USA_population/100000))
    deaths_pop.append(deaths[i]/(USA_population/100000))
    recovered_pop.append(recovered[i]/(USA_population/100000))
    i+=1

d_active = []
d_confirmed = []
d_deaths = []
d_recovered = []

for i in range(len(active)): #getting change in data
    adding = 0
    if i == 0:
        adding = active[i]
        d_active.append(adding)
        adding = confirmed[i]
        d_confirmed.append(adding)
        adding = deaths[i]
        d_deaths.append(adding)
        adding = recovered[i]
        d_recovered.append(adding)
    else:
        adding = active[i]-active[i-1]
        d_active.append(adding)
        adding = confirmed[i]-confirmed[i-1]
        d_confirmed.append(adding)
        adding = deaths[i]-deaths[i-1]
        d_deaths.append(adding)
        adding = recovered[i]-recovered[i-1]
        d_recovered.append(adding)


with open("data.txt", 'w') as filething: #writing sample data to a file
    print("Writing sample data to: " + filething.name)
    filething.writelines("Total Active Cases, each a new day: ")
    for datum in active:
        filething.writelines(str(datum) + '|')
    filething.writelines("\nChange in active cases from previous day: ")
    for datum in d_active:
        filething.writelines(str(datum) + '|')
    filething.writelines("\nTotal deaths, each a new day: ")
    for datum in deaths:
        filething.writelines(str(datum) + '|')
    filething.writelines("\nDeaths per day: ")
    for datum in d_deaths:
        filething.writelines(str(datum) + '|')

#two y axis https://matplotlib.org/gallery/api/two_scales.html
#coloring for colorblindness https://davidmathlogic.com/colorblind/#%23D81B60-%231E88E5-%23FFC107-%23004D40 
fig, ax1 = plt.subplots() #first plot
ax2 = ax1.twinx()

ax1.locator_params(axis="x", nbins="10")
plt.title(label=str(time.asctime()) + " United States SARS-CoV-2: Day One Count")
plt.grid()
ax1.set_ylabel("Cases Per One-Hundered Thousand People (Pop. " + USA_population_year + ")")
ax1.set_xlabel("Days Since First US Case (" + dates[0] + ")")
ax2.set_ylabel("Deaths Per One-Hundred Thousand People (Pop. " + USA_population_year + ")", color="#004D40")
ax1.plot(active_pop, color="#1E88E5", label="Active")
ax1.plot(confirmed_pop, color="#D81B60", label="Confirmed")
ax1.plot(recovered_pop, color="#FFC107", label="Recovered")
ax2.plot(deaths_pop, color="#004D40", label="Deaths")
ax2.tick_params(labelcolor = "#004D40")
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
print("Showing United States SARS-CoV-2: Day One Count graph...")
plt.show()


fig, ax1 = plt.subplots() #second plot
ax2 = ax1.twinx()

plt.title(label=str(time.asctime()) + " United States SARS-CoV-2: Daily Changes")
ax1.set_ylabel("Daily Confirmed Cases", color="#D81B60")
ax1.set_xlabel("Days Since First US Case (" + dates[0] + ")")
ax2.set_ylabel("Daily Deaths", color = "#004D40")
ax2.plot(d_deaths, color="#004D40", label="Deaths")
ax2.tick_params(axis='y', labelcolor="#004D40")
ax1.plot(d_confirmed, color="#D81B60", label="Confirmed")
ax1.tick_params(axis='y', labelcolor="#D81B60")
#ax1.set_facecolor("grey")
ax1.legend(loc = "upper left")
ax2.legend(loc="upper right")
print("Showing United States SARS-CoV-2: Daily Changes graph...")
plt.show()

print("Getting Description (Sometimes takes a while, probably because of cheap hosting...)")
description = requests.get("https://joshschaaf.com/fall_2020/api_description.txt")
print(description.text)
#maybe do this https://www.signalingpathways.org/docs/ in the future
input("Press enter to quit.")