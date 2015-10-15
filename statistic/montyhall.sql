declare 
   montyhall     number :=0 ;
   yourchoice    number :=0 ;   
   win_no_change    number :=0 ;   
   ind number := 10000;
begin
   DBMS_RANDOM.INITIALIZE( 267383 );
   for i in 1 .. ind
      loop
      montyhall := round(DBMS_RANDOM.value(1,3));
      yourchoice :=round(DBMS_RANDOM.value(1,3));
      
      if   montyhall=yourchoice then
         win_no_change:=win_no_change + 1; 
      end if;   
      end loop;
dbms_output.put_line('no change win:'||win_no_change/ind);
   end;
   
   /


declare 
   win_no_change number :=0 ;      
begin
   for i in 1 .. 10 loop
      win_no_change :=0;
      for i in 1 .. 10000 loop       if   round(DBMS_RANDOM.value(1,3)) = round(DBMS_RANDOM.value(1,3))then     win_no_change:=win_no_change + 1;       end if;   end loop;
      dbms_output.put_line('no change win:'||substr(to_char(win_no_change),1,2)||'%');
   end loop;
end;
   
   /

