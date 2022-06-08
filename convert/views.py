from django.shortcuts import redirect

import convertapi
convertapi.api_secret = '74Hq45X3sDqnIJcQ'
# Create your views here.
import logging
logging.basicConfig(filename='convertapi.log', level=logging.DEBUG)
convertapi_logger = logging.getLogger("file_log")



def pdf_builder(request):
    convertapi_logger.info("Test info log")
    convertapi_logger.exception("Test exception log")
    url = request.GET.get("url")
    print("inside the url")
    try:
        result = convertapi.convert(
            'pdf',
            {
                'Url': url,
                'FileName': 'Report',
                'ConversionDelay':23,

            },
            from_format = 'web',
            timeout = 180,
        )
        logging.info(result.__dict__)
        return redirect(result.response['Files'][0]['Url'])
    except Exception as error:
        logging.exception(error)
        raise error
