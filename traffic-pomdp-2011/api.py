domains = [{
    'description': '(pomdp11) Traffic:\n\nsubmitted by Scott Sanner.\n\nDescription: A simple binary version of the cell transition model (CTM) for modeling traffic.  Based on the original CTM Tech Report and its specification as a factored MDP in the following papers:\n The Cell Transition Model: Network Traffic.  Daganzo; Tech Report Berkeley Institute of Transport Studies, 1994. \n Efficient Solutions to Factored MDPs with Imprecise Transition Probabilities.  Delgado, Sanner, de Barros, Cozman; ICAPS, 2009. \n Because of the binary variable and no intermediate variable restrictions for the IPPC 2011, this model is quite simplified and ignores traffic aspects such as turns and turn probabilities. \n Note that this model uses concurrent actions, but that the number of total actions will only ever be 2^(# intersections).  Refer to the IPPC email list if you are unsure how to handle concurrent actions.',
    'ipc': '2011',
    'name': 'traffic',
    'problems': [('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__1.rddl'),
                 ('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__2.rddl'),
                 ('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__3.rddl'),
                 ('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__4.rddl'),
                 ('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__5.rddl'),
                 ('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__6.rddl'),
                 ('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__7.rddl'),
                 ('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__8.rddl'),
                 ('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__9.rddl'),
                 ('traffic-pomdp-2011/traffic_pomdp.rddl', 'traffic-pomdp-2011/traffic_inst_pomdp__10.rddl')]}]
