## Script to generate CrossRef XML for BMVC proceedings to be used for DOI registration.
##
## Neill Campbell, UCL, June 2025

import json
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
from pyrsistent import b
import xmlschema
from pprint import pprint
import os


def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, "utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def create_crossref_xml(
    publications,
    output_file,
    year,
    isbn,
    email_address,
    url_from_year_and_paper_id_func,
    location,
    chairs=None,
):
    # This is the correct format for the base DOI
    publication_doi = f"10.5244/C.{year - 2020 + 34}"
    base_doi = f"10.5244/C.{year - 2020 + 34}.%d"

    # Namespaces
    ns = {
        "xmlns": "http://www.crossref.org/schema/5.3.1",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }

    ET.register_namespace("", ns["xmlns"])
    ET.register_namespace("xsi", ns["xsi"])

    # Root element
    doi_batch = ET.Element(
        "doi_batch",
        {
            "version": "5.3.1",
            "xmlns": "http://www.crossref.org/schema/5.3.1",
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )

    # Head
    head = ET.SubElement(doi_batch, "head")
    ET.SubElement(head, "doi_batch_id").text = f"batch_{year}"
    ET.SubElement(head, "timestamp").text = datetime.utcnow().strftime("%Y%m%d%H%M")

    depositor = ET.SubElement(head, "depositor")
    ET.SubElement(depositor, "depositor_name").text = (
        "British Machine Vision Association"
    )
    ET.SubElement(depositor, "email_address").text = email_address

    ET.SubElement(head, "registrant").text = "British Machine Vision Association"

    # Body
    body = ET.SubElement(doi_batch, "body")
    conference = ET.SubElement(body, "conference")

    contributors = ET.SubElement(conference, "contributors")
    if chairs:
        for i, chair in enumerate(chairs):
            person = ET.SubElement(
                contributors,
                "person_name",
                {
                    "contributor_role": "chair",
                    "sequence": "first" if i == 0 else "additional",
                },
            )
            if isinstance(chair, list):
                ET.SubElement(person, "given_name").text = " ".join(chair[:-1])
                ET.SubElement(person, "surname").text = chair[-1]
            else:
                names = chair.split()
                ET.SubElement(person, "given_name").text = " ".join(names[:-1])
                ET.SubElement(person, "surname").text = names[-1]

    # Conference metadata
    event_metadata = ET.SubElement(conference, "event_metadata")
    ET.SubElement(event_metadata, "conference_name").text = (
        f"British Machine Vision Conference {year}"
    )
    ET.SubElement(event_metadata, "conference_theme").text = (
        "Machine Vision, Image Processing & Pattern Recognition"
    )
    ET.SubElement(event_metadata, "conference_acronym").text = f"BMVC {year}"
    ET.SubElement(event_metadata, "conference_sponsor").text = (
        "British Machine Vision Association"
    )
    ET.SubElement(event_metadata, "conference_number").text = str(year)

    ET.SubElement(event_metadata, "conference_location").text = f"{location}"

    proceedings_metadata = ET.SubElement(conference, "proceedings_metadata")
    ET.SubElement(proceedings_metadata, "proceedings_title").text = (
        f"Proceedings of the British Machine Vision Conference {year}"
    )
    ET.SubElement(proceedings_metadata, "proceedings_subject").text = (
        f"Machine Vision, Image Processing & Pattern Recognition"
    )

    publisher = ET.SubElement(proceedings_metadata, "publisher")
    ET.SubElement(publisher, "publisher_name").text = (
        "British Machine Vision Association"
    )

    publication_date = ET.SubElement(proceedings_metadata, "publication_date")
    ET.SubElement(publication_date, "year").text = str(year)

    ET.SubElement(proceedings_metadata, "isbn", {"media_type": "electronic"}).text = (
        isbn
    )
    doi_data = ET.SubElement(proceedings_metadata, "doi_data")
    ET.SubElement(doi_data, "doi").text = publication_doi
    ET.SubElement(doi_data, "resource").text = f"https://bmva.org/bmvc/{year}/"

    for i, pub in enumerate(publications):
        paper = ET.SubElement(
            conference, "conference_paper", {"publication_type": "full_text"}
        )

        contributors = ET.SubElement(paper, "contributors")
        for j, author in enumerate(pub["authors"]):
            person = ET.SubElement(
                contributors,
                "person_name",
                {
                    "contributor_role": "author",
                    "sequence": "first" if j == 0 else "additional",
                },
            )
            assert (
                not "(" in author or ")" in author
            ), f"Author names should not contain parentheses: {author}."
            names = author.split()
            ET.SubElement(person, "given_name").text = " ".join(names[:-1])
            ET.SubElement(person, "surname").text = names[-1]

        titles = ET.SubElement(paper, "titles")
        ET.SubElement(titles, "title").text = pub["title"]

        pub_date = ET.SubElement(paper, "publication_date", {"media_type": "online"})
        ET.SubElement(pub_date, "year").text = str(year)

        publisher_item = ET.SubElement(paper, "publisher_item")
        ET.SubElement(
            publisher_item, "item_number", {"item_number_type": "article_number"}
        ).text = str(pub["paper_number"])

        doi_data = ET.SubElement(paper, "doi_data")
        ET.SubElement(doi_data, "doi").text = base_doi % pub["paper_number"]
        ET.SubElement(doi_data, "resource").text = url_from_year_and_paper_id_func(
            year, pub["paper_id"]
        )

    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(prettify_xml(doi_batch))


def generate_crossref_xml_file_and_forwarding_links(
    year,
    chairs,
    input_json_file,
    isbn,
    email_address,
):
    MAKE_PAPER_PAGE_LINKS = True
    PAPER_PAGE_LINKS_LOCAL_FOLDER = f"./bmvc/{year}"

    OUTPUT_FILE = f"crossref_output_{year}.xml"
    VALIDATION_SCHEMA = "https://data.crossref.org/schemas/crossref5.3.1.xsd"

    ## There is some dodgy stuff in the 2020 and 2021 JSON files as the fomatting is
    ## strange (not my choice!) so we need to do some cleaning up..

    with open(input_json_file, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    data = [d["content"] for d in raw_data if "content" in d]

    for d in data:
        d["paper_id"] = re.search(r"/(\d{4})\.(pdf|zip)", d["link"][0]).group(1)

    data = sorted(data, key=lambda x: int(x["paper_id"]))

    def has_bad_authors(author_list):
        # Check if any author has parentheses in their name
        return any("(" in author or ")" in author for author in author_list)

    bad_authors = [
        (i, d["authors"]) for i, d in enumerate(data) if has_bad_authors(d["authors"])
    ]
    if len(bad_authors) > 0:
        print(f"{bad_authors=}")
        for i, a in bad_authors:
            print(i)
            print(a)
        assert False, "BAD AUTHORS DETECTED! Please fix the author names."

    for i, d in enumerate(data):
        d["paper_number"] = i + 1

    if MAKE_PAPER_PAGE_LINKS and not os.path.exists(PAPER_PAGE_LINKS_LOCAL_FOLDER):
        os.makedirs(PAPER_PAGE_LINKS_LOCAL_FOLDER, exist_ok=True)

    def url_from_year_and_paper_id_func(year, paper_id):
        paper_sublink = f"conference/papers/paper_{int(paper_id):04d}.html"

        paper_link = f"https://www.bmva.org/bmvc/{year}/{paper_sublink}"

        if MAKE_PAPER_PAGE_LINKS:
            local_filename = f"{PAPER_PAGE_LINKS_LOCAL_FOLDER}/{paper_sublink}"
            # Make directory..
            os.makedirs(os.path.dirname(local_filename), exist_ok=True)
            with open(local_filename, "w") as fp:
                fp.write(
                    f'<script>location.href = "https://www.bmva-archive.org.uk/bmvc/{year}/{paper_sublink}"</script>'
                )
            print(f'Written: "{local_filename}"..')

        return paper_link

    create_crossref_xml(
        data,
        OUTPUT_FILE,
        year=year,
        isbn=isbn,
        email_address=email_address,
        location="Online",
        chairs=chairs,
        url_from_year_and_paper_id_func=url_from_year_and_paper_id_func,
    )

    # Validation!

    xs = xmlschema.XMLSchema(VALIDATION_SCHEMA)
    pprint(xs.to_dict(OUTPUT_FILE))


if __name__ == "__main__":
    YEAR = 2020
    CHAIRS = [
        "Neill Campbell",
        ["Oisin", "Mac Aodha"],
        "William Smith",
        "Lourdes Agapito",
        "Martin Fergie",
        "Moi Hoon Yap",
    ]
    INPUT_JSON_FILE = "papers_2020.json"
    ISBN = "978-1-901725-67-4"
    EMAIL_ADDRESS = "neill.campbell@ucl.ac.uk"

    generate_crossref_xml_file_and_forwarding_links(
        year=YEAR,
        chairs=CHAIRS,
        input_json_file=INPUT_JSON_FILE,
        isbn=ISBN,
        email_address=EMAIL_ADDRESS,
    )

    YEAR = 2021
    CHAIRS = [
        "Neill Campbell",
        "Yi-Zhe Song",
        "Karteek Alahari",
        "Stefan Leutenegger",
        "Laura Sevilla",
        "Stuart James",
        "Tu Bui",
    ]
    INPUT_JSON_FILE = "papers_2021.json"
    ISBN = "978-1-901725-68-1"
    EMAIL_ADDRESS = "neill.campbell@ucl.ac.uk"

    generate_crossref_xml_file_and_forwarding_links(
        year=YEAR,
        chairs=CHAIRS,
        input_json_file=INPUT_JSON_FILE,
        isbn=ISBN,
        email_address=EMAIL_ADDRESS,
    )
