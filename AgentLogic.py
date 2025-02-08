"""
Author: Harsh Vardhan Singh, Seattle University
Model-based Reflex Agent Program
"""

import csv
from csv import DictReader
from Actuators import Actuators
from Sensors import Sensors


class agentMain:

    def __init__(self, areaInput, settingInput):
        self.environment = self.loadArea(areaInput)
        self.settings = self.loadSettings(settingInput)
        self.sensors = Sensors(self.environment, self.power_tracker)
        self.actuators = Actuators(self.environment, self.power_tracker)
        self.x, self.y = 0, 0  # Default Starting Position


    # Returns a dictionary with environment data loaded from area.csv input file
    def loadArea(self, areaInput):

        areaData={}

        with open(areaInput, mode="r") as inputFile:
            readFile = csv.DictReader(inputFile)
            for row in readFile:
                x, y = int(row["Xcoordination"]), int(row["YCoordination"])
                areaData[(x,y)] = {
                    "DeltaL": int(row["DeltaL"]),
                    "DeltaR": int(row["DeltaR"]),
                    "DeltaU": int(row["DeltaU"]),
                    "DeltaD": int(row["DeltaD"]),
                    "Texture": row["Texture"],
                    "DustWeight": int(row["DustWeight"]) }

        return areaData


    # Returns a dictionary with settings data loaded from Setting.txt input file
    def loadSettings(self, settingInput):

        settingData = {}

        with open(settingInput, mode="r") as inputFile:
            readFile = inputFile.readlines()

            inputValue = [int(line.strip()) for line in readFile]

        settingData = { "Time-Duration" : inputValue[0],
                            "Power-Cons-90Rotate": inputValue[1],
                        "Power-Cons-UnitMove": inputValue[2],
                        "Power-Cons-NormalPressure": inputValue[3],
                        "Power-Cons-HighPressure": inputValue[4],
                        "Power-Cons-UnitTime": inputValue[5],
                        "Power-Cons-SensorRead": inputValue[6],
                        "Power-Cons-Other": inputValue[7]}

        return settingData


    # main agent logic
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