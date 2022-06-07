
from socket import timeout
from fastapi import APIRouter, Response
from zeep import Client
from zeep.transports import Transport
from schemas.testSoap import SOAPTest
from starlette.responses import JSONResponse

testSoap = APIRouter()
transport = Transport(timeout=1)


@testSoap.post('/GetTokenUser')
async def GetTokenUser(dataapi: SOAPTest):
    
    try:
        client = Client('http://gps.rcontrol.com.mx/Tracking/wcf/RCService.svc?wsdl', transport=transport)
        login_result = client.service.GetUserToken(dataapi.username, dataapi.password)
        token = login_result.token
        return login_result
    except:
        return JSONResponse(status_code=501, content={"message": "Se ha excedido límite de tiempo de espera, está configurado de" + str(transport) +  "milisegundo"}) 
