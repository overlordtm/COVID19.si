# COVID19.si

COVID19 data for Slovenia

Idea is to colect data in CSV format, togehter with few scripts to agregate it. 

## Why?

CSV is easily ingested by most tools to create predictions, graphs, etc ...

## Structure

`/cases` directory contains data on individual case. Not up to date, much WIP

`/data` directory contains raw data. Confirmed cases and deaths and recoveries are counted by region like this

```
Province/State,Country/Region,Last Update,Confirmed,Deaths,Recovered
CE,Slovenia,2020-03-04 00:00,0,0,0
GO,Slovenia,2020-03-04 00:00,0,0,0
KK,Slovenia,2020-03-04 00:00,0,0,0
KP,Slovenia,2020-03-04 00:00,0,0,0
KR,Slovenia,2020-03-04 00:00,0,0,0
LJ,Slovenia,2020-03-04 00:00,1,0,0
MB,Slovenia,2020-03-04 00:00,0,0,0
MS,Slovenia,2020-03-04 00:00,0,0,0
NM,Slovenia,2020-03-04 00:00,0,0,0
PO,Slovenia,2020-03-04 00:00,0,0,0
SG,Slovenia,2020-03-04 00:00,0,0,0
```

Most of other data applies to whole Slovenia, so it is contained in single CSV, first column in each row is date (ISO format), followed by different metrics. Eg:

```
Date,Tests
2020-03-04,352
2020-03-05,433
2020-03-06,498
2020-03-07,785
2020-03-08,981
2020-03-09,1227
2020-03-10,1643
2020-03-11,2270
2020-03-12,3058
```

`/timeline` will contain agregated values from data in `/data`. Due to shuffling data around, I have to rewrite scripts to compute aggregates.

## Source of data
Most of the data provided by [Luka Renko](https://twitter.com/LukaRenko)

He manitains Google Sheet where he collects data https://docs.google.com/spreadsheets/d/1N1qLMoWyi3WFGhIpPFzKsFmVE0IwNP3elb_c18t2DwY/edit?pli=1#gid=1419250136


Feel free to make PR to update data
