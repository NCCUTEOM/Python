#利用excel的Write/Read寫一個行事曆，可以儲存 ["日期"],["時 間"],["人 員"],["地 點"],["事 項"],["內 容"]，
# coding: utf-8

# In[ ]:

import pandas as pd
import os 

filepath='df.csv'
if os.path.isfile(filepath):
    df=pd.read_csv('df.csv')


    #with open ('df.csv',newline='') as csvfile:
        #rows = csv.reader(csvfile)#若路徑檔案存在自動開啟
    

else:
    date=[]
    time=[]
    ppl=[]
    place=[]
    event=[]
    content=[]
    df=pd.DataFrame()
            
    df["日 期"]=date
    df["時 間"]=time
    df["人 員"]=ppl
    df["地 點"]=place
    df["事 項"]=event
    df["內 容"]=content

    
a =0#自由控制迴圈進出
#df.reset_index()
        
while a==0:
    a=input('請輸入進行的動作之代碼，1新增資料，2刪除資料，3查詢資料，4瀏覽所有資料，5離開')
    if a!='1' and a!='2' and a!='3' and a!='4' and a!='5':
        print('請輸入正確數字')
        a=0
        
    while a=='1':
        when=input('請輸入日期，例如190617')
        hour=input('請輸入時間，例如1030')
        if when.isdecimal() and hour.isdecimal():
            who=input('請輸入相關人員')
            where=input('請輸入地點')
            what=input('請輸入事項')
            how=input('請輸入內容大綱')
            
            """
            date.append(when)
            time.append(hour)
            ppl.append(who)
            place.append(where)
            event.append(what)
            content.append(how)
            """
            
            df2 = pd.DataFrame({
                    "日 期":  [when],
                    "時 間":  [hour],
                    "人 員":  [who],
                    "地 點": [where],
                    "事 項": [what],
                    "內 容": [how],
                })
            
           
            """
            df2["日 期"]=date
            df2["時 間"]=time
            df2["人 員"]=ppl
            df2["地 點"]=place
            df2["事 項"]=event
            df2["內 容"]=content

            df=pd.DataFrame()
            
            df["日 期"]=date
            df["時 間"]=time
            df["人 員"]=ppl
            df["地 點"]=place
            df["事 項"]=event
            df["內 容"]=content
            """
            
            df = df.append(df2)
            df= df.reset_index(drop=True)

            #df.reset_index()
            print(df)
            a=0

            break
        else:
            print("請輸入正確數字")
            

    while a=='2':
    
        b=input('請輸入欲刪除之項目，1日期，2人員，3地點，4事項')
        if b=='1':
             while True:  
                  deltime=input('請輸入欲搜尋日期:')
                  #if deltime in date:
                  #print(df['日 期'])
                  #print(list(df['日 期']))
                  #print(deltime in df['日 期'])
                  if deltime in list(df['日 期']):                      
                       #del1=[]
                       #del1.append(deltime)
                       is_trio=df['日 期'].isin([deltime])     
                       print(df[is_trio])     
                       delcode=input('請輸入要刪除之資料代碼')     
                       df=df.drop([int(delcode)])     
                       print('刪除成功')
                       a=0
                       break     
                  else:
                       print('請輸入正確日期')
            
             
             
                  
        elif b=='2':
            while True:
                 delppl=input('請輸入欲搜尋人員:')
                 #print(df['人 員'])
                 #print(list(df['人 員']))
                 if delppl in list(df['人 員']):
                      #del2=[]
                      #del2.append(delppl)
                      is_trio=df['人 員'].isin([delppl])
                      print(df[is_trio])
                      delcode2=input('請輸入要刪除之資料代碼')
                      df=df.drop([int(delcode2)])
                      print('刪除成功')
                      a=0
                      break
                 else:
                      print('請輸入正確人員')
        elif b=='3':
            while True:
                 delplace=input('請輸入欲搜尋地點:')
                 #print(df['地 點'])
                 #print(list(df['地 點']))
                 if delplace in list(df['地 點']):
                      #del3=[]
                      #del3.append(delplace)
                      is_trio=df['地 點'].isin([delplace])
                      print(df[is_trio])
                      delcode3=input('請輸入要刪除之資料代碼')
                      df=df.drop([int(delcode3)])
                      print('刪除成功')
                      a=0
                      break
                 else:
                      print('請輸入正確地點') 
        elif b=='4':
            while True:
                 delevent=input('請輸入欲搜尋事項:')
                 #print(df['事 項'])
                 #print(list(df['事 項']))
                 if delevent in list(df['事 項']):
                      #del4=[]
                      #del4.append(delevent)
                      is_trio=df['事 項'].isin([delevent])
                      print(df[is_trio])
                      delcode4=input('請輸入要刪除之資料代碼')
                      df=df.drop([int(delcode4)])
                      print('刪除成功')
                      a=0
                      break
                 else:
                      print('請輸入正確事項')
          
        else:
            print('請輸入正確代碼')

    while a=='3':#同a==2的例子
    
        c=input('請輸入欲搜尋之項目，1日期，2人員，3地點，4事項')
        if c=='1':
             while True:
                  searchtime=input('請輸入欲搜尋之日期')
                  if searchtime in list(df['日 期']):
                      #search1=[]
                      #search1.append(searchtime)
                      is_trio=df['日 期'].isin([searchtime])
                      print(df[is_trio])
                      a=0
                      break
                  else:
                      print('請輸入正確日期') 
           
        elif c=='2':
             while True:
                  searchppl=input('請輸入欲搜尋人員:')
                  if searchppl in list(df['人 員']):
                      #search2=[]
                      #search2.append(searchppl)
                      is_trio=df['人 員'].isin([searchppl])
                      print(df[is_trio])
                      a=0
                      break
                  else:
                      print('請輸入正確人員') 
        elif c=='3':
             while True:
                  searchplace=input('請輸入欲搜尋地點:')
                  if searchplace in list(df['地 點']):
                      #search3=[]
                      #search3.append(searchplace)
                      is_trio=df['地 點'].isin([searchplace])
                      print(df[is_trio])
                      a=0
                      break
                  else:
                      print('請輸入正確地點')  
        elif c=='4':
             while True:
                 searchevent=input('請輸入欲搜尋事項:')
                 if searchevent in list(df['事 項']):
                      #search4=[]
                      #search4.append(searchevent)
                      is_trio=df['事 項'].isin([searchevent])
                      print(df[is_trio])
                      a=0
                      break
                 else:
                      print('請輸入正確事項')
        else:
            print('請輸入正確代碼')
    if a=='4':
        print(df)
        a=0
        
        #排版問題待處理
    while a=='5':
        #df.index = np.arange(1, len(df))

        df.to_csv('df.csv',index=False,header=True)#將dataframe
         #內容轉成CSV寫入入電腦
        break#a=5要測試
    

   

        
    
        
        
    


# In[ ]:

print(df)


# In[ ]:



