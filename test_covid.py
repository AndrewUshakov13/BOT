import COVID19Py
covid19 = COVID19Py.COVID19()
latest = covid19.getLatest()
letest1 = covid19.getLocationByCountryCode("US")
print(latest)
print(letest1)