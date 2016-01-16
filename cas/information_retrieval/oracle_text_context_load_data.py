#########################################################################################################
#DATABASE DB (oracle)
import cx_Oracle
import os 


con = cx_Oracle.connect('p155121/+1@gpvvd')
cur = con.cursor()
indir = 'D:\\Information_retrieval\\02_Praktikum\\PT_5_MiniRetrieve\\PT_5_MiniRetrieve\\documents\\'
for root, dirs, filenames in os.walk(indir):
    for  f in filenames:
        file1 =  open(os.path.join(indir,f))
        text1 = file1.read()
        text=text1.replace('\'',' ')
        file1.close()
        print text
        #file.close()
        #create table test_ps (pers_instanz number, doc clob );
        #insert into  test_ps select * from partnersearch;
        #commit;
        stmt='insert into p155121.test_catsearch values ('+f+ ',\''+f+'\''\
           +',\''+text+'\',0,\''+text+'\')'
        #print stmt  
        try:
            cur.execute(stmt);
            cur.execute('commit')
        except:
            print "Error"
        #raw_input('>');
                      
cur.close()
con.close()


#row =  cur.fetchone()
#row =  cur.fetchall()
#row =  cur.description
