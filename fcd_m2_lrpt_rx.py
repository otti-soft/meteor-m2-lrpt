#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Meteor QPSK LRPT
# Author: bravoromeo5
# Generated: Wed Jul 20 21:01:28 2016
##################################################

from datetime import datetime
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import fcdproplus
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Meteor QPSK LRPT")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_airspy = samp_rate_airspy = 192000
        self.decim = decim = 1
        self.symb_rate = symb_rate = 72000
        self.samp_rate = samp_rate = samp_rate_airspy/decim
        self.sps = sps = (samp_rate*1.0)/(symb_rate*1.0)
        self.rfgain = rfgain = 9
        self.pll_alpha = pll_alpha = 0.015
        self.ifgain = ifgain = 10
        self.freq = freq = 137900000
        self.clock_alpha = clock_alpha = 0.001
        self.bitstream_name = bitstream_name = "/tmp/meteor_LRPT_" + datetime.now().strftime("%d%m%Y_%H%M") + ".s"

        ##################################################
        # Blocks
        ##################################################
        self.nb_0 = self.nb_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb_0.AddPage(grc_wxgui.Panel(self.nb_0), "SDR FFT")
        self.nb_0.AddPage(grc_wxgui.Panel(self.nb_0), "QPSK Constellation")
        self.Add(self.nb_0)
        _pll_alpha_sizer = wx.BoxSizer(wx.VERTICAL)
        self._pll_alpha_text_box = forms.text_box(
        	parent=self.nb_0.GetPage(1).GetWin(),
        	sizer=_pll_alpha_sizer,
        	value=self.pll_alpha,
        	callback=self.set_pll_alpha,
        	label="PLL Alpha",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._pll_alpha_slider = forms.slider(
        	parent=self.nb_0.GetPage(1).GetWin(),
        	sizer=_pll_alpha_sizer,
        	value=self.pll_alpha,
        	callback=self.set_pll_alpha,
        	minimum=0.001,
        	maximum=0.1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb_0.GetPage(1).Add(_pll_alpha_sizer)
        _clock_alpha_sizer = wx.BoxSizer(wx.VERTICAL)
        self._clock_alpha_text_box = forms.text_box(
        	parent=self.nb_0.GetPage(1).GetWin(),
        	sizer=_clock_alpha_sizer,
        	value=self.clock_alpha,
        	callback=self.set_clock_alpha,
        	label="Clock Alpha",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._clock_alpha_slider = forms.slider(
        	parent=self.nb_0.GetPage(1).GetWin(),
        	sizer=_clock_alpha_sizer,
        	value=self.clock_alpha,
        	callback=self.set_clock_alpha,
        	minimum=0.001,
        	maximum=0.01,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb_0.GetPage(1).Add(_clock_alpha_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.nb_0.GetPage(1).GetWin(),
        	title="Scope Plot",
        	sample_rate=symb_rate,
        	v_scale=0.5,
        	v_offset=0,
        	t_scale=0.5,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.nb_0.GetPage(1).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.nb_0.GetPage(0).GetWin(),
        	baseband_freq=freq,
        	y_per_div=5,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=768,
        	fft_rate=25,
        	average=True,
        	avg_alpha=0.1,
        	title="Filtered Spectrum",
        	peak_hold=False,
        )
        self.nb_0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, samp_rate, symb_rate, 0.6, 361))
        _rfgain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rfgain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rfgain_sizer,
        	value=self.rfgain,
        	callback=self.set_rfgain,
        	label="RF Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rfgain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rfgain_sizer,
        	value=self.rfgain,
        	callback=self.set_rfgain,
        	minimum=1,
        	maximum=15,
        	num_steps=14,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rfgain_sizer)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        _ifgain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ifgain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ifgain_sizer,
        	value=self.ifgain,
        	callback=self.set_ifgain,
        	label="IF Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ifgain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ifgain_sizer,
        	value=self.ifgain,
        	callback=self.set_ifgain,
        	minimum=1,
        	maximum=15,
        	num_steps=14,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_ifgain_sizer)
        self.fcdproplus_fcdproplus_0 = fcdproplus.fcdproplus("0",1)
        self.fcdproplus_fcdproplus_0.set_lna(1)
        self.fcdproplus_fcdproplus_0.set_mixer_gain(0)
        self.fcdproplus_fcdproplus_0.set_if_gain(30)
        self.fcdproplus_fcdproplus_0.set_freq_corr(0)
        self.fcdproplus_fcdproplus_0.set_freq(137900000)
          
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(pll_alpha, 4)
        self.digital_constellation_soft_decoder_cf_1 = digital.constellation_soft_decoder_cf(digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 1).base())
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_cc(sps, clock_alpha**2/4.0, 0.5, clock_alpha, 0.005)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 127)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, bitstream_name, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_rail_ff_0 = analog.rail_ff(-1, 1)
        self.analog_agc_xx_0 = analog.agc_cc(1000e-4, 0.5, 1.0)
        self.analog_agc_xx_0.set_max_gain(4000)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_constellation_soft_decoder_cf_1, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_1, 0), (self.analog_rail_ff_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.analog_agc_xx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.analog_rail_ff_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.analog_agc_xx_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.fcdproplus_fcdproplus_0, 0), (self.rational_resampler_xxx_0, 0))



    def get_samp_rate_airspy(self):
        return self.samp_rate_airspy

    def set_samp_rate_airspy(self, samp_rate_airspy):
        self.samp_rate_airspy = samp_rate_airspy
        self.set_samp_rate(self.samp_rate_airspy/self.decim)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samp_rate(self.samp_rate_airspy/self.decim)

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_sps((self.samp_rate*1.0)/(self.symb_rate*1.0))
        self.wxgui_scopesink2_0.set_sample_rate(self.symb_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.symb_rate, 0.6, 361))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps((self.samp_rate*1.0)/(self.symb_rate*1.0))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.symb_rate, 0.6, 361))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_clock_recovery_mm_xx_0.set_omega(self.sps)

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self._rfgain_slider.set_value(self.rfgain)
        self._rfgain_text_box.set_value(self.rfgain)

    def get_pll_alpha(self):
        return self.pll_alpha

    def set_pll_alpha(self, pll_alpha):
        self.pll_alpha = pll_alpha
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.pll_alpha)
        self._pll_alpha_slider.set_value(self.pll_alpha)
        self._pll_alpha_text_box.set_value(self.pll_alpha)

    def get_ifgain(self):
        return self.ifgain

    def set_ifgain(self, ifgain):
        self.ifgain = ifgain
        self._ifgain_slider.set_value(self.ifgain)
        self._ifgain_text_box.set_value(self.ifgain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.wxgui_fftsink2_0.set_baseband_freq(self.freq)

    def get_clock_alpha(self):
        return self.clock_alpha

    def set_clock_alpha(self, clock_alpha):
        self.clock_alpha = clock_alpha
        self.digital_clock_recovery_mm_xx_0.set_gain_omega(self.clock_alpha**2/4.0)
        self.digital_clock_recovery_mm_xx_0.set_gain_mu(self.clock_alpha)
        self._clock_alpha_slider.set_value(self.clock_alpha)
        self._clock_alpha_text_box.set_value(self.clock_alpha)

    def get_bitstream_name(self):
        return self.bitstream_name

    def set_bitstream_name(self, bitstream_name):
        self.bitstream_name = bitstream_name
        self.blocks_file_sink_0.open(self.bitstream_name)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
