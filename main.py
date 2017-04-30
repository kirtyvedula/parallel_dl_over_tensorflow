

import matplotlib.pyplot as plt
import experiment
import experiment_results
import experiments_manager

#from experiment_runner import find_cifar_baseline, find_cifar_history
from experiment_runner import find_cifar_baseline, find_cifar_multinode, find_simple_baseline, \
    ExperimentRunner, simple_with_history_baseline, \
    simple_multinode, simple





experiments = {}

############ SIMPLE (first make sure we can overfit the data) #################
# experiments = simple()
# runner = ExperimentRunner(experiments, force_rerun=True)
# runner.run()


############ BASELINE #################
# experiments = find_simple_baseline()
# runner = ExperimentRunner(experiments, force_rerun=True)
# runner.run()



############# HISTORY  #################
# experiments = simple_with_history_baseline(h=8, sesop_batch_mult=8)
# runner = ExperimentRunner(experiments, force_rerun=True)
# runner.run()


############ MULTI NODE #################
# experiments = simple_multinode(n=4, h=8, sesop_batch_mult=5)
# runner = ExperimentRunner(experiments, force_rerun=True)
# runner.run()



########### MIX #############
for h in [1, 2, 4, 8, 16]:
    experiments = simple_with_history_baseline(h=h, sesop_batch_mult=5)
    runner = ExperimentRunner(experiments, force_rerun=True)
    runner.run()

for h in [1, 2, 4, 8, 16]:
    experiments = simple_multinode(n=2, h=h, sesop_batch_mult=5)
    runner = ExperimentRunner(experiments, force_rerun=True)
    runner.run()

for h in [1, 2, 4, 8, 16]:
    experiments = simple_multinode(n=4, h=h, sesop_batch_mult=5)
    runner = ExperimentRunner(experiments, force_rerun=True)
    runner.run()

print '########### DONE #################'
print '########### DONE #################'
print '########### DONE #################'
print '########### DONE #################'
print '########### DONE #################'
