##################################################
## {Description}
##################################################
## {License_info}
##################################################
## Author: {author}
## Copyright: Copyright {year}, {project_name}
## Credits: [{credit_list}]
## License: {license}
## Version: {mayor}.{minor}.{rel}
## Mmaintainer: {maintainer}
## Email: {contact_email}
## Status: {dev_status}
##################################################
import falcon
import ujson
import json
from commons.connection import *

from commons.loggy import set_up_logging


class BaseModel(Model):
    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        self.logger = set_up_logging(type(self).__name__)
    ##############################################################
    # calcHypotenuse(a, b)
    # This function solves Pythagorean theorem a^2 + b^2 = c^2
    # for the value of c.
    # inputs: a and b are the lengths of sides of a right triangle.
    # returns: the length of the hypotenuse.
    def on_get(self, req, resp, **kwargs):
        try:
            self.logger.info("{0} = {1}".format("query_string", req.query_string))
            self.logger.info("{0} = {1}".format("query_string", "limit", req.get_param("limit")))
            self.logger.info("{0} = {1}".format("query_string", "limit", req.get_param("limit")))
            for key, value in req.params.items():
                self.logger.info("{0} = {1}".format(key, value))
            if kwargs.get('id'):
                self.logger.info("Ennnnnnnnnnn")
                result = type(self).find(int(kwargs.get('id')))
                #self.logger.info(ujson.dumps(result))
            else:
                if req.params:
                    if req.get_param("limit") and req.get_param("page"):
                        result = type(self).paginate(int(req.get_param("limit")), int(req.get_param("page")))
                        self.logger.info("{0} = {1}".format("total", result.total))
                        self.logger.info("{0} = {1}".format("hasattr", hasattr(result, 'total')))
                else:
                    result = type(self).all()
                    # result = type(self).where('FirstName','=','Leonie').where('CustomerId','=','2').get().to_json()
                    self.logger.info(result)
            doc = {
                'success': "True",
                'message': "",
                'total_records': result.total if hasattr(result, 'total') else 0,
                'records_per_page': result.per_page if hasattr(result, 'per_page') else 0,
                'current_page': result.current_page if hasattr(result, 'current_page') else 0,
                'last_page': result.last_page if hasattr(result, 'last_page') else 0,
                'next_page': result.next_page if hasattr(result, 'next_page') else 0,
                'has_more_pages': result.has_more_pages() if hasattr(result, 'current_page') else False,
                'data': ujson.loads(ujson.dumps(result.serialize()))
            }
        except Exception as e:
            doc = {
                'success': "False",
                'message': str(e)}
        resp.media = doc
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200

