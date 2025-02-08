"""
Author: Harsh Vardhan Singh, Seattle University
Model-based Reflex Agent
"""

class agentMain:
    print("Hello")

    def __init__(self):
        self.name = 0

    def modelBasedReflexAgent(self, percept):

        state = None #the agent's current conception of the world state

        model = None #a description of how the next state depends on the current
                    # state and action

        # a set of condition-action rules
        rule = dict()

        action = None # the most recent action, initially none

        #Update the agent's internal state based on the current percept and
        # previous action
        state = self.updateState(state, action, percept, model)

        # Match the current state against the condition-action rules
        rule = self.ruleMatch(state, rule)

        # Select the action prescribed by the matched rule
        action = rule.get(0)

        #Return the selected action
        return action

    def updateState(state, action, percept, model):
        x = 0

    def ruleMatch(state, rule):
        x = 0