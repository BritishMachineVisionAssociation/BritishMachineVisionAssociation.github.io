---
layout: default_sparse
title: Thesis Archive
---

<!--
  pdf-link: "theses/2004/2004-monadjemi.pdf"
- title: "Automatic Detection of Facial Features in Grey Scale Images"
  author: "David Cristinacce"
  institution: "University of Manchester"
  date: 2004-10-01
  pdf-link: "theses/2004/2004-cristinacce.pdf"


-->

## Thesis Archive

<div class="row mx-auto">
	<div class="col mx-auto">
		<p align="center" class="pt-3"><a class="btn btn-info" role="button" href="#thesis-submission">Please find submission details below!</a></p>
	</div>
</div>

The BMVA keeps an archive of PhD theses written by students at UK institutions. These are organised chronologically:

<table style="width:100%;" class="table">
<colgroup>
<col width="5%" />
<col width="15%" />
<col width="15%" />
<col width="65%" />
</colgroup>
<thead class="thead-dark">
<tr class="header sticky-top" style="top: 56px;">
<th align="left">Year</th>
<th align="left">Author</th>
<th align="left">Institution</th>
<th align="left">Title</th>
</tr>
</thead>
<tbody>
{% assign sorted_theses = site.data.theses | sort: "date" | reverse %}
{% for thesis in sorted_theses %}
<!--<p>{{ thesis }}</p>-->
<tr>
<td align="left">{{ thesis.date | date: "%Y" }}</td>
<td align="left">{{ thesis.author }}</td>
<td align="left">{{ thesis.institution }}</td>
<td align="left"><a href="{{ site.archive_url }}/{{ thesis.pdf-link }}">{{ thesis.title }}</a></td>
</tr>
{% endfor %}
</tbody>
</table>
<hr />

### Thesis Submission

To submit a thesis to the archive, please contact the [BMVA Chair](mailto:chair@bmva.org) with:

- your name
- the title of the thesis
- the awarding institution
- the month and year of the viva
- a DOI reference, if your thesis has one
- your supervisor's name and email address
- the thesis abstract as plain text
- a URL from which the thesis can be downloaded; it *must* be in PDF format

The thesis archive is also able to hold a reasonable amount of supplementary data, such as software and test data, with a thesis. If you would like to do this, please indicate so in your email.

By submitting your thesis, you are confirming that you hold the copyright of your work and are granting the BMVA a non-exclusive licence to distribute it.





