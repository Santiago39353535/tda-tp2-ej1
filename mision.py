import sys

people = []
f = open(sys.argv[1], "r")
for x in f:
  person = x.split(",")
  people.append(
    {
        "name":person[0],
        "weight":int(person[1]),
        "value":int(person[2])
    },
  )
maxPeople = int(sys.argv[2])
weight = int(sys.argv[3])


opt = []

for i in range(len(people)+1):
    a = []
    for j in range(maxPeople+1):
        b = []
        for k in range(weight+1):
            b.append(
                {
                    "name":'',
                    "weight":0,
                    "value":0
                },
            )
        a.append(b)
    opt.append(a)



for i in range(1,len(people)+1):
    for p in range(1,maxPeople+1):
        for k in range(1,weight+1):
            no_optime = opt[i-1][p][k]
            in_optime = {
                "value":float('-inf'),
            }
            if people[i-1]["weight"] <= k:
                value = {
                    "name":opt[i-1][p-1][k-people[i-1]["weight"]]["name"] + ', ' + people[i-1]["name"],
                    "value":people[i-1]["value"] + opt[i-1][p-1][k-people[i-1]["weight"]]["value"],
                    "weight":people[i-1]["weight"] + opt[i-1][p-1][k-people[i-1]["weight"]]["weight"],
                }
                in_optime = value #people[i-1]["value"] +  opt[i-1][p-1][k-people[i-1]["weight"]]
            if in_optime["value"]>no_optime["value"]:
                opt[i][p][k] = in_optime
            else:
                opt[i][p][k] = no_optime

print(opt[len(people)][maxPeople][weight])