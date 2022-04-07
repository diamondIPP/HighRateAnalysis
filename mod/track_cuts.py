#!/usr/bin/env python
# --------------------------------------------------------
#       cuts for the tracks
# created on March 30th 2022 by M. Reichmann (remichae@phys.ethz.ch)
# --------------------------------------------------------

from mod.dut_cuts import DUTCut


class TrackCut(DUTCut):
    def __init__(self, ana):
        super().__init__(ana, meta_sub_dir='track_cuts')

    def __call__(self, cut=None, data=None, pl=None):
        cut = super().__call__(cut)
        if data is None:
            return cut
        if data.size == self.Ana.NEvents:
            return self.ev2trk(data)[cut]
        if cut is not ... and cut.size == self.Ana.N:
            return self.trk2pl(data, pl)[cut]
        return data[cut]

    def make(self, redo=False):
        self.register('tp', self.make_trigger_phase(_redo=redo), 10, 'trigger phase')
        self.register('res', self.Ana.REF.Cut.make_trk_residual(redo), 20, 'tracks with a small residual in the REF')
        self.register('fid', self.make_fiducial(_redo=redo), 30, 'tracks in fiducial area')
        self.register('tstart', self.make_start_time(_redo=redo), 40, 'exclude first events')
        self.register('chi2', self.make_chi2(_redo=redo), 50, 'small chi2')

    def make_trk(self, trks):
        return self.make_ev(trks, self.Ana.NTracks)