from collections import Counter

def tweets():


    while True:
        try:
            tests =int(input("Please enter the no. of test cases:"))
            break
        except:
            print("That's not a valid option!Please enter a number.")
    # list containing username and tweet_id       
    d=[]
    # list of user names
    l=[]
    for i in range(tests):
        while True:
            try:
                n=int(input("Please enter the no of Tweets:"))
                break
            except:
                print("That's not a valid option!Please enter a number.")
        
        for j in range(n):
            d.append(input("Please enter the USER NAME and TWEET ID separated by a space : "))
        for i in range(len(d)):
            a=d[i].split()
            l.append(a[0])
        times = Counter(l)

        temp_max_result = [(key, value) for 
                            key, value in sorted(times.items()) if
                            value >= 1]
        for (key,value) in temp_max_result: 
                    print(f'Maximum number of tweets: {key} , {value} times.')
        temp_max_result=[]
        l=[]
        d=[]

tweets()