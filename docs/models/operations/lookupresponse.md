# LookupResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | HTTP response content type for this operation                                         |
| `lookup_response`                                                                     | [Optional[components.LookupResponse]](../../models/components/lookupresponse.md)      | :heavy_minus_sign:                                                                    | OK                                                                                    |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | HTTP response status code for this operation                                          |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |