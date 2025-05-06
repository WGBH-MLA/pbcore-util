from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from lxml import etree
import jsonschema
import json

app = FastAPI(title="PBCore Validation and Conversion Service")

# Placeholder paths
XSD_PATH = "schemas/pbcore-2.1.xsd"
XSL_PATH = "stylesheets/pbcore-to-json.xsl"
JSON_SCHEMA_PATH = "schemas/pbcore-schema.json"

@app.post("/validate/xml")
async def validate_xml(file: UploadFile = File(...)):
    try:
        xml_doc = etree.parse(file.file)
        xmlschema_doc = etree.parse(XSD_PATH)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        xmlschema.assertValid(xml_doc)
        return {"valid": True}
    except etree.DocumentInvalid as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/convert/xml-to-json")
async def convert_xml_to_json(file: UploadFile = File(...)):
    try:
        xml_doc = etree.parse(file.file)
        xslt_doc = etree.parse(XSL_PATH)
        transform = etree.XSLT(xslt_doc)
        json_str = str(transform(xml_doc))
        return JSONResponse(content=json.loads(json_str))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/validate/json")
async def validate_json(file: UploadFile = File(...)):
    try:
        instance = json.load(file.file)
        with open(JSON_SCHEMA_PATH) as schema_file:
            schema = json.load(schema_file)
        jsonschema.validate(instance=instance, schema=schema)
        return {"valid": True}
    except jsonschema.ValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)

@app.post("/convert/json-to-xml")
async def convert_json_to_xml(file: UploadFile = File(...)):
    try:
        # TODO: Implement either via XSLT or custom mapping logic
        return {"message": "Conversion not yet implemented"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/validate/roundtrip")
async def validate_roundtrip(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # Detect format: XML or JSON
        if contents.strip().startswith(b"<"):
            # XML → JSON → XML round trip
            original = etree.fromstring(contents)
            # Convert to JSON (reuse existing function)
            xslt_doc = etree.parse(XSL_PATH)
            transform = etree.XSLT(xslt_doc)
            json_str = str(transform(original))
            json_obj = json.loads(json_str)
            # Convert back to XML (placeholder)
            reconstructed = etree.Element("placeholder")  # TODO
        else:
            json_obj = json.loads(contents)
            # JSON → XML → JSON round trip (placeholder)
            reconstructed = json_obj  # TODO
        return {"roundtrip": "not yet fully implemented"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
