import matplotlib.pyplot as plt
import matplotlib.pyplot as np

import itertools
import random
import copy
import time


class Schelling:
    def __init__(self, width, height, empty_ratio, similarity_threshold, n_iterations, races = 2):
        self.width = width 
        self.height = height 
        self.races = races
        self.empty_ratio = empty_ratio
        self.similarity_threshold = similarity_threshold
        self.n_iterations = n_iterations
        self.empty_houses = []
        self.agents = {}
    
    def populate(self):
        self.all_houses = list(itertools.product(range(self.width),range(self.height)))
        random.shuffle(self.all_houses)

        self.n_empty = int( self.empty_ratio * len(self.all_houses) )
        self.empty_houses = self.all_houses[:self.n_empty]

        self.remaining_houses = self.all_houses[self.n_empty:]
        houses_by_race = [self.remaining_houses[i::self.races] for i in range(self.races)]
        for i in range(self.races):
            #create agents for each race
            self.agents = dict(
                                self.agents.items() |
                                dict(zip(houses_by_race[i], [i+1]*len(houses_by_race[i]))).items()
                            )
    

    def is_unsatisfied(self, x, y):

        race = self.agents[(x,y)]
        count_similar = 0
        count_different = 0

        if x > 0 and y > 0 and (x-1, y-1) not in self.empty_houses:
            if self.agents[(x-1, y-1)] == race:
                count_similar += 1
            else:
                count_different += 1
        if y > 0 and (x,y-1) not in self.empty_houses:
            if self.agents[(x,y-1)] == race:
                count_similar += 1
            else:
                count_different += 1
        if x < (self.width-1) and y > 0 and (x+1,y-1) not in self.empty_houses:
            if self.agents[(x+1,y-1)] == race:
                count_similar += 1
            else:
                count_different += 1
        if x > 0 and (x-1,y) not in self.empty_houses:
            if self.agents[(x-1,y)] == race:
                count_similar += 1
            else:
                count_different += 1        
        if x < (self.width-1) and (x+1,y) not in self.empty_houses:
            if self.agents[(x+1,y)] == race:
                count_similar += 1
            else:
                count_different += 1
        if x > 0 and y < (self.height-1) and (x-1,y+1) not in self.empty_houses:
            if self.agents[(x-1,y+1)] == race:
                count_similar += 1
            else:
                count_different += 1        
        if x > 0 and y < (self.height-1) and (x,y+1) not in self.empty_houses:
            if self.agents[(x,y+1)] == race:
                count_similar += 1
            else:
                count_different += 1        
        if x < (self.width-1) and y < (self.height-1) and (x+1,y+1) not in self.empty_houses:
            if self.agents[(x+1,y+1)] == race:
                count_similar += 1
            else:
                count_different += 1

        if (count_similar+count_different) == 0:
            return False
        else:
            return float(count_similar)/(count_similar+count_different) < self.similarity_threshold
    

    def neighborhood(self,x,y,empty_house):

        if (x-1, y-1) == empty_house:
            return True
        if (x,y-1) == empty_house:
            return True
        if empty_house == (x+1,y-1) :
            return True
        if empty_house == (x-1,y):
            return  True
        if empty_house == (x+1,y):
           return True
        if empty_house == (x-1,y+1):
            return  True
        if empty_house == (x,y+1):
            return True
        if empty_house == (x+1,y+1):
           return True
        
        return False


    def update(self,condition):
        for i in range(self.n_iterations):
            self.old_agents = copy.deepcopy(self.agents)
            n_changes = 0
            for agent in self.old_agents:
                if self.is_unsatisfied(agent[0], agent[1]):
                    n_changes += 1
                    agent_race = self.agents[agent]
                    empty_house = random.choice(self.empty_houses)
                    if(condition==1 and not self.neighborhood(agent[0],agent[1],empty_house)):
                        continue       
                    self.agents[empty_house] = agent_race
                    del self.agents[agent]
                    self.empty_houses.remove(empty_house)
                    self.empty_houses.append(agent)           
            print(n_changes)
            if n_changes == 0:
                break


    def move_to_empty(self, x, y):
        race = self.agents[(x,y)]
        empty_house = random.choice(self.empty_houses)
        self.updated_agents[empty_house] = race
        del self.updated_agents[(x, y)]
        self.empty_houses.remove(empty_house)
        self.empty_houses.append((x, y))

    def plot(self, title, file_name):
        plt.clf()
        fig, ax = plt.subplots()
        #If you want to run the simulation with more than 7 colors, you should set agent_colors accordingly
        agent_colors = {1:'b', 2:'r', 3:'g', 4:'c', 5:'m', 6:'y', 7:'k'}
        for agent in self.agents:
            ax.scatter(agent[0]+0.5, agent[1]+0.5, color=agent_colors[self.agents[agent]])

        ax.set_title(title, fontsize=10, fontweight='bold')
        ax.set_xlim([0, self.width])
        ax.set_ylim([0, self.height])
        ax.set_xticks([])
        ax.set_yticks([])
        plt.savefig(file_name)

    def calculate_similarity(self):
        similarity = []
        for agent in self.agents:
            count_similar = 0
            count_different = 0
            x = agent[0]
            y = agent[1]
            race = self.agents[(x,y)]
            if x > 0 and y > 0 and (x-1, y-1) not in self.empty_houses:
                if self.agents[(x-1, y-1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if y > 0 and (x,y-1) not in self.empty_houses:
                if self.agents[(x,y-1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if x < (self.width-1) and y > 0 and (x+1,y-1) not in self.empty_houses:
                if self.agents[(x+1,y-1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if x > 0 and (x-1,y) not in self.empty_houses:
                if self.agents[(x-1,y)] == race:
                    count_similar += 1
                else:
                    count_different += 1        
            if x < (self.width-1) and (x+1,y) not in self.empty_houses:
                if self.agents[(x+1,y)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            if x > 0 and y < (self.height-1) and (x-1,y+1) not in self.empty_houses:
                if self.agents[(x-1,y+1)] == race:
                    count_similar += 1
                else:
                    count_different += 1        
            if x > 0 and y < (self.height-1) and (x,y+1) not in self.empty_houses:
                if self.agents[(x,y+1)] == race:
                    count_similar += 1
                else:
                    count_different += 1        
            if x < (self.width-1) and y < (self.height-1) and (x+1,y+1) not in self.empty_houses:
                if self.agents[(x+1,y+1)] == race:
                    count_similar += 1
                else:
                    count_different += 1
            try:
                similarity.append(float(count_similar)/(count_similar+count_different))
            except:
                similarity.append(1)
        return sum(similarity)/len(similarity)
    

    def satisfatory_percentage(self,races,similarity_threshold,empty_ratio):
        x = list(range(1,races+1))
        x_names = [str(z) for z in x][:-1]

        x_names = x_names + ["total"]
        y = []
        plt.clf()
        total_unsatisfy = 0
        total = 0 
        for i in range(1,races):
            total_raca = 0
            unsatisfy = 0 
            for agent in self.agents:
                race = self.agents[agent]
                if (i == race):
                    if  self.is_unsatisfied(agent[0], agent[1]):
                        unsatisfy = unsatisfy + 1
                        total_unsatisfy = total_unsatisfy + 1
                    total_raca = total_raca + 1 
                    total = total + 1   
            #print(total_raca," ",unsatisfy,' ',race ) 
            pergentage = unsatisfy/total_raca * 100
            y = y+[pergentage]

        pergentage_total  = total_unsatisfy/total * 100
        y = y+[pergentage_total]

        y_min =min (y) - 2.5
        y_max =max (y) + 2.5
        
        print(y)

        if(y_min < 0):
            y_min = 0

        if(y_max > 100):
            y_max = 100

        plt.ylim(y_min,y_max)
        plt.xticks(x, x_names)
        plt.bar(x, y) 
        plt.xlabel('x - races') 
        plt.ylabel('y - percentage unsatisfied') 
        title = "race unsatisfied with " + str(similarity_threshold) + " and " + str(empty_ratio) + "% empty_ratio"
        plt.title(title) 
        plt.savefig(title+".png") 
    
similarity_threshold = 0.50
width = 35
height = 35 
empty_ratio = 0.01
n_iterations = 500
races = 2
condition=0
docs = open("simularity.txt",'a')

for i in range (2,8):
    races = i

    schelling_1 = Schelling(width, height,empty_ratio,similarity_threshold, n_iterations, races)
    schelling_1.populate()
    schelling_1.plot('Schelling Model with '+str(races)+' colors: Initial State', 'schelling_2_initial '+str(races)+'.png')

    schelling_1.update(condition)
    write = "calculate_similarity race "+str(races)+": "+ str(schelling_1.calculate_similarity())+"\n"
    docs.write(write)
    #print(docs.read())
    titlefinal='Schelling Model with'+str(races)+'colors: Final State with Similarity Threshold '+str(similarity_threshold*100)+'%'
    schelling_1.plot(titlefinal, ('schelling_2_ with '+str(races)+"color "+str(similarity_threshold*100)+'%''_final.png'))
    schelling_1.satisfatory_percentage(i+1,similarity_threshold,empty_ratio)