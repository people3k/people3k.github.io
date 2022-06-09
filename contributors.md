---
title: Data contributors
feature_image: "/assets/temple.jpg"
excerpt: "p3k14c contributors"
aside: false
---

p3k14c is an ensemble of a great many source datasets contributed to by an even
greater number of archaeologists.

A full list of BiBTeX citations for each data source is [available here](/data/p3k14c_refs.bib).

<h2>Data contributors</h2>

{% if site.contributors %}
<ul>
    {% assign names = site.contributors | sort %}
    {% for name in names %}
        <li>{{ name }}</li>
    {% endfor %}
</ul>
{% endif %}
