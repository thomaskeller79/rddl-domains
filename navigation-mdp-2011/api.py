domains = [{
    'description': '(mdp11) Navigation:\n\nsubmitted by Sungwook Yoon, modified by Scott Sanner.\n\nDescription: In a grid, a robot (R) must get to a goal (G).  Every cell offers the robot a (different) chance of disappearing.  The robot needs to choose a path which gets it to the goal most reliably within the finite horizon time. \n *********************** \n *  0   0   0   0   R  * \n * .1  .3  .5  .7  .9  * \n * .1  .3  .5  .7  .9  * \n * .1  .3  .5  .7  .9  * \n * .1  .3  .5  .7  .9  * \n *  0   0   0   0   G  * \n *********************** \n\n This is a good domain to test deteminized planners because one can see here that the path using the .3 chance of failure leads to a 1-step most likely outcome of survival, but a poor 4-step change of survival (.7^(.4)) whereas the path using a .1 chance of failure is much more safe. The domain generators for navigation have a flag to produce slightly obfuscated files to discourage hand-coded policies, but rddl.viz.NavigationDisplay can properly display these grids, e.g., \n ./run rddl.sim.Simulator files/final_comp/rddl rddl.policy.RandomBoolPolicy navigation_inst_mdp__1 rddl.viz.NavigationDisplay \n (Movement was not made stochastic due to the lack of intermediate variables and synchronic arcs to support both the PPDDL and SPUDD translations.)',
    'ipc': '2011',
    'name': 'navigation',
    'problems': [('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__1.rddl'),
                 ('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__2.rddl'),
                 ('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__3.rddl'),
                 ('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__4.rddl'),
                 ('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__5.rddl'),
                 ('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__6.rddl'),
                 ('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__7.rddl'),
                 ('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__8.rddl'),
                 ('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__9.rddl'),
                 ('navigation-mdp-2011/navigation_mdp.rddl', 'navigation-mdp-2011/navigation_inst_mdp__10.rddl')]}]
