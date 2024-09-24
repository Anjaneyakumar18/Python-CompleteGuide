class self_demo2:

    def myfun(self):
        print("At my fun method ")

        self.myfun2() ## accessing myfun2() using obj object as self keyword is current
                      # calling instance

    def myfun2(self):
        print("At my fun2 method " ,self)
    
obj=self_demo2()
obj2=self_demo2()
obj2.myfun() ## object address of obj2 and object address of obj are different 
obj.myfun()   ## that means each object is calling myfun2() using self keyword


