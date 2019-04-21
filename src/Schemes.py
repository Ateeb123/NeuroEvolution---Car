import numpy as np
import matplotlib.pyplot as plt
import math
import random
from copy import deepcopy
import sys


class Selection_Schemes:
    def __init__(self):
        self.see = 0
        self.Schemes_List = {'Fitness_Proportionate_Selection':self.Fitness_Proportionate_Selection,'Two_Point_Crossover':self.Two_Point_Crossover,
        'Mutation_Scheme':self.Mutation_Scheme, 'Random_Selection':self.Random_Selection,'Binary_Tournament':self.Binary_Tournament,'Truncation': self.Truncation,
        
        }
    
    def __str__(self):      
        return 'Parent & Survivor Selection Schemes'

    def Fitness_Proportionate_Selection(self,Population_With_Fitness):
        Population_List, Length_of_Checker, Checker = self.Scaler(Population_With_Fitness)
        Population_List.sort(key = lambda Population_List: Population_List[:][-1])

        Checker = sorted(Checker)
 
        Index_Tracker = 0
        random_number = round(random.uniform(math.floor(min(Checker)),max(Checker)), max(Length_of_Checker))
        for Citizen in Population_List:
            if random_number < Citizen[-1]:
                break
            Index_Tracker = Index_Tracker + 1
            # Parent_List.append(Population_List[Index_Tracker])


        return Population_List[Index_Tracker]


    def Two_Point_Crossover(self, Parent_1, Parent_2):


        # Parent_1 = Parent_1[:-1]
        # Parent_2 = Parent_2[:-1]
        # Children = []
        # Each_Child = []
        # Crossover_Point_1 = random.randint(0,len(Parent_1))
        # Crossover_Point_2 = random.randint(0,len(Parent_2))
        # while (Crossover_Point_1 == Crossover_Point_2):
        #     Crossover_Point_2 = random.randint(0,len(Parent_2)-1)
        # Crossover_Point_1, Crossover_Point_2 = min(Crossover_Point_1, Crossover_Point_2), max(Crossover_Point_1,Crossover_Point_2)


        # Parent_1 = [8,4,7,3,6,2,5,1,9,0]
        # Parent_2 = [0,1,2,3,4,5,6,7,8,9]

        # P_1 = Parent_1[:-1]
        # P_2 = Parent_2[:-1]
        P_1 = dict(Parent_1)
        P_2 = dict(Parent_2)
        del P_1['fitness']
        del P_2['fitness']
        Crossover_Point_1 = random.randint(0,len(Parent_1))
        Crossover_Point_2 = random.randint(0,len(Parent_2))
        print('Cross Over Points : ', Crossover_Point_1, Crossover_Point_2)
        Children = []
        while (Crossover_Point_1 == Crossover_Point_2):
            Crossover_Point_2 = random.randint(0,len(Parent_2)-1)
        Crossover_Point_1, Crossover_Point_2 = min(Crossover_Point_1, Crossover_Point_2), max(Crossover_Point_1,Crossover_Point_2)
        Each_Child = []
        Tracker = 0
        Key_List = list(P_1.keys())
        # print('P_1 and P_2 Before Before : ', P_1, P_2)
        print(' Before P 1 : ' , P_1)
        print(' Before P 2 : ' , P_2)
        for Tracker in range(0, len(P_1)):
            if Tracker >= Crossover_Point_1 and Tracker <= Crossover_Point_2:
                Value = P_1[Key_List[Tracker]]
                P_1[Key_List[Tracker]] = P_2[Key_List[Tracker]]
                P_2[Key_List[Tracker]] = Value

        print(' After P 1 : ', P_1)
        print(' After P 2 : ', P_2)
        # print('P_1 and P_2 After : ', P_1, P_2)
        # while (P_2!= []):
        #     if P_2[Tracker] not in P_1[Crossover_Point_1:Crossover_Point_2]:
        #         Each_Child.append(P_2[Tracker])
        #     P_2.popitem(0)

        # Adder = P_1[Crossover_Point_1:Crossover_Point_2]
        # Inserter = Crossover_Point_1
        # while (Adder != []):
        #     Each_Child.insert(Inserter, Adder['fitness'])
        #     Adder.pop('fitness')


        # Children.append(Each_Child)
        # Each_Child = []

        # P_1 = Parent_1
        # P_2 = Parent_2

        # Tracker = 0
        # for Tracker in P_1:
        # while (P_1!= []):
        #     if P_1[Tracker] not in P_2[Crossover_Point_1:Crossover_Point_2]:
        #         Each_Child.append(P_1[Tracker])
        #     P_1.pop(0)

        # Adder = P_2[Crossover_Point_1:Crossover_Point_2]
        # Inserter = Crossover_Point_1
        # while (Adder != []):
        #     Each_Child.insert(Inserter, Adder['fitness'])
        #     Adder.pop('fitness')
        # Children.append(Each_Child)
        return [P_1, P_2]


    def Mutation_Scheme(self,Children,Mutation_Rate):
        Probability_List = [1,2,3,4,5,6,7,8,9,10]
        Mutation_Rate = Mutation_Rate * 10
        # print(Mutation_Rate, type(Mutation_Rate))
        Keys_List = list(Children[0].keys())
        for Each_Child in Children:
            Random_Number = random.randint(1,10)
            if Random_Number in Probability_List[:int(Mutation_Rate)]:
                random_swapper_1 = random.randint(0,len(Each_Child)-1)
                random_swapper_2 = random.randint(0,len(Each_Child)-1)
                # print('Before',Each_Child[random_swapper_1],Each_Child[random_swapper_2])
                Conserver = Each_Child[Keys_List[random_swapper_1]]
                # print('Before Each Child',Each_Child)
                # print('random vals',random_swapper_1, random_swapper_2)
                Each_Child[Keys_List[random_swapper_1]] = Each_Child[Keys_List[random_swapper_2]]
                Each_Child[Keys_List[random_swapper_2]] = Conserver
                # print('After',Each_Child[random_swapper_1],Each_Child[random_swapper_2])
                # print('After',Each_Child)


        return Children



    def Scaler(self, Population_With_Fitness):
        Population_List = []
        for i in Population_With_Fitness:
            Population_List.append(list(i))

        # Population_List = deepcopy(Population_With_Fitness)
        Total_Sum = 0
        Checker = []
        Length_of_Checker = []

        # for Citizen in Population_List:
        #     Total_Sum = Total_Sum + Citizen[len(Citizen) - 1]

        for Citizen_Index in range(0,len(Population_List)):
            Population_List[Citizen_Index][-1] = float(1/Population_List[Citizen_Index][-1])
            # Population_List[Citizen_Index][-1] = float(Total_Sum/Population_List[Citizen_Index][-1])
            # print(Total_Sum)
            Checker.append((Population_List[Citizen_Index][-1]))
            Length_of_Checker.append(len(str(Population_List[Citizen_Index][-1])))
        return Population_List, Length_of_Checker, Checker

    def Random_Selection(self, Population_With_Fitness):
        random_parent = random.choice(Population_With_Fitness)
        return random_parent




    def Binary_Tournament(self, Population_With_Fitness):
        Parent_1 = random.choice(Population_With_Fitness)
        Parent_2 = random.choice(Population_With_Fitness)
        if Parent_1[-1] < Parent_2[-1]:
            return Parent_1
        else:
            return Parent_2


    def Truncation(self, Population_With_Fitness, Top_Best=5):
        # print('INITIAL POPULATION WITH BEST : ' , Population_With_Fitness)
        print(len(Population_With_Fitness))
        Fitness_List = list([i['fitness'] for i in Population_With_Fitness])
        # print()
        # print('EFFING FITNESS LIST', Fitness_List)
        Best_List= []
        for i in range(0,Top_Best):
            Minimum = max(Fitness_List)
            Index = Fitness_List.index(Minimum)
            Best_List.append(Population_With_Fitness[Index])
            Fitness_List.pop(Index)
            # print(Best_List)
        
        Best_List = sorted(Best_List, key=lambda k:k['fitness'])
        # print('SORTED SORTED BEST ; ', Best_List)
        # Best_List.sort(key = lambda Best_List: Best_List[:]['fitness'])
        # print('BEST LIST DAMMIT', Best_List)
        x = random.choice(Best_List)
        # print('RANDOMLY CHSEN X : ', x)
        return dict(x)
        

    






















