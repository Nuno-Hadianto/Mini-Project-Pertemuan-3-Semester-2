RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

class Node_Scooter:
    def __init__(self, id_scooter, nama_scooter):
        self.id_scooter = id_scooter
        self.nama_scooter = nama_scooter
        self.next = None

    def __str__(self):
        return f"ID: {self.id_scooter}, Nama Part Scooter: {self.nama_scooter}"


class LinkedList:
    def __init__(self):
        self.head = None

    def quicksort(self, head):
        if head is None or head.next is None:
            return head

        pivot = head.id_scooter
        left_head = left_tail = Node_Scooter(0, 0)
        equal_head = equal_tail = Node_Scooter(0, 0)
        right_head = right_tail = Node_Scooter(0, 0)

        current = head
        while current is not None:
            if current.id_scooter <  pivot: # biar bisa ascending : besar kecil < habistu descending kecil ke besar >
                left_tail.next = current
                left_tail = current
            elif current.id_scooter == pivot:
                equal_tail.next = current
                equal_tail = current
            else:
                right_tail.next = current
                right_tail = current
            current = current.next

        left_tail.next = None
        equal_tail.next = None
        right_tail.next = None

        left_head = self.quicksort(left_head.next)
        right_head = self.quicksort(right_head.next)

        if left_head:
            head = left_head
            left_tail.next = equal_head.next
        else:
            head = equal_head.next

        equal_tail.next = right_head

        return head

    def insert_at_end(self, head, id_scooter, nama_scooter):
        new_node = Node_Scooter(id_scooter, nama_scooter)
        if head is None:
            return new_node

        current = head
        while current.next is not None:
            current = current.next

        current.next = new_node
        return head

    def menambah_di_awalan(self, id_scooter, nama_scooter):
        new_node = Node_Scooter(id_scooter, nama_scooter)
        new_node.next = self.head
        self.head = new_node

    def menambah_di_akhiran(self, id_scooter, nama_scooter):
        new_node = Node_Scooter(id_scooter, nama_scooter)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def menambah_di_antara_node(self, id_scooter, nama_scooter, position):
        if position < 0:
            print("posisi pemilihan diantara node tidak valid.")
            return
        if position == 0:
            self.menambah_di_awalan(id_scooter, nama_scooter)
            return
        new_node = Node_Scooter(id_scooter, nama_scooter)
        current = self.head
        for i in range(position - 1):
            if current:
                current = current.next
            else:
                print("posisi pemilihan diantara node tidak valid.")
                return
        if not current:
            print("posisi pemilihan diantara node tidak valid.")
            return
        new_node.next = current.next
        current.next = new_node

    def menghapus_node(self, id_scooter):
        current = self.head
        if current and current.id_scooter == id_scooter:
            self.head = current.next
            return
        while current.next and current.next.id_scooter == id_scooter:
            current.next = current.next.next
            return
        print(f"Node dengan id scooter {id_scooter} tidak ada.")

    def display(self):
        current = self.head
        while current:
            print(current, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()

# Untuk menambahkan node di awal, di akhir, dan sesuai posisi yang diinginkan diantara node tersebut
print(BOLD + GREEN + "Node yang sudah tertambah: ")
print("====================================================================================================")
linked_list.menambah_di_awalan(1, "Pulley")
linked_list.menambah_di_awalan(4, "ECU")
linked_list.menambah_di_akhiran(9, "Roller")
linked_list.menambah_di_akhiran(2, "Injector")
linked_list.menambah_di_akhiran(3, "Busi")
# linked_list.menambah_di_antara_node(4, "Beat", 0)  # sesuai posisi 0 1 2 3 4 seterusnya
linked_list.display()
print("====================================================================================================")

# Untuk menghapus node
# print("Node yang sudah terhapus: ")
# print("====================================================================================================")
# # linked_list.menghapus_node(4)  # Contoh penghapusan berdasarkan id
# # linked_list.display()
# print("====================================================================================================")

# buat sorting
print("Node yang sudah tersorting: ") #baris 35 < >
print("====================================================================================================")
linked_list.head = linked_list.quicksort(linked_list.head)
linked_list.display()
print("====================================================================================================")
