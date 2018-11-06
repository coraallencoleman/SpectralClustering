import os
os.system("grep '^ ' monkey.txt > monkeyClean.txt") #original data monkey.txt
#separate matrices
os.system("head -20 monkeyClean.txt > monkeyM1.txt")
os.system("tail -20 monkeyClean.txt > monkeyM2.txt")

#Covariates
os.system("grep '^ ' monkeyCov.txt > ageRank.txt") #original data monkeyCov.txt
os.system("grep '^[0-9]' monkeyCov.txt > gender.txt")

import numpy as np
M1 = np.loadtxt("monkeyM1.txt")
M1.shape
M2 = np.loadtxt("monkeyM2.txt")
M2.shape
gender = np.loadtxt("gender.txt", dtype=str)
