#!/usr/bin/python3
""" a function that inserts a line of text to a file, after each line
    containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """ prototype defined """
    with open(filename, "r+") as MyList:
        """ comment """
        reading = MyList.readlines()
        MyList.seek(0)
        for i in reading:
            if search_string in i:
                MyList.write(new_string)
            MyList.write(i)
        MyList.truncate()
