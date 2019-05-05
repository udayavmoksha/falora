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


from model.user import *
from model.customer import *
from model.album import *


app = application = falcon.API()
app.add_route('/customers', Customer())
app.add_route('/customers/{id}', Customer())
app.add_route('/albums', Album())
app.add_route('/albums/{id}', Album())
