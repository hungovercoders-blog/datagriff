---
title: "Local Install of Spark on Windows"
date: 2023-04-14

author: dataGriff
---

Want to install python, spark and pyspark for some local data pipeline testing? Look no further... Accompanying this blog there is also this [video on youtube](https://www.youtube.com/watch?v=QYTPpqPYaw0). Multimedia has hit the hungovercoders!!! 

- [Pre-Requisites](#pre-requisites)

## Pre-Requisites

For testing you'll need to have an IDE installed, I tend to use [visual studio code](https://code.visualstudio.com/).

## Python Install

Install python by first downloading it from [here](https://www.python.org/downloads/). Choose the latest version and then the file for your operating system (in this case windows 64-bit).

![Python File Download]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/python_download_file.png)

When you start installing remember to tick "Add Python XXX to PATH" on install to ensure this is set in your environment variables.

![Python Install]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/python_install.png)

Click install now to complete. Check then in your environment variables to confirm python has been added to your PATH.

![Python Environment Variables]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/python_download_file.png)

## Java Install

Go to [java downloads](https://www.java.com/en/download/help/windows_manual_download.html) and  go to download and install.

![Java Download]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/java_download.png)

Choose the manual download page. On this page choose windows offline 64-bit.

![Java Manual Download]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/java_manual_download.png)

Install Java by double clicking the executable once downloaded. Once completed confirm that JAVA has been installed by checking the installation location. Then finally add JAVA_HOME and the path to your user environment variables and add the path to java here. For me the path is on my C drive at C:\Program Files\Java\jre1.8.0_271.

![Java Environment Variable]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/java_environment_variables.png)

## Spark Install

Download spark from [here](https://spark.apache.org/downloads.html).

![Spark Download]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/spark_download.png)

At the top of the download page, choose the suggested site for the tar file download. This will take a little while to download as its quite big.

**Note** the name of the download as it will tell you which version of hadoop winutils you need to install later. In the instance below it is Hadoop 3.

![Spark Suggested Download]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/spark_suggested_download.png)

Once downloaded, unzip the tar file twice...

Copy all of the contents of the unzipped file and paste into a location on your C:\drive called C:\Spark.

![Spark Copied]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/spark_copied.png)

Then add SPARK_HOME to your system environment variables with the value C:\Spark.

![Spark System Variables]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/spark_environment_variable.png)

Finally add a new Path in your system environment variables with the value %SPARK_HOME%\bin.

![Hadoop Path Environment Variable]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/hadoop_path_environment_variable.png)

## Hadoop WinUtils Install

Go to [github hadoop winutil](https://github.com/cdarlint/winutils).

Download the appropriate winutils.exe. You will know which is the correct one based on the version of the taf file you downloaded for spark.

![Hadoop Download]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/hadoop_download.png)

Add a C:\Hadoop\bin folder your machine and add the winutils.exe to this.

![Hadoop Copied]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/hadoop_copied.png)

Then add HADOOP_HOME to your system environment variables with the value C:\Hadoop.

![Hadoop System Variables]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/hadoop_system_variables.png)

Finally add a new Path in your system environment variables with the value %HADOOP_HOME%\bin.

![Hadoop Path Environment Variable]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/hadoop_path_environment_variable.png)

## Confirm Spark

Open a command prompt with admin privileges and run "spark-shell". You should then see the letter SPARK come up as per below. after a little while.

![Spark CMD]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/spark_cmd.png)

You can also navigate to the local host spark UI here [http://localhost:4040/](http://localhost:4040/).

![Spark UI]({{ site.baseurl }}/assets/2023-04-14-local-install-spark/spark_ui.png)

## Pyspark Install

To install pyspark open up visual studio code. Open a terminal and run the following command to create a virtual environment and pip install pyspark. Ensure you use the correct python version that you installed originally in the command.

```bash
py -3.11 -m venv venv 
venv\scripts\activate
pip install pyspark
pyspark
```

In the spark terminal just setup a simple dataframe and display it to confirm functionality.

```bash
data = [('Tiny Rebel','Stay Puft'),('Crafty Devil','Mike Rayer')]
columns = ["brewery","beer"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()
```

The deactivate your environment.

```
```bash
venv\scripts\deactivate
```

You have now successfully setup a local environment whereby you can run python, spark and pyspark locally! Time for a drink...
