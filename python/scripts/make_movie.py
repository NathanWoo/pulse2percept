
import sys
sys.path.append('..')

import numpy as np
import electrode2currentmap as e2cm
import effectivecurrent2brightness as ec2b

s1 = e2cm.Stimulus(freq=20, pulse_dur=0.075/1000., tsample=0.075/1000.)

ea = e2cm.ElectrodeArray([250], [0], [0])
r = e2cm.Retina(axon_map='../axon.npz')
ecm = r.ecm(ea, [s1])
tm1 = ec2b.TemporalModel()
sr = np.zeros(ecm.shape)

for xx in range(ecm.shape[0]):
    for yy in range(ecm.shape[1]):
        s1.amplitude = ecm[xx, yy]
        fr = tm1.fast_response(s1)
        ca = tm1.charge_accumulation(fr, s1)
        sn = tm1.stationary_nonlinearity(ca)
        sr[xx, yy] = tm1.slow_response(sn, s1)[:ecm.shape[-1]]