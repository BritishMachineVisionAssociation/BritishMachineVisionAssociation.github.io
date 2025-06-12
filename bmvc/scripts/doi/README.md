---
title: BMVA DOI Scripts and Workflow!
author: Neill Campbell (UCL)
date: 2025-06-12
---

**Goal**: To generate a CrossRef XML file for BMVC conference papers and upload it to CrossRef to sort DOIs.

# Script:

The "bmvc_doi_xml_generator_script.py" script is designed to generate a CrossRef XML file for BMVC conference papers. It reads a JSON file containing paper metadata and outputs an XML file formatted for CrossRef submission. At the moment there is some fixing of the JSON format as it is the format dictated by the visualiser code on the BMVC 2020 and 2021 virtual conferences. It should be very easy to adapt the script to work with the YAML files that are normally used for the new format of the BMVC website. I should add some documentation about this.

## ISBN: 

The ISBN values should be set in consultation with the ISBN spread sheet which is on the BMVA google drive - working down from the entries for 2020 and 2021 - please update the file when an ISBN is used. We should be using the 13-digit codes now!

# Uploading:

- Go to the CrossRef upload tool: https://doi.crossref.org/servlet/useragent

- Log in with your credentials.

- Select "Submissions" from the top menu and then the "Upload" option.

- Use the "Choose File" button to select the XML file you want to upload.

- Leave Type as "Metadata".

- Click the "Upload" button to submit your file.

- An email should be sent to the depositor email address with the status of the upload (with lots of "SUCCESS" messages or something went wrong).

# HTML Forwarding Files (to be added to the BMVA website):

- At the moment there are forwarding files for BMVC 2020 and 2021 - these are HTML files in the "bmvc" supfolder that need to be added to the BMVA website and will forward to the appropriate place on the archive website. This is in case we need to move the archive website, the DOI links will still be held on the BMVA github site and can be updated to forward to somewhere else if needed. 
