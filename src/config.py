import pathlib
import os
import torch
from yacs.config import CfgNode as CN

#GENERAL CONFIG

_C = CN()
_C.PROJECT_DIR = str(pathlib.Path(__file__).parent.parent.absolute())
_C.DATA_DIR = os.path.join(_C.PROJECT_DIR, 'data')
_C.DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

#Dataset config
_C.DATASET = CN()

#TILE CREATION
_C.DATASET.IMG_SCALE = 0.25
_C.DATASET.TRAIN_TILE_SIZE = 320
_C.DATASET.TRAIN_TILE_AVG_STEP = 160
_C.DATASET.TRAIN_TILE_MIN_SCORE = 0.25
_C.DATASET.TILE_DIR = os.path.join(
    _C.DATA_DIR, 
    'train', 
    f'{_C.DATASET.IMG_SCALE}_{_C.DATASET.TRAIN_TILE_MIN_SCORE}_{_C.DATASET.TRAIN_TILE_SIZE}_{_C.DATASET.TRAIN_TILE_AVG_STEP}_train'
)
_C.DATASET.VALID_ID = ['54f2eec69', 'aaa6a05cc']

 #DATASET AUGMENTATION
_C.DATASET.IMG_HEIGHT = 256
_C.DATASET.IMG_WIDTH = 256
_C.DATASET.H_FLIP_PROB = 0.5
_C.DATASET.NUM_WORKERS = 2

#Loader config
_C.TRAIN_LOADER = CN()
_C.TRAIN_LOADER.BATCH_SIZE = 32
_C.TRAIN_LOADER.NUM_WORKERS = 4

_C.VALID_LOADER = CN()
_C.VALID_LOADER.BATCH_SIZE = 128
_C.VALID_LOADER.NUM_WORKERS = 4

#solver config
_C.SOLVER = CN()
_C.SOLVER.NUM_EPOCHS = 40
_C.SOLVER.OPTIMIZER = 'Adam'
_C.SOLVER.SCHEDULER = 'ReduceLROnPlateau'
_C.SOLVER.SCHEDULER_MODE = 'max'
_C.SOLVER.LR = 1e-03
_C.SOLVER.WEIGHT_DECAY = 0
_C.SOLVER.BETAS = (0.9, 0.999)
_C.SOLVER.AMSGRAD = False
_C.SOLVER.SCHEDULER_REDFACT = 0.1
_C.SOLVER.SCHEDULER_PATIENCE = 10

#Parametri per CosineAnnealing
_C.SOLVER.SCHEDULER_COS_CPOCH = 2
_C.SOLVER.SCHEDULER_T_MUL = 2


#Model config
_C.MODEL = CN()
_C.MODEL.NAME = 'resnet18'
_C.MODEL.PRETRAINING = 'imagenet'
_C.MODEL.ATTENTION = True