# COVID19.si

COVID19 data for Slovenia

Idea is to colect data in CSV format, togehter with few scripts to agregate it. 

## Why?

CSV is easily ingested by most tools to create predictions, graphs, etc ...

## Structure

`/data` directory contains raw data automatically imported from Google sheet below

## Use data

```
let dataPromise = d3.csv("https://raw.githubusercontent.com/overlordtm/COVID19.si/master/data/full.csv")
  dataPromise.then(data => {
    console.log(data)
  })
```

## Webpage

Static page.

Uses yarn (packet manager) webpack (bundler), handlebars (templates), bootstrap (style).

Everything is static, datasource are CSV files in master branch of this repo. Published on github pages.

```
yarn install # install dependencies
yarn build # build into dist
yarn dev # run devserver and open browser
yarn gh # publish to gh-pages branch
```


## Source of data
Most of the data provided by [Luka Renko](https://twitter.com/LukaRenko)

He manitains Google Sheet where he collects data https://tinyurl.com/slo-covid-19
