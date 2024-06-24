input_file = open("royal.ged")
output_file = open("Family.pl", "w")
lines = input_file.readlines()
Id = []
Names = []

for line in lines:
    if line.find("INDI") != -1:
        words = line.split()
        id = words[1]
        Id += [id]
        Names += [id]
    if line.find("GIVN") != -1:
        words = line.split()
        name = words[2]
        for i in range (3, len(words), 1):
            name += " " + words[i]
        name=name.replace(". ", ".")
        Names[len(Names) - 1] = name + " " + Names[len(Names) - 1]
    if line.find("SURN") != -1:
        words = line.split()
        surname = words[2]
        for i in range (3, len(words), 1):
            surname += " " + words[i]
        surname=surname.replace(". ", ".")
        Names[len(Names) - 1] = surname

for ind in range(len(Names)-1,-1,-1):
    l = Names.count(Names[ind])
    if l>1:
        Names[ind]+= " " + str(l)

husb = -1
wife = -1
ind = 0
for line in lines:
    if line.find("FAM") != -1:
        husb = -1
        wife = -1
    if line.find("HUSB") != -1:
        words = line.split()
        husb = words[2]
    if line.find("WIFE") != -1:
        words = line.split()
        wife = words[2]
    if line.find("CHIL") != -1:
        words = line.split()
        child = words[2]
        if husb != -1 and Names[Id.index(husb)].find("@") != -1:
            continue
        if wife != -1 and Names[Id.index(wife)].find("@") != -1:
            continue
        if Names[Id.index(child)].find("@") != -1:
            continue
        if husb != -1 and wife != -1:
            ind = ind + 1
            output_file.write("parents(\'" + Names[Id.index(child)] +  "\', \'" + Names[Id.index(husb)] + "\', \'" + Names[Id.index(wife)] + "\').")
            output_file.write("\n")
        elif husb != -1:
            output_file.write("parents(\'" + Names[Id.index(child)] + "\', \'" + Names[Id.index(husb)] + "\', \'" + "NULL" + "\').")
            output_file.write("\n")
        elif wife != -1:
            output_file.write("parents(\'" + Names[Id.index(child)] + "\', \'" + "NULL" + "\', \'" + Names[Id.index(wife)] + "\').")
            output_file.write("\n")
        else:
            output_file.write("parents(\'" + Names[Id.index(child)] + "\', \'" + "NULL" + "\', \'" + "NULL" + "\').")
            output_file.write("\n")
            

input_file.close()
output_file.close()
