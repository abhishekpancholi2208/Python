class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head=None
	def insert_at_begining(self, data):
		node = Node(data,self.head)
		self.head=node
	def print(self):
		if self.head is None:
			print("Linked List is empty")
			return
		itr = self.head
		llist=[]
		while itr:
			llist=llist+[int(itr.data)]
			itr=itr.next
		print(llist)
	def insert_at_end(self,data):
		if self.head==None:
			self.head=Node(data,None)
			return
		itr=self.head
		while itr.next:
			itr=itr.next
		itr.next=Node(data, None)
	def insert_values(self,data_list):
		for data in data_list:
			self.insert_at_end(data)
	def get_length(self):
		count=0
		itr=self.head
		while itr.next:
			count=count+1
			itr=itr.next
		return count
	def remove_at(self,index):
		if index<0 or index>=self.get_length():
			raise Exception("Index out of range")
		if index==0:
			self.head=self.head.next
			return
		count=0
		itr=self.head
		while itr:
			if count == index-1:
				itr.next=itr.next.next
				break
			itr=itr.next
			count+=1
	def insert_at(self,index, data):
		if index<0 or index>=self.get_length():
			raise Exception("Index out of range")
		if index==0:
			self.insert_at_begining(data)
			return
		count=0
		itr=self.head
		while itr:
			if count == index-1:
				temp=Node(data,itr.next)
				itr.next=temp
				break
			count+=1
			itr=itr.next
	def insert_after_value(self,data_after, data_to_insert):
		itr=self.head
		while itr:
			if itr.data==data_after:
				node=Node(data_to_insert,itr.next)
				itr.next=node
				return
			itr=itr.next
		raise Exception("Data Not Found")
	def remove_by_value(self,data):
		itr=self.head
		backtrack=itr
		while itr:
			if itr.data == data:
				backtrack.next=itr.next
				itr=backtrack
				return
			backtrack=itr
			itr=itr.next




if __name__ == '__main__':
	ll=LinkedList()
	ll.insert_at_begining(5)
	ll.insert_at_begining(4)
	ll.insert_at_begining(3)
	ll.insert_at_begining(2)
	ll.insert_at_begining(1)
	ll.print()
	ll.insert_at_end(6)
	ll.insert_at_end(7)
	ll.insert_at_end(8)
	ll.insert_at_end(9)
	ll.print()
	ll.insert_values([10,11,12,13,14,15,16])
	ll.print()
	print(ll.get_length())
	ll.remove_at(6)
	ll.remove_at(4)
	ll.remove_at(2)
	ll.remove_at(0)
	ll.remove_at(8)
	ll.print()
	ll.insert_at(0, 1)
	ll.insert_at(2, 3)
	ll.insert_at(4, 5)
	ll.insert_at(6, 7)
	ll.insert_at(12, 13)
	ll.print()
	ll.insert_after_value(2, 4)
	ll.insert_after_value(4, 8)
	ll.insert_after_value(1, 3)
	ll.insert_after_value(4, 9)
	ll.insert_after_value(10, 40)
	ll.print()
	ll.remove_by_value(2)
	ll.remove_by_value(4)
	ll.remove_by_value(6)
	ll.remove_by_value(7)
	ll.remove_by_value(9)
	ll.print()
