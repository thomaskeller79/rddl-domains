domains = [{
    'description': '(mdp11) Skill Teaching:\n\nsubmitted by Tom Walsh, with special thanks to Derek Green and Paul Cohen at University of Arizona for help with the design.\n\nDescription: In the SkillTeaching MDP domain, the agent is trying to teach a series of skills to a student through the use of hints and multiple choice questions.  The student has a proficiency level for each skill, which indicates his ability to answer questions of that skill and positive reward is given for high proficiency on skills while negative reward is given for low proficiency.  Each skill also has a weight on how much it is worth. \n Many of the skills are connected in that some are "pre-conditions" of others.  If all of a skill\'s pre-conditions are learned, the student has some probability of answering questions about it right, and each precondition that is at high proficiency adds to the probability though knowing all of them can lead to a probability higher than the sum of the components.  Hints only work if all the preconditions are known and can only get you to medium proficiency.\n Student proficiency increases with questions answered right and decreases with questions about a skill answered wrong and sometimes decreases by chance.\n To model the teacher-student interaction, every other step in the domain is the student\'s turn, where they answer a question. The planning problems here are: \n 1) Whether or not to teach all the prerequisites of a skill before teaching it.\n 2) What skill to focus on next \n 3) When to give hints and when to use multiple choice problems',
    'ipc': '2011',
    'name': 'skill-teaching',
    'problems': [('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__1.rddl'),
                 ('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__2.rddl'),
                 ('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__3.rddl'),
                 ('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__4.rddl'),
                 ('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__5.rddl'),
                 ('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__6.rddl'),
                 ('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__7.rddl'),
                 ('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__8.rddl'),
                 ('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__9.rddl'),
                 ('skill-teaching-mdp-2011/skill_teaching_mdp.rddl', 'skill-teaching-mdp-2011/skill_teaching_inst_mdp__10.rddl')]}]
