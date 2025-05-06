from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from lxml import etree
from jsonschema import validate as json_validate, ValidationError
import httpx
import json

app = FastAPI(title="PBCore Validation and Conversion API")

# Placeholder paths
XSD_PATH = "schemas/pbcore-2.1.xsd"
XSL_PATH = "stylesheets/pbcore-xml-to-json.xsl"
JSON_SCHEMA_PATH = "schemas/pbcore-schema.json"

@app.post("/validate/xml-file", tags=["XML Validation"])
async def validate_xml(file: UploadFile = File(...)):
    try:
        xml_doc = etree.parse(file.file)
        xmlschema_doc = etree.parse(XSD_PATH)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        xmlschema.assertValid(xml_doc)
        return {
            "valid": True,
            "file": file.filename
        }
    except etree.DocumentInvalid as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/validate/xml-url", tags=["XML Validation"])
async def validate_xml_from_url(url: str = Query(..., description="URL pointing to a PBCore XML document")):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            response.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching URL: {str(e)}")

    try:
        xml_doc = etree.fromstring(response.content)
        with open(XSD_PATH, "rb") as xsd_file:
            schema_root = etree.parse(xsd_file)
            schema = etree.XMLSchema(schema_root)
            schema.assertValid(xml_doc)
    except etree.XMLSchemaError as e:
        raise HTTPException(status_code=422, detail=f"XML Validation Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"XML Parsing Error: {str(e)}")

    return {
        "valid": True,
        "url": url,
    }



@app.post("/validate/json-file", tags=["JSON Validation"])
async def validate_json(file: UploadFile = File(...)):
    try:
        instance = json.load(file.file)
        with open(JSON_SCHEMA_PATH) as schema_file:
            schema = json.load(schema_file)
        json_validate(instance=instance, schema=schema)
        return {
            "valid": True,
            "file": file.filename
        }
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)


@app.post("/validate/json-url", tags=["JSON Validation"])
async def validate_xml_from_url(url: str = Query(..., description="URL pointing to a PBCore JSON document")):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            response.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching URL: {str(e)}")

    try:
        instance = json.load(file.file)
        with open(JSON_SCHEMA_PATH) as schema_file:
            schema = json.load(schema_file)
        json_validate(instance=instance, schema=schema)
        return {
            "valid": True,
            "url": url,
        }
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)

    return {
        "valid": True,
        "url": url,
    }


@app.post("/convert/xml-to-json-file", tags=["Conversion"])
async def convert_xml_to_json(file: UploadFile = File(...)):
    try:
        xml_doc = etree.parse(file.file)
        xslt_doc = etree.parse(XSL_PATH)
        transform = etree.XSLT(xslt_doc)
        json_str = str(transform(xml_doc))
        return json.loads(json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/convert/xml-to-json-url", tags=["Conversion"])
async def convert_xml_to_json(url: str = Query(..., description="URL pointing to a PBCore XML document")):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            response.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching URL: {str(e)}")

    try:
        xml_doc = etree.fromstring(response.content)
        xslt_doc = etree.parse(XSL_PATH)
        transform = etree.XSLT(xslt_doc)
        json_str = str(transform(xml_doc))
        return json.loads(json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/convert/json-to-xml", tags=["PBCore Conversion"])
async def convert_json_to_xml(file: UploadFile = File(...)):
    try:
        # TODO: Implement either via XSLT or custom mapping logic
        return {"message": "Conversion not yet implemented"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/convert/roundtrip/xml-json/file", tags=["PBCore Conversion"])
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