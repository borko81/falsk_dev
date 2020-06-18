import fdb
from collections import defaultdict

database = {
    'host': '127.0.0.1',
    'database': r'D:\\PATH\\SOME_BASE.FDB',
    'user': 'SYSDBA',
    'password': 'password'
}


def con_to_firebird(query, *args):
    con = fdb.connect(**database)
    cur = con.cursor()
    try:
        cur.execute(query, *args)
    except fdb.Error as e:
        print(e)
    else:
        for line in cur.fetchall():
            yield line
    finally:
        con.close()


def insert_to_firebird(query, *args):
    con = fdb.connect(**database)
    cur = con.cursor()
    try:
        cur.execute(query, *args)
        con.commit()
    except fdb.Error as e:
        print(e)
    finally:
        con.close()


if __name__ == '__main__':
    insert_to_firebird('''
    execute block as
    begin
    update room_maintenance set room_maintenance.status = {status}
    where room_maintenance.id = {id};
    insert into maintenance_notes
    (
        maintenance_notes.maintanence_id,
        maintenance_notes.user_id,
        maintenance_notes.note,
        maintenance_notes.date_time_occurrence
    )
    values(
        {id},
        (select distinct(room_maintenance.user_id) from room_maintenance where room_maintenance.id={id}),
        '{note}',
        '{resdate}'
    );
    end'''.format(status=1, id=8, note='борко', resdate='2020-06-16'))
