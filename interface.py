'''
Code to generate the interface which takes initial uncleaned data
and extracts your chosen data points based on input
'''

def userinterface(x):
    interface = '''Below are the contents of each cell: \n 
        0) Age 
        1) workclass
        2) fnlwgt
        3) education
        4) aducation-num
        5) marital-status
        6) occupation
        7) relationship
        8) race
        9) sex
        10) capital-gain
        11) capital-loss
        12) Hours per week
        13) Native Country
        14) Salary
    '''
    #print(interface)
    #Selection = input("Please select which cells you wish to use followed by a comma: ")
    Selection = x
    return Selection


# function to select only the cells that are selected by user
def selectcells(Selection):

    with open('adult.data', 'r') as f:
        f = f.readlines()
        finalist = []
        newlist = []
        for line in f:
            data = line.split(',')
            for x in Selection:
                for j in data:
                    if int(x) == data.index(j):
                        newlist.append(j)
            finalist.append(newlist)
            newlist = []
        return(finalist)


def interface(x):
    Selection = userinterface(x)
    data = selectcells(Selection)
    return data
