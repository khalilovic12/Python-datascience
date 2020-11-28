import Modulebdd
import csv
import Moduleapi
from sqlite3 import Error
import sqlite3



def main():


    database = r"C:\Users\Khalil\Desktop\Projet_final\pythonsqlite_pays.db"
    data = 'C:\\Users\\Khalil\\Desktop\\Projet_final\\code_pays.csv'


    sql_create_pays_table = """ CREATE TABLE IF NOT EXISTS pays (
                                        nom text NOT NULL,
                                        code text NOT NULL
                                    ); """
    # create a database connection
    conn = Modulebdd.create_connection(database)

    # create table pays

    if conn is not None:
        # create pays table
        Modulebdd.create_table(conn, sql_create_pays_table)

    else:
        print("Error! cannot create the database connection.")

    #Modulebdd.insert_data_pays(conn, data)

    sql_create_jours_feries_table = """ CREATE TABLE IF NOT EXISTS jours_feries (
                                       pays text,
                                       jours ferie text 
                                    ); """


    if conn is not None:
        # create jours_feries table
        Modulebdd.create_table(conn, sql_create_jours_feries_table)

    else:
        print("Error! cannot create the database connection.")   



    with open (data,'r') as fin:

            dr = csv.DictReader(fin)

            for i in dr:
                
                #print ( i['Code'])
                Holidays_list = Moduleapi.get_holidays(i['Code'])
                #print (type(Holidays_list)) 
                
                if type(Holidays_list) == list:

                    # L : Liste des jours feries de chaque pays 
                    # i['name'] : Nom de la pays associée

                    L= [i['Name']]
                    for j in Holidays_list:
                        L.append(j['date'])  
                        #print(L)
                    # Insert data in the 2 columns (Pays et jours feries) of the table jours feries
                 
                        #Modulebdd.insert_data_jours_feries(conn, i, j)  
                            
                           

                    file = open('Liste_jours_feries.csv', 'a', newline='')

                    with file:
                        
                        write = csv.writer(file)
                        write.writerow(L) 
                  
                else:
                    continue

                   
     #   Afficherlepaysquialeplusdejoursfériés en 2017 à partir d’une requête SQL sur la base de données        
                    
    try:
        c = conn.cursor()
        c.execute('''SELECT pays, COUNT(pays) FROM jours_feries GROUP BY pays ORDER BY COUNT(pays) DESC LIMIT 1''')
        for row in c.fetchall():
            print (row)
    except:
        print("error303")                

    # Afficher le pays qui a le moins de jours fériés en 2017 à partir d’une requête SQL sur la base de données

    try:
        c = conn.cursor()
        c.execute('''SELECT pays, COUNT(pays) FROM jours_feries GROUP BY pays ORDER BY COUNT(pays) ASC LIMIT 1''')
        for row in c.fetchall():
            print (row)
    except:
        print("error303")

            


if __name__ == '__main__':

    main()