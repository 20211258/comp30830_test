import platform, multiprocessing, psutil, socket

def showinfo(tip, info):
    print("{}:{}".format(tip, info))


showinfo("Name of machine: ",platform.node())
showinfo("operating system name: ",platform.system())
showinfo("operating system version: ",platform.version())
showinfo("number of cup",multiprocessing.cpu_count())
showinfo("amount of memory",psutil.virtual_memory().total)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
showinfo("IP address: ",ip)
