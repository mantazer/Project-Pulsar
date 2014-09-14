Project Pulsar
==============

Power distributors have a tough time gauging which households in an area have power during major outages. This costs millions of dollars for them to physically visit each area, potentially wasting vital resources, such as time and tax payer dollars. Although smart meters have been presented as the solution to these problems, they are expensive and sparse across the nation.

Project Pulsar is a much more affordable and robust option for electrical distributors. It is a wireless sensor network of beacons that communicate to a central gateway node hosted in the cloud. Distributors simply install a beacon in the customer's household and they're all set.

Our backend servers keep track of the status of every beacon connected to the overall system in order to determine where power may potentially be out. By taking in data from multiple beacons, residents, and Internet Service Providers (among other inputs), we are able to notify electrical distributors with relative confidence when certain areas are lacking power.

This is just the first iteration of what we hope will become a useful product for millions of households. By combining inexpensive, widely available hardware with a powerful backend, we are able to provide a unique solution to a very real and pressing issue.

Created at PennApps X by Muntaser Ahmed and Gautam Kanumuru.
Demo: http://youtu.be/39Q1j3Qh_a4

#Setup
1. On the beacon, execute `python transmit.py` (found in /pulsar-beacon/src/)
2. Fill out the on-screen information.

We used an Intel Edison as our beacon.

![alt tag](http://i.imgur.com/e2IbAvj.gif)

Note: The two steps above are the only steps the distributor has to complete in order to successfully install a beacon in a customer's house.

The following steps describe running the gateway node and ISP server software.

1. On the gateway node server, execute `python server.py` (found in /pulsar-backend/src/)
2. On the ISP server, execute `python TwilioServer.py` (found in /isp-api/)
