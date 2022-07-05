student=[
{"name": "Joseph","score":85},
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for e in student:
    if e['score'] >= 80:
        for key,vale in e.items():
            print(key,vale,'ได้เกรด4')
    elif e['score'] >= 70:
        for key,vale in e.items():
            print(key,vale,'ได้เกรด3')
    elif e['score'] >= 60:
        for key,vale in e.items():
            print(key,vale,'ได้เกรด2')    
    elif e['score'] >= 50:
        for key,vale in e.items():
            print(key,vale,'ได้เกรด1')
    else:
        for key,vale in e.items():
            print(key,vale,'ได้เกรด0') 
#นายรัฐนันท์ ถิรพัฒนานนท์ เลขที่20 ชั้น ม.6/14                     