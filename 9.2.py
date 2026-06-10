capitals ={"India":"New Delhi",
           "USA":"Washington DC",
           "China":"Beiging",
           "Russia":"Moscow"}
capitals.update({"Switzerland":"Bern"})
capitals.update({"USA":"Las Angels"})
capitals.pop("China")
capitals.clear()
print(capitals["Switzerland"])
print(capitals.get("Switzerland"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
for key,value in capitals.items():
    print(key,value)