# select distinct name, company_name, conduct_name, img
# from (((bangumi_list natural join bangumi_company) natural join bangumi_conduct)
# 		natural join company) natural join conduct;

import pymysql
import traceback

def create_view_detail_info(db):
    cursor=db.cursor()
    sql1="""
        drop view if exists detail_info;
        """
    sql2 = """
        CREATE view detail_info as (
        select name,company_name,conduct_name,img
        from (((bangumi_list natural join bangumi_company) natural join bangumi_conduct)
 		natural join company) natural join conduct;
        )
        """
    try:
        print('start to execute:')
        print(sql2)
        cursor.execute(sql1)
        cursor.execute(sql2)
        print('create success !')
    except:
        print('create error!')
        traceback.print_exc()
    cursor.close()


def create_trigger_bangumi(db):
    cursor = db.cursor()
    #delete_on_bili
    sql1="""
        delimiter //
        drop trigger if exists delete_on_bili//
        create trigger delete_on_bili
        after delete on bilibili
        for each row
        begin
            if (ifexist_acfun(old.bangumi_id)=-1 AND ifexist_AGE(old.bangumi_id)=-1) then
                begin
                    delete from bangumi_list
                    where bangumi_list.bangumi_id = old.bangumi_id;
                end;
            end if;
        end; //
        delimiter ;
    """
    #delete_on_acfun
    sql2="""
        delimiter //
        drop trigger if exists delete_on_acfun//
        create trigger delete_on_acfun
        after delete on acfun
        for each row
        begin
            if (ifexist_bili(old.bangumi_id)=-1 AND ifexist_AGE(old.bangumi_id)=-1) then
                begin
                    delete from bangumi_list
                    where bangumi_list.bangumi_id = old.bangumi_id;
                end;
            end if;
        end; //
        delimiter ;
    """
    #delete_on_AGE
    sql3="""
        delimiter //
        drop trigger if exists delete_on_AGE//
        create trigger delete_on_AGE
        after delete on AGE
        for each row
        begin
            if (ifexist_bili(old.bangumi_id)=-1 AND ifexist_acfun(old.bangumi_id)=-1) then
                begin
                    delete from bangumi_list
                    where bangumi_list.bangumi_id = old.bangumi_id;
                end;
            end if;
        end; //
        delimiter ;
    """
    try:
        print('start to execute:')
        print(sql1)
        cursor.execute(sql1)
        print('create success !')
    except:
        print('create error!')
        traceback.print_exc()
    try:
        print(sql2)
        cursor.execute(sql2)
        print('create success !')
    except:
        print('create error!')
        traceback.print_exc()
    try:
        print(sql3)
        cursor.execute(sql3)
        print('create success !')
    except:
        print('create error!')
        traceback.print_exc()

    

def create_func_ifexist(db):
    cursor = db.cursor()
    sql1="""
        delimiter $$
        drop function if exists ifexist_bili$$
        create function ifexist_bili (id int) 
        returns int
        begin
            if (id in (select bangumi_id from bilibili)) then
                return(id);
            end if;
            return(-1);
        end$$
        delimiter ;
    """   
    sql2="""
        delimiter $$
        drop function if exists ifexist_acfun$$
        create function ifexist_acfun (id int) 
        returns int
        begin
            if (id in (select bangumi_id from acfun)) then
                return(id);
            end if;
            return(-1);
        end$$
        delimiter ;
    """ 
    sql3="""
        delimiter $$
        drop function if exists ifexist_AGE$$
        create function ifexist_AGE (id int) 
        returns int
        begin
            if (id in (select bangumi_id from AGE)) then
                return(id);
            end if;
            return(-1);
        end$$
        delimiter ;
    """ 
    try:
        print('start to execute:')
        print(sql1)
        cursor.execute(sql1)
        print('create success !')
        print(sql2)
        cursor.execute(sql2)
        print('create success !')
        print(sql3)
        cursor.execute(sql3)
        print('create success !')
    except:
        print('create error!')
        traceback.print_exc()
    


if __name__ == '__main__':
    db = pymysql.connect(host="localhost", port=3306, db="yukiyu", user="jhchen", password="123456",charset='utf8')
    create_view_detail_info(db) #create view
    create_func_ifexist(db)
    create_trigger_bangumi(db)  #create tigger， 需要手动创建
    db.close()
    