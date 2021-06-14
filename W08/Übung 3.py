file = open("fabeln.txt", "r")
story = file.read()
story = story.split("\n")
story1 = open("Story1.txt","w")
story2 = open("Story2.txt", "w")
count = 1
count2 = 0
count3 = 0
while True:
    story1.write(f"{story[count]}\n")
    story2.write(f"{story[count2]}\n")
    count = count + 2
    count2 = count2 + 2
    count3 = count3 + 1
    if count3 == 15:
        break