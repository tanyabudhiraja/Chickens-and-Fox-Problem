class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.chickens = start_state[0] #chickens number
        self.foxes = start_state[1] #foxes number
        self.boat = start_state[2] #boat number
       
    def rules(self,state): #rules for what is a legal move 

        #defining chickens and foxes on both sides 
        chickens_left , foxes_left, boat = state 
        chickens_right = self.chickens-chickens_left
        foxes_right = self.foxes-foxes_left

        #number of chickens foxes and position of boat must be possible
        if not (0<= chickens_left <= self.chickens and 0<=foxes_left <= self.foxes and boat in (0,1)):
            return False 
        #return false if number of chicken foxes are not possible or if boat is not on either bank
        
        #foxes can never outnumber chickens (left)
        if chickens_left > 0 and foxes_left > chickens_left:
            return False 
        
        #foxes can never outnumber chickens (right)
        if chickens_right > 0 and foxes_right > chickens_right:
            return False

        #if all rules pass, return true
        else: 
            return True 

    # get successor states for the given state
    def get_successors(self, state):
        children=[] #list to store children
        if state[2]==0: #if boat is on the right
            transitions= [(2,0,1),(1,1,1), (0,2,1), (1,0,1), (0,1,1)] #possible moves
        else: #if boat is on the left 
            transitions= [(-2,0,-1),(-1,-1,-1), (0,-2,-1), (-1,0,-1), (0,-1,-1)] #possible moves

            #move 
        for transition in transitions:
            newstate = (state[0] + transition[0], state[1] + transition[1], state[2] + transition[2])

            #if a child follows the rules, add to list
            if self.rules(newstate)== True:
                children.append(newstate)
        return children


    #test to see if current state is the goal state
    def goal_test(self,state):
        if self.goal_state== state:
            return True
        else:
            return False

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


##  test code
if __name__ == "__main__":
    test_cp = FoxProblem((3, 3, 1))
    print(test_cp.get_successors((3, 3, 1)))
    #print(test_cp)
