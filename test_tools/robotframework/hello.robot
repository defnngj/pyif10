*** Settings ***
Library           Collections
Library           RequestsLibrary

*** Test Cases ***
test case
    log    hello robot framework

Get Requests
    Create Session    api    http://127.0.0.1:8000/api
    ${resp}=    Get Request    api    /hello_api/
    Should Be Equal As Strings    ${resp.status_code}    200
    log    ${resp}

POST Request
    Create Session    event    http://127.0.0.1:8000/api
    &{headers}    Create Dictionary    Content-Type=application/x-www-form-urlencoded
    &{payload}=    Create Dictionary    name=huawei    limit=3000    address=beijing    start_time=2019
    ${r}=    Post Request    event    /add_event/    data=${payload}    headers=${headers}
    Should Be Equal As Strings    ${r.status_code}    200
    log    ${r.json()}
    ${dict}    Set variable    ${r.json()}
    #断言结果
    ${msg}    Get From Dictionary    ${dict}    message
    Should Be Equal    ${msg}    日期格式错误
    ${sta}    Get From Dictionary    ${dict}    status
    ${status}    Evaluate    int(10102)
    Should Be Equal    ${sta}    ${status}
