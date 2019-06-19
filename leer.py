fo = open("test.conf", "r+")
parameters = []
lines = fo.readlines()
for line in lines:
    parameters += [eval(line)]
fo.close()
