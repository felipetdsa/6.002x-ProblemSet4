# -*- coding: utf-8 -*-
# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab
from ps3b_precompiled_27 import * 

''' 
Begin helper code
'''
#
#class NoChildException(Exception):
#    """
#    NoChildException is raised by the reproduce() method in the SimpleVirus
#    and ResistantVirus classes to indicate that a virus particle does not
#    reproduce. You can use NoChildException as is, you do not need to
#    modify/add any code.
#    """
#
#'''
#End helper code
#'''
#
##
## PROBLEM 2
##
#class SimpleVirus(object):
#
#    """
#    Representation of a simple virus (does not model drug effects/resistance).
#    """
#    def __init__(self, maxBirthProb, clearProb):
#        """
#        Initialize a SimpleVirus instance, saves all parameters as attributes
#        of the instance.        
#        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
#        clearProb: Maximum clearance probability (a float between 0-1).
#        """
#        #self.maxBirthProb = random.random()
#        #self.clearProb = random.random()
#        self.maxBirthProb = maxBirthProb
#        self.clearProb = clearProb
#        # TODO
#
#    def getMaxBirthProb(self):
#        """
#        Returns the max birth probability.
#        """
#        return self.maxBirthProb
#        # TODO
#
#    def getClearProb(self):
#        """
#        Returns the clear probability.
#        """
#        return self.clearProb
#        # TODO
#
#    def doesClear(self):
#        """ Stochastically determines whether this virus particle is cleared from the
#        patient's body at a time step. 
#        returns: True with probability self.getClearProb and otherwise returns
#        False.
#        """
#        if random.random() > self.clearProb:
#            return False
#        else:
#            return True
#        # TODO
#
#    
#    def reproduce(self, popDensity):
#        """
#        Stochastically determines whether this virus particle reproduces at a
#        time step. Called by the update() method in the Patient and
#        TreatedPatient classes. The virus particle reproduces with probability
#        self.maxBirthProb * (1 - popDensity).
#        
#        If this virus particle reproduces, then reproduce() creates and returns
#        the instance of the offspring SimpleVirus (which has the same
#        maxBirthProb and clearProb values as its parent).         
#
#        popDensity: the population density (a float), defined as the current
#        virus population divided by the maximum population.         
#        
#        returns: a new instance of the SimpleVirus class representing the
#        offspring of this virus particle. The child should have the same
#        maxBirthProb and clearProb values as this virus. Raises a
#        NoChildException if this virus particle does not reproduce.               
#        """
#        prob = self.maxBirthProb * (1 - popDensity)
#        #try:
#        #    random.random() < prob
#        #except NoChildException:
#        #    pass
#        #else:
#        #    return SimpleVirus(self.maxBirthProb, self.clearProb)
#        if random.random() < prob:
#            return SimpleVirus(self.maxBirthProb, self.clearProb)
#        else:
#            raise NoChildException
#            
#        # TODO
#
#
#
#class Patient(object):
#    """
#    Representation of a simplified patient. The patient does not take any drugs
#    and his/her virus populations have no drug resistance.
#    """    
#
#    def __init__(self, viruses, maxPop):
#        """
#        Initialization function, saves the viruses and maxPop parameters as
#        attributes.
#
#        viruses: the list representing the virus population (a list of
#        SimpleVirus instances)
#
#        maxPop: the maximum virus population for this patient (an integer)
#        """
#        self.viruses = viruses
#        self.maxPop = maxPop
#        # TODO
#
#    def getViruses(self):
#        """
#        Returns the viruses in this Patient.
#        """
#        return self.viruses
#        # TODO
#
#
#    def getMaxPop(self):
#        """
#        Returns the max population.
#        """
#        return self.maxPop
#        # TODO
#
#
#    def getTotalPop(self):
#        """
#        Gets the size of the current total virus population. 
#        returns: The total virus population (an integer)
#        """
#        return len(self.viruses)
#
#        # TODO        
#
#
#    def update(self):
#        """
#        Update the state of the virus population in this patient for a single
#        time step. update() should execute the following steps in this order:
#        
#        - Determine whether each virus particle survives and updates the list
#        of virus particles accordingly.   
#        
#        - The current population density is calculated. This population density
#          value is used until the next call to update() 
#        
#        - Based on this value of population density, determine whether each 
#          virus particle should reproduce and add offspring virus particles to 
#          the list of viruses in this patient.                    
#
#        returns: The total virus population at the end of the update (an
#        integer)
#        """
#        for v in self.viruses:
#            if v.doesClear():
#                self.viruses.remove(v)
#        density = len(self.viruses)/float(self.maxPop)
#        for virus in self.viruses:
#            try:
#                self.viruses.append(virus.reproduce(density))
#            except NoChildException:
#                pass
#            #density = len(self.viruses)/float(self.maxPop)
#            #if density >= 1:
#            #    print density
#            #    break
#        return len(self.viruses)
#        # TODO
#
#
#
##
## PROBLEM 3
##
#def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
#                          numTrials):
#    """
#    Run the simulation and plot the graph for problem 3 (no drugs are used,
#    viruses do not have any drug resistance).    
#    For each of numTrials trial, instantiates a patient, runs a simulation
#    for 300 timesteps, and plots the average virus population size as a
#    function of time.
#
#    numViruses: number of SimpleVirus to create for patient (an integer)
#    maxPop: maximum virus population for patient (an integer)
#    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
#    clearProb: Maximum clearance probability (a float between 0-1)
#    numTrials: number of simulation runs to execute (an integer)
#    """
#    vpop = []
#    for i in xrange(300):
#        vpop.insert(i, 0)
#    #p = infect_p(numViruses, maxBirthProb, clearProb, maxPop)
#    for t in xrange(numTrials):
#        #templst = []
#        p = infect_p(numViruses, maxBirthProb, clearProb, maxPop)
#        for i in xrange(300):
#            vpop[i] += (p.update() / float(numTrials))
#        #for i in range(300):
#        #    templst.append(p.update())
#        #    print templst
#        #vpop.append(templst)
#    #return vpop
#    pylab.plot(range(300), vpop)
#    pylab.title("SimpleVirus simulation")
#    pylab.xlabel("Time Steps")
#    pylab.ylabel("Average Virus Population")
#    pylab.legend(["Virus Population"], 0)
#    pylab.show()
#    
#
#def infect_p(numViruses, maxBirthProb, clearProb, maxPop):
#    vl =[]
#    for i in xrange(numViruses):
#        vl.append(SimpleVirus(maxBirthProb, clearProb))
#    return Patient(vl, maxPop)
#
#    # TODO
#
#
#
##
## PROBLEM 4
#
#class ResistantVirus(SimpleVirus):
#    """
#    Representation of a virus which can have drug resistance.
#    """   
#
#    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
#        """
#        Initialize a ResistantVirus instance, saves all parameters as attributes
#        of the instance.
#
#        maxBirthProb: Maximum reproduction probability (a float between 0-1)       
#
#        clearProb: Maximum clearance probability (a float between 0-1).
#
#        resistances: A dictionary of drug names (strings) mapping to the state
#        of this virus particle's resistance (either True or False) to each drug.
#        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
#        particle is resistant to neither guttagonol nor srinol.
#
#        mutProb: Mutation probability for this virus particle (a float). This is
#        the probability of the offspring acquiring or losing resistance to a drug.
#        """
#        SimpleVirus.__init__(self, maxBirthProb, clearProb)
#        #self.maxBirthProb = maxBirthProb
#        self.resistances = resistances
#        self.mutProb = mutProb        
#
#        # TODO
#
#
#    def getResistances(self):
#        """
#        Returns the resistances for this virus.
#        """
#        return self.resistances
#
#    def getMutProb(self):
#        """
#        Returns the mutation probability for this virus.
#        """
#        return self.mutProb
#        # TODO
#
#    def isResistantTo(self, drug):
#        """
#        Get the state of this virus particle's resistance to a drug. This method
#        is called by getResistPop() in TreatedPatient to determine how many virus
#        particles have resistance to a drug.       
#
#        drug: The drug (a string)
#
#        returns: True if this virus instance is resistant to the drug, False
#        otherwise.
#        """
#        return self.getResistances().get(drug)
#        
#        # TODO
#
#
#    def reproduce(self, popDensity, activeDrugs):
#        """
#        Stochastically determines whether this virus particle reproduces at a
#        time step. Called by the update() meth7od in the TreatedPatient class.
#
#        A virus particle will only reproduce if it is resistant to ALL the drugs
#        in the activeDrugs list. For example, if there are 2 drugs in the
#        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
#        then it will NOT reproduce.
#
#        Hence, if the virus is resistant to all drugs
#        in activeDrugs, then the virus reproduces with probability:      
#
#        self.maxBirthProb * (1 - popDensity).                       
#
#        If this virus particle reproduces, then reproduce() creates and returns
#        the instance of the offspring ResistantVirus (which has the same
#        maxBirthProb and clearProb values as its parent). The offspring virus
#        will have the same maxBirthProb, clearProb, and mutProb as the parent.
#
#        For each drug resistance trait of the virus (i.e. each key of
#        self.resistances), the offspring has probability 1-mutProb of
#        inheriting that resistance trait from the parent, and probability
#        mutProb of switching that resistance trait in the offspring.       
#
#        For example, if a virus particle is resistant to guttagonol but not
#        srinol, and self.mutProb is 0.1, then there is a 10% chance that
#        that the offspring will lose resistance to guttagonol and a 90%
#        chance that the offspring will be resistant to guttagonol.
#        There is also a 10% chance that the offspring will gain resistance to
#        srinol and a 90% chance that the offspring will not be resistant to
#        srinol.
#
#        popDensity: the population density (a float), defined as the current
#        virus population divided by the maximum population       
#
#        activeDrugs: a list of the drug names acting on this virus particle
#        (a list of strings).
#
#        returns: a new instance of the ResistantVirus class representing the
#        offspring of this virus particle. The child should have the same
#        maxBirthProb and clearProb values as this virus. Raises a
#        NoChildException if this virus particle does not reproduce.
#        """
#        prop_reproduce = (random.random() < self.maxBirthProb * (1 - popDensity))
#        is_resistant = True
#        for drug in activeDrugs:
#            if self.isResistantTo(drug):
#                is_resistant = True
#            else:
#                is_resistant = False
#                break
#        if not is_resistant or not prop_reproduce:
#            raise NoChildException
#        else:
#            nresistances = self.resistances.copy()
#            for key in nresistances.keys():
#                will_mutate = random.random() > 1 - self.mutProb
#                if will_mutate:
#                    if nresistances[key] == True:
#                        nresistances[key] = False
#                    else:
#                        nresistances[key] = True
#            return  ResistantVirus(self.maxBirthProb, self.clearProb, nresistances, self.mutProb)
#
#        # TODO
#
#            
#
#class TreatedPatient(Patient):
#    """
#    Representation of a patient. The patient is able to take drugs and his/her
#    virus population can acquire resistance to the drugs he/she takes.
#    """
#
#    def __init__(self, viruses, maxPop):
#        """
#        Initialization function, saves the viruses and maxPop parameters as
#        attributes. Also initializes the list of drugs being administered
#        (which should initially include no drugs).              
#
#        viruses: The list representing the virus population (a list of
#        virus instances)
#
#        maxPop: The  maximum virus population for this patient (an integer)
#        """
#        Patient.__init__(self, viruses, maxPop)
#        self.activeDrugs = []
#
#        # TODO
#
#
#    def addPrescription(self, newDrug):
#        """
#        Administer a drug to this patient. After a prescription is added, the
#        drug acts on the virus population for all subsequent time steps. If the
#        newDrug is already prescribed to this patient, the method has no effect.
#
#        newDrug: The name of the drug to administer to the patient (a string).
#
#        postcondition: The list of drugs being administered to a patient is updated
#        """
#        if newDrug not in self.activeDrugs:
#            self.activeDrugs.append(newDrug)
#        
#
#        # TODO
#
#
#    def getPrescriptions(self):
#        """
#        Returns the drugs that are being administered to this patient.
#
#        returns: The list of drug names (strings) being administered to this
#        patient.
#        """
#        return self.activeDrugs
#
#        # TODO
#
#
#    def getResistPop(self, drugResist):
#        """
#        Get the population of virus particles resistant to the drugs listed in
#        drugResist.       
#
#        drugResist: Which drug resistances to include in the population (a list
#        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])
#
#        returns: The population of viruses (an integer) with resistances to all
#        drugs in the drugResist list.
#        """
#        count = 0
#        for virus in self.viruses:
#            flag = False
#            for drug in drugResist:
#                if virus.isResistantTo(drug) == True:
#                    flag = True
#                elif virus.isResistantTo(drug) == False:
#                    flag = False
#                    break
#                else:
#                    flag = False
#                    #break
#            if flag == True:
#                count += 1
#        return count
#
#        # TODO
#
#
#    def update(self):
#        """
#        Update the state of the virus population in this patient for a single
#        time step. update() should execute these actions in order:
#
#        - Determine whether each virus particle survives and update the list of
#          virus particles accordingly
#
#        - The current population density is calculated. This population density
#          value is used until the next call to update().
#
#        - Based on this value of population density, determine whether each 
#          virus particle should reproduce and add offspring virus particles to 
#          the list of viruses in this patient.
#          The list of drugs being administered should be accounted for in the
#          determination of whether each virus particle reproduces.
#
#        returns: The total virus population at the end of the update (an
#        integer)
#        """
#        for v in self.viruses:
#            if v.doesClear():
#                self.viruses.remove(v)
#        density = len(self.viruses)/float(self.maxPop)
#        viruscopy = self.viruses[:]
#        for virus in viruscopy:
#            try:
#                self.viruses.append(virus.reproduce(density, self.activeDrugs))
#            except NoChildException:
#                pass
#            #density = len(self.viruses)/float(self.maxPop)
#            #if density >= 1:
#            #    print density
#            #    break
#        return len(self.viruses)
#
#        # TODO
#
#
#
##
## PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    vpop = []
    vguttag = []
    for i in xrange(300):
        vpop.insert(i, 0)
        vguttag.insert(i, 0)
    for t in xrange(numTrials):
        p = infect_person(numViruses, maxBirthProb, clearProb, maxPop, resistances, mutProb)
        #p.addPrescription('guttagonol')
        for i in xrange(150):
            vpop[i] += p.update()
            for virus in p.viruses:
                if virus.isResistantTo('guttagonol'):
                    vguttag[i] += 1           
        p.addPrescription('guttagonol')

        for i in xrange(150, 300):
            vpop[i] += p.update()
            for virus in p.viruses:
                if virus.isResistantTo('guttagonol'):
                    vguttag[i] += 1

    for i in range(300):
        vpop[i] = vpop[i] / float(numTrials)
        vguttag[i] = vguttag[i] / float(numTrials)

    pylab.plot(range(300), vpop)
    pylab.plot(range(300), vguttag)
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.legend(["Regular Virus", "Resistant Virus"], 0)
    pylab.show()
    

def infect_person(numViruses, maxBirthProb, clearProb, maxPop, resistances, mutProb):
    vl =[]
    for i in xrange(numViruses):
        vl.append(ResistantVirus(maxBirthProb, clearProb, resistances , mutProb))
    return TreatedPatient(vl, maxPop)

    # TODO
