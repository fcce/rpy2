#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-09-21 22:43:00
# @Author  : Fengce kalelfc@gmail.com
# @Link    : www.rforgis.com

'''
python 调用 R语言，并使用 ggplot2
'''
import rpy2.robjects.lib.ggplot2 as ggplot2
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
datasets = importr('datasets')
mtcars = datasets.__rdata__.fetch('mtcars')['mtcars']
gp = ggplot2.ggplot(mtcars)
pp = ggplot2.ggplot(mtcars) + \
     ggplot2.aes_string(x='wt', y='mpg', col='factor(cyl)') + \
     ggplot2.geom_point() + \
     ggplot2.geom_smooth(ggplot2.aes_string(group = 'cyl'),
                         method = 'lm')
#pp.plot()
ro.r.pdf('ggplot2inPython.pdf')
pp.plot()
ro.r('dev.off')
