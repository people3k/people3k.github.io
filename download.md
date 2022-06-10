---
title: Download
feature_image: "/assets/wallofchina.jpg"
excerpt: "Download the People 3000 Radiocarbon Database"
aside: false
---

<div style="text-align:center;">
{% include button.html text="Download version 2022.06 (latest)" 
link="/data/p3k14c_2022.01.csv" color="#EF4E22" %} <br />
<a href="#version-downloads" style="font-size: 11pt; text-decoration: underline;">
    Download an older version
</a>
</div>

**Note!** To maintain legal compliance, dates for the United States, Canada, and
the Guedes and Bocinsky (2018) database have had their precise coordinates 
obfuscated to instead be the centroid of the encompassing county/administrative
subdivision. In general, this does not affect results for coarse-grained analysis.
If your analysis requires greater precision, archaeological professionals 
may [request access to the true-coordinates dataset](https://core.tdar.org/dataset/459172/p3k14c-scrubbed) through the Digital Archaeological Record (tDAR).

# Usage

Full details on each column/variable can be found in the 
[code sheet](/codesheet/). All dates are uncalibrated. Consider working with the
data using [our R package](https://github.com/people3k/p3k14c)! For more
detailed information about the data's purpose, intended usage, our methods, and
technical validation, check out [the whitepaper](https://www.nature.com/articles/s41597-022-01118-7).

# Version downloads

| **Version** | **Date** | **Notes** |
|-------------|----------|-------------------|
| [p3k14c 2022.06](/data/p3k14c_2022.06.csv) | 10 June 2022 (latest) | [Release notes](/release-notes/2022/06/10/release-notes/) |
| [p3k14c 2022.01](/data/p3k14c_2022.01.csv) | 27 January 2022 | Initial version |

<br />

<style>
table {
    width: 100%;
}

th {
    padding: 12px;
    color: white;
    background-color: #EF4E22;
}

td {
    padding: 12px;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}
</style>
