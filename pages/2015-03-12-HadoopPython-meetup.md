title: DC Python Meetup - Hadoop with Python
date: 2015-03-12
categories: [meetup, python]
tags: [data]
description: The March DC Python meetup with Donald Miner at iStrategyLabs

The following are my notes from the March DC Python meetup on Hadoop, given by Donald P. Miner (@donaldpminer). They might be incomplete. 

##What is Hadoop

This technology derives from Google and reimagines data storage. 
It mostly lives as a Hadoop Distributed File System (HDFS) which: 

* Stores files in folders
* Chunks large files into blocks
* Duplicates the block three times
* Scatters the blocks all over the place

Can only create, read, and delete. If you want to edit you can use
something like HBase to run on top on Hadoop such as Acumulo, created by the NSA. The core piece of Hadoop that helps organize the data is MapReduce.

##MapReduce

Analyzes raw data in HDFS. Jobs are split into Mappers and
Reducers. There are a lot of pieces that 'fall out' from mapping and
reducing. Donald Miner was able to write a book just on the different
things that can be done just with mapping and reducing. [See MapReduce
design patterns.][1]

###Mappers

The key items of Mappers:

* Loads data form HDFS
* Filter, transform, parse
* Outputs (key, value) pairs

###Reducers

The key pieces of Reducers:

* Automatically groups by the mapper's output key
* Aggregate, count, statistics
* Outputs to HDFS

MapReduce solves batching problems but is not a panacea. Other problems, such as
streaming data, are not appropriate for MapReduce.

Miner's personal workflow is to process in Hadoop and output to CSV or JSON.

##Hadoop Ecosystem

Hadoop lives within an ecosystem of other projects:

* Higher level languages like Pig and Hive
* HDFS data systems like HBase and Accumulo
* Alternative executiion engines like Storm and Spark
* Close friends like ZooKeeper, Flume, Avro, Kafka


###The one thing I don't like about Hadoop is Java
But Hadoop with Python is a bit half-baked.


##Cool things
Data Locality - the idea of processing data where it is instead of
moving it over the network
* Linear Scalability
  * HDFS and MapReduce scale linearly
* Schema on Read (opposed to schema on write)
  * You load the data first, before you know what you're going to do
    with it. And then the nature of the data, whether it's JSON and what data types there are done later. 
  * You don't have to get rid of the original data!
Example: image analysis. You can have a mapper analyze the metadata
(e.g. who took it) and another to analyze the image. You can even store
it first and then do something with it later.
* Transparent Parallelism
  * You don't have to care about a lot of traditional worries like
    scalability, locking,  and threading?
* Unstructed Data
  * MapReduce is just Java

*I can give a devleoper who knows nothing about HDFS a job to run (and
they have no appreciation of what they're doing.)*

##Python
**I've had long discussions with Java developers and I think it comes
down to a personality preference about why Python over Java.**
Compiled vs. Scripting
With Java I have to compile. I compile to a JAR file, copy that to the
cluster, realize there's a problem, and then come back. 

With scripting (python) it's fairly easy to edit-in-place.

* Python vs. Java
* Compiled vs. scripts
* Python libraries we all love
  * World-class libraries for data analysis, etc.
* Integration with other things

**Why Not Python?**

* You might be on your own in some cases with downloading, installing

* Smaller community, almost no official support

##Survey of Python Hadoop things
**MrJob**
Wrape Hadoop streaming that wraps the MapReduce processes (used and
maintained by Yelp). Well-documented and can run locally in Amazon
Elastic MapReduce (EMR),
or Hadoop.

**Pydoop**
You can write MapReduce jobs in Python. Uses C++ Pipes which should be
faster than wrapping streaming.

See Clouderas blogpost guide to python frameworks for Hadoop

**Pig**
Does data flow transformation. A higher level platform and language for
analyzing data that happens to run MapReduce underneath.
Book: Agile Data Science - not terribly useful but fun to read

**Snakebite**
Big missing part: cannot write data.

(See Luigi from Spotify, see the Spotify open source projects)

**HBase**
Not really there yet and has failed to gain community momentum. Java is
still King.

##The Future
**Spark**
Spark generally is a lot faster and easier to write than MapReduce. It provides a high-level API in Scala, Java, and Python that
makes parallel jobs easy to write. **PySpark** 
Some folks say that Spark is better than MapReduce
RDDs = Resilient Distributed Datasets
RDDs are kept in memory for the most part.
Spark does the computations in memory as opposed to MapReduce. But if
your dataset gets too large it writes to disk. Get get comfortable with
lambdas.

##Update, see the video of the talk below

<iframe width="560" height="315" src="https://www.youtube.com/embed/g99U7c4jSNs" frameborder="0" allowfullscreen></iframe>

[1]: http://shop.oreilly.com/product/0636920025122.do

