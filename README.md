# meteor-m2-lrpt
GNU Radio scripts for METEOR M2 Satellite LRPT reception with AIRSPY SDR.


These scripts require GNU radio 3.7.x - older versions of GNU radio will not work due to missing blocks.

These GRC flow graphs provide a realtime LRPT Soft-Symbol Receiver.

Original author of base script: Martin Blaho (modified by Raydel Abreu for RTL SDR)
Modification for Airspy: by Otti (decimating FIR, RRC filtering)


The following files are provided:

- airspy_m2_lrpt_rx_10msps.grc   (this is the LRPT RX script for Airspy in 10msps sampling mode)  
- airspy_m2_lrpt_rx.grc          (same as above, but in 2.5msps mode for less CPU load)


Usage:

Use a satellite prdecition software such a gpredict to determine when METEROR M2 is in radio range of your loacation. The signals are of similar strength as NOAA APT analogue weather satellite transmissions.
If you have received NOAA before, it should be possible to receive METEOR M2 with the same antenna.

I recommend you to familiarize yourself with NOAA APT reception before trying METEOR M2.

Load one of the GRC files into GNU Radio companion. 

When used for the first time:
Please set your file storage path to match your local file system. To do so please lacate the variable block with the ID "bitstream_name", double click on it and in the Value filed please overwrite the part "/home/otti/" with the local path of your choice. Make sure you leave the rest of the value field untouched.

IMPORTANT: You need to have access to the chosen path, otherwise an error may occur once you execute the flow graph.


When the flow graph is executed:

One of the tabs shows the received signal spectrum in a FFT graph.
Sliders allow setting the RF and IF gain of Airspy

The second tab shows a constellation graph of the demodulated bitstream.
Sliders allow setting the parameters of the QPSK demodulator to achieve a lock on the signal.
(under most cisrcumstances the default values should work fine) 

The flow graph continues to write the demodulated soft bits into the *.s file until you stop the flow graph by closing its GUI window.

When no satellite is in range and you execute the graph you should see a rather flat spectrum display and random noise in the QPSK constellation graph.


Now, when the satellite is in range execute the flowgraph (press the black "play" triangle in the menu bar).
You should now see a wideband signal "hump" centered in the spectrum praph.
When switching into the constellation tab you should see four dots representing the QPSK signal


Continue recording the *.s file until the satellite disappears (signal becoming so weak that the four dots disappear)

Once completed load the demodulated bitstream file (*.s file) into Oleg's METEOR M2 LRPT Decoder under Windows.

You can download it from here:  http://meteor.robonuka.ru/for-experts/soft/

The decoder should decode the various PIDs from the demodulated 72kbit/s QPSK signal and generate preview images of the three transmitted spectral channels. You can then generate a composite image and store it directly within the decoder software.

Please check various tutorials on YouTube which describe this last step (Oleg's decoder).

You may try to run it under Linux using Wine, but it seems that the newer versions do not run under Wine anymore.

Feel free to modify and improve these flow graphs, but please share :-)

Enjoy,

Otti


