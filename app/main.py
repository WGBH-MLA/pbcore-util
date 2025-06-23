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
        pbcore_xml = etree.parse(file.file)
        pbcore_schema = etree.XMLSchema(etree.parse(XSD_PATH))
        pbcore_schema.assertValid(pbcore_xml)
        return {"valid": True, "file": file.filename}
    except etree.DocumentInvalid as e:
        raise HTTPException(
            status_code=422, detail=f"PBCore XML Validation Error: {str(e)}"
        )
    except etree.XMLSyntaxError as e:
        raise HTTPException(status_code=422, detail=f"XML Parsing Error: {str(e)}")


@app.post("/validate/xml-url", tags=["XML Validation"])
async def validate_xml_from_url(
    url: str = Query(..., description="URL pointing to a PBCore XML document")
):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            response.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching URL: {str(e)}")

    try:
        pbcore_xml = etree.fromstring(response.content)
        pbcore_schema = etree.XMLSchema(etree.parse(XSD_PATH))
        pbcore_schema.assertValid(pbcore_xml)
    except etree.XMLSchemaError as e:
        raise HTTPException(status_code=422, detail=f"XML Validation Error: {str(e)}")
    except etree.XMLSyntaxError as e:
        raise HTTPException(status_code=422, detail=f"XML Parsing Error: {str(e)}")

    return {
        "valid": True,
        "url": url,
    }


@app.post("/validate/json-file", tags=["JSON Validation"])
async def validate_json(file: UploadFile = File(...)):
    HTTPException(status_code=400, detail=f"PBCore JSON validation not yet implemented")


@app.post("/validate/json-url", tags=["JSON Validation"])
async def validate_json_from_url(
    url: str = Query(..., description="URL pointing to a PBCore JSON document")
):
    HTTPException(status_code=400, detail=f"PBCore JSON validation not yet implemented")


@app.post("/convert/xml-to-json-file", tags=["Conversion"])
async def convert_xml_to_json(file: UploadFile = File(...)):
    try:
        pbcore_xml = etree.parse(file.file)
        xslt_doc = etree.parse(XSL_PATH)
        transform = etree.XSLT(xslt_doc)
        json_str = str(transform(pbcore_xml))
        return json.loads(json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/convert/xml-to-json-url", tags=["Conversion"])
async def convert_xml_to_json(
    url: str = Query(..., description="URL pointing to a PBCore XML document")
):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            response.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching URL: {str(e)}")

    try:
        pbcore_xml = etree.fromstring(response.content)
        xslt_doc = etree.parse(XSL_PATH)
        transform = etree.XSLT(xslt_doc)
        json_str = str(transform(pbcore_xml))
        return json.loads(json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/convert/json-to-xml", tags=["PBCore Conversion"])
async def convert_json_to_xml(file: UploadFile = File(...)):
    raise HTTPException(status_code=400, detail="PBCore JSON to XML Conversion not yet implemented")
        


@app.post("/convert/roundtrip/xml-json/file", tags=["PBCore Conversion"])
async def validate_roundtrip(file: UploadFile = File(...)):
    raise HTTPException(status_code=400, detail="PBCore XML-to-JSON round-trip validation not yet implemented")
