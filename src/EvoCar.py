
import os
import sys
import subprocess
import pickle
import random
from Schemes import Selection_Schemes
from copy import deepcopy

# print(sys.argv[0], sys.argv[1])
# for i in range(0,1):
    # os.system('python3 simulation.py')
    # print()

# architecture, activation = [3,5,2], 'tanh' # relu
population_size=10
All_Weights = []
# generations_number=80
# gene_mutation_prob=0.15
# gene_crossover_prob = 0.85
# tournament_size = 8
# rand_init = False
# n_possible_weight_values = 1000

weights_dict = {}
bias_dict ={}
architecture = {}
activation = {}
    

# pickle.dump((weights_dict, bias_dict, architecture, activation),open('weights.p','wb'), protocol = 2)
# print(weights_dict)


# weights, bias, architecture, activation = pickle.load(open('weights.p','rb'))
# weights_mod = dict(weights)
# pickle.dump((weights_mod, bias, architecture, activation),open('weights_modded.p','wb'), protocol = 2)

# weights, bias, architecture, activation = pickle.load(open('weights_modded.p','rb'))
# All_Weights.append(weights)
# Deep_Copy_Weights = dict(weights)
# for i in range(0,population_size-1):
#     for i in Deep_Copy_Weights:
#         Deep_Copy_Weights[i] = random.randint(-10,10)
#     All_Weights.append(dict(Deep_Copy_Weights))
    # print(All_Weights[-1])

# weights_2, bias, architecture, activation = pickle.load(open('weights_workable.p','rb'))
# print(All_Weights[0] == weights_2)

# print(len(All_Weights), All_Weights)
# for i in All_Weights:
#     pickle.dump((i, bias, architecture, activation),open('weights_workable.p','wb'), protocol = 2)
#     # W, B, AR, AT = pickle.load(open('weights_workable.p','rb'))
#     # print(W, B , AR, AT)
#     os.system('python3 simulation.py')
#     distance = pickle.load(open('distance.p','rb'))
#     i['fitness'] = distance


# for i in All_Weights:
#     print(i)






import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from Schemes import Selection_Schemes
from copy import deepcopy

