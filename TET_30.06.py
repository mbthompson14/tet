#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on juli 01, 2022, at 15:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'TET_test'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\sanderds\\Dropbox\\shared\\Old structure\\Tasks\\TET\\TET_psychopy\\TET_30.06.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='0.7255, 0.7255, 0.7255', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
import random
import time

#Hide mouse
win.mouseVisible = False

# default (fullscreen) image size in pixels
x = win.monitor.getSizePix()[0]
y = win.monitor.getSizePix()[1]
img_size = (x, y)

# initialize variables, will be updated
attack_dur = 0.25
last_stim = 0

# Setting up the serial port connection for triggering
# the biopac and digitimer system. 

import serial
ser = serial.Serial("COM4",115200, timeout=1)
print(ser.name)

# Check if the port is open, if it was not, open it.
if(ser.isOpen() == False):
    ser.open()

# set all pins to 0
ser.write(str.encode('00'))


# set up data output 

# custom VAS questionnaire file
# File name
custom_results_file = _thisDir + os.sep + u'data/%s_%s' % \
    (expInfo['participant'], expInfo['date']) + "_questionnaire_custom.csv"
# open file for writing
custom_q = open(custom_results_file,'w')
# write column names
custom_q.write('participant,stage,condition,distance,attack,startle,item_name,\
item_text,response,RT\n')

# Initialize components for Routine "intro_1"
intro_1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Welcome! During this experiment you will see large and small images which will sometimes grow in size. When the small images start to grow, it will be your job to prevent them from reaching full size by pressing the spacebar as fast as possible\n\n<push the right arrow button to see an example of a large image>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "img_example"
img_exampleClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', units='pix', 
    image='pics2/Safe2.png', mask=None,
    ori=0.0, pos=(0, 0), size=img_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "intro_2"
intro_2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='If you push the spacebar fast enough, the images will not reach full size.\n\nWhen the picture starts very small, you will have more time to push the spacebar, and prevent the picture from reaching full size.\n\n<push the right arrow button for an example>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "antic_ex_1"
antic_ex_1Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='pix', 
    image='pics2/Threat2.png', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "attack_ex_1"
attack_ex_1Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', units='pix', 
    image='pics2/Threat2.png', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "intro_3"
intro_3Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='When the picture starts slightly bigger, you will have less time to push the spacebar. Which is why you will have to react faster.\n\n<push the right arrow button for an example>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "antic_ex_2"
antic_ex_2Clock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', units='pix', 
    image='pics2/Safe2.png', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "attack_ex_2"
attack_ex_2Clock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', units='pix', 
    image='pics2/Safe2.png', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "intro_4"
intro_4Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='During this task you will hear loud screams. When you see a purple image, you are safe and you will not hear a scream. When you see an orange image, there is a chance that you will hear a scream. ',
    font='Open Sans',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='<push the right arrow button>',
    font='Open Sans',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
