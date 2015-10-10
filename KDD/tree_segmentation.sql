--target :status Keine Sollstellung (PRSL_INSTANZ) gefunden

create table p155121.out_tree (cols varchar2(100), ig number);

declare 
target     constant varchar2(256)  :='Keine Sollstellung (PRSL_INSTANZ) gefunden'  ;
n_target     number;
p_target     number;
p_not_target number;

total_rows         number;

total_node_rows   number;
p_node   number;

entropy_parent number;
entropy_node  number;
information_gain number;

child  varchar2(256) ;

v_query_str VARCHAR2(1000);
type t_crs is ref cursor;

--------------------------------------------------------------------------------
procedure f_ent is
begin 
    if n_target = 0 then
      p_target:= 0.001;
      p_not_target :=1;
    elsif n_target=total_node_rows then
      p_target:= 1;
      p_not_target :=0.001; 
    else
         p_target := n_target/(total_node_rows+0.000001);   
         p_not_target:= ( total_node_rows -n_target)/(total_node_rows+0.000001);   
    end if;

   entropy_node   :=(p_target * log(2,p_target) *-1)+(p_not_target * log(2,p_not_target) *-1); 
--   dbms_output.put_line(rec_i.vfrp_idt_traitement||'P target:'||p_target ||' / P not target:'||p_not_target ||' entropy_child:'||trunc(entropy_child,4) );
--    dbms_output.put_line(rec_i.vfrp_idt_traitement||' entropy_child:'||trunc(entropy_node,4) );
    information_gain:=information_gain-(entropy_node *(total_node_rows/total_rows));
--     dbms_output.put_line(total_node_rows/total_rows ||' baluffo');
end f_ent;

--------------------------------------------------------------------------------
procedure p_process(child in varchar)
is
crs        t_crs;
stmt  VARCHAR2(1000);
stmt2  VARCHAR2(1000);
pippo VARCHAR2(1000);
counter number;
begin
information_gain:=0;
information_gain:=entropy_parent;

stmt:= 'select distinct   ' || child||'  as col1 from vv_fremdproduktionen ';
stmt2:= 'select count(distinct   ' || child||')   from vv_fremdproduktionen';

EXECUTE IMMEDIATE stmt2    INTO counter    ;

if counter < 10 then
begin
open crs for stmt ;

     loop
       fetch crs into pippo;
       exit when crs%notfound;
          v_query_str := 'select count(*)   from vv_fremdproduktionen where vfrp_status like ''%'||target||'%'' '    ||'  and  '||child||'= :mycol'   ;
          EXECUTE IMMEDIATE v_query_str    INTO n_target    USING pippo;
          v_query_str := 'select count(*)   from vv_fremdproduktionen where   '||child||'= :mycol'   ;
          EXECUTE IMMEDIATE v_query_str    INTO total_node_rows    USING pippo;
      
         f_ent;
     end loop;
exception when others then
   dbms_output.put_line(sqlcode||'/'||sqlerrm);     
end;     
     

/*
for rec_i in (select distinct  vfrp_idt_traitement    as col1 from vv_fremdproduktionen )loop

   v_query_str := 'select count(*)   from vv_fremdproduktionen where vfrp_status like ''%'||target||'%'' '    ||'  and  '||child||'= :mycol'   ;
    EXECUTE IMMEDIATE v_query_str    INTO n_target    USING rec_i.col1;
   v_query_str := 'select count(*)   from vv_fremdproduktionen where   '||child||'= :mycol'   ;
    EXECUTE IMMEDIATE v_query_str    INTO total_node_rows    USING rec_i.col1;



   f_ent;

end loop;*/

dbms_output.put_line('information_gain('||child||'):'||trunc(information_gain,4));


insert into  p155121.out_tree (cols , ig ) values (child,trunc(information_gain,4));


dbms_output.put_line('----------------------------------------------');
end if;

exception when others then
   dbms_output.put_line(total_rows ||' X '||n_target);
end p_process;

--------------------------------------------------------------------------------
--  M A I N
--------------------------------------------------------------------------------

begin 
dbms_output.enable(100000);
select count(*) into total_rows from vv_fremdproduktionen ;
select count(*) into n_target from vv_fremdproduktionen where vfrp_status like '%'||target||'%';
p_target := n_target/total_rows;
p_not_target:= ( total_rows -n_target)/total_rows;
entropy_parent :=(p_target * log(2,p_target) *-1)+(p_not_target * log(2,p_not_target) *-1); 


---dbms_output.put_line('total_rows:'||total_rows ||'/n_target:'||n_target );
--dbms_output.put_line('P target:'||p_target ||' / P not target:'||p_not_target);
dbms_output.put_line('entropy_parent:'||trunc(entropy_parent,4) );
dbms_output.put_line('----------------------------------------------');



--p_process('vfrp_idt_traitement');


for rec_col in (select column_name from all_tab_columns  where table_name='VV_FREMDPRODUKTIONEN' and owner ='VERTRA'
and column_name not in ('VFRP_INSTANZ')   and rownum < 10
)
loop
dbms_output.put_line(rec_col.column_name);
entropy_node:=0;
p_process(rec_col.column_name);

end loop;

--------------------------------------------------------------------------------

end;


/


commit;

select * from all_tab_columns where table_name='VV_FREMDPRODUKTIONEN' ;


select  * from vv_fremdproduktionen;

select  * from  p155121.out_tree ;
truncate table  p155121.out_tree ;


VFRP_PROVISIONIERUNGSCODE        0.0004
VFRP_PROVISIONSTYP               0.044 
VFRP_VERTRAGSTYP                 0.0839
VFRP_GMU_CODE                    0.095 
VFRP_CODE_GENRE_AFFAIRE          0.1019
VFRP_KOMMISSIONSNUMMER           0.1067
VFRP_TMP_VERKAUFSMERKMAL         0.1435
VFRP_MUTATIONCODE_POLICE         0.1877
;



select distinct VFRP_PROVISIONSTYP         ||'-'||VFRP_VERTRAGSTYP    ,count(*)      
from VV_FREMDPRODUKTIONEN where vfrp_status  not like '%Keine Sollstellung (PRSL_INSTANZ) gefunden%'
group by VFRP_PROVISIONSTYP         ||'-'||VFRP_VERTRAGSTYP    
--order by VFRP_PROVISIONIERUNGSCODE  
;



select VFRP_IMPORT_SOURCE,count(*)       ,'true'   
from VV_FREMDPRODUKTIONEN where vfrp_status  not like '%Keine Sollstellung (PRSL_INSTANZ) gefunden%'
group by VFRP_IMPORT_SOURCE       
union
select VFRP_IMPORT_SOURCE,count(*)   ,'false'   
from VV_FREMDPRODUKTIONEN where vfrp_status   like '%Keine Sollstellung (PRSL_INSTANZ) gefunden%'
group by VFRP_IMPORT_SOURCE       
;

