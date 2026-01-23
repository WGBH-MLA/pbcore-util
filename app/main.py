from fastapi import FastAPI, File, UploadFile, HTTPException, Query, Depends
from pydantic import HttpUrl
from lxml import etree
import json
from app.helpers import safe_http_get

SECURE_XML_PARSER = etree.XMLParser(resolve_entities=False, no_network=True)

app = FastAPI(title="PBCore Validation and Conversion API")

# Placeholder paths
XSD_PATH = "schemas/pbcore-2.1.xsd"
XSL_PATH = "stylesheets/pbcore-xml-to-json.xsl"
JSON_SCHEMA_PATH = "schemas/pbcore-schema.json"


@app.post("/validate/xml-file", tags=["XML Validation"])
async def validate_xml(file: UploadFile = File(...)):
    try:
        parsed_pbcore_xml = etree.parse(file.file)
        pbcore_schema = etree.XMLSchema(etree.parse(XSD_PATH))
        pbcore_schema.assertValid(parsed_pbcore_xml)
        return {"valid": True, "file": file.filename}
    except etree.DocumentInvalid as e:
        raise HTTPException(
            status_code=422, detail=f"PBCore XML Validation Error: {str(e)}"
        )
    except etree.XMLSyntaxError as e:
        raise HTTPException(status_code=422, detail=f"XML Parsing Error: {str(e)}")


@app.post("/validate/xml-url", tags=["XML Validation"])
async def validate_xml_from_url(
    url: HttpUrl = Query(..., description="URL pointing to a PBCore XML document"),
    pbcore_xml: str = Depends(safe_http_get),
):
    try:
        parsed_pbcore_xml = etree.fromstring(pbcore_xml, parser=SECURE_XML_PARSER)
        pbcore_schema = etree.XMLSchema(etree.parse(XSD_PATH))
        pbcore_schema.assertValid(parsed_pbcore_xml)
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
    raise HTTPException(
        status_code=400, detail="PBCore JSON validation not yet implemented"
    )


@app.post("/validate/json-url", tags=["JSON Validation"])
async def validate_json_from_url(
    url: HttpUrl = Query(..., description="URL pointing to a PBCore JSON document"),
    pbcore_json: str = Depends(safe_http_get),
):
    raise HTTPException(
        status_code=400, detail="PBCore JSON validation not yet implemented"
    )


@app.post("/convert/xml-to-json-file", tags=["XML to JSON Conversion"])
async def convert_xml_to_json_from_file(file: UploadFile = File(...)):
    try:
        parsed_pbcore_xml = etree.parse(file.file, parser=SECURE_XML_PARSER)
        xslt_doc = etree.parse(XSL_PATH)
        transform = etree.XSLT(xslt_doc)
        json_str = str(transform(parsed_pbcore_xml))
        return json.loads(json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/convert/xml-to-json-url", tags=["XML to JSON Conversion"])
async def convert_xml_to_json_from_url(
    url: HttpUrl = Query(..., description="URL pointing to a PBCore XML document"),
    pbcore_xml: str = Depends(safe_http_get),
):
    try:
        parsed_pbcore_xml = etree.fromstring(pbcore_xml, parser=SECURE_XML_PARSER)
        xslt_doc = etree.parse(XSL_PATH)
        transform = etree.XSLT(xslt_doc)
        json_str = str(transform(parsed_pbcore_xml))
        return json.loads(json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/convert/json-to-xml-file", tags=["JSON to XML Conversion"])
async def convert_json_to_xml_from_file(file: UploadFile = File(...)):
    raise HTTPException(
        status_code=400, detail="PBCore JSON to XML Conversion not yet implemented"
    )


@app.post("/convert/json-to-xml-url", tags=["JSON to XML Conversion"])
async def convert_json_to_xml_from_url(
    url: HttpUrl = Query(..., description="URL pointing to a PBCore JSON document"),
    pbcore_json: str = Depends(safe_http_get),
):
    raise HTTPException(
        status_code=400, detail="PBCore JSON to XML Conversion not yet implemented"
    )


@app.post("/convert/roundtrip/xml-json/file", tags=["Roundtrip Conversion"])
async def convert_roundtrip(file: UploadFile = File(...)):
    raise HTTPException(
        status_code=400,
        detail="PBCore XML-to-JSON round-trip validation not yet implemented",
    )
