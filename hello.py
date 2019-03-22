# I am standing with my friend in front of skyscrapper with 100 floors
#  and I'am presenting him following bet,:
#I will toss die 100 times, 
# if integer 1 or 2 will be drawed I am going 1 floor lower
# if integer 3,4 or 5 will be drawed I am going 1 floor higher
# if integer 6 will be drawed I am tossing one more time, and integer which will be drawed indicate numbers
# of floors I'am going higher
# I am beting with my friend that I will reach 60's floor with 100 die tossing

#but before I accepted bet I run a program which helps me check how big chances I really have

# numpy and matplotlib imported, seed set.
import numpy as np
import matplotlib.pyplot as plt
# initialize and populate all_walks

#below I create function which will calulate to which floor I will reach till 100 tosses in 10 random separate occasions

#list which will old number of floor in each step in each random walk
all_walks = []
#i will calculate final floor in 10 separate random occasion
for i in range(10) :
    #floor on which i will finish in given random occasion
    random_walk = [0]
    #100 times i will toss a die
    for x in range(100) :
        #step is placeholder list keeping information about floor on which I am in a given moment
        step = random_walk[-1]
        #simulation of dice toss
        dice = np.random.randint(1,7)
        # I can't go below 0 flor, that why max function
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw - what changes dimmension of all_walks, thats why transposition is required
np_aw=np.array(all_walks)

# Transpose np_aw: np_aw_t
np_aw_t=np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

#in case of 6 of 10 attempts the goal was achieved
sum(np_aw_t[100]>60)
