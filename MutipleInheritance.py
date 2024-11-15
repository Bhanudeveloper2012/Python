class MIP1:
    def SC(scp):
        count=0
        for i in scp:
                count=count+1
        print(count)

class MIP2():
     def SL(self,scp2):
          print(len(scp2))

class MIC(MIP1,MIP2):
     def sl(scp2):
          count1=0
          while scp2[count1:]:
               count1=count1+1
          print(count1)


obj=MIC()
MIC.SC("Hello")

obj.SL("Villain")

MIC.sl("Hero")