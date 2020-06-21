from lxml import objectify,etree
import datetime
import pytz

class xmlutils():
    def __init__(self):
        pass

    def create_xml(self):
        root = etree.Element("EventLog")
        root.set("xmlns", "http://aarthi.com/LogDump")
        etree.SubElement(root, "timestamp").text = "2020-06-19T15:50:19.686Z"
        etree.SubElement(root, "typeofevent").text = "Servicing"
        etree.SubElement(root, "level").text = "Information"
        etree.SubElement(root, "source").text = "LoadPerf"

        value = self.nested_xml({
            "mlabel" : "tst.stuff.can",
            "deviceName" : "PC1",
            "workstation" : "Aarthi_PC"
        })

        root.append(value)
        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True)
        print(obj_xml)
        return obj_xml

    def nested_xml(self, data):
        testurl = objectify.Element("testurl")
        testurl.mlabel = data["mlabel"]
        testurl.deviceName = data["deviceName"]
        testurl.workstation = data["workstation"]
        return testurl


    def deserialize_string_to_obj(self):
        payload = self.create_xml()
        tag = objectify.XML(payload)
        print(tag.timestamp)
        tag.timestamp = datetime.datetime.now(pytz.utc).isoformat()
        print(tag.timestamp)

        obj_xml = etree.tostring(tag)
        print(obj_xml)
        return obj_xml


x = xmlutils()
#x.create_xml()
x.deserialize_string_to_obj()
