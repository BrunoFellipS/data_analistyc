import re

file = r"D:\visualcode\data_analistyc\files\0.xml"

with open(file, "r") as f:
    xml = f.read()
    
# print(xml)
xml_splited = xml.split('</line>')
# print(xml_splited)
list_escrever = []
for x in xml_splited:
    lines = re.findall(r'c=".*/>\n*', x)
    # print(lines)
    line = rf'{lines}'
    # print(line.replace('c="','').replace('"/>', ''))
    line_t1 = line.replace('c="','').replace('"/>', '')
    line_t2 = line_t1.replace(r'\n','').replace("'", '')
    line_true = line_t2.replace(r', ','').replace("[",'').replace("]",'')
    # print(line_true)
    list_escrever.append(line_true)
    
print(list_escrever)

with open('Arquivo final.txt', "w") as arquivo:
    for linha in list_escrever:
        arquivo.write(f"{linha}\n")
    arquivo.write("Arquivo escrito por Bruno Fellip para a empresa 4Docs")  
arquivo.close()

