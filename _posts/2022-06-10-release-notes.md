---
title: "Release notes: p3k14c version 2022.06"
categories:
- release-notes
feature_image: "/assets/neakpointemple.jpg"
excerpt: "Changes include standardized LabIDs, a fix for duplicate dates, and the introduction of p3k14c.org!"
---

Announcing the first official update release of p3k14c: Version 2022.06! 
[Download the data here](/download/), or access it via [the offical R package](https://github.com/people3k/p3k14c).

# Bugfixes

* All LabIDs are now standardized to ABC-1234 format prior to the cleaning procedure. This fixed an issue causing duplicate dates when a given date appeared multiple times with slight capitalization and separator variations in its LabID (e.g. MC-555, Mc555, Mc-555)
* 36 dates with malformed LabIDs placing the numerals before the letters, primarily from the ManningTimpson2014 dataset, have been temporarily removed while we investigate finding their true lab identifiers. 

# Additions

* Introduced [p3k14c.org](p3k14c.org) as a hub to download, submit new data to, see reference info, and get the latest news for p3k14c!
