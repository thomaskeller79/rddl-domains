domains = [{
    'description': '(mdp11) Crossing Traffic:\n\nsubmitted by Sungwook Yoon, modified by Scott Sanner.\n\nDescription: In a grid, a robot (R) must get to a goal (G) and avoid obstacles (O) arriving randomly and moving left. If an obstacle overlaps with the robot, the robot disappears and can no longer move around.  The robot can "duck" underneath a car by deliberately moving right/east when a car is to the right of it (this can make the solution interesting... the robot should start at the left side of the screen then). The robot receives -1 for every time step it has not reached the goal. The goal state is absorbing with 0 reward.\n\n ****************\n *            R * \n *  <-O <-O <-O *\n *    <-O   <-O *\n * <-O    <-O   *\n *     <-O  <-O *\n *            G *\n ****************\n\nYou can think of this as the RDDL version of Frogger:\n\n http:en.wikipedia.org/wiki/Frogger',
    'ipc': '2011',
    'name': 'crossing-traffic',
    'problems': [('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__1.rddl'),
                 ('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__2.rddl'),
                 ('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__3.rddl'),
                 ('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__4.rddl'),
                 ('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__5.rddl'),
                 ('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__6.rddl'),
                 ('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__7.rddl'),
                 ('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__8.rddl'),
                 ('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__9.rddl'),
                 ('crossing-traffic-mdp-2011/crossing_traffic_mdp.rddl', 'crossing-traffic-mdp-2011/crossing_traffic_inst_mdp__10.rddl')]}]
