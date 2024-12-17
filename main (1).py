import yaml
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from src.utils.load_evaluations import load_evaluation
from src.utils.load_trainers import load_trainer
from src.utils.load_analysis import load_analysis


if len(sys.argv) > 1:
    configfname = sys.argv[1]
else:
    # configfname = '/home/eheng/NLPScholarFork/final_project/LinearAlgebra_config.yaml'
    # configfname = '/home/eheng/NLPScholarFork/final_project/Algebra_config.yaml'
    # configfname = '/home/eheng/NLPScholarFork/final_project/AbstractAlgebra_config.yaml'
    # configfname = '/home/eheng/NLPScholarFork/final_project/Geometry_config.yaml'
    # configfname = '/home/eheng/NLPScholarFork/final_project/Calculus_config.yaml'
    # configfname = '/home/eheng/NLPScholarFork/final_project/DiscreteMathematics_config.yaml'
    configfname = '/home/eheng/NLPScholarFork/final_project/SetTheory_config.yaml'
    # configfname = '/home/eheng/NLPScholarFork/final_project/NumberTheory_config.yaml'
    # configfname = '/home/eheng/NLPScholarFork/final_project/Logic_config.yaml'
    # configfname = '/home/eheng/NLPScholarFork/final_project/Topology_config.yaml'

sys.stderr.write(f'Reading from {configfname}\n')

with open(configfname, 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

modes = config['mode']
for mode in modes:
    if mode == 'interact':
        exp = load_evaluation(config)
        exp.interact()
    if mode == 'evaluate':
        exp = load_evaluation(config)
        exp.evaluate()
    if mode == 'train':
        exp = load_trainer(config)
        exp.train()
    if mode == 'analyze':
        exp = load_analysis(config)
        exp.analyze()
