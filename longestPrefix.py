class Sol:
    def __init__(self,list):
        self.list=list
    def common_finder(self):
        sorted(list)
        f=str(list[0])
        l=str(list[-1])
        i=0
        for char in f:
            if(f[i]!=l[i]):
                return f[0:i]
            i+=1
        return f
if __name__ == '__main__':
    input_list=input("Enter a list seprated by space: ")
    list=input_list.split()
    p1=Sol(list)
    print(p1.common_finder())
