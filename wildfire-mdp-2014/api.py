domains = [{
    'description': '(mdp14) Wildfire:\n\nsubmitted by Zhenyu Yu.\n\nDescription: General reference: Karafyllidis, I., & Thanailakis, A. (1997). A model for predicting forest fire spreading using gridular automata. Ecological Modelling, 99(1), 87-97. http://www.dpi.inpe.br/gilberto/cursos/st-society-2013/Kara1997.pdf \n In a general wildfire scenario, its spread is mostly determined by the weather (i.e. wind), terrain slope, and fuel type (i.e. grass, wood). In this scenario, a map is represented with grids, size of n*n. Each grid has some attributes, including fuel type, terrain elevation. Furthermore, the fuel type and terrain elevation will affect the fire spreading speed.  Some fuel type is more easily on fire than other, and higher grids are always easier to catch fire.  Cell features and effects of wind are not modeled in this simplified version. \n In this version, whether a cell would be on fire is determined by its neighbor grids, and the fire spreading law is simplified with this function \n p(burning(xi, yj)=true) = 1 / (1 + exp(4.5 - k)) \n where k is the number of neighbors on fire. \n The decision task to a emergency manager is to control the fire and keep it away from important targets.',
    'ipc': '2014',
    'name': 'wildfire',
    'problems': [('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__1.rddl'),
                 ('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__2.rddl'),
                 ('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__3.rddl'),
                 ('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__4.rddl'),
                 ('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__5.rddl'),
                 ('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__6.rddl'),
                 ('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__7.rddl'),
                 ('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__8.rddl'),
                 ('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__9.rddl'),
                 ('wildfire-mdp-2014/wildfire_mdp.rddl', 'wildfire-mdp-2014/wildfire_inst_mdp__10.rddl')]}]
