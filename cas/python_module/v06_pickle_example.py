import cPickle

a_dict = {"Jess":"079 778 4565","Pete":"079 123 1234"}
a_list = ["Hello", "World", "!"]

pickle_file = open('test.pkl','wb') #open to write binary
cPickle.dump(a_dict, pickle_file, cPickle.HIGHEST_PROTOCOL)
cPickle.dump(a_list, pickle_file, cPickle.HIGHEST_PROTOCOL)
pickle_file.close()

pickle_file = open('test.pkl','rb') #open to read binary
a_dict_loaded = cPickle.load(pickle_file) # same load sequence as dump
a_list_loaded = cPickle.load(pickle_file)
pickle_file.close()

print a_dict, a_list
print 'Pickled and unpickled to get:'
print a_dict_loaded, a_list_loaded
