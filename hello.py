from datetime import datetime

print("hello git!!")

output = "output/sample_{}.txt".format(datetime.now())
with open(output, "w") as f:
    f.write("this is a sample output file.\n")
    f.write(str(datetime.now()))