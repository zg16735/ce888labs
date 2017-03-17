# Lab4


## Compare and plot Q-values

- [ ] Keep only e-decreasing, UCB and bootstrap from your examples
- [ ] Change the reward of each function from 1,0 to 1,-1 and redo the plots
* ![0.2-decreasing_1](./0.2-decreasing_1.pdf?raw=true)
* ![UCB_1](./UCB_1.pdf?raw=true)
* ![BootstrapTS_1](./BootstrapTS_1.pdf?raw=true)
- [ ] Change the rewards of each function to 10,-10 and redo the plots
* ![0.2-decreasing_10](./0.2-decreasing_10.pdf?raw=true)
* ![UCB_10](./UCB_10.pdf?raw=true)
* ![BootstrapTS_10](./BootstrapTS_10.pdf?raw=true)
* What do you observe? 
* When we change the 'n_trials', the clearance of the charts varies. The bigger 'n_trials' is, the shadow of the charts becomes smaller. However, the large number of 'n_trials' takes much time to run.
- [ ] Get the best bandit that you have for 10,-10 and plot the Q-values for each time step
* ![0.2-decreasing_10_Q](./0.2-decreasing_10_Q.pdf?raw=true)
* ![UCB_10_Q](./UCB_10_Q.pdf?raw=true)
* ![BootstrapTS_10_Q](./BootstrapTS_10_Q.pdf?raw=true)
* What do you observe?
* After comparison between e-decreasing, UCB and bootstrap, we find bootstrap has the best bandit.
