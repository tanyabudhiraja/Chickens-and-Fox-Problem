class SearchSolution:
    def __init__(self, problem, search_method):
        self.problem_name = str(problem) #name of problem
        self.search_method = search_method #which algorithm used
        self.path = [] #blank path
        self.nodes_visited = 0 #counter

    def __str__(self):
        string = "----\n" #divider line
        string += "{:s}\n" #insert string later
        string += "attempted with search method {:s}\n" 

        if len(self.path) > 0:

            string += "number of nodes visited: {:d}\n"
            string += "solution length: {:d}\n"
            string += "path: {:s}\n"

            string = string.format(self.problem_name, self.search_method,
                self.nodes_visited, len(self.path), str(self.path))
        else:
            string += "no solution found after visiting {:d} nodes\n"
            string = string.format(self.problem_name, self.search_method, self.nodes_visited)

        return string
