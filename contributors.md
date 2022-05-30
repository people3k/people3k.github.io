---
title: The P3k14C Team
excerpt: "P3k14C contributors"
aside: false
---

<html>
{% if site.team_members %}
<table>
{% for item in site.team_members %}
    <tr>
        <td>
            <img class="picture" src="{{ item.image }}" alt="{{ item.name }}">
        </td>
        <td>
            <p class="name">{{ item.name }}</p>
            <p class="pronouns">({{ item.pronouns }})</p><br />
            <p class="title">{{ item.title }}</p><br />
            <p class="contact">
                <a href="mailto:{{ item.contact }}">
                    {{ item.contact }}
                </a>
            </p>
        </td>
    </tr>
{% endfor %}
{% endif %}
</table>
</html>


<h2>Data contributors</h2>

{% if site.contributors %}
<ul>
    {% assign names = site.contributors | sort %}
    {% for name in names %}
        <li>{{ name }}</li>
    {% endfor %}
</ul>
{% endif %}

<style>

/* Display the columns below each other instead of side by side on small screens */
@media screen and (max-width: 650px) {
    .name {
        font-size: 12pt !important;
    }
    .picture {
        width: 80% !important;
    }
}

.name, .title, .contact, .pronouns {
    display: inline;
}

.pronouns {
    color: grey;
}

.title {
  color: #F78A2B;
  font-weight: bold;
}

.name {
    font-size: 15pt;
    font-weight: bold;
}

.picture {
    width: 250px;
    float: left;
}

td {
    padding-bottom: 16px !important;
    padding-left: 16px !important;
}


</style>