safe_text = visual.TextStim(win=win, name='safe_text',
    text='Safe',
    font='Open Sans',
    pos=(-0.3, -0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
scream_text = visual.TextStim(win=win, name='scream_text',
    text='SCREAM',
    font='Open Sans',
    pos=(0.3, -0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='pics2/Safe2.png', mask=None,
    ori=0.0, pos=(-0.3, 0), size=(0.15, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='pics2/Threat2.png', mask=None,
    ori=0.0, pos=(0.3, 0), size=(0.15, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "intro_5"
intro_5Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='The orange images will only give a scream when they reach full size. So, by preventing the orange images from reaching full size you will prevent the scream.\n\nSometimes, an orange image is already full size when it is shown to you. In these cases, there is a chance that you will get to hear the loud scream, and you cannot prevent this. \n\n<push the right arrow button to see the full size orange image>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "img_example_2"
img_example_2Clock = core.Clock()
image_9 = visual.ImageStim(
    win=win,
    name='image_9', units='pix', 
    image='pics2/Threat2.png', mask=None,
    ori=0.0, pos=(0, 0), size=img_size,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "intro_6"
intro_6Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Purple images will never give loud screams, but for this experiment it remains very important that you also prevent these images from growing in size. \n\nSo, at all times during this experiment, you should push the spacebar as fast as possible when you see that an image starts to grow in size. \n\n<push the right arrow button>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "start_practice"
start_practiceClock = core.Clock()
practice_text = visual.TextStim(win=win, name='practice_text',
    text='You are going to practice first. Here you will NOT get to hear the loud screams yet. However, you will see on the screen when you would get to hear the loud scream if it was the real experiment. \n\nTry to push the spacebar as fast as possible when the images grow in size. \n\nPlease look at the middle of the screen and move as little as possible. \n\n<push the right arrow button to start>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "anticipation"
anticipationClock = core.Clock()
antic_img = visual.ImageStim(
    win=win,
    name='antic_img', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
antic_resp = keyboard.Keyboard()
startle_sound = sound.Sound('sounds/whitenoise.wav', secs=-1, stereo=True, hamming=True,
    name='startle_sound')
startle_sound.setVolume(1.0)

# Initialize components for Routine "too_early"
too_earlyClock = core.Clock()
too_early_text = visual.TextStim(win=win, name='too_early_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "attack"
attackClock = core.Clock()
attack_img = visual.ImageStim(
    win=win,
    name='attack_img', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
attack_resp = keyboard.Keyboard()
loud_scream = sound.Sound('sounds/scream.wav', secs=1.0, stereo=True, hamming=True,
    name='loud_scream')
loud_scream.setVolume(1.0)
weak_scream = sound.Sound('sounds/screamweak.wav', secs=1.0, stereo=True, hamming=True,
    name='weak_scream')
weak_scream.setVolume(1.0)

# Initialize components for Routine "attack_feedback"
attack_feedbackClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "intro_7"
intro_7Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='That concludes the first practice phase of this experiment.\n\nAs explained before, you will hear loud screams and white noise in the real experiment. To get acquainted with these sounds you will now first hear a white noise. Afterwards we ask you to indicate how unpleasant this sound was for you.\n\nPlease put the headphones on now.\n\n<push the right arrow button to hear the sound>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "startle_ex"
startle_exClock = core.Clock()
startle_sound_ex = sound.Sound('sounds/whitenoise.wav', secs=2, stereo=True, hamming=True,
    name='startle_sound_ex')
startle_sound_ex.setVolume(1.0)

# Initialize components for Routine "rating_startle_ex"
rating_startle_exClock = core.Clock()
startle_slider = visual.Slider(win=win, name='startle_slider',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.1), units=None,
    labels=("neutral", "very unpleasant"), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
Instructions_scream_2 = visual.TextStim(win=win, name='Instructions_scream_2',
    text='How unpleasant was the sound that you heard?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "intro_8"
intro_8Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Next, you can get acquainted with the loud scream\n\n<push the right arrow button to hear the loud scream>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "scream_ex"
scream_exClock = core.Clock()
startle_sound_ex_2 = sound.Sound('sounds/scream.wav', secs=2, stereo=True, hamming=True,
    name='startle_sound_ex_2')
startle_sound_ex_2.setVolume(1.0)

# Initialize components for Routine "rating_scream_ex"
rating_scream_exClock = core.Clock()
startle_slider_2 = visual.Slider(win=win, name='startle_slider_2',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.1), units=None,
    labels=("neutral", "very unpleasant"), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
Instructions_scream_3 = visual.TextStim(win=win, name='Instructions_scream_3',
    text='How unpleasant was the scream that you heard?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "start_habituation"
start_habituationClock = core.Clock()
hab_text = visual.TextStim(win=win, name='hab_text',
    text='You will now start the second practice round. During this you will hear the white noises, and a low-volume version of the scream. In the real experiment, the scream will be played at full volume. \n\nAfter each trial you will also see relief and unpleasantness ratings. These rating screens will only be presented for 4 seconds. So don’t think too long, but try to answer spontaneously.\n\nPlease push the spacebar as fast as possible when an image starts growing in size. \n\nPlease look at the middle of the screen and try to move as little as possible.\n\nWhen you start the practice trials you will first hear the low-volume version of the scream to get acquainted with that sound too. Then the practice round will immediately start.\n\n<please notify the researcher before continuing>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "screamweak_ex"
screamweak_exClock = core.Clock()
weak_scream_ex = sound.Sound('sounds/screamweak.wav', secs=1.0, stereo=True, hamming=True,
    name='weak_scream_ex')
weak_scream_ex.setVolume(1.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "anticipation"
anticipationClock = core.Clock()
antic_img = visual.ImageStim(
    win=win,
    name='antic_img', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
antic_resp = keyboard.Keyboard()
startle_sound = sound.Sound('sounds/whitenoise.wav', secs=-1, stereo=True, hamming=True,
    name='startle_sound')
startle_sound.setVolume(1.0)

# Initialize components for Routine "attack"
attackClock = core.Clock()
attack_img = visual.ImageStim(
    win=win,
    name='attack_img', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
attack_resp = keyboard.Keyboard()
loud_scream = sound.Sound('sounds/scream.wav', secs=1.0, stereo=True, hamming=True,
    name='loud_scream')
loud_scream.setVolume(1.0)
weak_scream = sound.Sound('sounds/screamweak.wav', secs=1.0, stereo=True, hamming=True,
    name='weak_scream')
weak_scream.setVolume(1.0)

# Initialize components for Routine "rating_relief"
rating_reliefClock = core.Clock()
relief_slider = visual.Slider(win=win, name='relief_slider',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.1), units=None,
    labels=("neutral", "very pleasant"), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
Instructions_relief = visual.TextStim(win=win, name='Instructions_relief',
    text='How pleasant was the relief that you felt?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rating_scream"
rating_screamClock = core.Clock()
scream_slider = visual.Slider(win=win, name='scream_slider',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.1), units=None,
    labels=("neutral", "very unpleasant"), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
Instructions_scream = visual.TextStim(win=win, name='Instructions_scream',
    text='How unpleasant was the scream that you heard?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "start_real_task"
start_real_taskClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='The real experiment will start automatically in a few seconds.\n\nRemember to always push the spacebar as fast as you can when you see a picture growing in size.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "rest"
restClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "anticipation"
anticipationClock = core.Clock()
antic_img = visual.ImageStim(
    win=win,
    name='antic_img', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
antic_resp = keyboard.Keyboard()
startle_sound = sound.Sound('sounds/whitenoise.wav', secs=-1, stereo=True, hamming=True,
    name='startle_sound')
startle_sound.setVolume(1.0)

# Initialize components for Routine "attack"
attackClock = core.Clock()
attack_img = visual.ImageStim(
    win=win,
    name='attack_img', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
attack_resp = keyboard.Keyboard()
loud_scream = sound.Sound('sounds/scream.wav', secs=1.0, stereo=True, hamming=True,
    name='loud_scream')
loud_scream.setVolume(1.0)
weak_scream = sound.Sound('sounds/screamweak.wav', secs=1.0, stereo=True, hamming=True,
    name='weak_scream')
weak_scream.setVolume(1.0)

# Initialize components for Routine "rating_relief"
rating_reliefClock = core.Clock()
relief_slider = visual.Slider(win=win, name='relief_slider',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.1), units=None,
    labels=("neutral", "very pleasant"), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
Instructions_relief = visual.TextStim(win=win, name='Instructions_relief',
    text='How pleasant was the relief that you felt?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rating_scream"
rating_screamClock = core.Clock()
scream_slider = visual.Slider(win=win, name='scream_slider',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.1), units=None,
    labels=("neutral", "very unpleasant"), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
Instructions_scream = visual.TextStim(win=win, name='Instructions_scream',
    text='How unpleasant was the scream that you heard?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_1"
end_1Clock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='This is the end of the task.\n\nA few questions will be asked now.\n\nYou will see each image from the task again, but NO loud noises will be presented.\n\n<push the right arrow button to start>',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "end_imgs"
end_imgsClock = core.Clock()
end_img = visual.ImageStim(
    win=win,
    name='end_img', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "end_rating_fear"
end_rating_fearClock = core.Clock()
fear_slider = visual.Slider(win=win, name='fear_slider',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.1), units=None,
    labels=("not afraid", "very afraid"), ticks=(0, 100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
Instructions_fear = visual.TextStim(win=win, name='Instructions_fear',
    text='How afraid did you feel when you saw this picture?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_rating_pleasant"
end_rating_pleasantClock = core.Clock()
pleasant_slider = visual.Slider(win=win, name='pleasant_slider',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.1), units=None,
    labels=("unpleasant", "neutral", "very pleasant"), ticks=(0, 50, 100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='Black', fillColor='Red', borderColor='Black', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
Instructions_pleasant = visual.TextStim(win=win, name='Instructions_pleasant',
    text='How pleasant did you find this picture?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_2"
end_2Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Thank you very much for participating in this experiment! Please notify the researcher.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
#Hide mouse
win.mouseVisible = False
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro_1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
intro_1Components = [text_2, key_resp_3]
for thisComponent in intro_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_1"-------
while continueRoutine:
    # get current time
    t = intro_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_1"-------
for thisComponent in intro_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "img_example"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
img_exampleComponents = [image_2]
for thisComponent in img_exampleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
img_exampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "img_example"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = img_exampleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=img_exampleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    if image_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            image_2.tStop = t  # not accounting for scr refresh
            image_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
            image_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in img_exampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "img_example"-------
for thisComponent in img_exampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)

# ------Prepare to start Routine "intro_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
intro_2Components = [text_3, key_resp_4]
for thisComponent in intro_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_2"-------
while continueRoutine:
    # get current time
    t = intro_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_2"-------
for thisComponent in intro_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "antic_ex_1"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
img_size = (x/16, y/16)
image_4.setSize(img_size)
# keep track of which components have finished
antic_ex_1Components = [image_4]
for thisComponent in antic_ex_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
antic_ex_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "antic_ex_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = antic_ex_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=antic_ex_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    if image_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_4.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_4.tStop = t  # not accounting for scr refresh
            image_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
            image_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in antic_ex_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "antic_ex_1"-------
for thisComponent in antic_ex_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)

# ------Prepare to start Routine "attack_ex_1"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
frame = 1
# find the total number of frames
total_frames = (0.25*4)*expInfo['frameRate']
# keep track of which components have finished
attack_ex_1Components = [image_3]
for thisComponent in attack_ex_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
attack_ex_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "attack_ex_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = attack_ex_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=attack_ex_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    if image_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_3.tStop = t  # not accounting for scr refresh
            image_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
            image_3.setAutoDraw(False)
    if image_3.status == STARTED:  # only update if drawing
        image_3.setSize(img_size, log=False)
    # calculate new dimensions of the image for each frame
    curr_x = x/16 + frame*(x-x/16)/total_frames
    curr_y = y/16 + frame*(y-y/16)/total_frames
    # apply new dimensions
    img_size = (curr_x, curr_y)
    frame = frame + 1
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in attack_ex_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "attack_ex_1"-------
for thisComponent in attack_ex_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)

# ------Prepare to start Routine "intro_3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
intro_3Components = [text_4, key_resp_5]
for thisComponent in intro_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_3"-------
while continueRoutine:
    # get current time
    t = intro_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_3"-------
for thisComponent in intro_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "antic_ex_2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
img_size = (x/2, y/2)
image_5.setSize(img_size)
# keep track of which components have finished
antic_ex_2Components = [image_5]
for thisComponent in antic_ex_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
antic_ex_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "antic_ex_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = antic_ex_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=antic_ex_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    if image_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_5.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            image_5.tStop = t  # not accounting for scr refresh
            image_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
            image_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in antic_ex_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "antic_ex_2"-------
for thisComponent in antic_ex_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)

# ------Prepare to start Routine "attack_ex_2"-------
continueRoutine = True
routineTimer.add(0.250000)
# update component parameters for each repeat
frame = 1
# find the total number of frames
total_frames = (0.25*1)*expInfo['frameRate']
# keep track of which components have finished
attack_ex_2Components = [image_6]
for thisComponent in attack_ex_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
attack_ex_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "attack_ex_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = attack_ex_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=attack_ex_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    if image_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_6.tStartRefresh + 0.25-frameTolerance:
            # keep track of stop time/frame for later
            image_6.tStop = t  # not accounting for scr refresh
            image_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
            image_6.setAutoDraw(False)
    if image_6.status == STARTED:  # only update if drawing
        image_6.setSize(img_size, log=False)
    # calculate new dimensions of the image for each frame
    curr_x = x/2 + frame*(x-x/2)/total_frames
    curr_y = y/2 + frame*(y-y/2)/total_frames
    # apply new dimensions
    img_size = (curr_x, curr_y)
    frame = frame + 1
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in attack_ex_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "attack_ex_2"-------
for thisComponent in attack_ex_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)

# ------Prepare to start Routine "intro_4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
intro_4Components = [text_5, text_6, safe_text, scream_text, image_7, image_8, key_resp_6]
for thisComponent in intro_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_4"-------
while continueRoutine:
    # get current time
    t = intro_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *safe_text* updates
    if safe_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        safe_text.frameNStart = frameN  # exact frame index
        safe_text.tStart = t  # local t and not account for scr refresh
        safe_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(safe_text, 'tStartRefresh')  # time at next scr refresh
        safe_text.setAutoDraw(True)
    
    # *scream_text* updates
    if scream_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scream_text.frameNStart = frameN  # exact frame index
        scream_text.tStart = t  # local t and not account for scr refresh
        scream_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scream_text, 'tStartRefresh')  # time at next scr refresh
        scream_text.setAutoDraw(True)
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    
    # *image_8* updates
    if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_8.frameNStart = frameN  # exact frame index
        image_8.tStart = t  # local t and not account for scr refresh
        image_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
        image_8.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_4"-------
for thisComponent in intro_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
thisExp.addData('safe_text.started', safe_text.tStartRefresh)
thisExp.addData('safe_text.stopped', safe_text.tStopRefresh)
thisExp.addData('scream_text.started', scream_text.tStartRefresh)
thisExp.addData('scream_text.stopped', scream_text.tStopRefresh)
thisExp.addData('image_7.started', image_7.tStartRefresh)
thisExp.addData('image_7.stopped', image_7.tStopRefresh)
thisExp.addData('image_8.started', image_8.tStartRefresh)
thisExp.addData('image_8.stopped', image_8.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro_5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
intro_5Components = [text_7, key_resp_7]
for thisComponent in intro_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_5"-------
while continueRoutine:
    # get current time
    t = intro_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_5"-------
for thisComponent in intro_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "img_example_2"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
img_example_2Components = [image_9]
for thisComponent in img_example_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
img_example_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "img_example_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = img_example_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=img_example_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_9* updates
    if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_9.frameNStart = frameN  # exact frame index
        image_9.tStart = t  # local t and not account for scr refresh
        image_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
        image_9.setAutoDraw(True)
    if image_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_9.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            image_9.tStop = t  # not accounting for scr refresh
            image_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_9, 'tStopRefresh')  # time at next scr refresh
            image_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in img_example_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "img_example_2"-------
for thisComponent in img_example_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_9.started', image_9.tStartRefresh)
thisExp.addData('image_9.stopped', image_9.tStopRefresh)

# ------Prepare to start Routine "intro_6"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
intro_6Components = [text_8, key_resp_8]
for thisComponent in intro_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_6"-------
while continueRoutine:
    # get current time
    t = intro_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_6"-------
for thisComponent in intro_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start_practice"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
start_practiceComponents = [practice_text, key_resp_2]
for thisComponent in start_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_practice"-------
while continueRoutine:
    # get current time
    t = start_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_text* updates
    if practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_text.frameNStart = frameN  # exact frame index
        practice_text.tStart = t  # local t and not account for scr refresh
        practice_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_text, 'tStartRefresh')  # time at next scr refresh
        practice_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_practice"-------
for thisComponent in start_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice_text.started', practice_text.tStartRefresh)
thisExp.addData('practice_text.stopped', practice_text.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "start_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_practice.xlsx'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    print(tThisFlipGlobal)
    print(last_stim)
    print(startle_start)
    print(fix_adj)
    if practice == 1:
        fix_dur = 2
    else:
        if startle == True:
            fix_dur = 2.3 - (tThisFlipGlobal - last_stim) - startle_start + fix_adj
        else:
            if attac == True and condition == "Threat":
                fix_dur = 2.3 - (tThisFlipGlobal - last_stim) - anticipation_dur + fix_adj
            else:
                fix_dur = 2 - (tThisFlipGlobal - last_stim) - anticipation_dur + fix_adj
        if fix_dur < 1:
            fix_dur = random.uniform(1,3) # randomly select a float between 1&3 (both included)
    
    # add fix_dur to auto output
    thisExp.addData("fixation_duration", fix_dur)
    
    # fixation marker
    ser.write(str.encode('A0'))
    time.sleep(0.005)
    ser.write(str.encode('00'))
    # keep track of which components have finished
    restComponents = [fixation]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + fix_dur-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trials.addData('fixation.started', fixation.tStartRefresh)
    practice_trials.addData('fixation.stopped', fixation.tStopRefresh)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    too_early_outer = data.TrialHandler(nReps=100000.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='too_early_outer')
    thisExp.addLoop(too_early_outer)  # add the loop to the experiment
    thisToo_early_outer = too_early_outer.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisToo_early_outer.rgb)
    if thisToo_early_outer != None:
        for paramName in thisToo_early_outer:
            exec('{} = thisToo_early_outer[paramName]'.format(paramName))
    
    for thisToo_early_outer in too_early_outer:
        currentLoop = too_early_outer
        # abbreviate parameter names if possible (e.g. rgb = thisToo_early_outer.rgb)
        if thisToo_early_outer != None:
            for paramName in thisToo_early_outer:
                exec('{} = thisToo_early_outer[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        too_early_inner = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='too_early_inner')
        thisExp.addLoop(too_early_inner)  # add the loop to the experiment
        thisToo_early_inner = too_early_inner.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisToo_early_inner.rgb)
        if thisToo_early_inner != None:
            for paramName in thisToo_early_inner:
                exec('{} = thisToo_early_inner[paramName]'.format(paramName))
        
        for thisToo_early_inner in too_early_inner:
            currentLoop = too_early_inner
            # abbreviate parameter names if possible (e.g. rgb = thisToo_early_inner.rgb)
            if thisToo_early_inner != None:
                for paramName in thisToo_early_inner:
                    exec('{} = thisToo_early_inner[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "anticipation"-------
            continueRoutine = True
            # update component parameters for each repeat
            
            # for practice trials:
            # anticipation routine repeats if spacebar is pressed during it
            # too_early_outer controls how many times too_early_inner can be repeated (really big number)
            early_hit = False
            
            startle_probe_sent = False
            
            # define size and time factors for image
            if distance == "far":
                size_factor = 16
                time_factor = 4
            elif distance == "near":
                size_factor = 2
                time_factor = 1
            elif distance == "none":
                size_factor = 1
                time_factor = 0
            
            # add these vars to auto output
            thisExp.addData('size_factor', size_factor)
            thisExp.addData('time_factor', time_factor)
            
            # set size of image, changes every repeat
            img_size = (x/size_factor, y/size_factor)
            
            # convert duration to seconds
            antic_img_dur = anticipation_dur/1000
            
            # convert startle start to seconds
            startle_t = startle_start/1000
            
            # only play startle on startle trials
            if startle:
                startle_dur = 1
            else:
                startle_dur = 0
            
            # assign unique codes for each condition start, end & startle
            # see new_markers.docx in dropbox for a table of the codes
            # update: I don't think marking the end of the stimulus is necessary
            if condition == 'Threat':
                if distance == 'none':
                    hex_start = '04'
                    #hex_end = '0C'
                    hex_startle = '06'
                elif distance == 'far':
                    hex_start = '14'
                    #hex_end = '24'
                    hex_startle = '16'
                else:
                    hex_start = '44'
                    #hex_end = '84'
                    hex_startle = '46'
            else:
                if distance == 'none':
                    hex_start = '08'
                    #hex_end = '18'
                    hex_startle = '0A'
                elif distance == 'far':
                    hex_start = '28'
                    #hex_end = '48'
                    hex_startle = '2A'
                else:
                    hex_start = '88'
                    #hex_end = '10'
                    hex_startle = '8A'
            
            # stimulus marker
            ser.write(str.encode(hex_start))
            time.sleep(0.005)
            ser.write(str.encode('00'))
            antic_img.setSize(img_size)
            antic_img.setImage(image)
            antic_resp.keys = []
            antic_resp.rt = []
            _antic_resp_allKeys = []
            startle_sound.setSound('sounds/whitenoise.wav', secs=startle_dur, hamming=True)
            startle_sound.setVolume(1.0, log=False)
            # keep track of which components have finished
            anticipationComponents = [antic_img, antic_resp, startle_sound]
            for thisComponent in anticipationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            anticipationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "anticipation"-------
            while continueRoutine:
                # get current time
                t = anticipationClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=anticipationClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # startle probe marker (only once)
                if startle:
                    if startle_sound.status == STARTED and startle_probe_sent == False:
                        ser.write(str.encode(hex_startle))
                        time.sleep(0.005)
                        ser.write(str.encode('00'))
                        startle_probe_sent = True
                
                if practice == 1:
                    if len(_antic_resp_allKeys):
                        continueRoutine = False
                        early_hit = True
                
                # *antic_img* updates
                if antic_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    antic_img.frameNStart = frameN  # exact frame index
                    antic_img.tStart = t  # local t and not account for scr refresh
                    antic_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(antic_img, 'tStartRefresh')  # time at next scr refresh
                    antic_img.setAutoDraw(True)
                if antic_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > antic_img.tStartRefresh + antic_img_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        antic_img.tStop = t  # not accounting for scr refresh
                        antic_img.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(antic_img, 'tStopRefresh')  # time at next scr refresh
                        antic_img.setAutoDraw(False)
                
                # *antic_resp* updates
                waitOnFlip = False
                if antic_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    antic_resp.frameNStart = frameN  # exact frame index
                    antic_resp.tStart = t  # local t and not account for scr refresh
                    antic_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(antic_resp, 'tStartRefresh')  # time at next scr refresh
                    antic_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(antic_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(antic_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if antic_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > antic_resp.tStartRefresh + antic_img_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        antic_resp.tStop = t  # not accounting for scr refresh
                        antic_resp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(antic_resp, 'tStopRefresh')  # time at next scr refresh
                        antic_resp.status = FINISHED
                if antic_resp.status == STARTED and not waitOnFlip:
                    theseKeys = antic_resp.getKeys(keyList=['space'], waitRelease=False)
                    _antic_resp_allKeys.extend(theseKeys)
                    if len(_antic_resp_allKeys):
                        antic_resp.keys = _antic_resp_allKeys[-1].name  # just the last key pressed
                        antic_resp.rt = _antic_resp_allKeys[-1].rt
                # start/stop startle_sound
                if startle_sound.status == NOT_STARTED and tThisFlip >= startle_t-frameTolerance:
                    # keep track of start time/frame for later
                    startle_sound.frameNStart = frameN  # exact frame index
                    startle_sound.tStart = t  # local t and not account for scr refresh
                    startle_sound.tStartRefresh = tThisFlipGlobal  # on global time
                    startle_sound.play(when=win)  # sync with win flip
                if startle_sound.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > startle_sound.tStartRefresh + startle_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        startle_sound.tStop = t  # not accounting for scr refresh
                        startle_sound.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(startle_sound, 'tStopRefresh')  # time at next scr refresh
                        startle_sound.stop()
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in anticipationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "anticipation"-------
            for thisComponent in anticipationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            if startle:
                time_startle = startle_sound.tStartRefresh
                last_stim = time_startle
            
            if practice == 1 and not early_hit:
                too_early_inner.finished = True
                too_early_outer.finished = True
            
            # stimulus end
            #ser.write(str.encode(hex_end))
            #time.sleep(0.005)
            #ser.write(str.encode('00'))
            too_early_inner.addData('antic_img.started', antic_img.tStartRefresh)
            too_early_inner.addData('antic_img.stopped', antic_img.tStopRefresh)
            # check responses
            if antic_resp.keys in ['', [], None]:  # No response was made
                antic_resp.keys = None
            too_early_inner.addData('antic_resp.keys',antic_resp.keys)
            if antic_resp.keys != None:  # we had a response
                too_early_inner.addData('antic_resp.rt', antic_resp.rt)
            too_early_inner.addData('antic_resp.started', antic_resp.tStartRefresh)
            too_early_inner.addData('antic_resp.stopped', antic_resp.tStopRefresh)
            startle_sound.stop()  # ensure sound has stopped at end of routine
            too_early_inner.addData('startle_sound.started', startle_sound.tStartRefresh)
            too_early_inner.addData('startle_sound.stopped', startle_sound.tStopRefresh)
            # the Routine "anticipation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "too_early"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            if not early_hit:
                continueRoutine = False
            else:
                # send too early marker
                ser.write(str.encode('20'))
            too_early_text.setText('TOO EARLY!!!')
            # keep track of which components have finished
            too_earlyComponents = [too_early_text]
            for thisComponent in too_earlyComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            too_earlyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "too_early"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = too_earlyClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=too_earlyClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *too_early_text* updates
                if too_early_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    too_early_text.frameNStart = frameN  # exact frame index
                    too_early_text.tStart = t  # local t and not account for scr refresh
                    too_early_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(too_early_text, 'tStartRefresh')  # time at next scr refresh
                    too_early_text.setAutoDraw(True)
                if too_early_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > too_early_text.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        too_early_text.tStop = t  # not accounting for scr refresh
                        too_early_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(too_early_text, 'tStopRefresh')  # time at next scr refresh
                        too_early_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in too_earlyComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "too_early"-------
            for thisComponent in too_earlyComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # clear channels
            ser.write(str.encode('00'))
            
            too_early_inner.finished = True
            too_early_inner.addData('too_early_text.started', too_early_text.tStartRefresh)
            too_early_inner.addData('too_early_text.stopped', too_early_text.tStopRefresh)
        # completed 1.0 repeats of 'too_early_inner'
        
    # completed 100000.0 repeats of 'too_early_outer'
    
    
    # ------Prepare to start Routine "attack"-------
    continueRoutine = True
    # update component parameters for each repeat
    attack_img.setImage(image)
    attack_resp.keys = []
    attack_resp.rt = []
    _attack_resp_allKeys = []
    # hit is False unless user presses spacebar in time
    hit = False
    
    scream_sent = False
    
    # define the duration of this attack
    duration = attack_dur*time_factor
    
    # find the total number of frames of this attack
    total_frames = (attack_dur*time_factor)*expInfo['frameRate']
    
    # initialize frame counter
    frame = 1
    
    # scream starts immediately after attack
    #scream_start = duration
    
    play_loud_scream = False
    play_weak_scream = False
    play_scream_sound = False
    
    if condition == "Threat" and attac:
        if practice == 0:
            play_loud_scream = True
            play_weak_scream = False
        elif practice == 2:
            play_loud_scream = False
            play_weak_scream = True
        else:
            play_loud_scream = False
            play_weak_scream = False
    else:
        play_loud_scream = False
        play_weak_scream = False
        
    '''
    # set scream duration
    if condition == "Threat" and attac:
        if practice == 0:
            loud_scream_dur = 1.0
            weak_scream_dur = 0.0
        elif practice == 2:
            loud_scream_dur = 0.0
            weak_scream_dur = 1.0
        else:
            loud_scream_dur = 0.0
            weak_scream_dur = 0.0
    else:
        loud_scream_dur = 0.0
        weak_scream_dur = 0.0
    '''
    
    # attack marker
    if attac and distance != "none":
        ser.write(str.encode('60'))
        time.sleep(0.005)
        ser.write(str.encode('00'))
    loud_scream.setSound('sounds/scream.wav', secs=1.0, hamming=True)
    loud_scream.setVolume(1.0, log=False)
    weak_scream.setSound('sounds/screamweak.wav', secs=1.0, hamming=True)
    weak_scream.setVolume(1.0, log=False)
    # keep track of which components have finished
    attackComponents = [attack_img, attack_resp, loud_scream, weak_scream]
    for thisComponent in attackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    attackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "attack"-------
    while continueRoutine:
        # get current time
        t = attackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=attackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *attack_img* updates
        if attack_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            attack_img.frameNStart = frameN  # exact frame index
            attack_img.tStart = t  # local t and not account for scr refresh
            attack_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attack_img, 'tStartRefresh')  # time at next scr refresh
            attack_img.setAutoDraw(True)
        if attack_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attack_img.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                attack_img.tStop = t  # not accounting for scr refresh
                attack_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attack_img, 'tStopRefresh')  # time at next scr refresh
                attack_img.setAutoDraw(False)
        if attack_img.status == STARTED:  # only update if drawing
            attack_img.setSize(img_size, log=False)
        
        # *attack_resp* updates
        waitOnFlip = False
        if attack_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            attack_resp.frameNStart = frameN  # exact frame index
            attack_resp.tStart = t  # local t and not account for scr refresh
            attack_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attack_resp, 'tStartRefresh')  # time at next scr refresh
            attack_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(attack_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(attack_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if attack_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attack_resp.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                attack_resp.tStop = t  # not accounting for scr refresh
                attack_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attack_resp, 'tStopRefresh')  # time at next scr refresh
                attack_resp.status = FINISHED
        if attack_resp.status == STARTED and not waitOnFlip:
            theseKeys = attack_resp.getKeys(keyList=['space'], waitRelease=False)
            _attack_resp_allKeys.extend(theseKeys)
            if len(_attack_resp_allKeys):
                attack_resp.keys = _attack_resp_allKeys[-1].name  # just the last key pressed
                attack_resp.rt = _attack_resp_allKeys[-1].rt
        if attac and distance != "none":
            # calculate new dimensions of the image for each frame
            curr_x = x/size_factor + frame*(x-x/size_factor)/total_frames
            curr_y = y/size_factor + frame*(y-y/size_factor)/total_frames
            # apply new dimensions
            img_size = (curr_x, curr_y)
            # check if spacebar is pressed
            if len(_attack_resp_allKeys):
                hit = True
                continueRoutine = False
            frame = frame + 1
            
        attack_routine_time = t
        
        if play_loud_scream or play_weak_scream:
            if attack_routine_time >= duration:
                play_scream_sound = True
        else:
            if attack_routine_time >= duration:
                continueRoutine = False
        
        # send scream marker (if scream)
        if (loud_scream.status == STARTED or weak_scream.status == STARTED) \
            and scream_sent == False:
            if condition == "Threat" and attac and (practice == 0 or practice == 2):
                ser.write(str.encode('30'))
                time.sleep(0.005)
                ser.write(str.encode('00'))
                scream_sent = True
                
        if loud_scream.status == FINISHED or weak_scream.status == FINISHED:
            continueRoutine = False
        # start/stop loud_scream
        if loud_scream.status == NOT_STARTED and play_loud_scream and play_scream_sound:
            # keep track of start time/frame for later
            loud_scream.frameNStart = frameN  # exact frame index
            loud_scream.tStart = t  # local t and not account for scr refresh
            loud_scream.tStartRefresh = tThisFlipGlobal  # on global time
            loud_scream.play(when=win)  # sync with win flip
        if loud_scream.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loud_scream.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                loud_scream.tStop = t  # not accounting for scr refresh
                loud_scream.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loud_scream, 'tStopRefresh')  # time at next scr refresh
                loud_scream.stop()
        # start/stop weak_scream
        if weak_scream.status == NOT_STARTED and play_weak_scream and play_scream_sound:
            # keep track of start time/frame for later
            weak_scream.frameNStart = frameN  # exact frame index
            weak_scream.tStart = t  # local t and not account for scr refresh
            weak_scream.tStartRefresh = tThisFlipGlobal  # on global time
            weak_scream.play(when=win)  # sync with win flip
        if weak_scream.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > weak_scream.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                weak_scream.tStop = t  # not accounting for scr refresh
                weak_scream.frameNStop = frameN  # exact frame index
                win.timeOnFlip(weak_scream, 'tStopRefresh')  # time at next scr refresh
                weak_scream.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in attackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "attack"-------
    for thisComponent in attackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trials.addData('attack_img.started', attack_img.tStartRefresh)
    practice_trials.addData('attack_img.stopped', attack_img.tStopRefresh)
    # check responses
    if attack_resp.keys in ['', [], None]:  # No response was made
        attack_resp.keys = None
    practice_trials.addData('attack_resp.keys',attack_resp.keys)
    if attack_resp.keys != None:  # we had a response
        practice_trials.addData('attack_resp.rt', attack_resp.rt)
    practice_trials.addData('attack_resp.started', attack_resp.tStartRefresh)
    practice_trials.addData('attack_resp.stopped', attack_resp.tStopRefresh)
    if (practice == 0) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        time_scream = loud_scream.tStartRefresh
        last_stim = time_scream
    elif (practice == 2) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        time_scream = weak_scream.tStartRefresh
        last_stim = time_scream
    
    # ajdust time on 'near' trials
    # and in the real task on 'Threat' and 'near' trials
    if practice > 0 and distance == "near":
        if hit:
            attack_dur = attack_dur - 0.05
        else:
            attack_dur = attack_dur + 0.05
    elif practice == 0 and distance == "near" and condition == "Threat":
        if hit:
            attack_dur = attack_dur - 0.05
        else:
            attack_dur = attack_dur + 0.05
    
    loud_scream.stop()  # ensure sound has stopped at end of routine
    practice_trials.addData('loud_scream.started', loud_scream.tStartRefresh)
    practice_trials.addData('loud_scream.stopped', loud_scream.tStopRefresh)
    weak_scream.stop()  # ensure sound has stopped at end of routine
    practice_trials.addData('weak_scream.started', weak_scream.tStartRefresh)
    practice_trials.addData('weak_scream.stopped', weak_scream.tStopRefresh)
    # the Routine "attack" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "attack_feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if attac and hit:
        attack_msg = "WELL DONE!!!"
    elif (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        attack_msg = "LOUD SCREAM!!!"
        time_scream = tThisFlipGlobal
        last_stim = time_scream
    elif attac and not hit:
        attack_msg = "TOO SLOW!!!"
    else:
        attack_msg = ""
        continueRoutine = False
    feedback_text.setText(attack_msg)
    # keep track of which components have finished
    attack_feedbackComponents = [feedback_text]
    for thisComponent in attack_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    attack_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "attack_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = attack_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=attack_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in attack_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "attack_feedback"-------
    for thisComponent in attack_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trials.addData('feedback_text.started', feedback_text.tStartRefresh)
    practice_trials.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'practice_trials'


# ------Prepare to start Routine "intro_7"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
intro_7Components = [text_9, key_resp_9]
for thisComponent in intro_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_7"-------
while continueRoutine:
    # get current time
    t = intro_7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_7"-------
for thisComponent in intro_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "startle_ex"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
startle_sound_ex.setSound('sounds/whitenoise.wav', secs=2, hamming=True)
startle_sound_ex.setVolume(1.0, log=False)
# keep track of which components have finished
startle_exComponents = [startle_sound_ex]
for thisComponent in startle_exComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startle_exClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startle_ex"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = startle_exClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startle_exClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop startle_sound_ex
    if startle_sound_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startle_sound_ex.frameNStart = frameN  # exact frame index
        startle_sound_ex.tStart = t  # local t and not account for scr refresh
        startle_sound_ex.tStartRefresh = tThisFlipGlobal  # on global time
        startle_sound_ex.play(when=win)  # sync with win flip
    if startle_sound_ex.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > startle_sound_ex.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            startle_sound_ex.tStop = t  # not accounting for scr refresh
            startle_sound_ex.frameNStop = frameN  # exact frame index
            win.timeOnFlip(startle_sound_ex, 'tStopRefresh')  # time at next scr refresh
            startle_sound_ex.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startle_exComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startle_ex"-------
for thisComponent in startle_exComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startle_sound_ex.stop()  # ensure sound has stopped at end of routine
thisExp.addData('startle_sound_ex.started', startle_sound_ex.tStartRefresh)
thisExp.addData('startle_sound_ex.stopped', startle_sound_ex.tStopRefresh)

# ------Prepare to start Routine "rating_startle_ex"-------
continueRoutine = True
# update component parameters for each repeat
startle_slider.reset()
win.mouseVisible = True
# keep track of which components have finished
rating_startle_exComponents = [startle_slider, Instructions_scream_2]
for thisComponent in rating_startle_exComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rating_startle_exClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rating_startle_ex"-------
while continueRoutine:
    # get current time
    t = rating_startle_exClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rating_startle_exClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startle_slider* updates
    if startle_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startle_slider.frameNStart = frameN  # exact frame index
        startle_slider.tStart = t  # local t and not account for scr refresh
        startle_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startle_slider, 'tStartRefresh')  # time at next scr refresh
        startle_slider.setAutoDraw(True)
    
    # Check startle_slider for response to end routine
    if startle_slider.getRating() is not None and startle_slider.status == STARTED:
        continueRoutine = False
    
    # *Instructions_scream_2* updates
    if Instructions_scream_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_scream_2.frameNStart = frameN  # exact frame index
        Instructions_scream_2.tStart = t  # local t and not account for scr refresh
        Instructions_scream_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_scream_2, 'tStartRefresh')  # time at next scr refresh
        Instructions_scream_2.setAutoDraw(True)
    #if status_slider.status == FINISHED:
    #    continueRoutine = False 
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rating_startle_exComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rating_startle_ex"-------
for thisComponent in rating_startle_exComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('startle_slider.response', startle_slider.getRating())
thisExp.addData('startle_slider.rt', startle_slider.getRT())
thisExp.addData('startle_slider.started', startle_slider.tStartRefresh)
thisExp.addData('startle_slider.stopped', startle_slider.tStopRefresh)
win.mouseVisible = False
# the Routine "rating_startle_ex" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro_8"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
intro_8Components = [text_10, key_resp_10]
for thisComponent in intro_8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_8"-------
while continueRoutine:
    # get current time
    t = intro_8Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_8Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_8"-------
for thisComponent in intro_8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro_8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "scream_ex"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
startle_sound_ex_2.setSound('sounds/scream.wav', secs=2, hamming=True)
startle_sound_ex_2.setVolume(1.0, log=False)
# keep track of which components have finished
scream_exComponents = [startle_sound_ex_2]
for thisComponent in scream_exComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
scream_exClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "scream_ex"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = scream_exClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=scream_exClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop startle_sound_ex_2
    if startle_sound_ex_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startle_sound_ex_2.frameNStart = frameN  # exact frame index
        startle_sound_ex_2.tStart = t  # local t and not account for scr refresh
        startle_sound_ex_2.tStartRefresh = tThisFlipGlobal  # on global time
        startle_sound_ex_2.play(when=win)  # sync with win flip
    if startle_sound_ex_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > startle_sound_ex_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            startle_sound_ex_2.tStop = t  # not accounting for scr refresh
            startle_sound_ex_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(startle_sound_ex_2, 'tStopRefresh')  # time at next scr refresh
            startle_sound_ex_2.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in scream_exComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "scream_ex"-------
for thisComponent in scream_exComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startle_sound_ex_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('startle_sound_ex_2.started', startle_sound_ex_2.tStartRefresh)
thisExp.addData('startle_sound_ex_2.stopped', startle_sound_ex_2.tStopRefresh)

# ------Prepare to start Routine "rating_scream_ex"-------
continueRoutine = True
# update component parameters for each repeat
startle_slider_2.reset()
win.mouseVisible = True
# keep track of which components have finished
rating_scream_exComponents = [startle_slider_2, Instructions_scream_3]
for thisComponent in rating_scream_exComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rating_scream_exClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rating_scream_ex"-------
while continueRoutine:
    # get current time
    t = rating_scream_exClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rating_scream_exClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startle_slider_2* updates
    if startle_slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startle_slider_2.frameNStart = frameN  # exact frame index
        startle_slider_2.tStart = t  # local t and not account for scr refresh
        startle_slider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startle_slider_2, 'tStartRefresh')  # time at next scr refresh
        startle_slider_2.setAutoDraw(True)
    
    # Check startle_slider_2 for response to end routine
    if startle_slider_2.getRating() is not None and startle_slider_2.status == STARTED:
        continueRoutine = False
    
    # *Instructions_scream_3* updates
    if Instructions_scream_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_scream_3.frameNStart = frameN  # exact frame index
        Instructions_scream_3.tStart = t  # local t and not account for scr refresh
        Instructions_scream_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_scream_3, 'tStartRefresh')  # time at next scr refresh
        Instructions_scream_3.setAutoDraw(True)
    #if status_slider.status == FINISHED:
    #    continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rating_scream_exComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rating_scream_ex"-------
for thisComponent in rating_scream_exComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('startle_slider_2.response', startle_slider_2.getRating())
thisExp.addData('startle_slider_2.rt', startle_slider_2.getRT())
thisExp.addData('startle_slider_2.started', startle_slider_2.tStartRefresh)
thisExp.addData('startle_slider_2.stopped', startle_slider_2.tStopRefresh)
win.mouseVisible = False
# the Routine "rating_scream_ex" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start_habituation"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
start_habituationComponents = [hab_text, key_resp]
for thisComponent in start_habituationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_habituationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_habituation"-------
while continueRoutine:
    # get current time
    t = start_habituationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_habituationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *hab_text* updates
    if hab_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hab_text.frameNStart = frameN  # exact frame index
        hab_text.tStart = t  # local t and not account for scr refresh
        hab_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hab_text, 'tStartRefresh')  # time at next scr refresh
        hab_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_habituationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_habituation"-------
for thisComponent in start_habituationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('hab_text.started', hab_text.tStartRefresh)
thisExp.addData('hab_text.stopped', hab_text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "start_habituation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "screamweak_ex"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
weak_scream_ex.setSound('sounds/screamweak.wav', secs=1.0, hamming=True)
weak_scream_ex.setVolume(1.0, log=False)
# keep track of which components have finished
screamweak_exComponents = [weak_scream_ex]
for thisComponent in screamweak_exComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
screamweak_exClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "screamweak_ex"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = screamweak_exClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=screamweak_exClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop weak_scream_ex
    if weak_scream_ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        weak_scream_ex.frameNStart = frameN  # exact frame index
        weak_scream_ex.tStart = t  # local t and not account for scr refresh
        weak_scream_ex.tStartRefresh = tThisFlipGlobal  # on global time
        weak_scream_ex.play(when=win)  # sync with win flip
    if weak_scream_ex.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > weak_scream_ex.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            weak_scream_ex.tStop = t  # not accounting for scr refresh
            weak_scream_ex.frameNStop = frameN  # exact frame index
            win.timeOnFlip(weak_scream_ex, 'tStopRefresh')  # time at next scr refresh
            weak_scream_ex.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in screamweak_exComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "screamweak_ex"-------
for thisComponent in screamweak_exComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
weak_scream_ex.stop()  # ensure sound has stopped at end of routine
thisExp.addData('weak_scream_ex.started', weak_scream_ex.tStartRefresh)
thisExp.addData('weak_scream_ex.stopped', weak_scream_ex.tStopRefresh)

# set up handler to look after randomisation of conditions etc
habituation_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_habituation.xlsx'),
    seed=None, name='habituation_trials')
thisExp.addLoop(habituation_trials)  # add the loop to the experiment
thisHabituation_trial = habituation_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHabituation_trial.rgb)
if thisHabituation_trial != None:
    for paramName in thisHabituation_trial:
        exec('{} = thisHabituation_trial[paramName]'.format(paramName))

for thisHabituation_trial in habituation_trials:
    currentLoop = habituation_trials
    # abbreviate parameter names if possible (e.g. rgb = thisHabituation_trial.rgb)
    if thisHabituation_trial != None:
        for paramName in thisHabituation_trial:
            exec('{} = thisHabituation_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    print(tThisFlipGlobal)
    print(last_stim)
    print(startle_start)
    print(fix_adj)
    if practice == 1:
        fix_dur = 2
    else:
        if startle == True:
            fix_dur = 2.3 - (tThisFlipGlobal - last_stim) - startle_start + fix_adj
        else:
            if attac == True and condition == "Threat":
                fix_dur = 2.3 - (tThisFlipGlobal - last_stim) - anticipation_dur + fix_adj
            else:
                fix_dur = 2 - (tThisFlipGlobal - last_stim) - anticipation_dur + fix_adj
        if fix_dur < 1:
            fix_dur = random.uniform(1,3) # randomly select a float between 1&3 (both included)
    
    # add fix_dur to auto output
    thisExp.addData("fixation_duration", fix_dur)
    
    # fixation marker
    ser.write(str.encode('A0'))
    time.sleep(0.005)
    ser.write(str.encode('00'))
    # keep track of which components have finished
    restComponents = [fixation]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + fix_dur-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    habituation_trials.addData('fixation.started', fixation.tStartRefresh)
    habituation_trials.addData('fixation.stopped', fixation.tStopRefresh)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "anticipation"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    # for practice trials:
    # anticipation routine repeats if spacebar is pressed during it
    # too_early_outer controls how many times too_early_inner can be repeated (really big number)
    early_hit = False
    
    startle_probe_sent = False
    
    # define size and time factors for image
    if distance == "far":
        size_factor = 16
        time_factor = 4
    elif distance == "near":
        size_factor = 2
        time_factor = 1
    elif distance == "none":
        size_factor = 1
        time_factor = 0
    
    # add these vars to auto output
    thisExp.addData('size_factor', size_factor)
    thisExp.addData('time_factor', time_factor)
    
    # set size of image, changes every repeat
    img_size = (x/size_factor, y/size_factor)
    
    # convert duration to seconds
    antic_img_dur = anticipation_dur/1000
    
    # convert startle start to seconds
    startle_t = startle_start/1000
    
    # only play startle on startle trials
    if startle:
        startle_dur = 1
    else:
        startle_dur = 0
    
    # assign unique codes for each condition start, end & startle
    # see new_markers.docx in dropbox for a table of the codes
    # update: I don't think marking the end of the stimulus is necessary
    if condition == 'Threat':
        if distance == 'none':
            hex_start = '04'
            #hex_end = '0C'
            hex_startle = '06'
        elif distance == 'far':
            hex_start = '14'
            #hex_end = '24'
            hex_startle = '16'
        else:
            hex_start = '44'
            #hex_end = '84'
            hex_startle = '46'
    else:
        if distance == 'none':
            hex_start = '08'
            #hex_end = '18'
            hex_startle = '0A'
        elif distance == 'far':
            hex_start = '28'
            #hex_end = '48'
            hex_startle = '2A'
        else:
            hex_start = '88'
            #hex_end = '10'
            hex_startle = '8A'
    
    # stimulus marker
    ser.write(str.encode(hex_start))
    time.sleep(0.005)
    ser.write(str.encode('00'))
    antic_img.setSize(img_size)
    antic_img.setImage(image)
    antic_resp.keys = []
    antic_resp.rt = []
    _antic_resp_allKeys = []
    startle_sound.setSound('sounds/whitenoise.wav', secs=startle_dur, hamming=True)
    startle_sound.setVolume(1.0, log=False)
    # keep track of which components have finished
    anticipationComponents = [antic_img, antic_resp, startle_sound]
    for thisComponent in anticipationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    anticipationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "anticipation"-------
    while continueRoutine:
        # get current time
        t = anticipationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=anticipationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # startle probe marker (only once)
        if startle:
            if startle_sound.status == STARTED and startle_probe_sent == False:
                ser.write(str.encode(hex_startle))
                time.sleep(0.005)
                ser.write(str.encode('00'))
                startle_probe_sent = True
        
        if practice == 1:
            if len(_antic_resp_allKeys):
                continueRoutine = False
                early_hit = True
        
        # *antic_img* updates
        if antic_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            antic_img.frameNStart = frameN  # exact frame index
            antic_img.tStart = t  # local t and not account for scr refresh
            antic_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(antic_img, 'tStartRefresh')  # time at next scr refresh
            antic_img.setAutoDraw(True)
        if antic_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > antic_img.tStartRefresh + antic_img_dur-frameTolerance:
                # keep track of stop time/frame for later
                antic_img.tStop = t  # not accounting for scr refresh
                antic_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(antic_img, 'tStopRefresh')  # time at next scr refresh
                antic_img.setAutoDraw(False)
        
        # *antic_resp* updates
        waitOnFlip = False
        if antic_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            antic_resp.frameNStart = frameN  # exact frame index
            antic_resp.tStart = t  # local t and not account for scr refresh
            antic_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(antic_resp, 'tStartRefresh')  # time at next scr refresh
            antic_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(antic_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(antic_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if antic_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > antic_resp.tStartRefresh + antic_img_dur-frameTolerance:
                # keep track of stop time/frame for later
                antic_resp.tStop = t  # not accounting for scr refresh
                antic_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(antic_resp, 'tStopRefresh')  # time at next scr refresh
                antic_resp.status = FINISHED
        if antic_resp.status == STARTED and not waitOnFlip:
            theseKeys = antic_resp.getKeys(keyList=['space'], waitRelease=False)
            _antic_resp_allKeys.extend(theseKeys)
            if len(_antic_resp_allKeys):
                antic_resp.keys = _antic_resp_allKeys[-1].name  # just the last key pressed
                antic_resp.rt = _antic_resp_allKeys[-1].rt
        # start/stop startle_sound
        if startle_sound.status == NOT_STARTED and tThisFlip >= startle_t-frameTolerance:
            # keep track of start time/frame for later
            startle_sound.frameNStart = frameN  # exact frame index
            startle_sound.tStart = t  # local t and not account for scr refresh
            startle_sound.tStartRefresh = tThisFlipGlobal  # on global time
            startle_sound.play(when=win)  # sync with win flip
        if startle_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > startle_sound.tStartRefresh + startle_dur-frameTolerance:
                # keep track of stop time/frame for later
                startle_sound.tStop = t  # not accounting for scr refresh
                startle_sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(startle_sound, 'tStopRefresh')  # time at next scr refresh
                startle_sound.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in anticipationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "anticipation"-------
    for thisComponent in anticipationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if startle:
        time_startle = startle_sound.tStartRefresh
        last_stim = time_startle
    
    if practice == 1 and not early_hit:
        too_early_inner.finished = True
        too_early_outer.finished = True
    
    # stimulus end
    #ser.write(str.encode(hex_end))
    #time.sleep(0.005)
    #ser.write(str.encode('00'))
    habituation_trials.addData('antic_img.started', antic_img.tStartRefresh)
    habituation_trials.addData('antic_img.stopped', antic_img.tStopRefresh)
    # check responses
    if antic_resp.keys in ['', [], None]:  # No response was made
        antic_resp.keys = None
    habituation_trials.addData('antic_resp.keys',antic_resp.keys)
    if antic_resp.keys != None:  # we had a response
        habituation_trials.addData('antic_resp.rt', antic_resp.rt)
    habituation_trials.addData('antic_resp.started', antic_resp.tStartRefresh)
    habituation_trials.addData('antic_resp.stopped', antic_resp.tStopRefresh)
    startle_sound.stop()  # ensure sound has stopped at end of routine
    habituation_trials.addData('startle_sound.started', startle_sound.tStartRefresh)
    habituation_trials.addData('startle_sound.stopped', startle_sound.tStopRefresh)
    # the Routine "anticipation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "attack"-------
    continueRoutine = True
    # update component parameters for each repeat
    attack_img.setImage(image)
    attack_resp.keys = []
    attack_resp.rt = []
    _attack_resp_allKeys = []
    # hit is False unless user presses spacebar in time
    hit = False
    
    scream_sent = False
    
    # define the duration of this attack
    duration = attack_dur*time_factor
    
    # find the total number of frames of this attack
    total_frames = (attack_dur*time_factor)*expInfo['frameRate']
    
    # initialize frame counter
    frame = 1
    
    # scream starts immediately after attack
    #scream_start = duration
    
    play_loud_scream = False
    play_weak_scream = False
    play_scream_sound = False
    
    if condition == "Threat" and attac:
        if practice == 0:
            play_loud_scream = True
            play_weak_scream = False
        elif practice == 2:
            play_loud_scream = False
            play_weak_scream = True
        else:
            play_loud_scream = False
            play_weak_scream = False
    else:
        play_loud_scream = False
        play_weak_scream = False
        
    '''
    # set scream duration
    if condition == "Threat" and attac:
        if practice == 0:
            loud_scream_dur = 1.0
            weak_scream_dur = 0.0
        elif practice == 2:
            loud_scream_dur = 0.0
            weak_scream_dur = 1.0
        else:
            loud_scream_dur = 0.0
            weak_scream_dur = 0.0
    else:
        loud_scream_dur = 0.0
        weak_scream_dur = 0.0
    '''
    
    # attack marker
    if attac and distance != "none":
        ser.write(str.encode('60'))
        time.sleep(0.005)
        ser.write(str.encode('00'))
    loud_scream.setSound('sounds/scream.wav', secs=1.0, hamming=True)
    loud_scream.setVolume(1.0, log=False)
    weak_scream.setSound('sounds/screamweak.wav', secs=1.0, hamming=True)
    weak_scream.setVolume(1.0, log=False)
    # keep track of which components have finished
    attackComponents = [attack_img, attack_resp, loud_scream, weak_scream]
    for thisComponent in attackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    attackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "attack"-------
    while continueRoutine:
        # get current time
        t = attackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=attackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *attack_img* updates
        if attack_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            attack_img.frameNStart = frameN  # exact frame index
            attack_img.tStart = t  # local t and not account for scr refresh
            attack_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attack_img, 'tStartRefresh')  # time at next scr refresh
            attack_img.setAutoDraw(True)
        if attack_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attack_img.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                attack_img.tStop = t  # not accounting for scr refresh
                attack_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attack_img, 'tStopRefresh')  # time at next scr refresh
                attack_img.setAutoDraw(False)
        if attack_img.status == STARTED:  # only update if drawing
            attack_img.setSize(img_size, log=False)
        
        # *attack_resp* updates
        waitOnFlip = False
        if attack_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            attack_resp.frameNStart = frameN  # exact frame index
            attack_resp.tStart = t  # local t and not account for scr refresh
            attack_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attack_resp, 'tStartRefresh')  # time at next scr refresh
            attack_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(attack_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(attack_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if attack_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attack_resp.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                attack_resp.tStop = t  # not accounting for scr refresh
                attack_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attack_resp, 'tStopRefresh')  # time at next scr refresh
                attack_resp.status = FINISHED
        if attack_resp.status == STARTED and not waitOnFlip:
            theseKeys = attack_resp.getKeys(keyList=['space'], waitRelease=False)
            _attack_resp_allKeys.extend(theseKeys)
            if len(_attack_resp_allKeys):
                attack_resp.keys = _attack_resp_allKeys[-1].name  # just the last key pressed
                attack_resp.rt = _attack_resp_allKeys[-1].rt
        if attac and distance != "none":
            # calculate new dimensions of the image for each frame
            curr_x = x/size_factor + frame*(x-x/size_factor)/total_frames
            curr_y = y/size_factor + frame*(y-y/size_factor)/total_frames
            # apply new dimensions
            img_size = (curr_x, curr_y)
            # check if spacebar is pressed
            if len(_attack_resp_allKeys):
                hit = True
                continueRoutine = False
            frame = frame + 1
            
        attack_routine_time = t
        
        if play_loud_scream or play_weak_scream:
            if attack_routine_time >= duration:
                play_scream_sound = True
        else:
            if attack_routine_time >= duration:
                continueRoutine = False
        
        # send scream marker (if scream)
        if (loud_scream.status == STARTED or weak_scream.status == STARTED) \
            and scream_sent == False:
            if condition == "Threat" and attac and (practice == 0 or practice == 2):
                ser.write(str.encode('30'))
                time.sleep(0.005)
                ser.write(str.encode('00'))
                scream_sent = True
                
        if loud_scream.status == FINISHED or weak_scream.status == FINISHED:
            continueRoutine = False
        # start/stop loud_scream
        if loud_scream.status == NOT_STARTED and play_loud_scream and play_scream_sound:
            # keep track of start time/frame for later
            loud_scream.frameNStart = frameN  # exact frame index
            loud_scream.tStart = t  # local t and not account for scr refresh
            loud_scream.tStartRefresh = tThisFlipGlobal  # on global time
            loud_scream.play(when=win)  # sync with win flip
        if loud_scream.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loud_scream.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                loud_scream.tStop = t  # not accounting for scr refresh
                loud_scream.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loud_scream, 'tStopRefresh')  # time at next scr refresh
                loud_scream.stop()
        # start/stop weak_scream
        if weak_scream.status == NOT_STARTED and play_weak_scream and play_scream_sound:
            # keep track of start time/frame for later
            weak_scream.frameNStart = frameN  # exact frame index
            weak_scream.tStart = t  # local t and not account for scr refresh
            weak_scream.tStartRefresh = tThisFlipGlobal  # on global time
            weak_scream.play(when=win)  # sync with win flip
        if weak_scream.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > weak_scream.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                weak_scream.tStop = t  # not accounting for scr refresh
                weak_scream.frameNStop = frameN  # exact frame index
                win.timeOnFlip(weak_scream, 'tStopRefresh')  # time at next scr refresh
                weak_scream.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in attackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "attack"-------
    for thisComponent in attackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    habituation_trials.addData('attack_img.started', attack_img.tStartRefresh)
    habituation_trials.addData('attack_img.stopped', attack_img.tStopRefresh)
    # check responses
    if attack_resp.keys in ['', [], None]:  # No response was made
        attack_resp.keys = None
    habituation_trials.addData('attack_resp.keys',attack_resp.keys)
    if attack_resp.keys != None:  # we had a response
        habituation_trials.addData('attack_resp.rt', attack_resp.rt)
    habituation_trials.addData('attack_resp.started', attack_resp.tStartRefresh)
    habituation_trials.addData('attack_resp.stopped', attack_resp.tStopRefresh)
    if (practice == 0) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        time_scream = loud_scream.tStartRefresh
        last_stim = time_scream
    elif (practice == 2) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        time_scream = weak_scream.tStartRefresh
        last_stim = time_scream
    
    # ajdust time on 'near' trials
    # and in the real task on 'Threat' and 'near' trials
    if practice > 0 and distance == "near":
        if hit:
            attack_dur = attack_dur - 0.05
        else:
            attack_dur = attack_dur + 0.05
    elif practice == 0 and distance == "near" and condition == "Threat":
        if hit:
            attack_dur = attack_dur - 0.05
        else:
            attack_dur = attack_dur + 0.05
    
    loud_scream.stop()  # ensure sound has stopped at end of routine
    habituation_trials.addData('loud_scream.started', loud_scream.tStartRefresh)
    habituation_trials.addData('loud_scream.stopped', loud_scream.tStopRefresh)
    weak_scream.stop()  # ensure sound has stopped at end of routine
    habituation_trials.addData('weak_scream.started', weak_scream.tStartRefresh)
    habituation_trials.addData('weak_scream.stopped', weak_scream.tStopRefresh)
    # the Routine "attack" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rating_relief"-------
    continueRoutine = True
    # update component parameters for each repeat
    relief_slider.reset()
    if (practice == 0 or practice == 2) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        continueRoutine = False
    else:
        win.mouseVisible = True
        ser.write(str.encode('50'))  # rating marker
        time.sleep(0.005)
        ser.write(str.encode('00'))
    # keep track of which components have finished
    rating_reliefComponents = [relief_slider, Instructions_relief]
    for thisComponent in rating_reliefComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rating_reliefClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rating_relief"-------
    while continueRoutine:
        # get current time
        t = rating_reliefClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rating_reliefClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *relief_slider* updates
        if relief_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            relief_slider.frameNStart = frameN  # exact frame index
            relief_slider.tStart = t  # local t and not account for scr refresh
            relief_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(relief_slider, 'tStartRefresh')  # time at next scr refresh
            relief_slider.setAutoDraw(True)
        if relief_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > relief_slider.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                relief_slider.tStop = t  # not accounting for scr refresh
                relief_slider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(relief_slider, 'tStopRefresh')  # time at next scr refresh
                relief_slider.setAutoDraw(False)
        
        # *Instructions_relief* updates
        if Instructions_relief.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_relief.frameNStart = frameN  # exact frame index
            Instructions_relief.tStart = t  # local t and not account for scr refresh
            Instructions_relief.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_relief, 'tStartRefresh')  # time at next scr refresh
            Instructions_relief.setAutoDraw(True)
        if relief_slider.status == FINISHED:
            continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rating_reliefComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating_relief"-------
    for thisComponent in rating_reliefComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    habituation_trials.addData('relief_slider.response', relief_slider.getRating())
    habituation_trials.addData('relief_slider.rt', relief_slider.getRT())
    habituation_trials.addData('relief_slider.started', relief_slider.tStartRefresh)
    habituation_trials.addData('relief_slider.stopped', relief_slider.tStopRefresh)
    win.mouseVisible = False
    # save response if the slider was shown
    if (practice == 0 or practice == 2) and not\
        ((condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none")):
        # define stage
        #if practice == 2:
        #    stage = 'habituation'
        #elif practice == 0:
        #    stage = 'real'
    
        # get the item text and strip newlines/spaces
        item_text = Instructions_relief.text.strip()
    
        # write entry into custom file
        custom_q.write(expInfo['participant'] +','+ stage +','+ condition +','+ \
            distance +','+ str(attac) +','+ str(startle) +','+ 'relief' +','+ item_text +','+ \
            str(relief_slider.getRating()) +','+ str(relief_slider.getRT()) + '\n')
    
    # the Routine "rating_relief" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rating_scream"-------
    continueRoutine = True
    # update component parameters for each repeat
    scream_slider.reset()
    if (practice == 0 or practice == 2) and not\
        ((condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none")):
        continueRoutine = False
    else:
        win.mouseVisible = True
        ser.write(str.encode('50'))  # rating marker
        time.sleep(0.005)
        ser.write(str.encode('00'))
    # keep track of which components have finished
    rating_screamComponents = [scream_slider, Instructions_scream]
    for thisComponent in rating_screamComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rating_screamClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rating_scream"-------
    while continueRoutine:
        # get current time
        t = rating_screamClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rating_screamClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *scream_slider* updates
        if scream_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scream_slider.frameNStart = frameN  # exact frame index
            scream_slider.tStart = t  # local t and not account for scr refresh
            scream_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scream_slider, 'tStartRefresh')  # time at next scr refresh
            scream_slider.setAutoDraw(True)
        if scream_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > scream_slider.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                scream_slider.tStop = t  # not accounting for scr refresh
                scream_slider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(scream_slider, 'tStopRefresh')  # time at next scr refresh
                scream_slider.setAutoDraw(False)
        
        # *Instructions_scream* updates
        if Instructions_scream.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_scream.frameNStart = frameN  # exact frame index
            Instructions_scream.tStart = t  # local t and not account for scr refresh
            Instructions_scream.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_scream, 'tStartRefresh')  # time at next scr refresh
            Instructions_scream.setAutoDraw(True)
        if scream_slider.status == FINISHED:
            continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rating_screamComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating_scream"-------
    for thisComponent in rating_screamComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    habituation_trials.addData('scream_slider.response', scream_slider.getRating())
    habituation_trials.addData('scream_slider.rt', scream_slider.getRT())
    habituation_trials.addData('scream_slider.started', scream_slider.tStartRefresh)
    habituation_trials.addData('scream_slider.stopped', scream_slider.tStopRefresh)
    win.mouseVisible = False
    # save response if the slider was shown
    if (practice == 0 or practice == 2) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        # define stage
        #if practice == 2:
        #    stage = 'habituation'
        #elif practice == 0:
        #    stage = 'real'
    
        # get the item text and strip newlines/spaces
        item_text = Instructions_scream.text.strip()
    
        # write entry into custom file
        custom_q.write(expInfo['participant'] +','+ stage +','+ condition +','+ \
            distance +','+ str(attac) +','+ str(startle) +','+ 'scream' +','+ item_text +','+ \
            str(scream_slider.getRating()) +','+ str(scream_slider.getRT()) + '\n')
            
    # clear channels
    #ser.write(str.encode('00'))
    # the Routine "rating_scream" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'habituation_trials'


# ------Prepare to start Routine "start_real_task"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
start_real_taskComponents = [text]
for thisComponent in start_real_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_real_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_real_task"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = start_real_taskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_real_taskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_real_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_real_task"-------
for thisComponent in start_real_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
task_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_task.xlsx'),
    seed=None, name='task_trials')
thisExp.addLoop(task_trials)  # add the loop to the experiment
thisTask_trial = task_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask_trial.rgb)
if thisTask_trial != None:
    for paramName in thisTask_trial:
        exec('{} = thisTask_trial[paramName]'.format(paramName))

for thisTask_trial in task_trials:
    currentLoop = task_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTask_trial.rgb)
    if thisTask_trial != None:
        for paramName in thisTask_trial:
            exec('{} = thisTask_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    print(tThisFlipGlobal)
    print(last_stim)
    print(startle_start)
    print(fix_adj)
    if practice == 1:
        fix_dur = 2
    else:
        if startle == True:
            fix_dur = 2.3 - (tThisFlipGlobal - last_stim) - startle_start + fix_adj
        else:
            if attac == True and condition == "Threat":
                fix_dur = 2.3 - (tThisFlipGlobal - last_stim) - anticipation_dur + fix_adj
            else:
                fix_dur = 2 - (tThisFlipGlobal - last_stim) - anticipation_dur + fix_adj
        if fix_dur < 1:
            fix_dur = random.uniform(1,3) # randomly select a float between 1&3 (both included)
    
    # add fix_dur to auto output
    thisExp.addData("fixation_duration", fix_dur)
    
    # fixation marker
    ser.write(str.encode('A0'))
    time.sleep(0.005)
    ser.write(str.encode('00'))
    # keep track of which components have finished
    restComponents = [fixation]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + fix_dur-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    task_trials.addData('fixation.started', fixation.tStartRefresh)
    task_trials.addData('fixation.stopped', fixation.tStopRefresh)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "anticipation"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    # for practice trials:
    # anticipation routine repeats if spacebar is pressed during it
    # too_early_outer controls how many times too_early_inner can be repeated (really big number)
    early_hit = False
    
    startle_probe_sent = False
    
    # define size and time factors for image
    if distance == "far":
        size_factor = 16
        time_factor = 4
    elif distance == "near":
        size_factor = 2
        time_factor = 1
    elif distance == "none":
        size_factor = 1
        time_factor = 0
    
    # add these vars to auto output
    thisExp.addData('size_factor', size_factor)
    thisExp.addData('time_factor', time_factor)
    
    # set size of image, changes every repeat
    img_size = (x/size_factor, y/size_factor)
    
    # convert duration to seconds
    antic_img_dur = anticipation_dur/1000
    
    # convert startle start to seconds
    startle_t = startle_start/1000
    
    # only play startle on startle trials
    if startle:
        startle_dur = 1
    else:
        startle_dur = 0
    
    # assign unique codes for each condition start, end & startle
    # see new_markers.docx in dropbox for a table of the codes
    # update: I don't think marking the end of the stimulus is necessary
    if condition == 'Threat':
        if distance == 'none':
            hex_start = '04'
            #hex_end = '0C'
            hex_startle = '06'
        elif distance == 'far':
            hex_start = '14'
            #hex_end = '24'
            hex_startle = '16'
        else:
            hex_start = '44'
            #hex_end = '84'
            hex_startle = '46'
    else:
        if distance == 'none':
            hex_start = '08'
            #hex_end = '18'
            hex_startle = '0A'
        elif distance == 'far':
            hex_start = '28'
            #hex_end = '48'
            hex_startle = '2A'
        else:
            hex_start = '88'
            #hex_end = '10'
            hex_startle = '8A'
    
    # stimulus marker
    ser.write(str.encode(hex_start))
    time.sleep(0.005)
    ser.write(str.encode('00'))
    antic_img.setSize(img_size)
    antic_img.setImage(image)
    antic_resp.keys = []
    antic_resp.rt = []
    _antic_resp_allKeys = []
    startle_sound.setSound('sounds/whitenoise.wav', secs=startle_dur, hamming=True)
    startle_sound.setVolume(1.0, log=False)
    # keep track of which components have finished
    anticipationComponents = [antic_img, antic_resp, startle_sound]
    for thisComponent in anticipationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    anticipationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "anticipation"-------
    while continueRoutine:
        # get current time
        t = anticipationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=anticipationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # startle probe marker (only once)
        if startle:
            if startle_sound.status == STARTED and startle_probe_sent == False:
                ser.write(str.encode(hex_startle))
                time.sleep(0.005)
                ser.write(str.encode('00'))
                startle_probe_sent = True
        
        if practice == 1:
            if len(_antic_resp_allKeys):
                continueRoutine = False
                early_hit = True
        
        # *antic_img* updates
        if antic_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            antic_img.frameNStart = frameN  # exact frame index
            antic_img.tStart = t  # local t and not account for scr refresh
            antic_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(antic_img, 'tStartRefresh')  # time at next scr refresh
            antic_img.setAutoDraw(True)
        if antic_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > antic_img.tStartRefresh + antic_img_dur-frameTolerance:
                # keep track of stop time/frame for later
                antic_img.tStop = t  # not accounting for scr refresh
                antic_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(antic_img, 'tStopRefresh')  # time at next scr refresh
                antic_img.setAutoDraw(False)
        
        # *antic_resp* updates
        waitOnFlip = False
        if antic_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            antic_resp.frameNStart = frameN  # exact frame index
            antic_resp.tStart = t  # local t and not account for scr refresh
            antic_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(antic_resp, 'tStartRefresh')  # time at next scr refresh
            antic_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(antic_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(antic_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if antic_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > antic_resp.tStartRefresh + antic_img_dur-frameTolerance:
                # keep track of stop time/frame for later
                antic_resp.tStop = t  # not accounting for scr refresh
                antic_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(antic_resp, 'tStopRefresh')  # time at next scr refresh
                antic_resp.status = FINISHED
        if antic_resp.status == STARTED and not waitOnFlip:
            theseKeys = antic_resp.getKeys(keyList=['space'], waitRelease=False)
            _antic_resp_allKeys.extend(theseKeys)
            if len(_antic_resp_allKeys):
                antic_resp.keys = _antic_resp_allKeys[-1].name  # just the last key pressed
                antic_resp.rt = _antic_resp_allKeys[-1].rt
        # start/stop startle_sound
        if startle_sound.status == NOT_STARTED and tThisFlip >= startle_t-frameTolerance:
            # keep track of start time/frame for later
            startle_sound.frameNStart = frameN  # exact frame index
            startle_sound.tStart = t  # local t and not account for scr refresh
            startle_sound.tStartRefresh = tThisFlipGlobal  # on global time
            startle_sound.play(when=win)  # sync with win flip
        if startle_sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > startle_sound.tStartRefresh + startle_dur-frameTolerance:
                # keep track of stop time/frame for later
                startle_sound.tStop = t  # not accounting for scr refresh
                startle_sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(startle_sound, 'tStopRefresh')  # time at next scr refresh
                startle_sound.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in anticipationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "anticipation"-------
    for thisComponent in anticipationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if startle:
        time_startle = startle_sound.tStartRefresh
        last_stim = time_startle
    
    if practice == 1 and not early_hit:
        too_early_inner.finished = True
        too_early_outer.finished = True
    
    # stimulus end
    #ser.write(str.encode(hex_end))
    #time.sleep(0.005)
    #ser.write(str.encode('00'))
    task_trials.addData('antic_img.started', antic_img.tStartRefresh)
    task_trials.addData('antic_img.stopped', antic_img.tStopRefresh)
    # check responses
    if antic_resp.keys in ['', [], None]:  # No response was made
        antic_resp.keys = None
    task_trials.addData('antic_resp.keys',antic_resp.keys)
    if antic_resp.keys != None:  # we had a response
        task_trials.addData('antic_resp.rt', antic_resp.rt)
    task_trials.addData('antic_resp.started', antic_resp.tStartRefresh)
    task_trials.addData('antic_resp.stopped', antic_resp.tStopRefresh)
    startle_sound.stop()  # ensure sound has stopped at end of routine
    task_trials.addData('startle_sound.started', startle_sound.tStartRefresh)
    task_trials.addData('startle_sound.stopped', startle_sound.tStopRefresh)
    # the Routine "anticipation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "attack"-------
    continueRoutine = True
    # update component parameters for each repeat
    attack_img.setImage(image)
    attack_resp.keys = []
    attack_resp.rt = []
    _attack_resp_allKeys = []
    # hit is False unless user presses spacebar in time
    hit = False
    
    scream_sent = False
    
    # define the duration of this attack
    duration = attack_dur*time_factor
    
    # find the total number of frames of this attack
    total_frames = (attack_dur*time_factor)*expInfo['frameRate']
    
    # initialize frame counter
    frame = 1
    
    # scream starts immediately after attack
    #scream_start = duration
    
    play_loud_scream = False
    play_weak_scream = False
    play_scream_sound = False
    
    if condition == "Threat" and attac:
        if practice == 0:
            play_loud_scream = True
            play_weak_scream = False
        elif practice == 2:
            play_loud_scream = False
            play_weak_scream = True
        else:
            play_loud_scream = False
            play_weak_scream = False
    else:
        play_loud_scream = False
        play_weak_scream = False
        
    '''
    # set scream duration
    if condition == "Threat" and attac:
        if practice == 0:
            loud_scream_dur = 1.0
            weak_scream_dur = 0.0
        elif practice == 2:
            loud_scream_dur = 0.0
            weak_scream_dur = 1.0
        else:
            loud_scream_dur = 0.0
            weak_scream_dur = 0.0
    else:
        loud_scream_dur = 0.0
        weak_scream_dur = 0.0
    '''
    
    # attack marker
    if attac and distance != "none":
        ser.write(str.encode('60'))
        time.sleep(0.005)
        ser.write(str.encode('00'))
    loud_scream.setSound('sounds/scream.wav', secs=1.0, hamming=True)
    loud_scream.setVolume(1.0, log=False)
    weak_scream.setSound('sounds/screamweak.wav', secs=1.0, hamming=True)
    weak_scream.setVolume(1.0, log=False)
    # keep track of which components have finished
    attackComponents = [attack_img, attack_resp, loud_scream, weak_scream]
    for thisComponent in attackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    attackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "attack"-------
    while continueRoutine:
        # get current time
        t = attackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=attackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *attack_img* updates
        if attack_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            attack_img.frameNStart = frameN  # exact frame index
            attack_img.tStart = t  # local t and not account for scr refresh
            attack_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attack_img, 'tStartRefresh')  # time at next scr refresh
            attack_img.setAutoDraw(True)
        if attack_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attack_img.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                attack_img.tStop = t  # not accounting for scr refresh
                attack_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attack_img, 'tStopRefresh')  # time at next scr refresh
                attack_img.setAutoDraw(False)
        if attack_img.status == STARTED:  # only update if drawing
            attack_img.setSize(img_size, log=False)
        
        # *attack_resp* updates
        waitOnFlip = False
        if attack_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            attack_resp.frameNStart = frameN  # exact frame index
            attack_resp.tStart = t  # local t and not account for scr refresh
            attack_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attack_resp, 'tStartRefresh')  # time at next scr refresh
            attack_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(attack_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(attack_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if attack_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attack_resp.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                attack_resp.tStop = t  # not accounting for scr refresh
                attack_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attack_resp, 'tStopRefresh')  # time at next scr refresh
                attack_resp.status = FINISHED
        if attack_resp.status == STARTED and not waitOnFlip:
            theseKeys = attack_resp.getKeys(keyList=['space'], waitRelease=False)
            _attack_resp_allKeys.extend(theseKeys)
            if len(_attack_resp_allKeys):
                attack_resp.keys = _attack_resp_allKeys[-1].name  # just the last key pressed
                attack_resp.rt = _attack_resp_allKeys[-1].rt
        if attac and distance != "none":
            # calculate new dimensions of the image for each frame
            curr_x = x/size_factor + frame*(x-x/size_factor)/total_frames
            curr_y = y/size_factor + frame*(y-y/size_factor)/total_frames
            # apply new dimensions
            img_size = (curr_x, curr_y)
            # check if spacebar is pressed
            if len(_attack_resp_allKeys):
                hit = True
                continueRoutine = False
            frame = frame + 1
            
        attack_routine_time = t
        
        if play_loud_scream or play_weak_scream:
            if attack_routine_time >= duration:
                play_scream_sound = True
        else:
            if attack_routine_time >= duration:
                continueRoutine = False
        
        # send scream marker (if scream)
        if (loud_scream.status == STARTED or weak_scream.status == STARTED) \
            and scream_sent == False:
            if condition == "Threat" and attac and (practice == 0 or practice == 2):
                ser.write(str.encode('30'))
                time.sleep(0.005)
                ser.write(str.encode('00'))
                scream_sent = True
                
        if loud_scream.status == FINISHED or weak_scream.status == FINISHED:
            continueRoutine = False
        # start/stop loud_scream
        if loud_scream.status == NOT_STARTED and play_loud_scream and play_scream_sound:
            # keep track of start time/frame for later
            loud_scream.frameNStart = frameN  # exact frame index
            loud_scream.tStart = t  # local t and not account for scr refresh
            loud_scream.tStartRefresh = tThisFlipGlobal  # on global time
            loud_scream.play(when=win)  # sync with win flip
        if loud_scream.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > loud_scream.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                loud_scream.tStop = t  # not accounting for scr refresh
                loud_scream.frameNStop = frameN  # exact frame index
                win.timeOnFlip(loud_scream, 'tStopRefresh')  # time at next scr refresh
                loud_scream.stop()
        # start/stop weak_scream
        if weak_scream.status == NOT_STARTED and play_weak_scream and play_scream_sound:
            # keep track of start time/frame for later
            weak_scream.frameNStart = frameN  # exact frame index
            weak_scream.tStart = t  # local t and not account for scr refresh
            weak_scream.tStartRefresh = tThisFlipGlobal  # on global time
            weak_scream.play(when=win)  # sync with win flip
        if weak_scream.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > weak_scream.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                weak_scream.tStop = t  # not accounting for scr refresh
                weak_scream.frameNStop = frameN  # exact frame index
                win.timeOnFlip(weak_scream, 'tStopRefresh')  # time at next scr refresh
                weak_scream.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in attackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "attack"-------
    for thisComponent in attackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    task_trials.addData('attack_img.started', attack_img.tStartRefresh)
    task_trials.addData('attack_img.stopped', attack_img.tStopRefresh)
    # check responses
    if attack_resp.keys in ['', [], None]:  # No response was made
        attack_resp.keys = None
    task_trials.addData('attack_resp.keys',attack_resp.keys)
    if attack_resp.keys != None:  # we had a response
        task_trials.addData('attack_resp.rt', attack_resp.rt)
    task_trials.addData('attack_resp.started', attack_resp.tStartRefresh)
    task_trials.addData('attack_resp.stopped', attack_resp.tStopRefresh)
    if (practice == 0) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        time_scream = loud_scream.tStartRefresh
        last_stim = time_scream
    elif (practice == 2) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        time_scream = weak_scream.tStartRefresh
        last_stim = time_scream
    
    # ajdust time on 'near' trials
    # and in the real task on 'Threat' and 'near' trials
    if practice > 0 and distance == "near":
        if hit:
            attack_dur = attack_dur - 0.05
        else:
            attack_dur = attack_dur + 0.05
    elif practice == 0 and distance == "near" and condition == "Threat":
        if hit:
            attack_dur = attack_dur - 0.05
        else:
            attack_dur = attack_dur + 0.05
    
    loud_scream.stop()  # ensure sound has stopped at end of routine
    task_trials.addData('loud_scream.started', loud_scream.tStartRefresh)
    task_trials.addData('loud_scream.stopped', loud_scream.tStopRefresh)
    weak_scream.stop()  # ensure sound has stopped at end of routine
    task_trials.addData('weak_scream.started', weak_scream.tStartRefresh)
    task_trials.addData('weak_scream.stopped', weak_scream.tStopRefresh)
    # the Routine "attack" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rating_relief"-------
    continueRoutine = True
    # update component parameters for each repeat
    relief_slider.reset()
    if (practice == 0 or practice == 2) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        continueRoutine = False
    else:
        win.mouseVisible = True
        ser.write(str.encode('50'))  # rating marker
        time.sleep(0.005)
        ser.write(str.encode('00'))
    # keep track of which components have finished
    rating_reliefComponents = [relief_slider, Instructions_relief]
    for thisComponent in rating_reliefComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rating_reliefClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rating_relief"-------
    while continueRoutine:
        # get current time
        t = rating_reliefClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rating_reliefClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *relief_slider* updates
        if relief_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            relief_slider.frameNStart = frameN  # exact frame index
            relief_slider.tStart = t  # local t and not account for scr refresh
            relief_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(relief_slider, 'tStartRefresh')  # time at next scr refresh
            relief_slider.setAutoDraw(True)
        if relief_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > relief_slider.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                relief_slider.tStop = t  # not accounting for scr refresh
                relief_slider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(relief_slider, 'tStopRefresh')  # time at next scr refresh
                relief_slider.setAutoDraw(False)
        
        # *Instructions_relief* updates
        if Instructions_relief.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_relief.frameNStart = frameN  # exact frame index
            Instructions_relief.tStart = t  # local t and not account for scr refresh
            Instructions_relief.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_relief, 'tStartRefresh')  # time at next scr refresh
            Instructions_relief.setAutoDraw(True)
        if relief_slider.status == FINISHED:
            continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rating_reliefComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating_relief"-------
    for thisComponent in rating_reliefComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    task_trials.addData('relief_slider.response', relief_slider.getRating())
    task_trials.addData('relief_slider.rt', relief_slider.getRT())
    task_trials.addData('relief_slider.started', relief_slider.tStartRefresh)
    task_trials.addData('relief_slider.stopped', relief_slider.tStopRefresh)
    win.mouseVisible = False
    # save response if the slider was shown
    if (practice == 0 or practice == 2) and not\
        ((condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none")):
        # define stage
        #if practice == 2:
        #    stage = 'habituation'
        #elif practice == 0:
        #    stage = 'real'
    
        # get the item text and strip newlines/spaces
        item_text = Instructions_relief.text.strip()
    
        # write entry into custom file
        custom_q.write(expInfo['participant'] +','+ stage +','+ condition +','+ \
            distance +','+ str(attac) +','+ str(startle) +','+ 'relief' +','+ item_text +','+ \
            str(relief_slider.getRating()) +','+ str(relief_slider.getRT()) + '\n')
    
    # the Routine "rating_relief" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rating_scream"-------
    continueRoutine = True
    # update component parameters for each repeat
    scream_slider.reset()
    if (practice == 0 or practice == 2) and not\
        ((condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none")):
        continueRoutine = False
    else:
        win.mouseVisible = True
        ser.write(str.encode('50'))  # rating marker
        time.sleep(0.005)
        ser.write(str.encode('00'))
    # keep track of which components have finished
    rating_screamComponents = [scream_slider, Instructions_scream]
    for thisComponent in rating_screamComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rating_screamClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rating_scream"-------
    while continueRoutine:
        # get current time
        t = rating_screamClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rating_screamClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *scream_slider* updates
        if scream_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scream_slider.frameNStart = frameN  # exact frame index
            scream_slider.tStart = t  # local t and not account for scr refresh
            scream_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scream_slider, 'tStartRefresh')  # time at next scr refresh
            scream_slider.setAutoDraw(True)
        if scream_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > scream_slider.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                scream_slider.tStop = t  # not accounting for scr refresh
                scream_slider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(scream_slider, 'tStopRefresh')  # time at next scr refresh
                scream_slider.setAutoDraw(False)
        
        # *Instructions_scream* updates
        if Instructions_scream.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_scream.frameNStart = frameN  # exact frame index
            Instructions_scream.tStart = t  # local t and not account for scr refresh
            Instructions_scream.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_scream, 'tStartRefresh')  # time at next scr refresh
            Instructions_scream.setAutoDraw(True)
        if scream_slider.status == FINISHED:
            continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rating_screamComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating_scream"-------
    for thisComponent in rating_screamComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    task_trials.addData('scream_slider.response', scream_slider.getRating())
    task_trials.addData('scream_slider.rt', scream_slider.getRT())
    task_trials.addData('scream_slider.started', scream_slider.tStartRefresh)
    task_trials.addData('scream_slider.stopped', scream_slider.tStopRefresh)
    win.mouseVisible = False
    # save response if the slider was shown
    if (practice == 0 or practice == 2) and \
        (condition == "Threat" and attac and not hit) or \
        (condition == "Threat" and attac and distance == "none"):
        # define stage
        #if practice == 2:
        #    stage = 'habituation'
        #elif practice == 0:
        #    stage = 'real'
    
        # get the item text and strip newlines/spaces
        item_text = Instructions_scream.text.strip()
    
        # write entry into custom file
        custom_q.write(expInfo['participant'] +','+ stage +','+ condition +','+ \
            distance +','+ str(attac) +','+ str(startle) +','+ 'scream' +','+ item_text +','+ \
            str(scream_slider.getRating()) +','+ str(scream_slider.getRT()) + '\n')
            
    # clear channels
    #ser.write(str.encode('00'))
    # the Routine "rating_scream" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'task_trials'


# ------Prepare to start Routine "end_1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
end_1Components = [text_11, key_resp_11]
for thisComponent in end_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_1"-------
while continueRoutine:
    # get current time
    t = end_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_1"-------
for thisComponent in end_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
# the Routine "end_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
end_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('end_q.xlsx'),
    seed=None, name='end_trials')
thisExp.addLoop(end_trials)  # add the loop to the experiment
thisEnd_trial = end_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEnd_trial.rgb)
if thisEnd_trial != None:
    for paramName in thisEnd_trial:
        exec('{} = thisEnd_trial[paramName]'.format(paramName))

for thisEnd_trial in end_trials:
    currentLoop = end_trials
    # abbreviate parameter names if possible (e.g. rgb = thisEnd_trial.rgb)
    if thisEnd_trial != None:
        for paramName in thisEnd_trial:
            exec('{} = thisEnd_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "end_imgs"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # define size and time factors for image
    if distance == "far":
        size_factor = 16
        time_factor = 4
    elif distance == "near":
        size_factor = 2
        time_factor = 1
    elif distance == "none":
        size_factor = 1
        time_factor = 0
    
    # set size of image, changes every repeat
    img_size = (x/size_factor, y/size_factor)
    end_img.setSize(img_size)
    end_img.setImage(image)
    # keep track of which components have finished
    end_imgsComponents = [end_img]
    for thisComponent in end_imgsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_imgsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_imgs"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_imgsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_imgsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_img* updates
        if end_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_img.frameNStart = frameN  # exact frame index
            end_img.tStart = t  # local t and not account for scr refresh
            end_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_img, 'tStartRefresh')  # time at next scr refresh
            end_img.setAutoDraw(True)
        if end_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_img.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                end_img.tStop = t  # not accounting for scr refresh
                end_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_img, 'tStopRefresh')  # time at next scr refresh
                end_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_imgsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_imgs"-------
    for thisComponent in end_imgsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    end_trials.addData('end_img.started', end_img.tStartRefresh)
    end_trials.addData('end_img.stopped', end_img.tStopRefresh)
    
    # ------Prepare to start Routine "end_rating_fear"-------
    continueRoutine = True
    # update component parameters for each repeat
    fear_slider.reset()
    win.mouseVisible = True
    # keep track of which components have finished
    end_rating_fearComponents = [fear_slider, Instructions_fear]
    for thisComponent in end_rating_fearComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_rating_fearClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_rating_fear"-------
    while continueRoutine:
        # get current time
        t = end_rating_fearClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_rating_fearClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fear_slider* updates
        if fear_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fear_slider.frameNStart = frameN  # exact frame index
            fear_slider.tStart = t  # local t and not account for scr refresh
            fear_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fear_slider, 'tStartRefresh')  # time at next scr refresh
            fear_slider.setAutoDraw(True)
        
        # Check fear_slider for response to end routine
        if fear_slider.getRating() is not None and fear_slider.status == STARTED:
            continueRoutine = False
        
        # *Instructions_fear* updates
        if Instructions_fear.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_fear.frameNStart = frameN  # exact frame index
            Instructions_fear.tStart = t  # local t and not account for scr refresh
            Instructions_fear.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_fear, 'tStartRefresh')  # time at next scr refresh
            Instructions_fear.setAutoDraw(True)
        #if fear_slider.status == FINISHED:
        #    continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_rating_fearComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_rating_fear"-------
    for thisComponent in end_rating_fearComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    end_trials.addData('fear_slider.response', fear_slider.getRating())
    end_trials.addData('fear_slider.rt', fear_slider.getRT())
    end_trials.addData('fear_slider.started', fear_slider.tStartRefresh)
    end_trials.addData('fear_slider.stopped', fear_slider.tStopRefresh)
    
    # get the item text and strip newlines/spaces
    item_text = Instructions_fear.text.strip()
    
    # write entry into custom file
    custom_q.write(expInfo['participant'] +','+ stage +','+ condition +','+ \
        distance +',NA,NA,'+ 'pic_fear' +','+ item_text +','+ \
        str(fear_slider.getRating()) +','+ str(fear_slider.getRT()) + '\n')
        
    # clear channels
    #ser.write(str.encode('00'))
    # the Routine "end_rating_fear" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "end_rating_pleasant"-------
    continueRoutine = True
    # update component parameters for each repeat
    pleasant_slider.reset()
    win.mouseVisible = True
    # keep track of which components have finished
    end_rating_pleasantComponents = [pleasant_slider, Instructions_pleasant]
    for thisComponent in end_rating_pleasantComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_rating_pleasantClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_rating_pleasant"-------
    while continueRoutine:
        # get current time
        t = end_rating_pleasantClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_rating_pleasantClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pleasant_slider* updates
        if pleasant_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasant_slider.frameNStart = frameN  # exact frame index
            pleasant_slider.tStart = t  # local t and not account for scr refresh
            pleasant_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasant_slider, 'tStartRefresh')  # time at next scr refresh
            pleasant_slider.setAutoDraw(True)
        
        # Check pleasant_slider for response to end routine
        if pleasant_slider.getRating() is not None and pleasant_slider.status == STARTED:
            continueRoutine = False
        
        # *Instructions_pleasant* updates
        if Instructions_pleasant.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_pleasant.frameNStart = frameN  # exact frame index
            Instructions_pleasant.tStart = t  # local t and not account for scr refresh
            Instructions_pleasant.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_pleasant, 'tStartRefresh')  # time at next scr refresh
            Instructions_pleasant.setAutoDraw(True)
        #if pleasant_slider.status == FINISHED:
        #    continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_rating_pleasantComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_rating_pleasant"-------
    for thisComponent in end_rating_pleasantComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    end_trials.addData('pleasant_slider.response', pleasant_slider.getRating())
    end_trials.addData('pleasant_slider.rt', pleasant_slider.getRT())
    end_trials.addData('pleasant_slider.started', pleasant_slider.tStartRefresh)
    end_trials.addData('pleasant_slider.stopped', pleasant_slider.tStopRefresh)
    
    # get the item text and strip newlines/spaces
    item_text = Instructions_pleasant.text.strip()
    
    # write entry into custom file
    custom_q.write(expInfo['participant'] +','+ stage +','+ condition +','+ \
        distance +',NA,NA,'+ 'pic_pleasant' +','+ item_text +','+ \
        str(pleasant_slider.getRating()) +','+ str(pleasant_slider.getRT()) + '\n')
    
    # clear channels
    #ser.write(str.encode('00'))
    # the Routine "end_rating_pleasant" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'end_trials'


# ------Prepare to start Routine "end_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
win.mouseVisible = False
# keep track of which components have finished
end_2Components = [text_12, key_resp_12]
for thisComponent in end_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_2"-------
while continueRoutine:
    # get current time
    t = end_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['right'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_2"-------
for thisComponent in end_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
# the Routine "end_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
