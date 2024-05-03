# FeedbackResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | HTTP response content type for this operation                                         |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | HTTP response status code for this operation                                          |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_check_mark:                                                                    | Raw HTTP response; suitable for custom response parsing                               |
| `feedback_response`                                                                   | [Optional[components.FeedbackResponse]](../../models/components/feedbackresponse.md)  | :heavy_minus_sign:                                                                    | OK                                                                                    |
| `error_response`                                                                      | *Optional[errors.ErrorResponse]*                                                      | :heavy_minus_sign:                                                                    | Bad Request                                                                           |