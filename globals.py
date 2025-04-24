import websockets

# this files a little USEFUL
fdtrusteds = [1089345596499951719,1214634114125271040,1196631678584623117,1213964198468526253,1101301651022827550]
sock: websockets.ClientConnection = None
connected_channel_id = 0

FILE_DIR = "filedb/"
GEN_DIR = "gens/"

trusteds = []
with open("trustedusers.txt") as f:
    for line in f.readlines():
        trusteds.append(line.split(" #")[0])