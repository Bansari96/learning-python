# Example for parsing and processing XML 

import xml.dom.minidom
from xml.etree import ElementTree

def main():

    tree=ElementTree.parse("samplexml.xml")
    doc=xml.dom.minidom.parse("samplexml.xml")

    print(doc.nodeName)
    root=tree.getroot()
    print("Name: " + root.find("firstname").text)

    skills=doc.getElementsByTagName("skill")
    print("Total skills: %d" %skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))
    print("------------\n")

    newSkill=doc.createElement("skill")
    newSkill.setAttribute("name","python")
    doc.firstChild.appendChild(newSkill)
    skills=doc.getElementsByTagName("skill")
    print("After new Skill added")
    print("Total skills: %d" %skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))


if __name__ == "__main__":
    main()