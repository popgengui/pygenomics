# -*- coding: utf-8 -*-
'''
.. module:: genomics.config
   :synopsis: library configuration
   :noindex:
   :copyright: Copyright 2014 by Tiago Antao
   :license: GNU Affero, see LICENSE for details

.. moduleauthor:: Tiago Antao <tra@popgen.net>

'''
import configparser
import os

config_file = os.path.expanduser('~/.config/pygenomics/main.conf')
# This can be configured before loading of the main module to read another file


class Config:
    '''Configuration object

    :param config_file: The config file to use

    The default config file is defined above and can be changed before doing
    import genomics


    Configuration parameters are separated by section

    **Section main**

    * **mr_dir** Directory where temporary map_reduce communication is stored
    * **grid** Grid type (Local)

    **Section grid.local**

    The parameters for grid type Local.

    Currently limit (see :py:class:`genomics.parallel.executor.Local`)
    '''
    def __init__(self, config_file=config_file):
        self.config_file = config_file

    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        self.grid = config['main']['grid']
        if self.grid == 'Local':
            self.grid_limit = config['grid.local']['limit']
            if self.grid_limit.find('.') > -1:
                self.grid_limit = float(self.grid_limit)
            else:
                self.grid_limit = int(self.grid_limit)
