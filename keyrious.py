import os
def game():
    return 18

def save_top5(top5, filename="score.txt"):
    file = open(filename, "w")
    for score, name in top5:
        file.write("%s,%s\n"%(score,name))
        file.close

def load_top5(filename="score.txt"):
    if not os.path.isfile(filename):
        return[]
    file = open(filename,"r")
    top5 = []
    while 1:
        line =file.readline()
        line = line.replace('\n','')
        print("load_top5 readline: "+ str(line))
        if len(line)<2:
            break
        datas =line.split(',')
        datas[0]= int(datas[0])
        top5.append(datas)
    file.close()
    return top5

def find_rank(top5, score):
    i = 0
    while i < len(top5):
        score, name= top5[]
        

def
test = [[12,"Albert"], [16, "Francis"]]
save_top5(test)
test2 = load_top5()
print(test2)

place("Francis")