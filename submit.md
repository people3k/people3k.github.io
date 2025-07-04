---
title: Submit data
feature_image: "/assets/excavation.jpg"
excerpt: "Submit data to be included in p3k14c"
aside: False
---

# Submit data to p3k14c
p3k14c has been made possible through the generous sharing of data from archaeologists
across the world. If you have or know of radiocarbon dates that aren't in p3k14c, we 
want to add them! Submitting data bolsters its dissemination,
fills in geographical gaps, and contributes to the future of how we understand 
ourselves and our ancestors.

## Submission instructions

Before handing off data to us, we ask that you format it in a few ways so 
as to make the process of integrating it into p3k14c as smooth as possible:

1. **Remove all non-archaeological radiocarbon dates**. 
2. **Format the data using the p3k14c column schema.** We provide a [starting 
header](/data/p3k14c_starting-header.csv) to assist with this. At a minimum, data is required in the
_LabID, Age, Error, LocAccuracy,_ and _Continent_ columns. 
Refer to the [codebook](/codebook) for descriptions of each column. 
3. **Include a "LocAccuracy" for each date**. LocAccuracy is a general rating
of the accuracy of a given date's location. It ranges from 0 (lowest accuracy) 
to 3 (highest accuracy) according to the following scale: <br>
    0: No specific locational information other than encompassing Country<br>
    1: Province/State (non-US) or county (US) locational information<br>
    2: Very close locational information (within 500m)<br>
    3: Exact location of site provided <br>
    So, for example, if you collected a date personally and know that its 
    coordinates are the exact location, you should assign a _LocAccuracy_ of 3
    to that date. If you have a date with no particular coordinates, but you 
    know what country it was found in, you should assign a _LocAccuracy_ of 0, 
    and so on.
4. **Ensure all latitude/longitude coordinates are only in decimal format.**
    Ensure that you use decimal PERIOD rather than decimal comma.
    If you need assistance with this step, let us know in your submission form.
5. **Include Continent and (if possible) Country and Province information for each date**. 
    To assist with this step, we provide a [spreadsheet](/data/p3k14c_province-country-info.xlsx)
    indicating which countries given provinces belong to and which continents given countries belong to. 



<div style="text-align:center;">
Ready to submit? <br><br>
{% include button.html text="Submit data now" link="https://forms.gle/HCSxx5Pxmn2jPaYa6" color="#F78A2B" %} </div>



### Questions?
If you have any questions, feel free to email the p3k14c data stewardship team
at [p3k14c@gmail.com](mailto:p3k14c@gmail.com). We'll get back to you as 
soon as we can!



