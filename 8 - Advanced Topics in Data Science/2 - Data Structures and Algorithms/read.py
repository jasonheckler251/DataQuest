
from collections import Counter

def exponential_search():

    aviation_data = []
    with open("AviationData.txt") as aviationdata:
        for i in aviationdata:
            aviation_data.append(i)

    aviation_list = []
    for j in aviation_data:
        aviation_list.append(j.split("|"))

    lax_code = []

    for i in aviation_list:
        for j in i:
            if "LAX94LA336" in j:
                lax_code.append(i)

    print(lax_code)

## This approach's drawbacks is that the entire dataset needs to be linearly searched to find the value. O(n*m)


def linear_time_search():

    aviation_data = []
    lax_code = []

    with open("AviationData.txt") as aviationdata:
        for i in aviationdata:
            value = (i.split("|"))
            #print(value)
            for k in value:
                if "LAX94LA336" in k:
                    lax_code.append(value)
    print(lax_code)

## O(n) search time.  (logn search time is not possible)
    

def list_of_dicts():

    aviation_dict_list = []

    with open("AviationData.txt") as aviationdata:
        k = 0
        for i in aviationdata:
            value = (i.split("|"))
            if k ==0:
                keys = value
                k +=1
            else:
                new_dict = dict(zip(keys,value))
                k += 1
                aviation_dict_list.append(new_dict)
    
    lax_dict = []

    for val in aviation_dict_list:
        for key, value in val.items():
            if  "LAX94LA336" in value:
                lax_dict.append(val)
    print(lax_dict)


def count_accidents():
    with open("AviationData.txt") as aviationdata:
        dict_count = {}
        for i in aviationdata:
            value = (i.split("|"))
            if value[5] == " United States ":
                state = value[4]
                state = state.split(",")[-1]
                dict_count[state] = dict_count.get(state, 0) + 1
        print(dict_count)
        k = Counter(dict_count)
        print(k.most_common(1))

def monthly_injuries():
        k = 0
        month_count = {}
        with open("AviationData.txt") as aviationdata:
            for i in aviationdata:
                value = (i.split("|"))
                if k ==0:
                    keys = value
                    k +=1
                else:
                    new_dict = dict(zip(keys,value))
                    k += 1
                    total_fatal = new_dict[" Total Fatal Injuries "].strip(" ")
                    if total_fatal== "":
                        total_fatal = 0
                    total_serious = new_dict[" Total Serious Injuries "].strip(" ")
                    if total_serious == "":
                        total_serious = 0
                    total = int(total_fatal) + int(total_serious)

                    month = new_dict[" Event Date "]

                    month = month.split("/")[0]
                    try:
                        month = int(month)
                    except:
                        month = 0


                    month_count[month] = month_count.get(month, 0) + total


        print(month_count)
            


monthly_injuries()