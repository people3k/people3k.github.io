---
title: Code sheet
feature_image:
excerpt: "Explanation of variables for p3k14c"
aside: false
---

# Code sheet

Below is an explanation for each variable/column in p3k14c.

† indicates variables which have been collected directly from source datasets
without any consolidation, cleaning, or verification. Use with discretion.

| **Column**     | **Type**      | **Description**                                                  |
|----------------|---------------|------------------------------------------------------------------|
|**LabID**       | String        | Lab identification code, unique to every date |
|**Age**         | Integer       | Radiocarbon age in [years before present (BP)](https://en.wikipedia.org/wiki/Before_Present) |
|**Error**       | Integer       | One sigma standard error of the radiocarbon age |
|**Material**†   | String        | Dated material |
|**Taxa**†       | String        | Taxonomic name for dated material |
|**d13C**†       | Float         | [δ<sup>13</sup>C](https://en.wikipedia.org/wiki/%CE%9413C) istopic signature. Note that some datasets use "0" instead of NA or a blank cell |
|**Method**†     | String        | The method of radiocarbon dating used, such as AMS or radiometric|
|**Long**        | Float         | Longitude in decimal degrees |
|**Lat**         | Float         | Latitude in decimal degrees |
|**LocAccuracy** | Integer       | A general rating of the accuracy of a given date's location, according to dataset authors and our own verification. Ranges from 0 (lowest accuracy) to 3 (highest accuracy): <br> 0: No specific locational information / only date's Country provided <br> 1: Province/State (non-US) or county (US) locational information <br> 2: Very close locational information (within 500m) <br> 3: Exact location of site provided / data's source collected personally |
|**Period**†     | String          | Archaeological time period. Common in European datasets, generally uncommon elsewhere |
|**SiteID**†     | String        | Site identification number. Very useful for US and Canadian sites, otherwise uncommon |
|**SiteName**†   | String        | Site name, usually unique to each site within each country. Common in sites outside of North America |
|**Country**     | String        | The country in which the date was found |
|**Province**    | String        | The administrative subdivision in which the date was found |
|**Continent**   | String        | The continent on which the date was found |
|**Source**      | String        | The source dataset which provided the date |
|**Reference**†  | String        | Full academic reference for the date, if available |


<style>
body {
}

table {
    width: 100%;
}

th {
    padding: 12px;
    color: white;
    background-color: #EF4E22;
}

td {
    font-size: 13pt;
    padding: 12px;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}
</style>
