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
        self.Cities = []
        self.Scheme_Selector = Selection_Schemes()
        self.Create_File = open('Data.txt', "w+")

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
            
        self.Cities = self.Cities[:]


    def Plot_Raw_Cities(self):
        plt.scatter([float(i[1]) for i in self.Cities],[float(i[2]) for i in self.Cities])
        plt.show()


    def Initialization(self, Population):
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
        return Population



    def Fitness_Function(self, Population):
        Total_Distance = 0
        for Sample in Population:
            for City in range(0,len(Sample)):
                try:
                    X_Square = Sample[City][1] - Sample[City+1][1]
                    X_Square = X_Square ** 2
                    Y_Square = Sample[City][2] - Sample[City+1][2]
                    Y_Square = Y_Square ** 2
                    Distance = X_Square + Y_Square
                    Distance = math.sqrt(Distance)
                    Total_Distance = Total_Distance + Distance
                except:
                    X_Square = Sample[City][1] - Sample[0][1]
                    X_Square = X_Square ** 2
                    Y_Square = Sample[City][2] - Sample[0][2]
                    Y_Square = Y_Square ** 2
                    Distance = X_Square + Y_Square
                    Distance = math.sqrt(Distance)
                    Total_Distance = Total_Distance + Distance


            Index_of_Sample = Population.index(Sample)
            Population[Index_of_Sample].append(Total_Distance)
            Total_Distance = 0
        return Population


    # def Parent_Selection_Scheme(self, Scheme_Name, Population):
    #     # Parent_Selection = Selection_Schemes.Fitness_Proportionate_Selection(self,Population_With_Fitness)
    #     Parent_Selected = self.Scheme_Selector.Schemes_List[Scheme_Name](Population)
    #     print(Parent_Selected)

    #     return 0

    def Crossover(self):
        return 0


    def Mutation(self):
        return 0

    
    def Survival_Scheme(self):
        return 0


    def Execute(self, Parent_Scheme, Survivor_Scheme, Crossover_Scheme):
        # self.Prepare_Data()

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
        self.Prepare_Data()
        for Runner in range(0,1):
            # print(Runner, self.Iteration)
            Population = self.Initialization()
            Population_With_Fitness = self.Fitness_Function(Population)

            Generation_Tracker = 0
            Generation_List = []
            Best = []
            Average = []
            Temporary_List = [] 
            Current_Best = 0
            Long = []

            self.Create_File.write('\n')
            self.Create_File.write('Iteration:' + str(Runner) + ' Best_Fitness' + ' Average_Fitness' + '\n')

            while (Generation_Tracker <self.Generation):
                self.Create_File.write('Generation'+ str(Generation_Tracker))
                for i in range(0,int(self.OffSpring/2)):

                    Parent_1 = self.Scheme_Selector.Schemes_List[Parent_Scheme](Population_With_Fitness)                
                    Parent_2 = self.Scheme_Selector.Schemes_List[Parent_Scheme](Population_With_Fitness)


                    # while (Parent_2 == Parent_1):
                    #     # print(Parent_1 == Parent_2) 
                    #     Parent_2 = self.Scheme_Selector.Schemes_List[Parent_Scheme](Population_With_Fitness)
                    Children = self.Scheme_Selector.Schemes_List[Crossover_Scheme](Parent_1,Parent_2)

                    Mutated_Children = self.Scheme_Selector.Schemes_List['Mutation_Scheme'](Children,self.Mutation_Rate)

                    Mutated_Children_with_Fitness = self.Fitness_Function(Mutated_Children)

                    # if Mutated_Children_with_Fitness in Population_With_Fitness:
                    #     print('Might be the cause')

                    for Child in Mutated_Children_with_Fitness: 
                        Population_With_Fitness.append(Child)
        
        
                Temporary_List = [i[:-1] for i in Population_With_Fitness]


                # Selected_Population = []
                # while (len(Selected_Population) < self.Population_Size):
                    
                #     Death_From_Fitness = self.Scheme_Selector.Schemes_List[Survivor_Scheme](Population_With_Fitness)        
                #     Axes = Temporary_List.index(Death_From_Fitness[:-1])
                #     Selected_Population.append(Population_With_Fitness[Axes])
                #     Population_With_Fitness.pop(Axes)
                #     Temporary_List.pop(Axes)
                #         # Population_With_Fitness.pop(Axes)
                #         # Temporary_List.pop(Axes)
                # Population_With_Fitness = list(Selected_Population)


                while (len(Population_With_Fitness) > self.Population_Size):
                    Death_From_Fitness = self.Scheme_Selector.Schemes_List[Survivor_Scheme](Population_With_Fitness)        
                    Axes = Temporary_List.index(Death_From_Fitness[:-1])
                    Population_With_Fitness.pop(Axes)
                    Temporary_List.pop(Axes)


                Long = [] 
                for i in Population_With_Fitness:
                    Long.append(i[-1])
                # print(Generation_Tracker,min(Long))f
                Best.append(min(Long))
                Average_Average = sum(Long)/len(Long)
                self.Create_File.write((' '+str(min(Long))) + ' ' + str(Average_Average) + '\n' )
                Average.append(Average_Average)
                print('Generation ' + str(Generation_Tracker) + ' : ','The Average is: ', Average_Average)
                Generation_List.append(Generation_Tracker)
                # print(Generation_Tracker)
                Generation_Tracker = Generation_Tracker + 1
            self.Create_File.write('Average-Best-Fitness: ' +  str((sum(Best)/len(Best))) + '\n')
            self.Create_File.write('Average-Average-Fitness: ' +  str((sum(Average)/len(Average))) + '\n')
                
            print(min(Best), 'Long Long ' ,min(Long), float(min(Best))==float(min(Long)))
            plt.plot(Generation_List, Average)
            plt.show()

            Minimum = [i[-1] for i in Population_With_Fitness]
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
TSP = Travelling_Salesman(30,10,3000,0.3,10)
#Modified Paramters for FSP and fSP
# TSP = Travelling_Salesman(10,20,3000,0.3,10)


#For Truncations and FPS
# TSP = Travelling_Salesman(10,50,3000,1,10)

#For Binary Tournament and Fitness portionate scheme
# TSP = Travelling_Salesman(20,150,1000,0.9,10)
# TSP = Travelling_Salesman(20,40,1000,0.9,10)

print(TSP)
# for i in range(0,10):
TSP.Execute(Parent_Scheme='Binary_Tournament', Survivor_Scheme='Fitness_Proportionate_Selection', Crossover_Scheme='Two_Point_Crossover')



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








