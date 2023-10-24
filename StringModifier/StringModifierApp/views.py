from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HomePage(request):
    return render(request,'HomePage.html')




def AssignValue(request):

    global CurValRemovePuncution
    global CurValCaptilizeFirst
    global CurValNewLineRemover
    global CurValSpaceRemover
    global CurValCharCount
    global PunctuationCharacters
    global Data
    global CharCount 

    CurInput = request.POST.get('InputText','')
    CurValRemovePuncution = request.POST.get('RemovePunctution','off')
    CurValCaptilizeFirst = request.POST.get('CaptilizeFirst','off')
    CurValNewLineRemover = request.POST.get('NewLineRemover','off')
    CurValSpaceRemover = request.POST.get('SpaceRemover','off')
    CurValCharCount = request.POST.get('CharCount','off')
    CharCount =-1

    PunctuationCharacters = [',', '.', '?', '!', ':', ';', '-', '_', '"', '\'', '(', ')', '[', ']', '{', '}']
    Data ={
            "flag":False,
            "input":CurInput,
            "Result" : CurInput,
            "CharCount": CharCount,
        }

def RmvPuchOp(CurInput):
    FinalString=""
    for CurChar in CurInput:
        IsFound = False
        for Punch in PunctuationCharacters:
            if CurChar == Punch:
                IsFound=True
                break
        if IsFound == False:
            FinalString+=CurChar

    Data['Result']=FinalString

def CapFstOp(CurInput):
    FinalString=""
    PrevSafe = False
    for CurChar in CurInput:
        if (PrevSafe == False) and (CurChar<='z' and CurChar >='a'):
            PrevSafe = True
            FinalString+=chr(ord(CurChar)-ord('a')+ord('A')) 
            continue   
        if CurChar in(' ','\n','\b'):
            PrevSafe = False;
        FinalString +=CurChar 
    Data['Result']=FinalString                

def NwLneRmvOp(CurInput):   
    FinalString=""
    PreStatus = True
    for CurChar in CurInput:
        if CurChar =='\n' or CurChar =='\r':
            if PreStatus == True:
                continue
            PreStatus = True
        else:
            PreStatus = False    
        FinalString+=CurChar    
    
    Data['Result']=FinalString 

def SpcRmvOp(CurInput):
    FinalString=""
    PrevSafe = False
    for CurChar in CurInput:
        if (PrevSafe == False) and (CurChar == ' ') :
            continue   

        if CurChar in(' ','\n','\b'):
            PrevSafe = False;
        else:
            PrevSafe = True
        
        FinalString +=CurChar 
    Data['Result']=FinalString 

def CrCntOp(CurInput):
    CharCount =0
    for CurCur in CurInput:
        CharCount+=1
    Data['CharCount']=CharCount    
    
def StringOperations(request):
    AssignValue(request)
    if Data['input'] != "":
        if CurValRemovePuncution == 'on':
            RmvPuchOp(Data['Result'])
        if CurValCaptilizeFirst == 'on':
            CapFstOp(Data['Result']) 
        if CurValNewLineRemover == 'on':
            NwLneRmvOp(Data['Result'])   
        if CurValSpaceRemover == 'on':
            SpcRmvOp(Data['Result'])   
        if CurValCharCount =='on':
            CrCntOp(Data['Result'])      
        Data['flag'] = True
        
     
    return render(request,'HomePage.html',Data)

