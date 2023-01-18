domains = [{
    'description': '(mdp18) Manufacturer:\n\nsubmitted by Thomas Keller.\n\nDescription: In this domain, the agent manages a manufacturing company that buys goods to use them in the production of other goods. The relationship between the various goods (i.e., which good is required in the production of which other good) takes the form of a directed acyclic graph.\n Prizes of goods are determined stochastically by being drawn towards a long-term trend price level with higher probability than moving away from it. The accumulated reward encodes the bank account of the company, i.e., all monetary costs in the domain incur a negative reward while selling      goods yields a positive reward. \n This domain is modular in the sense that additional options are available in more challenging instances, all of which have in common that the agent has to take an immediate cost for an increased long-term reward. This is already true for the basic concept of buying goods (cost) to produce another good that can be sold for more than the sum of the costs. The following modules (that can be mixed) are available:\n M1 Construction of factories: in addition to having an initial factory, it is possible to build new factories (at a cost) and produce different goods with higher expected profit.\n M2 Marketing managers and lobbyists: it is possible to hire marketing managers that allow to sell produced goods for a higher prize, and lobbyists that allow to buy products for a lower prize, but the company has to pay a salary. \n M3 Production managers: production managers can be hired to enable the use of actions that purchase, produce (and sell) in a single step rather than in  two (or three) steps. This speeds up the positive reward from producing goods, but also comes with the cost of paying the production manager\'s salary.',
    'ipc': '2018',
    'name': 'manufacturer',
    'problems': [('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__01.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__02.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__03.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__04.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__05.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__06.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__07.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__08.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__09.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__10.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__11.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__12.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__13.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__14.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__15.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__16.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__17.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__18.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__19.rddl'),
                 ('manufacturer-mdp-2018/manufacturer_mdp.rddl', 'manufacturer-mdp-2018/manufacturer_inst_mdp__20.rddl')]}]