class Travelling_Salesman:
    
    def __init__(self, Population_Size, OffSpring, Generation, Mutation_Rate, Iteration):        
        self.Population_Size = Population_Size
        self.OffSpring = OffSpring
        self.Generation = Generation
        self.Mutation_Rate = Mutation_Rate
        self.Iteration = Iteration
        self.All_Weights = []
        self.Scheme_Selector = Selection_Schemes()
        self.Create_File = open('Data.txt', "w+")
        self.initial_weights = {}
        self.bias = {}
        self.architecture = {}
        self.activation = {}
        self.Gen = open('Stats.txt',"w+")
        self.data = open('AllData.txt',"w+")   
        self.every = open('Every_Generation.txt','w+')     
        # self.Population = []

    def __str__(self):
        x = "TSP Problem with the following configurations: \n"
        x = x + "Population_Size:" + " " + str(self.Population_Size) + "\n"
        x = x + "OffSpring:" + " " + str(self.OffSpring) + "\n"
        x = x + "Generation:" + " " + str(self.Generation) + "\n"
        x = x + "Mutation_Rate:" + " " + str(self.Mutation_Rate) + "\n"
        x = x + "Iteration:" + " " + str(self.Iteration) + "\n"
        return x




    def Prepare_Data(self,TextFile="qa194.tsp"):
        self.initial_weights, self.bias, self.architecture, self.activation = pickle.load(open('weights_modded.p','rb'))
        
        # Text = open("qa194.tsp","r")
        # LineTracker = 0
        # for i in Text:
        #     LineTracker = LineTracker + 1
        #     if LineTracker > 7:
        #         i = i.split(' ')
        #         i[-1] = i[-1].strip()
        #         for j in range(0,len(i)):
        #             try:
        #                 i[j] = float(i[j])
        #             except:
        #                 donothing = 0
        #         self.Cities.append(i)




    def Initialization(self):
        self.All_Weights.append(self.initial_weights)
        Deep_Copy_Weights = dict(self.initial_weights)
        for i in range(0,self.Population_Size-1):
            for i in Deep_Copy_Weights:
                Deep_Copy_Weights[i] = random.randint(-20,20)
            self.All_Weights.append(dict(Deep_Copy_Weights))
        # Dummy_Cities_List = self.Cities[:]
        # Citizen = []
        # Tracker = 0
        # Population = []
        # for i in range(0,self.Population_Size):
        #     while (Dummy_Cities_List != []):
        #         Tracker = Tracker + 1
        #         Random_Choice = random.choice(Dummy_Cities_List)
        #         Citizen.append(Random_Choice)
        #         Dummy_Cities_List.remove(Random_Choice)
        #     Dummy_Cities_List = self.Cities[:]
        #     Population.append(Citizen)
        #     Citizen = []
        return self.All_Weights[:]



    def Fitness_Function(self, Population):
        # print('\n')
        # print(Population, len(Population))
        for i in Population:

            pickle.dump((i, self.bias, self.architecture, self.activation),open('weights_workable.p','wb'), protocol = 2)
            # W, B, AR, AT = pickle.load(open('weights_workable.p','rb'))
            # print(W, B , AR, AT)
            os.system('python3 simulation.py')
            distance = pickle.load(open('distance.p','rb'))

            i['fitness'] = distance
        return Population



    # def Crossover(self):
    #     return 0


    # def Mutation(self):
    #     return 0

    
    # def Survival_Scheme(self):
    #     return 0


    def Execute(self, Parent_Scheme, Survivor_Scheme, Crossover_Scheme):
        self.Prepare_Data()

        # Population = self.Initialization()

        # Population_With_Fitness = self.Fitness_Function(Population)

        # Population_With_Fitness_Parents, Length_of_Checker, Checker = self.Scheme_Selector.Scaler(Population_With_Fitness)
        # Population_With_Fitness.sort(key = lambda Population_List: Population_List[:][-1])
        # Generation_Tracker = 0
        # Generation_List = []
        # Best = []
        # Average = []
        # Temporary_List = [] 
        # Current_Best = 0
        # Long = []
        # self.Prepare_Data()
        for Runner in range(0,1):
            # print(Runner, self.Iteration)
            # Population = self.Initialization()
            # Population_With_Fitness = self.Fitness_Function(Population)
            print(self.initial_weights, type(self.initial_weights))

            Population_With_Fitness = [{'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 474.794074793273}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': -20, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': 19, 'w24': 11, 'fitness': 10000.109907896085}, {'w0': 19, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 1908.4489290533318}, {'w0': 19, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 1920.018246275621}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 18, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 471.4560774914817}, {'w0': 19, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 18, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 9337.239781921166}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 18, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 473.88523346682535}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 473.0921212780961}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 481.8461847850954}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 473.20961212652423}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 474.7535928100445}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 472.9891292591939}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': -20, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 6038.10838355058}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 18, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 4264.456678628335}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 1327.1693134576103}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 475.53476905472667}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 1332.8662721250753}, {'w0': 19, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 4869.73973689101}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 2496.2371592615664}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 138.92502113781006}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 136.83028135060908}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 3099.302368347505}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 1909.500004696187}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 18, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': -13, 'w18': -8, 'w19': 19, 'w20': 18, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 2.239041424635136}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 727.0709778257983}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -20, 'w23': -16, 'w24': 11, 'fitness': 479.6618728012743}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 733.0114929593669}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 2509.7372573752787}, {'w0': 19, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -20, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -10, 'w24': 11, 'fitness': 4830.156802304039}, {'w0': 19, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': 11, 'w22': -16, 'w23': -20, 'w24': -19, 'fitness': 16.43431489140347}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 1904.5471274436713}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 18, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 473.31149075124705}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 5467.30059093789}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 476.6096011114896}, {'w0': 18, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 18, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': 19, 'w24': 11, 'fitness': 1838.7040941606099}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 472.8423620159789}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 473.9294730613336}, {'w0': 19, 'w1': 9, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 11, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 15, 'w12': -20, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 1321.7503219207706}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 474.2909342832723}, {'w0': 19, 'w1': 9, 'w2': 1, 'w3': -20, 'w4': -20, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': -3, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': -20, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 1317.0434973880365}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 472.85831924784765}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 474.6538037564914}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 472.68825256175074}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 473.2702822970806}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 206.36521809089012}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 203.15811262901713}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 476.8991117463466}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 476.5609315464484}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 475.6974341793704}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 477.2674079490672}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 470.6248944998893}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 473.0049047451352}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 477.2907019130746}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 478.7610109079479}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': 19, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': -14, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 476.6323421369691}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 473.2323136465475}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 475.5368724765859}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 473.3371507445447}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 469.7689175269798}, {'w0': 18, 'w1': -3, 'w2': -20, 'w3': -20, 'w4': 1, 'w5': 4, 'w6': 15, 'w7': -14, 'w8': 9, 'w9': -17, 'w10': -10, 'w11': 11, 'w12': 19, 'w13': 20, 'w14': -19, 'w15': 7, 'w16': 20, 'w17': 18, 'w18': -8, 'w19': 19, 'w20': -13, 'w21': -19, 'w22': -16, 'w23': -20, 'w24': 11, 'fitness': 475.48824105368186}]
            # print('Pop with Fitness', Population_With_Fitness)

            Generation_Tracker = 0
            Generation_List = []
            Best = []
            Average = []
            Temporary_List = [] 
            Current_Best = 0
            Long = []


            while (Generation_Tracker <self.Generation):
                # print('POP WITH FITNESS FITNESS : ' , Population_With_Fitness)
                for i in range(0,int(self.OffSpring/2)):
                    
                    Parent_1 = self.Scheme_Selector.Schemes_List[Parent_Scheme](Population_With_Fitness)                
                    Parent_2 = self.Scheme_Selector.Schemes_List[Parent_Scheme](Population_With_Fitness)

                    # for k in Population_With_Fitness:
                    #     print('FITNESSERERERER', k['fitness'])
                    # print('EFFING THEN', Parent_1['fitness'], Parent_2['fitness'])

                    while (Parent_2 == Parent_1):
                        # print(Parent_1 == Parent_2) 
                        Parent_2 = self.Scheme_Selector.Schemes_List[Parent_Scheme](Population_With_Fitness)
                    Children = self.Scheme_Selector.Schemes_List[Crossover_Scheme](Parent_1,Parent_2)

                    Mutated_Children = self.Scheme_Selector.Schemes_List['Mutation_Scheme'](Children,self.Mutation_Rate)
                    Checker_Before = []
                    # for i in Population_With_Fitness:
                    #     Checker_Before.append(i['fitness'])
                    # print('Just Bfore Mutation Fitness : \n ',len(Checker_Before), max(Checker_Before), min(Checker_Before) ,Checker_Before)

                    Mutated_Children_with_Fitness = self.Fitness_Function(Mutated_Children)
                    Checker_Before = []
                    # for i in Population_With_Fitness:
                    #     Checker_Before.append(i['fitness'])
                    # print('Bfore V111111111 : \n ',len(Checker_Before), max(Checker_Before), min(Checker_Before) ,Checker_Before)

                    # if Mutated_Children_with_Fitness in Population_With_Fitness:
                    #     print('Might be the cause')

                    for Child in Mutated_Children_with_Fitness: 
                        Population_With_Fitness.append(Child)
        
                Temporary_List = []
                for i in Population_With_Fitness:
                    Temporary_List.append({j:i[j] for j in i if j!='fitness'})
                for i in range(0,10):
                    print(' ')
                Checker_Before = []
                for i in Population_With_Fitness:
                    Checker_Before.append(i['fitness'])
                # print('Bfore : \n ',len(Checker_Before), max(Checker_Before), min(Checker_Before) ,Checker_Before)

                Selected_Population = []
                while (len(Selected_Population) < self.Population_Size):

                    Death_From_Fitness = self.Scheme_Selector.Schemes_List[Survivor_Scheme](Population_With_Fitness)        
                    # print('\n SAVING : ', Death_From_Fitness['fitness'])
                    Death_From_Fitness = {i:Death_From_Fitness[i] for i in Death_From_Fitness if i != 'fitness'}                    
                    Axes = Temporary_List.index(Death_From_Fitness)
                    # print('LET"S SEEEEE :   ', Population_With_Fitness[Axes]['fitness'])               
                    Selected_Population.append(Population_With_Fitness[Axes])
                    Population_With_Fitness.pop(Axes)
                    Temporary_List.pop(Axes)
                        # Population_With_Fitness.pop(Axes)
                        # Temporary_List.pop(Axes)
                Population_With_Fitness = list(Selected_Population)
                self.data = open('AllData.txt',"w+")        
                self.data.write(  str(Generation_Tracker) + ' ' + str(Population_With_Fitness))
                self.data.close()
                self.every = open('Every_Generation.txt','w+')     
                self.every.write(' Generation is : ' + str(Generation_Tracker) + ' ' + str(Population_With_Fitness))
                self.every.close()

                # for i in range(0,20):
                #     print(' Survivor Selector : ', len(Population_With_Fitness))
                # while (len(Population_With_Fitness) > self.Population_Size):
                #     Death_From_Fitness = self.Scheme_Selector.Schemes_List[Survivor_Scheme](Population_With_Fitness)        
                #     print('\n DELETING : ', Death_From_Fitness['fitness'])
                #     Death_From_Fitness = {i:Death_From_Fitness[i] for i in Death_From_Fitness if i != 'fitness'}                    
                #     Axes = Temporary_List.index(Death_From_Fitness)
                #     Population_With_Fitness.pop(Axes)
                #     Temporary_List.pop(Axes)

                Checker_Before = []
                for i in Population_With_Fitness:
                    Checker_Before.append(i['fitness'])
                    print(i['fitness'])
                print('Same AFTER : \n ',len(Checker_Before), max(Checker_Before), min(Checker_Before), Checker_Before)
                print('Same AFTER : \n ',len(Checker_Before), max(Checker_Before), min(Checker_Before),Checker_Before)
                print(Generation_Tracker)
                print(Checker_Before)

                Long = [] 
                for i in Population_With_Fitness:
                    Long.append(i['fitness'])
                # print(Generation_Tracker,min(Long))f
                X = max(Long)
                Index = Long.index(X)

                self.Gen = open('Stats.txt',"w+")
                self.Gen.write(str(Population_With_Fitness[Index]) + ', Generation is ' + str(Generation_Tracker) + ' and Best is ' + str(X) + '\n')
                self.Gen.close()
                Best.append(max(Long))
                print(Best[-1])
                Average_Average = sum(Long)/len(Long)
                self.Create_File.write((' '+str(min(Long))) + ' ' + str(Average_Average) + '\n' )
                Average.append(Average_Average)
                # print('Generation ' + str(Generation_Tracker) + ' : ','The Average is: ', Average_Average)
                Generation_List.append(Generation_Tracker)
                # print(Generation_Tracker)
                Generation_Tracker = Generation_Tracker + 1
                self.Create_File.write('Average-Best-Fitness: ' +  str((sum(Best)/len(Best))) + '\n')
                self.Create_File.write('Average-Average-Fitness: ' +  str((sum(Average)/len(Average))) + '\n')
                
                print(Best)
                print(max(Best), 'Long Long ' ,max(Long), float(max(Best))==float(max(Long)))
            plt.plot(Generation_List, Average)
            plt.plot(Generation_List, Best)
            plt.show()

            Minimum = [i for i in Population_With_Fitness]
            X = Minimum.index(min(Minimum))
            # print(Population_With_Fitness[X])
            # Tracker = 0
            # for i in Population_With_Fitness[X]:
            #     if Population_With_Fitness[X].count(i) > 1:
            #         print(i, Tracker)

            #     Tracker = Tracker + 1
                    # print(Temporary_List[Axes][1], Population_With_Fitness[Axes][1])
                #     for check in Temporary_List:
                #         if d[:-1] == check:
                #             print(True)
                        # Death[:-1] = 

            # print(min(Best) in Tracker, Tracker.index(min(Best)), Population_With_Fitness[X][-1] == Tracker[X])
            # # print(Population_With_Fitness[X])
            # X_Coords = []
            # Y_Coords = []
            # for i in (0,len(Population_With_Fitness[X])):
            #     X_Coords.append(Population_With_Fitness[X][1])
            #     Y_Coords.append(Population_With_Fitness[X][2])
            # print(X_Coords)
            # plt.plot(X_Coords, Y_Coords)
            # plt.show()

        return 0

## UnModified Parameters
# TSP = Travelling_Salesman(30,10,50,0.3,10)
TSP = Travelling_Salesman(60,10,100 ,0.2,10)
#Modified Paramters for FSP and fSP
# TSP = Travelling_Salesman(10,20,3000,0.3,10)


#For Truncations and FPS
# TSP = Travelling_Salesman(10,50,3000,1,10)

#For Binary Tournament and Fitness portionate scheme
# TSP = Travelling_Salesman(20,150,1000,0.9,10)
# TSP = Travelling_Salesman(20,40,1000,0.9,10)
# TSP.Prepare_Data()
# TSP.Initialization()
# TSP.Fitness_Function()
TSP.Execute(Parent_Scheme='Truncation', Survivor_Scheme='Truncation', Crossover_Scheme='Two_Point_Crossover')
print(TSP.All_Weights)
# for i in range(0,10):



# Fitness_Proportionate_Selection
# Random_Selection
# Two_Point_Crossover
# Binary_Tournament
# Random_Selection
# Truncation


# self.Population_Size = Population_Size
# self.OffSpring = OffSpring
# self.Generation = Generation
# self.Mutation_Rate = Mutation_Rate
# self.Iteration = Iteration
# self.Cities = []
# self.Scheme_Selector = Selection_Schemes()









