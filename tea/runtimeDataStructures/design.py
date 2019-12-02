import attr
from typing import Dict

from tea.global_vals import *
from tea.runtimeDataStructures.variable import AbstractVariable, NominalVariable, OrdinalVariable, NumericVariable


class AbstractDesign(object):
    
    @staticmethod
    def create(attributes, variables):
        if STUDY_TYPE in attributes: 
            study = attributes[STUDY_TYPE]
            if study == OBS_STUDY: 
                return ObservationalDesign(attributes, variables)
            elif study == EXPERIMENT: 
                return ExperimentDesign(attributes, variables)
            else:
                raise ValueError(f"Study type is not supported: {study}. Study can be {OBS_STUDY} or {EXPERIMENT}.")
        else: 
            raise ValueError(f"Missing study type information! Study can be {OBS_STUDY} or {EXPERIMENT}.")

@attr.s(init=False)
class ObservationalDesign(AbstractDesign): 
    xs : list # list of Variables
    ys : list # list of Variables

    def __init__(self, attributes, variables): 
        # private function for getting variable by @param name from list of @param variables
        def get_variable(variables: list, name: str):  
            # Assume that name is a str
            assert(isinstance(name, str))
            for var in variables: 
                assert(isinstance(var, AbstractVariable))
                if AbstractVariable.get_name(var) == name: 
                    return var

        for key, value in attributes.items():
            if key in OBS_X: 
                # Assign observational x variable, must be a list first
                if isinstance(value, list): 
                    self.xs = [get_variable(variables, v) for v in value]
                    # TODO make sure to get the variable from the variables list, assign Variable object
                elif isinstance(value, str): 
                    self.xs = [get_variable(variables, value)]
                else: 
                    raise ValueError(f"{value} for {key} is neither a list nor a string.")
            elif key in OBS_Y: 
                if isinstance(value, list): 
                    self.ys = [get_variable(variables, v) for v in value]
                elif isinstance(value, str): 
                    self.ys = [get_variable(variables, value)]
                else: 
                    raise ValueError(f"{value} for {key} is neither a list nor a string.")
            elif key == STUDY_TYPE: 
                pass # already handled to AbstractDesign
            elif key in EXP_X: 
                raise ValueError(f"{key} is not available in an {OBS_STUDY}. Did you mean to say the study is an {EXPERIMENT} or that the variable/s are one of {OBS_X}?")
            elif key in EXP_Y: 
                raise ValueError(f"{key} is not available in an {OBS_STUDY}. Did you mean to say the study is an {EXPERIMENT} or that the variable/s are one of {OBS_Y}?")
            else: 
                print(f"Extra aspects of study design are not necessary and not considered:{key}, {value}")
            
@attr.s(init=False)
class ExperimentDesign(AbstractDesign):
    xs : list # list of Variables
    ys : list # list of Variables

    def __init__(self, attributes, variables): 
        # private function for getting variable by @param name from list of @param variables
        def get_variable(variables: list, name: str):  
            # Assume that name is a str
            assert(isinstance(name, str))
            for var in variables: 
                assert(isinstance(var, AbstractVariable))
                if AbstractVariable.get_name(var) == name: 
                    return var

        for key, value in attributes.items():
            if key in EXP_X: 
                # Assign observational x variable, must be a list first
                if isinstance(value, list): 
                    self.xs = [get_variable(variables, v) for v in value]
                    # TODO make sure to get the variable from the variables list, assign Variable object
                elif isinstance(value, str): 
                    self.xs = [get_variable(variables, value)]
                else: 
                    raise ValueError(f"{value} for {key} is neither a list nor a string.")
            elif key in EXP_Y: 
                if isinstance(value, list): 
                    self.ys = [get_variable(variables, v) for v in value]
                elif isinstance(value, str): 
                    self.ys = [get_variable(variables, value)]
                else: 
                    raise ValueError(f"{value} for {key} is neither a list nor a string.")
            elif key == STUDY_TYPE: 
                pass # already handled to AbstractDesign
            elif key in OBS_X: 
                raise ValueError(f"{key} is not available in an {EXPERIMENT}. Did you mean to say the study is an {OBS_STUDY} or that the variable/s are one of {EXP_X}?")
            elif key in OBS_Y: 
                raise ValueError(f"{key} is not available in an {EXPERIMENT}. Did you mean to say the study is an {OBS_STUDY} or that the variable/s are one of {EXP_Y}?")
            else: 
                print(f"Extra aspects of study design are not necessary and not considered:{key}, {value}")

    def __eq__(self, other): 
        if len(self.xs) == len(other.xs):
            if len(self.ys) == len(other.ys):
                xs_found = [x in other.xs for x in self.xs]
                ys_found = [y in other.ys for y in self.ys]

                return all(xs_found) and all(ys_found)
                    
        return False
    


 




  