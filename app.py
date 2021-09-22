from SList import SList
from SLNode import SLNode

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!

testList = SList()
testList.insert_at("first",0).insert_at("second",1).insert_at("second",1).insert_at("last",3).print_values()
print(f"removed value {testList.remove_from_front()}")
testList.print_values()
print(f"removed value {testList.remove_from_back()}")
testList.print_values()
testList.remove_val("second").print_values()


