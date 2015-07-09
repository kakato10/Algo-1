from datetime import datetime


def get_priority(protocol):
    priorities = {
        "ICMP": 6,
        "UDP": 5,
        "RTM": 4,
        "IGMP": 3,
        "DNS": 2,
        "TCP": 1
    }
    return priorities[protocol]


class Package():
    def __init__(self, protocol, payload):
        self.protocol = protocol
        self.payload = payload
        self.priority = get_priority(protocol)
        self.date = datetime.now()

    def get_protocol(self):
        return self.protocol

    def get_payload(self):
        return self.payload

    def get_priority(self):
        return self.priority

    def get_date(self):
        return self.date


class BandwidthManager():
    def __init__(self):
        self.heap = []

    def recieve(self, package):
        self.heap.append(package)
        i = len(self.heap) - 1
        parent_index = int((i - 1) / 2)
        package_priority = package.get_priority()
        parent_priority = self.heap[parent_index].get_priority()
        while not i == 0 and package_priority > parent_priority:
            self.swap(i, parent_index)
            i = parent_index
            parent_index = int((i - 1) / 2)
            parent_priority = self.heap[parent_index].get_priority()
# implement date comparison here and in self.send
        # while not i == 0 and package_priority == parent_priority and package.get_date() < :

    def send(self):
        if len(self.heap) == 0:
            print("All packages were sent")
            return False
        self.swap(0, len(self.heap) - 1)
        root = self.heap[-1]
        del self.heap[-1]
        item_index = 0
        left_child = item_index * 2 + 1
        right_child = item_index * 2 + 2
        while left_child < len(self.heap):
            if right_child < len(self.heap):
                if self.heap[left_child].get_priority() < self.heap[right_child].get_priority():
                    compare_to = left_child
                else:
                    compare_to = right_child
            else:
                compare_to = left_child
            if self.heap[item_index].get_priority() < self.heap[compare_to].get_priority():
                self.swap(item_index, compare_to)
            else:
                break
            item_index = compare_to
            left_child = item_index * 2 + 1
            right_child = item_index * 2 + 2
        print(root.get_payload())

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp


def main():
    manager = BandwidthManager()
    while True:
        command = input("Enter command> ")
        if command == "send":
            manager.send()
        elif command[:3] == "rcv":
            command = command.split(" ")
            package = Package(command[1], command[2])
            manager.recieve(package)
        else:
            break
if __name__ == '__main__':
    main()
