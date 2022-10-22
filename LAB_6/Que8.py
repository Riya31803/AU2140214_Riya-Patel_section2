# Riya Patel  AU2140214

def makeNone(li):
    for i in range(len(li)):
        li[i] = None


class ServerHashTable():
    def init(self, total):
        self.total = total
        self.size = 0
        self.elements = [None]*total
        for i in range(total):
            self.elements[i] = []

    def print_hash_table(self):
        for i in range(self.total):
            print(str(i)+"==>")
            for j in range(len(self.elements[i])):
                print(str(self.elements[i][j]), end=" ")
            print()

    def insert_element(self, value):
        m = self.total
        pos = value % m
        self.elements[pos].append(value)

    def crash_servers(self, server1, server2, server3, server4):
        x = server1+server2+server3+server4
        m = self.total
        for i in range(m):
            if (i == server1):
                key = (x+(self.elements[server1][0])) % 17
                print("People of server "+str(i) +
                      " will be re-assigned to "+str(key))
                for j in range(len(self.elements[server1])):
                    self.elements[key].append(self.elements[server1][j])
                makeNone(self.elements[server1])
            elif (i == server2):
                key = (x+(self.elements[server2][0])) % 17
                print("People of server "+str(i) +
                      " will be re-assigned to "+str(key))
                for j in range(len(self.elements[server2])):
                    self.elements[key].append(self.elements[server2][j])
                makeNone(self.elements[server2])

            elif (i == server3):
                key = (x+(self.elements[server3][0])) % 17
                print("People of server "+str(i) +
                      " will be re-assigned to "+str(key))
                for j in range(len(self.elements[server3])):
                    self.elements[key].append(self.elements[server3][j])
                makeNone(self.elements[server3])

            elif (i == server4):
                key = (x+(self.elements[server4][0])) % 17
                print("People of server "+str(i) +
                      " will be re-assigned to "+str(key))
                for j in range(len(self.elements[server4])):
                    self.elements[key].append(self.elements[server4][j])
                makeNone(self.elements[server4])
            else:
                continue


h = ServerHashTable(17)
for i in range(127):
    l.insert_element(i)

h.print_hash_table()

h.crash_servers(0,1,2,3)
h.print_hash_table()