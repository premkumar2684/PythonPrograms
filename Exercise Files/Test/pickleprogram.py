import pickle
import traceback

#pickling
mylist1 =["prem","Jash"]
with open("data.txt","wb") as file_handle:
    pickle.dump(mylist1,file_handle,pickle.HIGHEST_PROTOCOL)
print("pickling done")    

mylist = ['a', 'b', 'c', 'd']
with open("dat.txt","wb") as fh:
    pickle.dump(mylist,fh)
#unpickling
pickle_off= open("dat.txt","rb")
emplist= pickle.load(pickle_off)
print(emplist)
traceback.print_exc(traceback,limit=None,file=None)

