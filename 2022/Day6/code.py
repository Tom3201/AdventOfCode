with open("data.txt") as f:
    data = f.read().splitlines()


def getPacketLength(packetLength):
    for line in data:
        packet = []
        for a, char in enumerate(line):
            if len(packet) >= packetLength:
                print(a)
                break
            while char in packet:
                packet = packet[1:]
            packet.append(char)


#Part1
getPacketLength(4)


#Part2
getPacketLength(14)