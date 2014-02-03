#! /usr/bin/env python

"""
Demo script for a RSVP experiment

christophe@pallier.org
"""

from expyriment import design, control, stimuli, io, misc

import random, csv


#%% Load the stimuli 

import csv
sequences = [ i for i in csv.reader(open('sentences.txt'), delimiter='\t') ]


#%%

exp = design.Experiment(name="First Experiment")

# comment out the following line to get in real mode
control.set_develop_mode(True)

control.initialize(exp)


#%%

block = design.Block(name="block1")

for line in sequences:
    trial = design.Trial()
    stim = []

    for w in line:
        stim = stimuli.TextLine(w.decode('utf-8'),
                            text_size=32)
        trial.add_stimulus(stim)
    
    block.add_trial(trial)
    
exp.add_block(block)

#%%

control.start(exp)

for block in exp.blocks:
    for trial in block.trials:
        for stim in trial.stimuli:
            stim.preload()
            stim.present()
            exp.clock.reset_stopwatch()
            exp.clock.wait(300 - exp.clock.stopwatch_time)
            exp.screen.clear()
            exp.screen.update()
            keys = exp.keyboard.read_out_buffered_keys()
            print(keys)

        exp.clock.wait(3000)
        #exp.data.add([keys])
#        button, rt = exp.keyboard.wait()
#       exp.data.add([trial.get_factor("Position"), 
#                      button, rt])
        

### 

control.end()
