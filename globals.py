USER_DIR = "userdata/"
GEN_DIR = "gens/"

trusteds = []
with open("trustedusers.txt") as f:
    for line in f.readlines():
        trusteds.append(line.split(" #")[0])