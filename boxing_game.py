from typing import Dict

karekter1 = {"adı": "Muhammet Ali Klay",
             "canı": 100,
             "silah": "sol kroşe",
             "gücü": 100}
print("Boksörün adı : ",karekter1["adı"])
print("Boksörün canı :", karekter1["canı"])
print("Boksörün silahı :", karekter1["silah"])
print("Boksörün gücü :", karekter1["gücü"])
print("================fight======================")
karekter2 = {"adı": "Jason Mamoa",
             "canı": 100,
             "silah": "sağ kroşe",
             "gücü": 90}
print("Boksörün adı : ",karekter2["adı"])
print("Boksörün canı :", karekter2["canı"])
print("Boksörün silahı :", karekter2["silah"])
print("Boksörün gücü :", karekter2["gücü"])

def vur(vuran: dict, vurulan: dict):
    eksilen = vuran["gücü"]
    vurulan["canı"] = vurulan["canı"] - eksilen


vur(karekter1,karekter2)
vur(karekter2,karekter1)
print("==================nakavt====================")

print("Karekter 1'in kalan canı :", karekter1["canı"])
print("Karekter 2' nin kalan canı :", karekter2["canı"])
print("sonuç...")
print("Karekter 2 allahına kavuştu.")
