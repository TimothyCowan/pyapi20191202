#!/usr/bin/python3

def main():
    mylist = []
    mylist.append("monday")
    mylist.append("tuesday")
    mylist.append("wednesday")

    # print(mylist)
    # print(mylist[0])
    # print(mylist[2])
    #
    studiomovies = {}   # or --->   studiomovies = {"pixar": "toystory", "universal": "jaws", "paramount": "raiders of lost ark"}
    studiomovies["pixar"] = "toystory"
    studiomovies["universal"] = "jaws"
    studiomovies["paramount"] = "raiders of lost ark"
    # print(studiomovies['pixar'])
    studiomovies["pixar"] = ["toy story", "up"]
    print(studiomovies["pixar"][1])

    # print(studiomovies['paramount'])
    # print(studiomovies['pixar'])

if __name__ == "__main__":
    main()
