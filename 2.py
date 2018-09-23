class Linklist():
    def __init__(self,x):
        self.val=x
        self.next=None

if __name__=="__main__":
        tmp=Linklist(5)
        tmp.next=6
        print(tmp)
        print(tmp.val,tmp.next)
