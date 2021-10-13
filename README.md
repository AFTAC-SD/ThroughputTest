# Influx-stress
This program is designed to let the user test write limits to an influxdb.  It is setup by default to look for an internally*(This is configurable to externally hosted at the CLI)* hosted influxdb on port 8086.  It will write to a new database called 'stress' *(This is configurable at the CLI)*.

For pulling this in, inside of grafana, you need to change the database name in the database source page, to read 'stress'.  This should immediately turn on the data in the panels for viewing.

The stress program writes multiple tags under a single measurement called 'ctr'.  Even though these are separate tags, the architecture appears to stitches them back together for viewers like grafana.  This splitting into different 'series' is something that can be controlled at the CLI for influx-stress, so you are able to see the performance difference between 1 series *(what most people use for a measurement)* and some other larger value *(100,000 in the case of 2M samples per second)*.

# Installing on arm64 devices, pull the program by running:
<code>git clone https://go.googlesource.com/go goroot</code>

go into the src folder and run:
<code>./influx-stress insert -r 1m --pps 1000000</code>

where 1m is the duration of 1 minute, can be adjusted to secounds, hours, days as well
&
pps sets the points per second to test

# Installing on x86 devices
install go via:
https://golang.org/doc/install

then run:
<code>go get -v github.com/influxdata/influx-stress/cmd/...</code>
