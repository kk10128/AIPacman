# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def recursiveDFS(current, problem, visited, actions):
    visited[current] = 1
    if problem.isGoalState(current):
        return True, actions

    for(child, direction, cost) in problem.getSuccessors(current):
        if(child in visited) and (visited[child] == 1):
            continue
        actions.append(direction)
        destination, correct = recursiveDFS(child, problem, visited, actions)
        if(destination): 
            return True, correct
        actions.pop()

    return False, None

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    _, actions = recursiveDFS(problem.getStartState(), problem, {}, [])
    return actions


    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    queue = Queue()
    queue.push(problem.getStartState())
    visited = []
    tempPath = []
    currentPath = Queue()
    currentPos = queue.pop()
    path = []
    while not problem.isGoalState(currentPos):
        if currentPos not in visited: 
            visited.append(currentPos)
            successors = problem.getSuccessors(currentPos)
            for child, direction, cost in successors: 
                queue.push(child)
                tempPath = path + [direction]
                currentPath.push(tempPath)
        currentPos = queue.pop()
        path = currentPath.pop()
    return path
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue
    queue = PriorityQueue()
    queue.push(problem.getStartState(), 0)
    visited = []
    tempPath = []
    path = []
    currentPath = PriorityQueue()
    currentPos = queue.pop()
    while not problem.isGoalState(currentPos):
        if currentPos not in visited: 
            visited.append(currentPos)
            successors = problem.getSuccessors(currentPos)
            for child, direction, cost in successors: 
                tempPath = path + [direction]
                costLeft = problem.getCostOfActions(tempPath)
                if child not in visited: 
                    queue.push(child, costLeft)
                    currentPath.push(tempPath, costLeft)
        currentPos = queue.pop()
        path = currentPath.pop()

    return path

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    x1, y1 = state
    x2, y2 = problem.goal
    return abs(x1 - x2) + abs(y1 - y2)

    #return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    queue = PriorityQueue()
    queue.push(problem.getStartState(), 0)
    currentPos = queue.pop()
    visited = []
    tempPath = []
    path = []
    currentPath = PriorityQueue()
    path = []
    while not problem.isGoalState(currentPos):
        if currentPos not in visited: 
            visited.append(currentPos)
            successors = problem.getSuccessors(currentPos)
            for child, direction, cost in successors:
                tempPath = path + [direction]
                costToGo = problem.getCostOfActions(tempPath) + heuristic(child, problem)
                if child not in visited: 
                    queue.push(child, costToGo)
                    currentPath.push(tempPath, costToGo)
        currentPos = queue.pop()
        path = currentPath.pop()
    return path

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
