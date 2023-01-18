domains = [{
    'description': '(pomdp11) Elevators:\n\nsubmitted by Tom Walsh, modified by Scott Sanner.\n\nDescription: The "elevators" domain has a number of elevators delivering passengers to either the top or the bottom floor (the only allowable destinations). Potential passengers arrive at a floor based on Bernoulli draws with a potentially different arrival probability for each floor.\n The elevator can move in its current direction if the doors are closed, can remain stationary (noop), or can open its door while indicating the direction that it will go in next (this allows potential passengers to determine whether to board or not).  Note that the elevator can only change direction by opening its door while indicating the opposite  direction. \n A passable plan in this domain is to pick up a passenger every time they appear and take them to their destination.  A better plan includes having the elevator "hover" near floors where passengers are likely to arrive and coordinating multiple elevators for up and down passengers.\n This domain was designed to support extension to multiple elevators and may be used in either single or multi-elevator mode.', 
    'ipc': '2011',
    'name': 'elevators',
    'problems': [('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__1.rddl'),
                 ('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__2.rddl'),
                 ('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__3.rddl'),
                 ('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__4.rddl'),
                 ('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__5.rddl'),
                 ('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__6.rddl'),
                 ('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__7.rddl'),
                 ('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__8.rddl'),
                 ('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__9.rddl'),
                 ('elevators-pomdp-2011/elevators_pomdp.rddl', 'elevators-pomdp-2011/elevators_inst_pomdp__10.rddl')]}]
