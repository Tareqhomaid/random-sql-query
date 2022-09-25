import random
import sys, os

red = '\033[31;1m'
re = '\033[m'


def open_file(file):
    with open(file) as opened:
        return opened.read().split("\n")

def insert():
    tablecount = int(input("How many tables do you have? "))
    for l in range(tablecount):
        TableName = input("Enter Table's name : ")
        print(red + "available input Types: id name email city country phone address price date food salary firstname "
                    "lastname ints count randomquantity" + re)
        columnsin = input("Enter your columns' Types separated by space: ")
        columns = columnsin.split()
        rows = int(input("How many rows do you want to print? "))
        # files

        randomquantity = [i for i in range(100)]

        filedicts = {
            f.replace(".txt",""): open_file(f) for f in os.listdir() if ".txt" in f
        }
        print("\nINSERT INTO " + TableName + " VALUES")
        for i in range(rows):
            print("(", end="")
            for x in range(len(columns)):
                if columns[x] in filedicts:
                    rand = filedicts[columns[x]]
                    if columns[x] == "ints":
                        print(random.choice(rand), end=", ")
                    # elif columns[x] == "count":
                    # print (i, end = ", ")
                    elif columns[x] == "rndomquantity":
                        print(random.choice(randomquantity), end=", ")
                    else:
                        print("'", random.choice(rand), "'", end=", ")

                else:
                    continue
            sys.stdout.write("\b\b), ")
        sys.stdout.flush()
        sys.stdout.write("\b\b;\n")


def createone():
    dbname = input("Enter your database name: ")
    print("CREATE DATABASE " + dbname + ";")
    print("USE " + dbname + ";")


functions = {
    "create": createone,
    "insert": insert
}

while True:
    print("""
***************************************************
*    This program creates SQL commands to         *
*    generate random DATA INPUT and to create     *
*               a Database                        *
*			                                      *
*						                          *
*  these are the functions that you can choose :  *
*       *Write the function name to use it        *
*						                          *
*    create : To create a database                *
*    insert : To insert random values into tables *
*						                          *
*		         AND				              *
*    exit : To exit the program                   *
*                                                 *
***************************************************""")
    try:
        option = input(red + "\nChoose a function : " + re)
        option = option.split()
        for i in range(len(option)):
            if option[i] in functions:
                for i in range(len(option)):
                    functions[option[i]]()
            elif option[i] == "exit":
                break
            else:
                print("Error, wrong Input")
        if "exit" in option:
            break
    except KeyboardInterrupt:
        print("Bye!")
        break
